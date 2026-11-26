#!/usr/bin/env python3
"""Regenerate help/shared-frameworks.md from GitHub.

scripts/shared-frameworks.json holds what a person writes: which packages are listed,
in what order, what each one does, which apps use it, and an optional note. Everything
else is read from each package's GitHub repository on every run: latest version and its
date, whether that release ships prebuilt XCFrameworks, platforms, license, languages,
topics, and the links.

Run by .github/workflows/sync-shared-frameworks.yml (daily, and by hand). Locally:

    GH_TOKEN=$(gh auth token) python3 scripts/sync-shared-frameworks.py

Without a token GitHub allows 60 requests an hour, fewer than one run needs.
"""
import base64
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "scripts" / "shared-frameworks.json"
PAGE = ROOT / "help" / "shared-frameworks.md"
TOKEN = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
SEMVER = re.compile(r"^v?(\d+)\.(\d+)\.(\d+)$")
PLATFORM = re.compile(r"\.(iOS|tvOS|macOS|watchOS|visionOS)\(\s*(?:\.v|\")([0-9_.]+)")
PLATFORM_ORDER = ["iOS", "tvOS", "macOS", "watchOS", "visionOS"]


def api(path):
    request = urllib.request.Request(f"https://api.github.com/{path}")
    request.add_header("Accept", "application/vnd.github+json")
    if TOKEN:
        request.add_header("Authorization", f"Bearer {TOKEN}")
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.load(response)
    except urllib.error.HTTPError as error:
        if error.code == 404:
            return None
        raise


def version_key(name):
    return tuple(int(part) for part in SEMVER.match(name).groups())


def latest_version(owner, name):
    """The highest major.minor.patch tag, with its date and whether it has binaries."""
    releases = [r for r in api(f"repos/{owner}/{name}/releases?per_page=100") or []
                if SEMVER.match(r["tag_name"]) and not r["draft"] and not r["prerelease"]]
    tags = [t["name"] for t in api(f"repos/{owner}/{name}/tags?per_page=100") or []
            if SEMVER.match(t["name"])]
    if not tags:
        return None
    tag = max(tags, key=version_key)
    release = next((r for r in releases if r["tag_name"] == tag), None)
    if release:
        date = release["published_at"][:10]
        binary = any(a["name"].endswith(".xcframework.zip") for a in release["assets"])
    else:
        commit = api(f"repos/{owner}/{name}/commits/{tag}")
        date = commit["commit"]["committer"]["date"][:10]
        binary = False
    return {"tag": tag, "date": date, "binary": binary, "release": release is not None}


def platforms(owner, name, branch):
    manifest = api(f"repos/{owner}/{name}/contents/Package.swift?ref={branch}")
    if not manifest:
        return ""
    source = base64.b64decode(manifest["content"]).decode()
    found = {}
    for platform, version in PLATFORM.findall(source):
        found.setdefault(platform, version.replace("_", "."))
    return ", ".join(f"{p} {found[p]}" for p in PLATFORM_ORDER if p in found)


def describe(owner, entry):
    name = entry["name"]
    repo = api(f"repos/{owner}/{name}")
    if repo is None:
        sys.exit(f"{owner}/{name}: repository not found")
    languages = api(f"repos/{owner}/{name}/languages") or {}
    total = sum(languages.values()) or 1
    shown = [f"{language} {round(100 * size / total)}%"
             for language, size in sorted(languages.items(), key=lambda item: -item[1])
             if size / total >= 0.01]
    license_id = (repo.get("license") or {}).get("spdx_id")
    return {
        **entry,
        "url": repo["html_url"],
        "version": latest_version(owner, name),
        "platforms": platforms(owner, name, repo["default_branch"]),
        "license": license_id if license_id and license_id != "NOASSERTION" else None,
        "languages": ", ".join(shown),
        "topics": repo.get("topics") or [],
    }


def version_cell(package):
    version = package["version"]
    if not version:
        return "unreleased"
    target = "releases/tag" if version["release"] else "tree"
    return f"[{version['tag']}]({package['url']}/{target}/{version['tag']})"


def section(package):
    name, url, version = package["name"], package["url"], package["version"]
    lines = [f"## {name}", "", package["summary"], "",
             f"* **Repository:** [{url.removeprefix('https://')}]({url})"]
    if version:
        kind = "prebuilt XCFramework" if version["binary"] else "source"
        lines.append(f"* **Latest version:** {version_cell(package)}, released {version['date']} ({kind})")
        lines.append(f"* **Releases:** [all versions]({url}/releases)")
    lines.append(f"* **Used by:** {', '.join(package['usedBy'])}")
    if package["platforms"]:
        lines.append(f"* **Platforms:** {package['platforms']}")
    if package["languages"]:
        lines.append(f"* **Languages:** {package['languages']}")
    if package["license"]:
        lines.append(f"* **License:** [{package['license']}]({url}/blob/HEAD/LICENSE.md)")
    else:
        lines.append(f"* **License:** [see the repository]({url})")
    if package["topics"]:
        topics = ", ".join(f"[{t}](https://github.com/topics/{t})" for t in package["topics"])
        lines.append(f"* **Topics:** {topics}")
    if version:
        minor = int(SEMVER.match(version["tag"]).group(1)) == 0
        requirement = (f".upToNextMinor(from: \"{version['tag']}\")" if minor
                       else f"from: \"{version['tag']}\"")
        lines += ["", "```swift", f".package(url: \"{url}.git\", {requirement})", "```"]
    if package.get("note"):
        lines += ["", package["note"]]
    return lines + [""]


def render(owner, packages):
    table = ["| Package | What it does | Latest | Used by | Platforms |", "|---|---|---|---|---|"]
    for p in packages:
        table.append(f"| [{p['name']}](#{p['name'].lower()}) | {p['summary']} | {version_cell(p)} "
                     f"| {', '.join(p['usedBy'])} | {p['platforms']} |")
    zero = [p["name"] for p in packages
            if p["version"] and SEMVER.match(p["version"]["tag"]).group(1) == "0"]
    first = next(p for p in packages if p["version"])
    out = [
        "---",
        "description: The Swift packages Provenance, iFly and iCube share, what each one does, "
        "and how to add one to your own app.",
        "---",
        "",
        "# Shared Frameworks",
        "",
        "Provenance, [iFly](https://ifly-emu.com) (Dreamcast) and [iCube](https://icube-emu.com) "
        "(GameCube / Wii) are three apps built on the same parts. Anything two of them need lives in "
        f"its own Swift package, in its own repository under [github.com/{owner}](https://github.com/{owner}), "
        "and each app depends on it by URL. A fix made once lands in all three.",
        "",
        "None of these packages knows which app it is in. App group names, CloudKit containers, URL "
        "schemes and colors are passed in by the host app, so the packages work in any emulator "
        "frontend for Apple platforms, not only ours.",
        "",
        "## The packages",
        "",
        *table,
        "",
        "Versions, dates, platforms, languages and topics on this page are read from each "
        "repository once a day; the descriptions are written by hand.",
        "",
        "## Adding a package",
        "",
        "Every package is a plain SwiftPM package with version tags. In `Package.swift`:",
        "",
        "```swift",
        "dependencies: [",
        f"    .package(url: \"{first['url']}.git\", from: \"{first['version']['tag']}\")",
        "],",
        "targets: [",
        "    .target(name: \"MyApp\", dependencies: [",
        f"        .product(name: \"{first['name']}Core\", package: \"{first['name']}\")"
        if first["name"] == "SkinKit" else
        f"        .product(name: \"{first['name']}\", package: \"{first['name']}\")",
        "    ])",
        "]",
        "```",
        "",
        "In Xcode: **File → Add Package Dependencies…** and paste the repository URL.",
        "",
        "A version marked *prebuilt XCFramework* resolves to a binary, so your app compiles none of "
        "the package. To build it from source instead, set `PV_BUILD_FROM_SOURCE=1` in the "
        "environment Xcode starts in and resolve packages again.",
        "",
    ]
    if zero:
        out += ["{% hint style=\"info\" %}",
                f"Packages at `0.x` ({', '.join(zero)}) may break their API in a minor release. "
                "Pin them with `.upToNextMinor(from:)`.",
                "{% endhint %}", ""]
    for p in packages:
        out += section(p)
    out += [
        "## Contributing",
        "",
        "Change a package in its own repository, release it, then bump the version in each app that "
        "uses it. Pull requests are welcome on any of them; see [Contributing](contribute.md).",
        "",
        "## See Also",
        "",
        "* [Contributing](contribute.md)",
        "* [Building from Source](../installation-and-usage/installing-provenance/building-from-source.md)",
        "* [Skins](../info/skins-guide.md)",
        "* [Open Source Licenses](../info/open-source-licenses.md)",
        "",
        "{% hint style=\"info\" %}",
        "Need help? Ask on [Discord](https://discord.gg/provenance).",
        "{% endhint %}",
        "",
    ]
    return "\n".join(out)


def main():
    data = json.loads(DATA.read_text())
    owner = data["organization"]
    packages = [describe(owner, entry) for entry in data["packages"]]
    page = render(owner, packages)
    if PAGE.exists() and PAGE.read_text() == page:
        print("help/shared-frameworks.md is up to date")
        return
    PAGE.write_text(page)
    print("help/shared-frameworks.md regenerated")


if __name__ == "__main__":
    main()
