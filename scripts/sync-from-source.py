#!/usr/bin/env python3
"""
Sync wiki metadata from Provenance source code.

Parses Systems.plist and Core.plist files from the Provenance app repository
to generate auto-updated wiki reference pages.

Usage:
    python3 sync-from-source.py <provenance-repo-path> <wiki-output-dir>
"""

import plistlib
import os
import sys
from pathlib import Path
from datetime import datetime, timezone


# Delta skin identifier mapping (from DeltaSkinTypes.swift)
DELTA_IDS = {
    'com.provenance.gb': 'com.rileytestut.delta.game.gbc',
    'com.provenance.gbc': 'com.rileytestut.delta.game.gbc',
    'com.provenance.gba': 'com.rileytestut.delta.game.gba',
    'com.provenance.nes': 'com.rileytestut.delta.game.nes',
    'com.provenance.snes': 'com.rileytestut.delta.game.snes',
    'com.provenance.n64': 'com.rileytestut.delta.game.n64',
    'com.provenance.nds': 'com.rileytestut.delta.game.ds',
    'com.provenance.genesis': 'com.rileytestut.delta.game.genesis',
    'com.provenance.gamegear': 'com.rileytestut.delta.game.gg',
    'com.provenance.mastersystem': 'com.rileytestut.delta.game.ms',
    'com.provenance.psx': 'com.rileytestut.delta.game.psx',
}

# DeltaStyles search slugs for direct linking
DELTASTYLES_SLUGS = {
    'com.provenance.nes': 'nes',
    'com.provenance.snes': 'snes',
    'com.provenance.gb': 'gameboy',
    'com.provenance.gbc': 'gameboy+color',
    'com.provenance.gba': 'gba',
    'com.provenance.n64': 'n64',
    'com.provenance.nds': 'ds',
    'com.provenance.genesis': 'genesis',
    'com.provenance.gamegear': 'game+gear',
    'com.provenance.mastersystem': 'master+system',
    'com.provenance.psx': 'playstation',
    'com.provenance.psp': 'psp',
    'com.provenance.dreamcast': 'dreamcast',
    'com.provenance.3ds': '3ds',
    'com.provenance.segacd': 'sega+cd',
    'com.provenance.saturn': 'saturn',
}


def parse_systems(plist_path):
    """Parse the systems.plist file into a list of system dicts."""
    with open(plist_path, 'rb') as f:
        raw = plistlib.load(f)

    systems = []
    for entry in raw:
        system = {
            'id': entry.get('PVSystemIdentifier', '').strip(),
            'name': entry.get('PVSystemName', '').strip(),
            'short_name': entry.get('PVSystemShortName', '').strip(),
            'long_name': entry.get('PVSystemLongName', entry.get('PVSystemName', '')).strip(),
            'manufacturer': entry.get('PVManufacturer', '').strip(),
            'year': entry.get('PVReleaseYear', ''),
            'bits': entry.get('PVBit', ''),
            'screen_type': entry.get('PVScreenType', ''),
            'portable': entry.get('PVPortable', False),
            'extensions': sorted(entry.get('PVSupportedExtensions', [])),
            'requires_bios': entry.get('PVRequiresBIOS', False),
            'uses_cds': entry.get('PVUsesCDs', False),
            'supports_rumble': entry.get('PVSupportsRumble', False),
            'supported': entry.get('PVSupported', True),
            'app_store_disabled': entry.get('PVAppStoreDisabled', False),
            'bios_files': [],
        }

        for bios in entry.get('PVBIOSNames', []):
            system['bios_files'].append({
                'name': bios.get('Name', ''),
                'description': bios.get('Description', ''),
                'md5': bios.get('MD5', ''),
                'size': bios.get('Size', 0),
                'optional': bios.get('Optional', False),
            })

        systems.append(system)

    return systems


def find_core_plists(repo_root):
    """Recursively find all Core.plist files."""
    plists = []
    for root, dirs, files in os.walk(repo_root):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        if 'Core.plist' in files:
            plists.append(os.path.join(root, 'Core.plist'))
    return plists


def parse_core(plist_path):
    """Parse a Core.plist, returning a list of core dicts (multiple for RetroArch)."""
    with open(plist_path, 'rb') as f:
        data = plistlib.load(f)

    def extract(d):
        return {
            'id': d.get('PVCoreIdentifier', '').strip(),
            'name': d.get('PVProjectName', '').strip(),
            'systems': d.get('PVSupportedSystems', []),
            'url': d.get('PVProjectURL', '').strip(),
            'version': d.get('PVProjectVersion', '').strip(),
            'disabled': d.get('PVDisabled', False),
            'app_store_disabled': d.get('PVAppStoreDisabled', False),
            'cheat_types': d.get('PVSupportedCheatTypes', []),
        }

    sub_cores = data.get('PVCores', [])
    if sub_cores:
        return [extract(sc) for sc in sub_cores]
    return [extract(data)]


def format_size(size_bytes):
    """Format bytes as human-readable string."""
    if not size_bytes:
        return ''
    if size_bytes >= 1_048_576:
        return f"{size_bytes / 1_048_576:.1f} MB"
    if size_bytes >= 1024:
        return f"{size_bytes / 1024:.0f} KB"
    return f"{size_bytes} B"


def generate_system_reference(systems, cores, timestamp):
    """Generate the full system-reference.md content."""
    # Pre-compute lookups
    sys_map = {s['id']: s for s in systems}
    active_systems = [s for s in systems if s['supported'] and not s['app_store_disabled']]
    dev_systems = [s for s in systems if not s['supported'] or s['app_store_disabled']]
    sorted_systems = sorted(active_systems, key=lambda s: (s['manufacturer'], s['year']))

    # Build core-to-system mapping
    core_for_system = {}
    for core in cores:
        if core['disabled']:
            continue
        for sid in core['systems']:
            core_for_system.setdefault(sid, []).append(core)

    lines = []

    # --- Header ---
    lines.append('---')
    lines.append('description: Auto-generated system and core reference from Provenance source code')
    lines.append('---')
    lines.append('')
    lines.append('# System Reference')
    lines.append('')
    lines.append('{% hint style="info" %}')
    lines.append(f'**Auto-generated** from [Provenance source code](https://github.com/Provenance-Emu/Provenance) on {timestamp}. Do not edit manually — changes will be overwritten by the [sync workflow](https://github.com/Provenance-Emu/wiki/actions/workflows/sync-from-source.yml).')
    lines.append('{% endhint %}')
    lines.append('')
    lines.append('**Quick links:** [Systems](#systems) | [BIOS Requirements](#bios-requirements) | [File Extensions](#supported-file-extensions) | [Core Matrix](#core-to-system-matrix) | [Cheat Support](#cheat-support) | [Skin Identifiers](#skin-identifiers)')
    lines.append('')
    lines.append('---')
    lines.append('')

    # --- Systems Table ---
    lines.append('## Systems')
    lines.append('')
    lines.append(f'Provenance supports **{len(active_systems)} systems** ({len(dev_systems)} additional in development or disabled).')
    lines.append('')
    lines.append('| Manufacturer | System | Short | Year | Bits | Screen | Portable | CD | Rumble | BIOS |')
    lines.append('|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|')

    for s in sorted_systems:
        portable = 'Yes' if s['portable'] else ''
        cd = 'Yes' if s['uses_cds'] else ''
        rumble = 'Yes' if s['supports_rumble'] else ''
        bios = '✅ Required' if s['requires_bios'] else ('🔶 Optional' if s['bios_files'] else '')
        lines.append(f"| {s['manufacturer']} | {s['name']} | {s['short_name']} | {s['year']} | {s['bits']} | {s['screen_type']} | {portable} | {cd} | {rumble} | {bios} |")

    lines.append('')

    if dev_systems:
        lines.append('<details>')
        lines.append('<summary><strong>Systems in Development / Disabled</strong></summary>')
        lines.append('')
        lines.append('| Manufacturer | System | Year | Status |')
        lines.append('|:---|:---|:---|:---|')
        for s in sorted(dev_systems, key=lambda s: s['name']):
            status = 'App Store disabled' if s['app_store_disabled'] else 'In development'
            lines.append(f"| {s['manufacturer']} | {s['name']} | {s['year']} | {status} |")
        lines.append('')
        lines.append('</details>')
        lines.append('')

    lines.append('---')
    lines.append('')

    # --- BIOS Requirements ---
    lines.append('## BIOS Requirements')
    lines.append('')
    lines.append('{% hint style="warning" %}')
    lines.append('**DO NOT** ask us where to obtain BIOS files. Distributing BIOS files violates copyright law.')
    lines.append('{% endhint %}')
    lines.append('')
    lines.append('| System | File | Description | MD5 | Size | Status |')
    lines.append('|:---|:---|:---|:---|:---|:---|')

    for s in sorted_systems:
        if not s['bios_files']:
            continue
        for i, bios in enumerate(s['bios_files']):
            sys_col = s['name'] if i == 0 else ''
            status = '🔶 Optional' if bios['optional'] else '✅ Required'
            md5 = f"`{bios['md5']}`" if bios['md5'] else ''
            size = format_size(bios['size'])
            lines.append(f"| {sys_col} | `{bios['name']}` | {bios['description']} | {md5} | {size} | {status} |")

    lines.append('')
    lines.append('---')
    lines.append('')

    # --- File Extensions ---
    lines.append('## Supported File Extensions')
    lines.append('')
    lines.append('| System | Extensions |')
    lines.append('|:---|:---|')

    for s in sorted_systems:
        exts = ', '.join(f'`.{e}`' for e in s['extensions'])
        lines.append(f"| {s['name']} | {exts} |")

    lines.append('')
    lines.append('---')
    lines.append('')

    # --- Core Matrix ---
    lines.append('## Core-to-System Matrix')
    lines.append('')
    lines.append('Shows which emulator cores are available for each system.')
    lines.append('')
    lines.append('| System | Available Cores | Versions |')
    lines.append('|:---|:---|:---|')

    for s in sorted_systems:
        sys_cores = core_for_system.get(s['id'], [])
        if not sys_cores:
            lines.append(f"| {s['name']} | — | — |")
            continue
        active = [c for c in sys_cores if not c['app_store_disabled'] and not c['disabled']]
        if not active:
            active = sys_cores  # show all if none are active
        names = ', '.join(f"[{c['name']}]({c['url']})" if c['url'] else c['name']
                          for c in sorted(active, key=lambda c: c['name']))
        versions = ', '.join(c['version'] for c in sorted(active, key=lambda c: c['name']) if c['version'])
        lines.append(f"| {s['name']} | {names} | {versions} |")

    lines.append('')
    lines.append('---')
    lines.append('')

    # --- Cheat Support ---
    lines.append('## Cheat Support')
    lines.append('')
    lines.append('Cores declaring cheat support in their `Core.plist` metadata:')
    lines.append('')
    lines.append('| Core | Systems | Cheat Formats |')
    lines.append('|:---|:---|:---|')

    cheat_cores = [c for c in cores if c['cheat_types'] and not c['disabled']]
    for c in sorted(cheat_cores, key=lambda c: c['name']):
        sys_names = ', '.join(
            sys_map[sid]['short_name']
            for sid in sorted(c['systems'])
            if sid in sys_map
        )
        cheats = ', '.join(c['cheat_types'])
        lines.append(f"| {c['name']} | {sys_names} | {cheats} |")

    lines.append('')
    lines.append('{% hint style="info" %}')
    lines.append('Additional cores support cheats through code-level protocol conformance not declared in Core.plist. See [Cheats Guide](cheats.md) for the complete list including Stella, Dolphin, PPSSPP, Azahar, and Play!.')
    lines.append('{% endhint %}')
    lines.append('')
    lines.append('---')
    lines.append('')

    # --- Skin Identifiers ---
    lines.append('## Skin Identifiers')
    lines.append('')
    lines.append('Use these identifiers when creating `.deltaskin` files. Browse column links directly to system-filtered skins on DeltaStyles.')
    lines.append('')
    lines.append('| System | Provenance ID | Delta Skin ID | Browse Skins |')
    lines.append('|:---|:---|:---|:---|')

    for s in sorted_systems:
        prov_id = f"`{s['id']}`"
        delta_id = f"`{DELTA_IDS[s['id']]}`" if s['id'] in DELTA_IDS else '—'
        slug = DELTASTYLES_SLUGS.get(s['id'], '')
        browse = f"[DeltaStyles](https://deltastyles.com/?search={slug})" if slug else '—'
        lines.append(f"| {s['name']} | {prov_id} | {delta_id} | {browse} |")

    lines.append('')
    lines.append('---')
    lines.append('')
    lines.append('{% hint style="info" %}')
    lines.append('For the interactive community database, see [eduo.info/pvl](https://eduo.info/pvl/). Need help? Ask on [Discord](https://discord.gg/provenance).')
    lines.append('{% endhint %}')

    return '\n'.join(lines) + '\n'


def main():
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <provenance-repo-path> <wiki-output-dir>")
        sys.exit(1)

    repo_path = sys.argv[1]
    wiki_path = sys.argv[2]

    # Find systems.plist
    candidates = [
        os.path.join(repo_path, 'PVLibrary', 'Sources', 'PVLibrary', 'Resources', 'systems.plist'),
        os.path.join(repo_path, 'PVCoreLoader', 'Sources', 'PVCoreLoader', 'Resources', 'systems.plist'),
    ]
    systems_plist = next((p for p in candidates if os.path.exists(p)), None)
    if not systems_plist:
        print(f"Error: systems.plist not found in {repo_path}")
        sys.exit(1)

    print(f"Parsing systems from {systems_plist}...")
    systems = parse_systems(systems_plist)
    print(f"  Found {len(systems)} systems")

    # Find and parse all Core.plist files
    print("Finding Core.plist files...")
    core_plists = find_core_plists(repo_path)
    print(f"  Found {len(core_plists)} Core.plist files")

    all_cores = []
    for cp in core_plists:
        try:
            parsed = parse_core(cp)
            all_cores.extend(parsed)
        except Exception as e:
            print(f"  Warning: Failed to parse {cp}: {e}")

    print(f"  Parsed {len(all_cores)} total core entries")

    # Generate output
    timestamp = datetime.now(timezone.utc).strftime("%B %d, %Y")
    content = generate_system_reference(systems, all_cores, timestamp)

    output_file = os.path.join(wiki_path, 'info', 'system-reference.md')
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, 'w') as f:
        f.write(content)

    print(f"Written {len(content):,} bytes to {output_file}")
    print("Done!")


if __name__ == '__main__':
    main()
