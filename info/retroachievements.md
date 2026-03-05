---
description: "Earn achievements in retro games with RetroAchievements integration — badges, leaderboards, and progress tracking across thousands of classic titles"
keywords: "RetroAchievements, retro achievements, emulator achievements, gaming badges, retro leaderboards, achievement tracking"
---

# RetroAchievements

Provenance integrates with [RetroAchievements](https://retroachievements.org/) — a community-driven project that adds achievement systems to retro games. Earn badges, track progress, and compete on leaderboards across thousands of classic titles.

---

## Overview

RetroAchievements works by monitoring game memory for specific conditions (e.g., "defeat boss X without taking damage"). When a condition is met, you earn an achievement — just like modern console achievements.

**What you get:**
- Achievements and badges for thousands of retro games
- Progress tracking across your entire retro library
- Leaderboards and community rankings
- Mastery awards for 100% completion

{% hint style="info" %}
RetroAchievements is available for **RetroArch-based cores only**. Not all systems or games have achievement sets — check [retroachievements.org](https://retroachievements.org/) for the full game list.
{% endhint %}

---

## Setup

### 1. Create a RetroAchievements Account

1. Visit [retroachievements.org](https://retroachievements.org/)
2. Click **Register** and create a free account
3. Note your **username** and **password**

### 2. Log In from Provenance

1. Open Provenance → **Settings**
2. Scroll to **RetroAchievements**
3. Enter your **username** and **password**
4. Tap **Log In**
5. A confirmation appears when you're connected

### 3. Play!

Launch any supported game using a RetroArch-based core. Achievements trigger automatically during gameplay — no additional setup needed per game.

---

## Supported Systems

RetroAchievements are available for these systems (when using RetroArch-based cores):

| System | Achievement Sets Available |
|--------|--------------------------|
| NES / Famicom | 1,500+ games |
| SNES / Super Famicom | 1,200+ games |
| Game Boy | 600+ games |
| Game Boy Color | 400+ games |
| Game Boy Advance | 900+ games |
| Nintendo 64 | 300+ games |
| Nintendo DS | 200+ games |
| Genesis / Mega Drive | 700+ games |
| Master System | 200+ games |
| Game Gear | 100+ games |
| Sega CD | 50+ games |
| Sega Saturn | 50+ games |
| PlayStation | 900+ games |
| PSP | 300+ games |
| Atari 2600 | 100+ games |
| Atari 7800 | 50+ games |
| Atari Lynx | 30+ games |
| PC Engine / TurboGrafx-16 | 100+ games |
| Neo Geo Pocket | 30+ games |
| WonderSwan | 20+ games |

**Total:** 7,000+ games with achievement support across all systems.

{% hint style="info" %}
Achievement counts are approximate and growing — the RetroAchievements community actively creates new achievement sets.
{% endhint %}

---

## How Achievements Work

### During Gameplay

- Achievements **pop up automatically** when conditions are met
- No need to pause or check manually
- Progress towards achievements can be tracked on the RetroAchievements website

### Hardcore Mode

RetroAchievements offers two modes:

| Mode | Save States | Cheats | Fast Forward | Leaderboards |
|------|------------|--------|-------------|-------------|
| **Softcore** | Allowed | Allowed | Allowed | No |
| **Hardcore** | Disabled | Disabled | Disabled | Yes |

**Hardcore mode** proves you earned achievements legitimately — no save-scumming or cheating. It also enables leaderboard submissions.

### Checking Your Progress

- **In-app:** Achievements display during gameplay
- **Online:** Visit your profile at `retroachievements.org/user/[YourUsername]`
- **Stats:** Track completion percentage, points earned, and rankings

---

## Tips

- **Check game compatibility first** — Search your game at [retroachievements.org](https://retroachievements.org/) to see if it has achievements
- **Use the correct ROM** — Achievements are tied to specific ROM versions (usually No-Intro verified dumps). Hacked, translated, or bad dump ROMs may not trigger achievements
- **Hardcore for competition** — Enable Hardcore mode if you want to appear on leaderboards
- **One game at a time** — Achievement tracking works for the currently active game

---

## Troubleshooting

<details>
<summary><strong>Achievements not triggering</strong></summary>

- Verify you're logged in (Settings → RetroAchievements)
- Check that you're using a **RetroArch-based core** — native cores don't support RetroAchievements
- Verify your ROM is the correct version — achievements require specific ROM dumps (usually No-Intro). Check the game's page on retroachievements.org for supported hashes
- Make sure the game actually has an achievement set

</details>

<details>
<summary><strong>Can't log in</strong></summary>

- Double-check your username and password at [retroachievements.org](https://retroachievements.org/) first
- Ensure you have an internet connection
- Try logging out and back in from Settings → RetroAchievements

</details>

<details>
<summary><strong>Achievements not available for my game</strong></summary>

Not all games have achievement sets. The RetroAchievements community creates them over time. You can:
- Check if someone is working on a set at [retroachievements.org](https://retroachievements.org/)
- Request a set on the RetroAchievements forums
- Learn to create achievement sets yourself (the community welcomes new developers!)

</details>

<details>
<summary><strong>Hardcore mode is too restrictive</strong></summary>

You can disable Hardcore mode in the RetroArch settings (pause menu → RetroArch Settings → Achievements). Softcore mode lets you use save states and fast forward while still earning achievements (but no leaderboards).

</details>

---

## See Also

- [Game Saves](saves.md) — Battery saves and save states
- [Performance Optimization](performance-optimization.md) — Ensure smooth gameplay for achievement hunting
- [Cheats](cheats.md) — Note: cheats disable Hardcore mode achievements

---

{% hint style="info" %}
Need help? Ask on [Discord](https://discord.gg/provenance) or check the [RetroAchievements Discord](https://discord.gg/retroachievements).
{% endhint %}
