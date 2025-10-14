# Git CLI Cheat Sheet
Here you have nearly everything you need to know about git in the command line. I am ignoring a lot of options and commands, that might be handy too, but after all, this will get you far in the every day usage of git.
Following the unix conventions variables in `<>` need to be replaced by your own values.
Also be careful what you do, some commands are dangerous and will make you loose data! Also note that some commands might not work if you have a very old git version.



## Table of Contents

- [Cloning/Initializing a Repository](#cloninginitializing-a-repository)
  - [Clone a repository](#clone-a-repository)
  - [Clone a bare repository (without remot ref)](#clone-a-bare-repository-without-remot-ref)
  - [Initialize a new repository and push to remote](#initialize-a-new-repository-and-push-to-remote)
- [Creating/Removing/Switching Branches](#creatingremovingswitching-branches)
  - [Create a branch](#create-a-branch)
  - [Switch to a branch](#switch-to-a-branch)
  - [Delete a branch locally](#delete-a-branch-locally)
  - [Delete a branch remotely](#delete-a-branch-remotely)
- [Merging Branches](#merging-branches)
  - [Merge a branch into the current branch](#merge-a-branch-into-the-current-branch)
  - [Abort a merge](#abort-a-merge)
- [Adding/Commiting/Updating](#addingcommitingupdating)
  - [Stage changes](#stage-changes)
  - [Add all tracked files changes and push](#add-all-tracked-files-changes-and-push)
  - [See remote updates without merging](#see-remote-updates-without-merging)
- [Undo Changes](#undo-changes)
  - [Unstage a file](#unstage-a-file)
  - [Undo last commit but keep changes](#undo-last-commit-but-keep-changes)
  - [Reset working tree to last commit & a loose all changes (dangerous!)](#reset-working-tree-to-last-commit--a-loose-all-changes-dangerous)
  - [Discard unstaged changes (dangerous!)](#discard-unstaged-changes-dangerous)
  - [(careful!) Deletes unstaged changes in tracked files](#careful-deletes-unstaged-changes-in-tracked-files)
  - [Revert a file to a previous state](#revert-a-file-to-a-previous-state)
  - [Revert a commit & create new commit (dangerous!)](#revert-a-commit--create-new-commit-dangerous)
  - [Restore files from a specific commit](#restore-files-from-a-specific-commit)
- [See what happened in the repository](#see-what-happened-in-the-repository)
  - [View commit history (you’ll see what the options do)](#view-commit-history-youll-see-what-the-options-do)
  - [View commits by author](#view-commits-by-author)
  - [Show differences between two commits for a file](#show-differences-between-two-commits-for-a-file)
- [Stashing](#stashing)
  - [Stash current changes in tracked files (it's like saving them in a temp directory)](#stash-current-changes-in-tracked-files-its-like-saving-them-in-a-temp-directory)
  - [List stashes](#list-stashes)
  - [Apply the most recent stash](#apply-the-most-recent-stash)
  - [Apply a specific stash from the list](#apply-a-specific-stash-from-the-list)



## Cloning/Initializing a Repository

  ### Clone a repository
  ```bash
  git clone <repository-url>
  ```

  ### Clone a bare repository (without remot ref)
  ```bash
  git clone --bare <repository-url>
  ```

  ### Initialize a new repository and push to remote
  ```bash
  git init
  git add --all
  git commit -m "Initial project version"
  git remote add origin <git@github.com>:<User>/<UserRepo.git>
  git push -u origin main
  ```

## Creating/Removing/Switching Branches
  ### Create a branch
  ```bash
  git branch <branch-name>
  git push -u <origin> <branch-name>
  ```

  ### Switch to a branch
  ```bash
  git switch <branch-name>
  ```

  ### Delete a branch locally
  ```bash
  git branch -d <branch-name>
  ```

  ### Delete a branch remotely
  ```bash
  git push -d <origin> <branch-name>
  ```

## Merging Branches
  ### Merge a branch into the current branch
  ```bash
  git merge <branch-name>
  ```

  ### Abort a merge
  ```bash
  git merge --abort
  ```

## Adding/Commiting/Updating

  ### Stage changes
  ```bash
  git add <file-name>
  ```

  ### Add all tracked files changes and push
  ```bash
  git commit -a -m "<your-commit-message>"
  # forgot to add something?
  # if so:
  git add <forgotten-file-name>
  git commit --amend
  # if not, just push
  git push


  ```

  ### See remote updates without merging
  ```bash
  git fetch
  ```

## Undo Changes

  ### Unstage a file
  ```bash
  git restore --staged <file-name>
  ```

  ### Undo last commit but keep changes
  ```bash
  git reset --soft HEAD~1
  ```

  ### Reset working tree to last commit & a loose all changes (dangerous!)
  ```bash
  git reset --hard HEAD
  ```

  ### Discard unstaged changes (dangerous!)
  ```bash
  git restore <file-name>
  ```

  ### (careful!) Deletes unstaged changes in tracked files
  ```bash
  git checkout <file-name>
  ```

  ### Revert a file to a previous state
  ```bash
  git restore --source=<commit-reference> <file-1-to-restore> <file-2-to-restore>
  ```

  ### Revert a commit & create new commit (dangerous!)
  ```bash
  git revert <commit-reference>
  ```

  ### Restore files from a specific commit
  ```bash
  git restore --source <commit-reference> <file1> <file2 etc.>
  ```

## See what happened in the repository

  ### View commit history (you’ll see what the options do)
  ```bash
  git log --oneline --graph --decorate
  ```

  ### View commits by author
  ```bash
  git log --author="<author-name>"
  ```

  ### Show differences between two commits for a file
  ```bash
  git diff <commit1> <commit2> -- <file-path>
  ```

## Stashing
  ### Stash current changes in tracked files (it's like saving them in a temp directory)
  ```bash
  git stash push
  #### use the following to stash ALL files
  git stash --all push
  ```
  ### List stashes
  ```bash
  git stash list
  ```
  ### Apply the most recent stash
  ```bash
  git stash apply
  ```
  ### Apply a specific stash from the list
  ```bash
  git stash apply stash@{<n>}
  ```