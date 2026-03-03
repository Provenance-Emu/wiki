---
description: How to contribute code, documentation, or bug reports to Provenance
---

# Contributing

Provenance is an open-source project and welcomes contributions from the community. Here's how you can help:

## Ways to Contribute

| Contribution | Where | Skill Level |
|-------------|-------|-------------|
| **Report bugs** | [GitHub Issues](https://github.com/Provenance-Emu/Provenance/issues) | Any |
| **Improve documentation** | [Wiki repo](https://github.com/Provenance-Emu/wiki) | Any |
| **Submit code fixes** | [Main repo](https://github.com/Provenance-Emu/Provenance) (fork & PR) | Developer |
| **Add features** | [Main repo](https://github.com/Provenance-Emu/Provenance) (fork & PR) | Developer |
| **Test beta builds** | [TestFlight](../faqs.md#what-is-provenance-plus) or build from source | Intermediate |
| **Share controller skins** | [DeltaStyles](https://deltastyles.com) or [Discord](https://discord.gg/provenance) | Designer |

---

## Code Contributions (Fork & PR Workflow)

Provenance uses a **fork-and-pull-request workflow** — you work on your own fork and submit PRs back to the main repo. This means you don't need write access to contribute.

### 1. Create a Fork

1. Go to the [Provenance GitHub page](https://github.com/Provenance-Emu/Provenance) and click **Fork**
2. Clone your fork locally:

```bash
# Clone your fork (with submodules)
git clone --recurse-submodules -j4 git@github.com:YOUR-USERNAME/Provenance.git ProvFork
cd ProvFork
```

3. Add the upstream remote so you can pull future updates:

```bash
# Add the original repo as "upstream"
git remote add upstream git@github.com:Provenance-Emu/Provenance.git

# Verify remotes
git remote -v
```

### 2. Create a Feature Branch

Always work on a dedicated branch — never commit directly to `develop`:

```bash
git checkout -b feature/your-feature-name
```

### 3. Keep Your Fork Up to Date

Before starting work (and periodically while working), sync with upstream:

```bash
# Fetch latest from upstream
git fetch upstream

# Update your local develop branch
git checkout develop
git pull upstream develop
git push origin develop

# Rebase your feature branch on the latest develop
git checkout feature/your-feature-name
git merge upstream/develop
```

You can also use the **Fetch upstream** button on your fork's GitHub page.

### 4. Submit a Pull Request

PRs should contain all changes **squashed into a single commit** to keep the git history clean:

```bash
# Make sure you're on your feature branch
git checkout feature/your-feature-name

# Squash all commits into one
git reset --soft develop
git add -A
git commit -m "Add your feature description here"

# Push (force push needed since history was rewritten)
git push --force origin feature/your-feature-name
```

Then open a Pull Request on GitHub from your branch to `Provenance-Emu/Provenance:develop`.

---

## Wiki / Documentation Contributions

The wiki lives in a [separate repo](https://github.com/Provenance-Emu/wiki). It's all Markdown files rendered by GitBook.

**Quick fixes:** Edit directly on GitHub (click the pencil icon on any file) and submit a PR.

**Larger changes:** Fork the wiki repo, make edits locally, and submit a PR to `master`.

**Style notes:**
- Use relative links between pages (e.g., `[FAQ](../faqs.md)`)
- Preserve existing YAML frontmatter
- Update `SUMMARY.md` if adding or renaming pages

---

## Reporting Bugs

Good bug reports help us fix issues faster:

1. **Search first** — Check [existing issues](https://github.com/Provenance-Emu/Provenance/issues) to avoid duplicates
2. **Use the latest version** — Update from the App Store or build from the latest source
3. **Include details:**
   - Device model and OS version
   - Provenance version (Settings → About)
   - Steps to reproduce the issue
   - What you expected vs what happened
   - Screenshots or screen recordings if applicable
4. **One bug per issue** — Don't bundle multiple problems together

{% hint style="warning" %}
**Before reporting:** Make sure you installed from an [official source](../installation-and-usage/installing-provenance/README.md). We cannot support 3rd-party builds or signing services.
{% endhint %}

---

## Community

- **[Discord](https://discord.gg/provenance)** — Chat, help, and discussion
- **[GitHub Discussions](https://github.com/Provenance-Emu/Provenance/discussions)** — Feature requests and Q&A
- **[Twitter/X](https://twitter.com/provenanceapp)** — Updates and announcements

{% hint style="success" %}
Every contribution matters — whether it's a one-line typo fix, a detailed bug report, or a major feature. Thank you for helping make Provenance better!
{% endhint %}
