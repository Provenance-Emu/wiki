---
description: Local and online multiplayer setup — connect multiple controllers and play together
---

# Multiplayer

Provenance supports **local multiplayer** for most systems and **online multiplayer** for RetroArch-based cores. Grab some controllers and play together on the couch, or connect with friends online.

---

## Local Multiplayer

### How It Works

Connect multiple Bluetooth or MFi controllers and Provenance automatically assigns them to player slots. Most systems that originally supported multiplayer work in Provenance.

### Setup

1. **Pair controllers** — Connect 2-4 Bluetooth controllers via Settings → Bluetooth
2. **Launch a multiplayer game**
3. **Assign players** — From the pause menu, verify controller assignments:
   - Player 1, Player 2, Player 3, Player 4
   - Reassign if needed by selecting a controller and changing its player slot

{% hint style="info" %}
**On-screen controls** are always Player 1. To play local multiplayer, at least Player 2 needs a physical controller.
{% endhint %}

### Supported Player Counts

Player support depends on the system and the specific game. Here are the maximum players per system:

| System | Max Players | Notes |
|--------|-------------|-------|
| **NES / Famicom** | 2 | Most games support 2 players |
| **SNES / Super Famicom** | 4-5 | Up to 5 with Multitap (Bomberman, Secret of Mana) |
| **Nintendo 64** | 4 | Native 4-player (GoldenEye, Mario Kart 64, Smash Bros.) |
| **Game Boy Advance** | 4 | Link cable games via core support |
| **Genesis / Mega Drive** | 4 | Up to 4 with Team Player adapter |
| **Sega Saturn** | 6 | Up to 6 with multitap |
| **Dreamcast** | 4 | Native 4-player |
| **PlayStation** | 4-8 | Up to 8 with Multitap (varies by game) |
| **Neo Geo** | 2 | Most fighting games |
| **Atari 2600** | 2 | Most games |
| **NES / Famicom** | 2 | Standard |
| **TurboGrafx-16** | 5 | Up to 5 with Multitap |

{% hint style="info" %}
The actual player count for each game depends on the game itself, not just the system. A 2-player system can still have single-player-only games.
{% endhint %}

### Recommended Controller Setups

{% tabs %}
{% tab title="Couch Co-op (2 Players)" %}
**iPhone/iPad:**
- Player 1: On-screen controls or clip-on controller (Backbone, Kishi)
- Player 2: Bluetooth controller (DualSense, Xbox, 8BitDo)

**Apple TV:**
- Player 1 + 2: Two Bluetooth controllers
- Siri Remote can navigate menus but not play games
{% endtab %}

{% tab title="Party Gaming (3-4 Players)" %}
**Apple TV (best for groups):**
- 3-4 Bluetooth controllers
- Great for N64 (Mario Kart, Smash Bros., GoldenEye)
- PS1 Multitap games (Bomberman, Crash Bash)

**iPad (works too):**
- 3-4 Bluetooth controllers
- Larger screen helps for split-screen games
{% endtab %}
{% endtabs %}

---

## Online Multiplayer

{% hint style="warning" %}
Online multiplayer is currently available through **RetroArch-based cores only** and requires using the native RetroArch settings interface. A native Provenance UI for online play is in development.
{% endhint %}

### How to Access

1. Launch a game using a **RetroArch-based core**
2. Open the **pause menu**
3. Select **RetroArch Settings**
4. Navigate to **Netplay** settings
5. Configure host/client settings

### Online Play Options

| Option | Description |
|--------|-------------|
| **Host** | Start a netplay session that others can join |
| **Client** | Join an existing netplay session by IP address |
| **Relay Server** | Use a relay server if direct connection fails |

### Requirements

- Both players must use the **same ROM** (identical file, same region)
- Both players must use the **same RetroArch core**
- Stable internet connection (wired or strong WiFi recommended)
- Low latency between players for best experience

### Tips for Online Play

- **Use wired internet** when possible — WiFi adds latency
- **Same ROM version** — Both players must have an identical ROM file (same CRC/MD5)
- **Start fresh** — Don't load save states before connecting
- **Fighting and puzzle games** work best — they require less bandwidth than fast-action games

---

## Troubleshooting

<details>
<summary><strong>Second controller not detected</strong></summary>

- Verify the controller is paired in Settings → Bluetooth
- Open the pause menu and check controller assignments
- Try disconnecting and reconnecting the controller
- Some controllers need a firmware update to work with iOS — check the manufacturer's app

</details>

<details>
<summary><strong>Controller assigned to wrong player</strong></summary>

From the pause menu, you can reassign controllers to different player slots. If controllers keep swapping, try turning on controllers in the order you want them assigned (Player 1 first, then Player 2, etc.).

</details>

<details>
<summary><strong>Multiplayer game only shows 1 player</strong></summary>

- Verify the game actually supports multiplayer (not all games do)
- Some games require selecting "2 Player" mode from the game's main menu
- Check that the correct core is being used — some cores have better multiplayer support than others

</details>

<details>
<summary><strong>Online netplay is laggy</strong></summary>

- Use a wired connection if possible
- Choose a server closer to both players
- Try increasing the netplay input latency frames in RetroArch settings
- Simpler games (puzzle, turn-based) are more tolerant of latency

</details>

---

## See Also

- [Controllers & Controls](controllers-and-controls/README.md) — Controller setup and pairing
- [Supported Controllers](controllers-and-controls/controllers/README.md) — Compatible controllers list
- [Apple TV Guide](tvos-guide.md) — Best platform for local multiplayer

---

{% hint style="info" %}
Need help? Ask on [Discord](https://discord.gg/provenance).
{% endhint %}
