---
description: Update your existing installation.
---

# Updating

When there is a new release or recent commits to a source branch you have a few options for updating. You can _sideload_ a prebuild over your existing sideloaded installation or you can _pull_ the local source and build over your existing built-from-source installation. _**New:**_ Update & Build via `make` \(untested\).

**Update Options:**

* ⤵️  [**Sideload**](sideloading.md)\*\*\*\*
* 🔃  [**Pull**](updating.md#pull) latest changes using…
  * ![](https://user-images.githubusercontent.com/3118097/37563629-48ec3f26-2a42-11e8-9fd8-784e9e830ebe.png)  [Terminal](updating.md#update-with-terminal)
  * ![](https://user-images.githubusercontent.com/3118097/37563630-4903ebbc-2a42-11e8-888a-09a94fc0058d.png)  [Tower](updating.md#update-with-tower)
* ⏩  [**Update & Build**](updating.md#update-and-build)\*\*\*\*

## Pull

### **Update with Terminal**

{% hint style="info" %}
The Terminal app can be found in: _/Applications/Utilities_
{% endhint %}

1. Navigate to the 'Provenance' directory with: `cd [path]` \(drag & drop a folder on Terminal after `cd`  to get directory path\)
2. Update latest source _\(Options\)_:
   * Overwrite Changes: If you haven't yet made _any_ changes to source files or don't mind overwriting them and reapplying your Bundle IDs, App Groups from the original installation:

     ```bash
       git pull origin develop
     ```

   * Stash Changes: If want to reapply your changes to source files \(especially any PRs you are working on or simply your Bundle IDs App Groups\), you will need to stash and re-apply them with:

     ```bash
       git stash
       git reset --hard HEAD
       git pull origin develop
       git stash pop
     ```
3. Update submodules and frameworks

   ```bash
    make update
    make open
   ```

4. Return to Xcode and…
   * Return to Build: Step 3 to reapply your settings, else…
   * If stashed changes above, just hit the `▶︎` \(Run\) button.
5. Provenance will compile and run on your device. Unless testing, hit `◼︎` \(Stop\). _Done._ 

### **Update with Tower**

1. In `Repositories` double-click `Provenance` or select and click `Open`
2. With 'develop' branch marked \(HEAD\), click `Fetch`
3. If develop branch shows a number next to it, click `Pull`
4. Click `Stash Changes`
5. After changes are pulled, click `Apply Stash`, select stash and click `Apply Stash` 
6. In Terminal:

   ```bash
    cd [path to Provenance]
    make update
    make open
   ```

7. Return to Xcode: Hit the `▶︎` \(Run\) button.
8. Provenance will compile and run on your device. Unless testing, hit `◼︎` \(Stop\). _Done._

{% hint style="info" %}
To learn more about stashing refer to Tower's [Using the Stash](https://www.git-tower.com/help/mac/working-copy/stash) documentation.
{% endhint %}

## Update & Build

If you've already done the First-time Setup, then you can build from the command-line using the following commands. These commands will pull any updates and build, so you can opt to update and build using only the terminal in the future.

* **iOS \(iPhone, iPad\):**

  ```bash
    make ios
  ```

* **tvOS \(Apple TV\):**

  ```bash
    make tvos
  ```





{% hint style="info" %}
🗯 If you are still stuck ask for [help](https://discord.gg/NhzgrXh) on our Discord.
{% endhint %}

