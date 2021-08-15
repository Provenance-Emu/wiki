All contributions on GitHub are made using fork workflow instead of branchy workflow - which you might be used to. The reason behind this is that the project maintainer do not need to grant you write access to their repository. The following instructions are based on the "GitHub Standard Fork & Pull Request Workflow" by Chase Pettit (Chaser324, see https://gist.github.com/Chaser324/ce0505fbed06b947d962) and have been adapted to suit the Provenance project.

## Creating a Fork
Go to GitHub page and click the "Fork" button
```shell
# Clone your fork to your local machine
git clone --recurse-submodules -j4 git@github.com:username/Provenance.git ProvFork

# Make sure you switch to the cloned source directory
cd ProvFork
```
You'll want to make sure you keep your fork up to date by tracking the original "upstream" repo that you forked. To do this, you'll need to add a remote:
```shell
# Add "upstream" repo to list of remotes
git remote add upstream git@github.com:Provenance-Emu/Provenance.git

# Verify the new remote named 'upstream'
git remote -v
```

## Creating a feature branch
```shell
git checkout -b feature/name-of-your-feature
```

## Keeping Your Fork Up to Date
Whenever you want to update your fork with the latest upstream changes, you'll need to first fetch the upstream repo's branches and latest commits to bring them into your repository. This is either possible on the GitHub page using the "Fetch upstream" button or using git console as described below:

```shell
# Fetch from upstream remote
git fetch upstream

# EITHER Fast-forward your develop (= master) branch to the latest upstream changes (without checking out the develop branch)
git fetch upstream develop:develop

# OR Checkout develop and pull the latest upstream changes
git checkout develop
git pull upstream develop
git push origin develop
```
Now, your local develop (= master) branch is up-to-date with everything modified upstream and you can merge the changes in your feature branch.

```shell
# Merge latest changes in your feature branch
git merge upstream/develop
```

## Creating a Pull request
Pull requests to the Provenance project should contain all changes in a single commit to keep the git history clean. In order to do so, squash all changes of your feature branch into one commit:

```shell
# Checkout your feature branch
git checkout -b feature/name-of-your-feature

# Do a soft reset of your changes to develop
git reset --soft develop

# Add all of the changes in your git repo directory, to the new commit that is going to be created
git add -A

# Commit the same with a message
git commit -m "commit message goes here"

# As you re-wrote the git history, we need to force push to update the remote branch
git push --force origin feature/name-of-your-feature
```
