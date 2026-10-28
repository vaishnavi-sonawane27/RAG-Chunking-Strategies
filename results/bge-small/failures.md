# Failure cases: bge-small, dense retrieval, selected configurations

A question counts as a miss when its first relevant chunk is not in the top 5.

## fixed 200 - q003: wrong document

- **Question:** From which Git release can the name of the initial branch be customised?
- **Evidence (01_first-time-setup):** From Git version 2.28 onwards, you can set a different name for the initial branch.
- **First relevant rank:** 6
- **Top-1 retrieved (03_branch-management):** ame a branch like master/main/mainline without having read the section _changing_master. Suppose you have a branch that is called bad-branch-name and you want to change it to corrected-branch-name, while keeping all history. You also want …

## fixed 200 - q009: wrong document

- **Question:** Why can I keep committing while on a train with no internet?
- **Evidence (01_what-is-git):** you can commit happily (to your local copy, remember?) until you get to a network connection to upload.
- **First relevant rank:** >10
- **Top-1 retrieved (07_reset):** | NO | YES | checkout [commit] <paths> | NO | YES | YES | NO |================================

## fixed 200 - q011: wrong document

- **Question:** What is the formal name for the area that holds what will go into the next commit?
- **Evidence (01_what-is-git):** Its technical name in Git parlance is the "index", but the phrase "staging area" works just as well.
- **First relevant rank:** >10
- **Top-1 retrieved (10_objects):** blank line, and then the commit message. Next, you'll write the other two commit objects, each referencing the commit that came directly before it: $ echo 'Second commit' | git commit-tree 0155eb -p fdf4fc3 cac0cab538b970a37ea1e769cbbde608…

## fixed 200 - q014: wrong document

- **Question:** What goes wrong with the habit of duplicating project folders by hand as a backup scheme?
- **Evidence (01_about-version-control):** It is easy to forget which directory you're in and accidentally write to the wrong file or copy over files you don't mean to.
- **First relevant rank:** 9
- **Top-1 retrieved (02_undoing):** checkout -- <file>..." to discard changes in working directory) modified: CONTRIBUTING.md The command is a bit strange, but it works. The CONTRIBUTING.md file is modified but once again unstaged. ===== It's true that git reset can be a dan…

## fixed 200 - q022: wrong document

- **Question:** Which URL styles can be used to clone, besides https?
- **Evidence (02_getting-a-repository):** you may also see git:// or user@server:path/to/repo.git, which uses the SSH transfer protocol.
- **First relevant rank:** >10
- **Top-1 retrieved (04_protocols):** goes for read access. In fact, for services like GitHub, the URL you use to view the repository online (for example, ^ (https://github.com/schacon/simplegit)) is the same URL you can use to clone and, if you have access, push over. Dumb HT…

## fixed 200 - q048: wrong document

- **Question:** After committing three files, how many objects are stored and of which kinds?
- **Evidence (03_nutshell):** Your Git repository now contains five objects: three blobs
- **First relevant rank:** 10
- **Top-1 retrieved (10_packfiles):** Packfiles If you followed all of the instructions in the example from the previous section, you should now have a test Git repository with 11 objects -- four blobs, three trees, three commits, and one tag: $ find .git/objects -type f git/o…

## fixed 200 - q052: wrong document

- **Question:** What makes a merge commit different from an ordinary commit?
- **Evidence (03_basic-branching-and-merging):** This is referred to as a merge commit, and is special in that it has more than one parent.
- **First relevant rank:** 10
- **Top-1 retrieved (07_advanced-merging):** Merge made by the 'ours' strategy. $ git diff HEAD HEAD~ $ You can see that there is no difference between the branch we were on and the result of the merge. This can often be useful to basically trick Git into thinking that a branch is al…

## fixed 200 - q055: right document, wrong passage

- **Question:** Which two kinds of tags does Git support?
- **Evidence (02_tagging):** Git supports two types of tags: lightweight and annotated.
- **First relevant rank:** 7
- **Top-1 retrieved (02_tagging):** Tagging Like most VCSs, Git has the ability to tag specific points in a repository's history as being important. Typically, people use this functionality to mark release points (v1.0, v2.0 and so on). In this section, you'll learn how to l…

## fixed 200 - q066: wrong document

- **Question:** What does the star next to a branch name in the listing mean?
- **Evidence (03_branch-management):** it indicates the branch that you currently have checked out
- **First relevant rank:** 6
- **Top-1 retrieved (06_3-maintaining):** if you're in your repository and you run git ls-remote origin or whatever remote you want to check, it will show you something similar to this. If the repository is on GitHub and you have any Pull Requests that have been opened, you'll get…

## fixed 200 - q068: wrong document

- **Question:** How do I delete a branch that still has unmerged work?
- **Evidence (03_branch-management):** If you really do want to delete the branch and lose that work, you can force it with -D
- **First relevant rank:** 6
- **Top-1 retrieved (07_rewriting-history):** filter-branch. Its documentation and source code can be found at ^ (https://github.com/newren/git-filter-repo). Removing a File from Every Commit This occurs fairly commonly. Someone accidentally commits a huge binary file with a thoughtle…

## fixed 200 - q069: right document, wrong passage

- **Question:** Is it fine to rename a branch my teammates are using?
- **Evidence (03_branch-management):** Do not rename branches that are still in use by other collaborators.
- **First relevant rank:** >10
- **Top-1 retrieved (03_branch-management):** branch-name remotes/origin/corrected-branch-name remotes/origin/main Notice that you're on the branch corrected-branch-name and it's available on the remote. However, the branch with the bad name is also still present there but you can del…

## fixed 200 - q071: wrong document

- **Question:** Which branches are safe to remove with the lowercase delete flag?
- **Evidence (03_branch-management):** Branches on this list without the * in front of them are generally fine to delete with git branch -d; you've already incorporated their work into another branch, so you're not going to lose anything.
- **First relevant rank:** >10
- **Top-1 retrieved (08_config):** .denyDeletes to true: $ git config --system receive.denyDeletes true This denies any deletion of branches or tags -- no user can do it. To remove remote branches, you must remove the ref files from the server manually. There are also more …

## fixed 200 - q074: wrong document

- **Question:** Does branching and merging involve contacting a server?
- **Evidence (03_workflows):** everything is being done only in your Git repository -- there is no communication with the server
- **First relevant rank:** >10
- **Top-1 retrieved (03_basic-branching-and-merging):** Basic Branching and Merging Let's go through a simple example of branching and merging with a workflow that you might use in the real world. You'll follow these steps: - Do some work on a website. - Create a branch for a new user story you…

## fixed 200 - q075: wrong document

- **Question:** What goes into the proposed-updates branch of large projects?
- **Evidence (03_workflows):** that has integrated branches that may not be ready to go into the next or master branch
- **First relevant rank:** >10
- **Top-1 retrieved (05_maintaining):** a while, you fast-forward your master branch. Large-Merging Workflows The Git project has four long-running branches: master, next, and seen (formerly 'pu' -- proposed updates) for new work, and maint for maintenance backports. When new wo…

## fixed 200 - q077: right document, wrong passage

- **Question:** What does rebasing do, in one sentence?
- **Evidence (03_rebasing):** you can take all the changes that were committed on one branch and replay them on a different branch.
- **First relevant rank:** >10
- **Top-1 retrieved (03_rebasing):** Rebasing In Git, there are two main ways to integrate changes from one branch into another: the merge and the rebase. In this section you'll learn what rebasing is, how to do it, why it's a pretty amazing tool, and in what cases you won't …

## fixed 200 - q080: wrong document

- **Question:** What is a patch-id?
- **Evidence (03_rebasing):** Git also calculates a checksum that is based just on the patch introduced with the commit.
- **First relevant rank:** 6
- **Top-1 retrieved (05_maintaining):** scripts if you want. Applying a Patch with `am` If the contributor is a Git user and was good enough to use the format-patch command to generate their patch, then your job is easier because the patch contains author information and a commi…

## fixed 200 - q081: right document, wrong passage

- **Question:** How can I make pulling replay my commits rather than merge by default?
- **Evidence (03_rebasing):** you can set the pull.rebase config value
- **First relevant rank:** >10
- **Top-1 retrieved (03_rebasing):** to the main project. That way, the maintainer doesn't have to do any integration work -- just a fast-forward or a clean apply. Note that the snapshot pointed to by the final commit you end up with, whether it's the last of the rebased comm…

## fixed 200 - q084: right document, wrong passage

- **Question:** Step by step, how does a rebase work internally?
- **Evidence (03_rebasing):** This operation works by going to the common ancestor of the two branches (the one you're on and the one you're rebasing onto), getting the diff introduced by each commit of the branch you're on, saving those diffs to temporary files, resetting the current branch to the same commit as the branch you are rebasing onto, …
- **First relevant rank:** 8
- **Top-1 retrieved (03_rebasing):** to the main project. That way, the maintainer doesn't have to do any integration work -- just a fast-forward or a clean apply. Note that the snapshot pointed to by the final commit you end up with, whether it's the last of the rebased comm…

## fixed 200 - q089: right document, wrong passage

- **Question:** Why can't I move origin/master by hand?
- **Evidence (03_remote-branches):** They're local references that you can't move; Git moves them for you whenever you do any network communication
- **First relevant rank:** >10
- **Top-1 retrieved (03_remote-branches):** , neither does "origin". While "master" is the default name for a starting branch when you run git init which is the only reason it's widely used, "origin" is the default name for a remote when you run git clone. If you run git clone -o bo…

## fixed 200 - q091: wrong document

- **Question:** Are my local branches pushed to the server automatically?
- **Evidence (03_remote-branches):** Your local branches aren't automatically synchronized to the remotes you write to
- **First relevant rank:** 10
- **Top-1 retrieved (02_remotes):** new work that has been pushed to that server since you cloned (or last fetched from) it. It's important to note that the git fetch command only downloads the data to your local repository -- it doesn't automatically merge it with any of yo…

## fixed 200 - q104: wrong document

- **Question:** Do ignore files in subfolders affect the whole repository?
- **Evidence (02_recording-changes):** The rules in these nested .gitignore files apply only to the files under the directory where they are located.
- **First relevant rank:** 6
- **Top-1 retrieved (08_config):** ignoring. But sometimes you want to ignore certain files for all repositories that you work with. If your computer is running macOS, you're probably familiar with .DS_Store files. If your preferred editor is Emacs or Vim, you know about fi…

## fixed 200 - q107: wrong document

- **Question:** How should I think about what git add really does?
- **Evidence (02_recording-changes):** git add is a multipurpose command -- you use it to begin tracking new files, to stage files, and to do other things like marking merge-conflicted files as resolved. It may be helpful to think of it more as "add precisely this content to the next commit" rather than "add this file to the project
- **First relevant rank:** >10
- **Top-1 retrieved (01_help):** if you don't need the full-blown manpage help, but just need a quick refresher on the available options for a Git command, you can ask for the more concise "help" output with the -h option, as in: $ git add -h usage: git add [<options>] [-…

## fixed 200 - q112: right document, wrong passage

- **Question:** How do I jump back to the branch I was on before?
- **Evidence (03_nutshell):** Return to your previously checked out branch: git switch -.
- **First relevant rank:** 7
- **Top-1 retrieved (03_nutshell):** and then switched back to your main branch and did other work. Both of those changes are isolated in separate branches: you can switch back and forth between the branches and merge them together when you're ready. And you did all that with…

## fixed 200 - q116: right document, wrong passage

- **Question:** What are the two effects of switching back to the master branch?
- **Evidence (03_nutshell):** That command did two things. It moved the HEAD pointer back to point to the master branch, and it reverted the files in your working directory back to the snapshot that master points to.
- **First relevant rank:** >10
- **Top-1 retrieved (03_nutshell):** it reverted the files in your working directory back to the snapshot that master points to. This also means the changes you make from this point forward will diverge from an older version of the project. It essentially rewinds the work you…

## fixed 200 - q124: wrong document

- **Question:** How hard is it to lose committed work, and what makes it safer still?
- **Evidence (01_what-is-git):** It is hard to get the system to do anything that is not undoable or to make it erase data in any way. As with any VCS, you can lose or mess up changes you haven't committed yet, but after you commit a snapshot into Git, it is very difficult to lose, especially if you regularly push your database to another repository.
- **First relevant rank:** >10
- **Top-1 retrieved (01_about-version-control):** that the centralized server represents. If that server goes down for an hour, then during that hour nobody can collaborate at all or save versioned changes to anything they're working on. If the hard disk the central database is on becomes…

## fixed 200 - q125: wrong document

- **Question:** What are the three steps of the basic Git workflow?
- **Evidence (01_what-is-git):** 1. You modify files in your working tree. 2. You selectively stage just those changes you want to be part of your next commit, which adds only those changes to the staging area. 3. You do a commit, which takes the files as they are in the staging area and stores that snapshot permanently to your Git directory.
- **First relevant rank:** >10
- **Top-1 retrieved (07_reset):** these three trees. Git's typical workflow Let's visualize this process: say you go into a new directory with a single file in it. We'll call this v1 of the file, and we'll indicate it in blue. Now we run git init, which will create a Git r…

## fixed 200 - q126: wrong document

- **Question:** Could a corrupted server be restored from a client's clone?
- **Evidence (02_getting-a-repository):** Every version of every file for the history of the project is pulled down by default when you run git clone. In fact, if your server disk gets corrupted, you can often use nearly any of the clones on any client to set the server back to the state it was in when it was cloned
- **First relevant rank:** >10
- **Top-1 retrieved (01_about-version-control):** client repositories can be copied back up to the server to restore it. Every clone is really a full backup of all the data. Distributed version control diagram Furthermore, many of these systems deal pretty well with having several remote …

## sentence 100 - q011: wrong document

- **Question:** What is the formal name for the area that holds what will go into the next commit?
- **Evidence (01_what-is-git):** Its technical name in Git parlance is the "index", but the phrase "staging area" works just as well.
- **First relevant rank:** 10
- **Top-1 retrieved (10_objects):** Next, you'll write the other two commit objects, each referencing the commit that came directly before it: $ echo 'Second commit' | git commit-tree 0155eb -p fdf4fc3 cac0cab538b970a37ea1e769cbbde608743bc96d $ echo 'Third commit' | git comm…

## sentence 100 - q014: wrong document

- **Question:** What goes wrong with the habit of duplicating project folders by hand as a backup scheme?
- **Evidence (01_about-version-control):** It is easy to forget which directory you're in and accidentally write to the wrong file or copy over files you don't mean to.
- **First relevant rank:** >10
- **Top-1 retrieved (04_protocols):** This is often used if everyone on your team has access to a shared filesystem such as an NFS^ (https://en.wikipedia.org/wiki/Network_File_System) mount, or in the less likely case that everyone logs in to the same computer. The latter woul…

## sentence 100 - q020: right document, wrong passage

- **Question:** How does cloning in Git differ from a Subversion-style checkout?
- **Evidence (02_getting-a-repository):** instead of getting just a working copy, Git receives a full copy of nearly all data that the server has.
- **First relevant rank:** 7
- **Top-1 retrieved (02_getting-a-repository):** At this point, you have a Git repository with tracked files and an initial commit. Cloning an Existing Repository If you want to get a copy of an existing Git repository -- for example, a project you'd like to contribute to -- the command …

## sentence 100 - q022: right document, wrong passage

- **Question:** Which URL styles can be used to clone, besides https?
- **Evidence (02_getting-a-repository):** you may also see git:// or user@server:path/to/repo.git, which uses the SSH transfer protocol.
- **First relevant rank:** >10
- **Top-1 retrieved (02_getting-a-repository):** You clone a repository with git clone <url>. For example, if you want to clone the Git linkable library called libgit2, you can do so like this: $ git clone https://github.com/libgit2/libgit2

## sentence 100 - q029: right document, wrong passage

- **Question:** What flag is needed to delete a file from Git when it has staged or modified content?
- **Evidence (02_recording-changes):** If you modified the file or had already added it to the staging area, you must force the removal with the -f option.
- **First relevant rank:** >10
- **Top-1 retrieved (02_recording-changes):** This is convenient, but be careful; sometimes this flag will cause you to include unwanted changes. Removing Files To remove a file from Git, you have to remove it from your tracked files (more accurately, remove it from your staging area)…

## sentence 100 - q031: right document, wrong passage

- **Question:** Does Git remember that a file was renamed?
- **Evidence (02_recording-changes):** Unlike many other VCSs, Git doesn't explicitly track file movement.
- **First relevant rank:** >10
- **Top-1 retrieved (02_recording-changes):** If you rename a file in Git, no metadata is stored in Git that tells it you renamed the file. However, Git is pretty smart about figuring that out after the fact -- we'll deal with detecting file movement a bit later. Thus it's a bit confu…

## sentence 100 - q033: right document, wrong passage

- **Question:** In what order does the history command list commits when run without options?
- **Evidence (02_viewing-history):** lists the commits made in that repository in reverse chronological order
- **First relevant rank:** 7
- **Top-1 retrieved (02_viewing-history):** This command works with lots of formats -- you can specify a specific date like "2008-01-15", or a relative date such as "2 years 1 day 3 minutes ago". You can also filter the list to commits that match some search criteria. The --author o…

## sentence 100 - q047: right document, wrong passage

- **Question:** Is the default branch special compared with other branches?
- **Evidence (03_nutshell):** The only reason nearly every repository has one is that the git init command creates it by default
- **First relevant rank:** >10
- **Top-1 retrieved (03_nutshell):** A branch in Git is simply a lightweight movable pointer to one of these commits. The default branch name in Git is master. As you start making commits, you're given a master branch that points to the last commit you made. Every time you co…

## sentence 100 - q052: wrong document

- **Question:** What makes a merge commit different from an ordinary commit?
- **Evidence (03_basic-branching-and-merging):** This is referred to as a merge commit, and is special in that it has more than one parent.
- **First relevant rank:** >10
- **Top-1 retrieved (06_3-maintaining):** If the merge is trivial, you can also just hit the "Merge" button on the GitHub site. This will do a "non-fast-forward" merge, creating a merge commit even if a fast-forward merge was possible. This means that no matter what, every time yo…

## sentence 100 - q065: right document, wrong passage

- **Question:** Will Git guess my command if I type only part of its name?
- **Evidence (02_aliases):** Git doesn't automatically infer your command if you type it in partially.
- **First relevant rank:** >10
- **Top-1 retrieved (02_aliases):** If you don't want to type the entire text of each of the Git commands, you can easily set up an alias for each command using git config. Here are a couple of examples you may want to set up: $ git config --global alias.co checkout $ git co…

## sentence 100 - q069: right document, wrong passage

- **Question:** Is it fine to rename a branch my teammates are using?
- **Evidence (03_branch-management):** Do not rename branches that are still in use by other collaborators.
- **First relevant rank:** 6
- **Top-1 retrieved (03_branch-management):** Suppose you have a branch that is called bad-branch-name and you want to change it to corrected-branch-name, while keeping all history. You also want to change the branch name on the remote (GitHub, GitLab, other server). How do you do thi…

## sentence 100 - q077: right document, wrong passage

- **Question:** What does rebasing do, in one sentence?
- **Evidence (03_rebasing):** you can take all the changes that were committed on one branch and replay them on a different branch.
- **First relevant rank:** >10
- **Top-1 retrieved (03_rebasing):** Rebasing In Git, there are two main ways to integrate changes from one branch into another: the merge and the rebase. In this section you'll learn what rebasing is, how to do it, why it's a pretty amazing tool, and in what cases you won't …

## sentence 100 - q079: wrong document

- **Question:** What is the main rule to follow when rebasing?
- **Evidence (03_rebasing):** Do not rebase commits that exist outside your repository and that people may have based work on.
- **First relevant rank:** >10
- **Top-1 retrieved (07_rerere):** This same tactic can be used if you want to keep a branch rebased so you don't have to deal with the same rebasing conflicts each time you do it. Or if you want to take a branch that you merged and fixed a bunch of conflicts and then decid…

## sentence 100 - q080: wrong document

- **Question:** What is a patch-id?
- **Evidence (03_rebasing):** Git also calculates a checksum that is based just on the patch introduced with the commit.
- **First relevant rank:** >10
- **Top-1 retrieved (05_maintaining):** The Commit information indicates the person who applied the patch and the time it was applied. The Author information is the individual who originally created the patch and when it was originally created. But it's possible that the patch w…

## sentence 100 - q081: wrong document

- **Question:** How can I make pulling replay my commits rather than merge by default?
- **Evidence (03_rebasing):** you can set the pull.rebase config value
- **First relevant rank:** >10
- **Top-1 retrieved (07_advanced-merging):** This approach also won't work if any other commits have been created since the merge; moving the refs would effectively lose those changes. Reverse the commit If moving the branch pointers around isn't going to work for you, Git gives you …

## sentence 100 - q084: wrong document

- **Question:** Step by step, how does a rebase work internally?
- **Evidence (03_rebasing):** This operation works by going to the common ancestor of the two branches (the one you're on and the one you're rebasing onto), getting the diff introduced by each commit of the branch you're on, saving those diffs to temporary files, resetting the current branch to the same commit as the branch you are rebasing onto, …
- **First relevant rank:** 7
- **Top-1 retrieved (07_rewriting-history):** See ch10-git-internals#_data_recovery for more information on the reflog command. Drew DeVault made a practical hands-on guide with exercises to learn how to use git rebase. You can find it at: ^ (https://git-rebase.io/) The Nuclear Option…

## sentence 100 - q089: right document, wrong passage

- **Question:** Why can't I move origin/master by hand?
- **Evidence (03_remote-branches):** They're local references that you can't move; Git moves them for you whenever you do any network communication
- **First relevant rank:** >10
- **Top-1 retrieved (03_remote-branches):** If you do some work on your local master branch, and, in the meantime, someone else pushes to git.ourcompany.com and updates its master branch, then your histories move forward differently. Also, as long as you stay out of contact with you…

## sentence 100 - q091: right document, wrong passage

- **Question:** Are my local branches pushed to the server automatically?
- **Evidence (03_remote-branches):** Your local branches aren't automatically synchronized to the remotes you write to
- **First relevant rank:** 10
- **Top-1 retrieved (03_remote-branches):** Now, your local branch sf will automatically pull from origin/serverfix. If you already have a local branch and want to set it to a remote branch you just pulled down, or want to change the upstream branch you're tracking, you can use the …

## sentence 100 - q104: wrong document

- **Question:** Do ignore files in subfolders affect the whole repository?
- **Evidence (02_recording-changes):** The rules in these nested .gitignore files apply only to the files under the directory where they are located.
- **First relevant rank:** >10
- **Top-1 retrieved (08_attributes):** You can tell Git not to export certain files or directories when generating an archive. If there is a subdirectory or file that you don't want to include in your archive file but that you do want checked into your project, you can determin…

## sentence 100 - q112: wrong document

- **Question:** How do I jump back to the branch I was on before?
- **Evidence (03_nutshell):** Return to your previously checked out branch: git switch -.
- **First relevant rank:** >10
- **Top-1 retrieved (05_maintaining):** When you have work in a topic branch and have determined that you want to integrate it, you move to that branch and run the rebase command to rebuild the changes on top of your current master (or develop, and so on) branch. If that works w…

## sentence 100 - q119: right document, wrong passage

- **Question:** Why does the book use the terminal instead of graphical clients?
- **Evidence (01_command-line):** the command line is the only place you can run all Git commands
- **First relevant rank:** 9
- **Top-1 retrieved (01_command-line):** If you know how to run the command-line version, you can probably also figure out how to run the GUI version, while the opposite is not necessarily true. Also, while your choice of graphical client is a matter of personal taste, all users …

## sentence 100 - q125: wrong document

- **Question:** What are the three steps of the basic Git workflow?
- **Evidence (01_what-is-git):** 1. You modify files in your working tree. 2. You selectively stage just those changes you want to be part of your next commit, which adds only those changes to the staging area. 3. You do a commit, which takes the files as they are in the staging area and stores that snapshot permanently to your Git directory.
- **First relevant rank:** 7
- **Top-1 retrieved (07_reset):** Think of the working directory as a sandbox, where you can try changes out before committing them to your staging area (index) and then to history. $ tree . ├── README ├── Rakefile └── lib └── simplegit.rb 1 directory, 3 files The Workflow…

## recursive 200 - q011: wrong document

- **Question:** What is the formal name for the area that holds what will go into the next commit?
- **Evidence (01_what-is-git):** Its technical name in Git parlance is the "index", but the phrase "staging area" works just as well.
- **First relevant rank:** >10
- **Top-1 retrieved (03_nutshell):** Your Git repository now contains five objects: three blobs (each representing the contents of one of the three files), one tree that lists the contents of the directory and specifies which file names are stored as which blobs, and one comm…

## recursive 200 - q013: wrong document

- **Question:** Which part of a Git project holds the metadata and the object database?
- **Evidence (01_what-is-git):** The Git directory is where Git stores the metadata and object database for your project.
- **First relevant rank:** 7
- **Top-1 retrieved (10_plumbing-porcelain):** This leaves four important entries: the HEAD and (yet to be created) index files, and the objects and refs directories. These are the core parts of Git. The objects directory stores all the content for your database, the refs directory sto…

## recursive 200 - q022: wrong document

- **Question:** Which URL styles can be used to clone, besides https?
- **Evidence (02_getting-a-repository):** you may also see git:// or user@server:path/to/repo.git, which uses the SSH transfer protocol.
- **First relevant rank:** >10
- **Top-1 retrieved (04_protocols):** In fact, for services like GitHub, the URL you use to view the repository online (for example, ^ (https://github.com/schacon/simplegit)) is the same URL you can use to clone and, if you have access, push over. Dumb HTTP

## recursive 200 - q029: right document, wrong passage

- **Question:** What flag is needed to delete a file from Git when it has staged or modified content?
- **Evidence (02_recording-changes):** If you modified the file or had already added it to the staging area, you must force the removal with the -f option.
- **First relevant rank:** 10
- **Top-1 retrieved (02_recording-changes):** If you simply remove the file from your working directory, it shows up under the "Changes not staged for commit" (that is, unstaged) area of your git status output: $ rm PROJECTS.md $ git status On branch master Your branch is up-to-date w…

## recursive 200 - q048: wrong document

- **Question:** After committing three files, how many objects are stored and of which kinds?
- **Evidence (03_nutshell):** Your Git repository now contains five objects: three blobs
- **First relevant rank:** >10
- **Top-1 retrieved (10_packfiles):** The objects that remain are the blobs that aren't pointed to by any commit -- in this case, the "what is up, doc?" example and the "test content" example blobs you created earlier. Because you never added them to any commits, they're consi…

## recursive 200 - q060: right document, wrong passage

- **Question:** What happens to a commit I make while sitting on a checked-out tag?
- **Evidence (02_tagging):** your new commit won't belong to any branch and will be unreachable, except by the exact commit hash
- **First relevant rank:** 6
- **Top-1 retrieved (02_tagging):** The second (and more intuitive) way to delete a remote tag is with: $ git push origin --delete <tagname> Checking out Tags If you want to view the versions of files a tag is pointing to, you can do a git checkout of that tag, although this…

## recursive 200 - q075: wrong document

- **Question:** What goes into the proposed-updates branch of large projects?
- **Evidence (03_workflows):** that has integrated branches that may not be ready to go into the next or master branch
- **First relevant rank:** 6
- **Top-1 retrieved (05_maintaining):** If you have a more important project, you might want to use a two-phase merge cycle. In this scenario, you have two long-running branches, master and develop, in which you determine that master is updated only when a very stable release is…

## recursive 200 - q077: right document, wrong passage

- **Question:** What does rebasing do, in one sentence?
- **Evidence (03_rebasing):** you can take all the changes that were committed on one branch and replay them on a different branch.
- **First relevant rank:** >10
- **Top-1 retrieved (03_rebasing):** The Perils of Rebasing Ahh, but the bliss of rebasing isn't without its drawbacks, which can be summed up in a single line: Do not rebase commits that exist outside your repository and that people may have based work on. If you follow that…

## recursive 200 - q080: wrong document

- **Question:** What is a patch-id?
- **Evidence (03_rebasing):** Git also calculates a checksum that is based just on the patch introduced with the commit.
- **First relevant rank:** 6
- **Top-1 retrieved (05_maintaining):** To apply a patch generated by format-patch, you use git am (the command is named am as it is used to "apply a series of patches from a mailbox"). Technically, git am is built to read an mbox file, which is a simple, plain-text format for s…

## recursive 200 - q081: right document, wrong passage

- **Question:** How can I make pulling replay my commits rather than merge by default?
- **Evidence (03_rebasing):** you can set the pull.rebase config value
- **First relevant rank:** >10
- **Top-1 retrieved (03_rebasing):** Note that the snapshot pointed to by the final commit you end up with, whether it's the last of the rebased commits for a rebase or the final merge commit after a merge, is the same snapshot -- it's only the history that is different. Reba…

## recursive 200 - q084: right document, wrong passage

- **Question:** Step by step, how does a rebase work internally?
- **Evidence (03_rebasing):** This operation works by going to the common ancestor of the two branches (the one you're on and the one you're rebasing onto), getting the diff introduced by each commit of the branch you're on, saving those diffs to temporary files, resetting the current branch to the same commit as the branch you are rebasing onto, …
- **First relevant rank:** >10
- **Top-1 retrieved (03_rebasing):** - Determine what work is unique to our branch (C2, C3, C4, C6, C7) - Determine which are not merge commits (C2, C3, C4) - Determine which have not been rewritten into the target branch (just C2 and C3, since C4 is the same patch as C4') - …

## recursive 200 - q087: right document, wrong passage

- **Question:** What is the argument for tidying up commits before merging them?
- **Evidence (03_rebasing):** The opposing point of view is that the commit history is the story of how your project was made. You wouldn't publish the first draft of a book, so why show your messy work?
- **First relevant rank:** 6
- **Top-1 retrieved (03_rebasing):** Now, to the question of whether merging or rebasing is better: hopefully you'll see that it's not that simple. Git is a powerful tool, and allows you to do many things to and with your history, but every team and every project is different…

## recursive 200 - q089: right document, wrong passage

- **Question:** Why can't I move origin/master by hand?
- **Evidence (03_remote-branches):** They're local references that you can't move; Git moves them for you whenever you do any network communication
- **First relevant rank:** >10
- **Top-1 retrieved (03_remote-branches):** ."origin" is not special Just like the branch name "master" does not have any special meaning in Git, neither does "origin". While "master" is the default name for a starting branch when you run git init which is the only reason it's widel…

## recursive 200 - q091: wrong document

- **Question:** Are my local branches pushed to the server automatically?
- **Evidence (03_remote-branches):** Your local branches aren't automatically synchronized to the remotes you write to
- **First relevant rank:** 9
- **Top-1 retrieved (10_refspec):** If they want Git to do that automatically each time they run git push origin, they can add a push value to their config file: url = https://github.com/schacon/simplegit-progit fetch = +refs/heads/:refs/remotes/origin/ push = refs/heads/mas…

## recursive 200 - q092: right document, wrong passage

- **Question:** How can a local branch be pushed under a different name on the remote?
- **Evidence (03_remote-branches):** You can use this format to push a local branch into a remote branch that is named differently.
- **First relevant rank:** 6
- **Top-1 retrieved (03_remote-branches):** Remote-tracking branch names take the form <remote>/<branch>. For instance, if you wanted to see what the master branch on your origin remote looked like as of the last time you communicated with it, you would check the origin/master branc…

## recursive 200 - q093: wrong document

- **Question:** After fetching a new remote branch do I get an editable local copy of it?
- **Evidence (03_remote-branches):** you don't automatically have local, editable copies of them
- **First relevant rank:** 10
- **Top-1 retrieved (05_maintaining):** If your contribution came from a Git user who set up their own repository, pushed a number of changes into it, and then sent you the URL to the repository and the name of the remote branch the changes are in, you can add them as a remote a…

## recursive 200 - q100: right document, wrong passage

- **Question:** What does the status command report right after a fresh clone?
- **Evidence (02_recording-changes):** This means you have a clean working directory; in other words, none of your tracked files are modified.
- **First relevant rank:** >10
- **Top-1 retrieved (02_recording-changes):** Let's change a file that was already tracked. If you change a previously tracked file called CONTRIBUTING.md and then run your git status command again, you get something that looks like this: $ git status On branch master Your branch is u…

## recursive 200 - q104: wrong document

- **Question:** Do ignore files in subfolders affect the whole repository?
- **Evidence (02_recording-changes):** The rules in these nested .gitignore files apply only to the files under the directory where they are located.
- **First relevant rank:** 8
- **Top-1 retrieved (08_attributes):** You can tell Git not to export certain files or directories when generating an archive. If there is a subdirectory or file that you don't want to include in your archive file but that you do want checked into your project, you can determin…

## recursive 200 - q107: wrong document

- **Question:** How should I think about what git add really does?
- **Evidence (02_recording-changes):** git add is a multipurpose command -- you use it to begin tracking new files, to stage files, and to do other things like marking merge-conflicted files as resolved. It may be helpful to think of it more as "add precisely this content to the next commit" rather than "add this file to the project
- **First relevant rank:** >10
- **Top-1 retrieved (07_interactive-staging):** Interactive Staging In this section, you'll look at a few interactive Git commands that can help you craft your commits to include only certain combinations and parts of files. These tools are helpful if you modify a number of files extens…

## recursive 200 - q109: right document, wrong passage

- **Question:** What does git rm do beyond removing the file from disk?
- **Evidence (02_recording-changes):** To remove a file from Git, you have to remove it from your tracked files (more accurately, remove it from your staging area) and then commit. The git rm command does that, and also removes the file from your working directory so you don't see it as an untracked file the next time around.
- **First relevant rank:** >10
- **Top-1 retrieved (02_recording-changes):** If you simply remove the file from your working directory, it shows up under the "Changes not staged for commit" (that is, unstaged) area of your git status output: $ rm PROJECTS.md $ git status On branch master Your branch is up-to-date w…

## recursive 200 - q112: wrong document

- **Question:** How do I jump back to the branch I was on before?
- **Evidence (03_nutshell):** Return to your previously checked out branch: git switch -.
- **First relevant rank:** >10
- **Top-1 retrieved (03_branch-management):** Your local master branch is gone, as it's replaced with the main branch. The main branch is present on the remote. However, the old master branch is still present on the remote. Other collaborators will continue to use the master branch as…

## recursive 200 - q124: wrong document

- **Question:** How hard is it to lose committed work, and what makes it safer still?
- **Evidence (01_what-is-git):** It is hard to get the system to do anything that is not undoable or to make it erase data in any way. As with any VCS, you can lose or mess up changes you haven't committed yet, but after you commit a snapshot into Git, it is very difficult to lose, especially if you regularly push your database to another repository.
- **First relevant rank:** >10
- **Top-1 retrieved (07_rewriting-history):** Don't push your work until you're happy with it One of the cardinal rules of Git is that, since so much work is local within your clone, you have a great deal of freedom to rewrite your history locally. However, once you push your work, it…

## recursive 200 - q125: wrong document

- **Question:** What are the three steps of the basic Git workflow?
- **Evidence (01_what-is-git):** 1. You modify files in your working tree. 2. You selectively stage just those changes you want to be part of your next commit, which adds only those changes to the staging area. 3. You do a commit, which takes the files as they are in the staging area and stores that snapshot permanently to your Git directory.
- **First relevant rank:** >10
- **Top-1 retrieved (05_contributing):** All these questions can affect how you contribute effectively to a project and what workflows are preferred or available to you. We'll cover aspects of each of these in a series of use cases, moving from simple to more complex; you should …

## fixed_overlap 200+80 - q022: wrong document

- **Question:** Which URL styles can be used to clone, besides https?
- **Evidence (02_getting-a-repository):** you may also see git:// or user@server:path/to/repo.git, which uses the SSH transfer protocol.
- **First relevant rank:** >10
- **Top-1 retrieved (04_protocols):** uses the same data-transfer mechanism as the SSH protocol but without the encryption and authentication overhead. The Cons Due to the lack of TLS or other cryptography, cloning over git:// might lead to an arbitrary code execution vulnerab…

## fixed_overlap 200+80 - q041: wrong document

- **Question:** What is the standard nickname for the server a repository was cloned from?
- **Evidence (02_remotes):** origin -- that is the default name Git gives to the server you cloned from
- **First relevant rank:** >10
- **Top-1 retrieved (05_contributing):** shared repository. The first developer, John, clones the repository, makes a change, and commits locally. The protocol messages have been replaced with ... in these examples to shorten them somewhat. # John's Machine $ git clone john@githo…

## fixed_overlap 200+80 - q048: wrong document

- **Question:** After committing three files, how many objects are stored and of which kinds?
- **Evidence (03_nutshell):** Your Git repository now contains five objects: three blobs
- **First relevant rank:** >10
- **Top-1 retrieved (10_packfiles):** Packfiles If you followed all of the instructions in the example from the previous section, you should now have a test Git repository with 11 objects -- four blobs, three trees, three commits, and one tag: $ find .git/objects -type f git/o…

## fixed_overlap 200+80 - q052: wrong document

- **Question:** What makes a merge commit different from an ordinary commit?
- **Evidence (03_basic-branching-and-merging):** This is referred to as a merge commit, and is special in that it has more than one parent.
- **First relevant rank:** 9
- **Top-1 retrieved (07_rewriting-history):** no original merge commit was # . specified). Use -c <commit> to reword the commit message. # # These lines can be re-ordered; they are executed from top to bottom. # # If you remove a line here THAT COMMIT WILL BE LOST. # # However, if you…

## fixed_overlap 200+80 - q066: wrong document

- **Question:** What does the star next to a branch name in the listing mean?
- **Evidence (03_branch-management):** it indicates the branch that you currently have checked out
- **First relevant rank:** 8
- **Top-1 retrieved (02_recording-changes):** 't see any untracked files, or they would be listed here. Finally, the command tells you which branch you're on and informs you that it has not diverged from the same branch on the server. For now, that branch is always master, which is th…

## fixed_overlap 200+80 - q071: wrong document

- **Question:** Which branches are safe to remove with the lowercase delete flag?
- **Evidence (03_branch-management):** Branches on this list without the * in front of them are generally fine to delete with git branch -d; you've already incorporated their work into another branch, so you're not going to lose anything.
- **First relevant rank:** 9
- **Top-1 retrieved (07_stashing-cleaning):** the --dry-run (or -n) option, which means "do a dry run and tell me what you would have removed". $ git clean -d -n Would remove test.o Would remove tmp/ By default, the git clean command will only remove untracked files that are not ignor…

## fixed_overlap 200+80 - q077: right document, wrong passage

- **Question:** What does rebasing do, in one sentence?
- **Evidence (03_rebasing):** you can take all the changes that were committed on one branch and replay them on a different branch.
- **First relevant rank:** >10
- **Top-1 retrieved (03_rebasing):** , but rebasing makes for a cleaner history. If you examine the log of a rebased branch, it looks like a linear history: it appears that all the work happened in series, even when it originally happened in parallel. Often, you'll do this to…

## fixed_overlap 200+80 - q080: wrong document

- **Question:** What is a patch-id?
- **Evidence (03_rebasing):** Git also calculates a checksum that is based just on the patch introduced with the commit.
- **First relevant rank:** 8
- **Top-1 retrieved (05_maintaining):** information indicates the person who applied the patch and the time it was applied. The Author information is the individual who originally created the patch and when it was originally created. But it's possible that the patch won't apply …

## fixed_overlap 200+80 - q081: right document, wrong passage

- **Question:** How can I make pulling replay my commits rather than merge by default?
- **Evidence (03_rebasing):** you can set the pull.rebase config value
- **First relevant rank:** 6
- **Top-1 retrieved (03_rebasing):** to the main project. That way, the maintainer doesn't have to do any integration work -- just a fast-forward or a clean apply. Note that the snapshot pointed to by the final commit you end up with, whether it's the last of the rebased comm…

## fixed_overlap 200+80 - q084: right document, wrong passage

- **Question:** Step by step, how does a rebase work internally?
- **Evidence (03_rebasing):** This operation works by going to the common ancestor of the two branches (the one you're on and the one you're rebasing onto), getting the diff introduced by each commit of the branch you're on, saving those diffs to temporary files, resetting the current branch to the same commit as the branch you are rebasing onto, …
- **First relevant rank:** >10
- **Top-1 retrieved (03_rebasing):** , but rebasing makes for a cleaner history. If you examine the log of a rebased branch, it looks like a linear history: it appears that all the work happened in series, even when it originally happened in parallel. Often, you'll do this to…

## fixed_overlap 200+80 - q089: wrong document

- **Question:** Why can't I move origin/master by hand?
- **Evidence (03_remote-branches):** They're local references that you can't move; Git moves them for you whenever you do any network communication
- **First relevant rank:** >10
- **Top-1 retrieved (03_branch-management):** > origin/master remotes/origin/main remotes/origin/master Your local master branch is gone, as it's replaced with the main branch. The main branch is present on the remote. However, the old master branch is still present on the remote. Oth…

## fixed_overlap 200+80 - q092: wrong document

- **Question:** How can a local branch be pushed under a different name on the remote?
- **Evidence (03_remote-branches):** You can use this format to push a local branch into a remote branch that is named differently.
- **First relevant rank:** 7
- **Top-1 retrieved (03_branch-management):** ame a branch like master/main/mainline without having read the section _changing_master. Suppose you have a branch that is called bad-branch-name and you want to change it to corrected-branch-name, while keeping all history. You also want …

## fixed_overlap 200+80 - q101: wrong document

- **Question:** Why do newer repositories often start on main instead of master?
- **Evidence (02_recording-changes):** GitHub changed the default branch name from master to main in mid-2020, and other Git hosts followed suit.
- **First relevant rank:** >10
- **Top-1 retrieved (03_branch-management):** > origin/master remotes/origin/main remotes/origin/master Your local master branch is gone, as it's replaced with the main branch. The main branch is present on the remote. However, the old master branch is still present on the remote. Oth…

## fixed_overlap 200+80 - q104: right document, wrong passage

- **Question:** Do ignore files in subfolders affect the whole repository?
- **Evidence (02_recording-changes):** The rules in these nested .gitignore files apply only to the files under the directory where they are located.
- **First relevant rank:** >10
- **Top-1 retrieved (02_recording-changes):** .gitignore file: # ignore all .a files *.a # but do track lib.a, even though you're ignoring .a files above !lib.a # only ignore the TODO file in the current directory, not subdir/TODO /TODO # ignore all files in any directory named build …

## fixed_overlap 200+80 - q107: wrong document

- **Question:** How should I think about what git add really does?
- **Evidence (02_recording-changes):** git add is a multipurpose command -- you use it to begin tracking new files, to stage files, and to do other things like marking merge-conflicted files as resolved. It may be helpful to think of it more as "add precisely this content to the next commit" rather than "add this file to the project
- **First relevant rank:** >10
- **Top-1 retrieved (01_help):** "help" output with the -h option, as in: $ git add -h usage: git add [<options>] [--] <pathspec>... -n, --dry-run dry run -v, --verbose be verbose -i, --interactive interactive picking -p, --patch select hunks interactively -e, --edit edit…

## fixed_overlap 200+80 - q110: wrong document

- **Question:** Why must I commit before switching branches?
- **Evidence (03_basic-branching-and-merging):** if your working directory or staging area has uncommitted changes that conflict with the branch you're checking out, Git won't let you switch branches.
- **First relevant rank:** >10
- **Top-1 retrieved (03_nutshell):** which involves copying all of the project's files into a second directory. This can take several seconds or even minutes, depending on the size of the project, whereas in Git the process is always instantaneous. Also, because we're recordi…

## fixed_overlap 200+80 - q112: wrong document

- **Question:** How do I jump back to the branch I was on before?
- **Evidence (03_nutshell):** Return to your previously checked out branch: git switch -.
- **First relevant rank:** >10
- **Top-1 retrieved (07_rewriting-history):** the sequence that depend on the one you just deleted. If you get partway through a rebase like this and decide it's not a good idea, you can always stop. Type git rebase --abort, and your repo will be returned to the state it was in before…

## fixed_overlap 200+80 - q116: right document, wrong passage

- **Question:** What are the two effects of switching back to the master branch?
- **Evidence (03_nutshell):** That command did two things. It moved the HEAD pointer back to point to the master branch, and it reverted the files in your working directory back to the snapshot that master points to.
- **First relevant rank:** >10
- **Top-1 retrieved (03_nutshell):** it reverted the files in your working directory back to the snapshot that master points to. This also means the changes you make from this point forward will diverge from an older version of the project. It essentially rewinds the work you…

## fixed_overlap 200+80 - q124: wrong document

- **Question:** How hard is it to lose committed work, and what makes it safer still?
- **Evidence (01_what-is-git):** It is hard to get the system to do anything that is not undoable or to make it erase data in any way. As with any VCS, you can lose or mess up changes you haven't committed yet, but after you commit a snapshot into Git, it is very difficult to lose, especially if you regularly push your database to another repository.
- **First relevant rank:** >10
- **Top-1 retrieved (01_about-version-control):** that the centralized server represents. If that server goes down for an hour, then during that hour nobody can collaborate at all or save versioned changes to anything they're working on. If the hard disk the central database is on becomes…

## fixed_overlap 200+80 - q125: wrong document

- **Question:** What are the three steps of the basic Git workflow?
- **Evidence (01_what-is-git):** 1. You modify files in your working tree. 2. You selectively stage just those changes you want to be part of your next commit, which adds only those changes to the staging area. 3. You do a commit, which takes the files as they are in the staging area and stores that snapshot permanently to your Git directory.
- **First relevant rank:** >10
- **Top-1 retrieved (07_reset):** le └── lib └── simplegit.rb 1 directory, 3 files The Workflow Git's typical workflow is to record snapshots of your project in successively better states, by manipulating these three trees. Git's typical workflow Let's visualize this proce…

## fixed_overlap 200+80 - q129: wrong document

- **Question:** Why use a custom log format when a script will parse the output?
- **Evidence (02_viewing-history):** The most interesting option value is format, which allows you to specify your own log output format. This is especially useful when you're generating output for machine parsing -- because you specify the format explicitly, you know it won't change with updates to Git
- **First relevant rank:** 10
- **Top-1 retrieved (08_attributes):** wrapping: $ echo '$Format:Last commit: %h by %aN at %cd%n%+w(76,6,9)%B$' > LAST_COMMIT $ git commit -am 'export-subst uses git log'\''s custom formatter git archive uses git log'\''s pretty=format: processor directly, and strips the surrou…

## semantic p85 - q014: right document, wrong passage

- **Question:** What goes wrong with the habit of duplicating project folders by hand as a backup scheme?
- **Evidence (01_about-version-control):** It is easy to forget which directory you're in and accidentally write to the wrong file or copy over files you don't mean to.
- **First relevant rank:** >10
- **Top-1 retrieved (01_about-version-control):** However, this setup also has some serious downsides. The most obvious is the single point of failure that the centralized server represents. If that server goes down for an hour, then during that hour nobody can collaborate at all or save …

## semantic p85 - q022: wrong document

- **Question:** Which URL styles can be used to clone, besides https?
- **Evidence (02_getting-a-repository):** you may also see git:// or user@server:path/to/repo.git, which uses the SSH transfer protocol.
- **First relevant rank:** >10
- **Top-1 retrieved (07_submodules):** ===== Since the URL in the .gitmodules file is what other people will first try to clone/fetch from, make sure to use a URL that they can access if possible. For example, if you use a different URL to push to than others would to pull from…

## semantic p85 - q041: wrong document

- **Question:** What is the standard nickname for the server a repository was cloned from?
- **Evidence (02_remotes):** origin -- that is the default name Git gives to the server you cloned from
- **First relevant rank:** 7
- **Top-1 retrieved (04_git-on-a-server):** This is generally straightforward to do. In order to clone your repository to create a new bare repository, you run the clone command with the --bare option. By convention, bare repository directory names end with the suffix .git, like so:…

## semantic p85 - q048: wrong document

- **Question:** After committing three files, how many objects are stored and of which kinds?
- **Evidence (03_nutshell):** Your Git repository now contains five objects: three blobs
- **First relevant rank:** >10
- **Top-1 retrieved (10_transfer-protocols):** Next, you have two more objects to retrieve – cfda3b, which is the tree of content that the commit we just retrieved points to; and 085bb3, which is the parent commit: => GET objects/08/5bb3bcb608e1e8451d4b2432f8ecbe6306e7e7 (179 bytes of …

## semantic p85 - q052: wrong document

- **Question:** What makes a merge commit different from an ordinary commit?
- **Evidence (03_basic-branching-and-merging):** This is referred to as a merge commit, and is special in that it has more than one parent.
- **First relevant rank:** >10
- **Top-1 retrieved (05_contributing):** The --squash option takes all the work on the merged branch and squashes it into one changeset producing the repository state as if a real merge happened, without actually making a merge commit. This means your future commit will have one …

## semantic p85 - q056: wrong document

- **Question:** What does a lightweight tag amount to?
- **Evidence (02_tagging):** A lightweight tag is very much like a branch that doesn't change -- it's just a pointer to a specific commit.
- **First relevant rank:** 6
- **Top-1 retrieved (10_refs):** That is all a lightweight tag is -- a reference that never moves. An annotated tag is more complex, however. If you create an annotated tag, Git creates a tag object and then writes a reference to point to it rather than directly to the co…

## semantic p85 - q073: wrong document

- **Question:** Why do some teams keep a develop or next branch next to master?
- **Evidence (03_workflows):** whenever it gets to a stable state, it can be merged into master
- **First relevant rank:** 6
- **Top-1 retrieved (05_maintaining):** This means master almost always moves forward, next is rebased occasionally, and seen is rebased even more often: Merging contributed topic branches into long-term integration branches When a topic branch has finally been merged into maste…

## semantic p85 - q077: right document, wrong passage

- **Question:** What does rebasing do, in one sentence?
- **Evidence (03_rebasing):** you can take all the changes that were committed on one branch and replay them on a different branch.
- **First relevant rank:** >10
- **Top-1 retrieved (03_rebasing):** There is no difference in the end product of the integration, but rebasing makes for a cleaner history. If you examine the log of a rebased branch, it looks like a linear history: it appears that all the work happened in series, even when …

## semantic p85 - q079: right document, wrong passage

- **Question:** What is the main rule to follow when rebasing?
- **Evidence (03_rebasing):** Do not rebase commits that exist outside your repository and that people may have based work on.
- **First relevant rank:** 7
- **Top-1 retrieved (03_rebasing):** Rebasing In Git, there are two main ways to integrate changes from one branch into another: the merge and the rebase. In this section you'll learn what rebasing is, how to do it, why it's a pretty amazing tool, and in what cases you won't …

## semantic p85 - q080: wrong document

- **Question:** What is a patch-id?
- **Evidence (03_rebasing):** Git also calculates a checksum that is based just on the patch introduced with the commit.
- **First relevant rank:** >10
- **Top-1 retrieved (05_maintaining):** Applying a Patch with `am` If the contributor is a Git user and was good enough to use the format-patch command to generate their patch, then your job is easier because the patch contains author information and a commit message for you. If…

## semantic p85 - q084: right document, wrong passage

- **Question:** Step by step, how does a rebase work internally?
- **Evidence (03_rebasing):** This operation works by going to the common ancestor of the two branches (the one you're on and the one you're rebasing onto), getting the diff introduced by each commit of the branch you're on, saving those diffs to temporary files, resetting the current branch to the same commit as the branch you are rebasing onto, …
- **First relevant rank:** >10
- **Top-1 retrieved (03_rebasing):** That way, the maintainer doesn't have to do any integration work -- just a fast-forward or a clean apply. Note that the snapshot pointed to by the final commit you end up with, whether it's the last of the rebased commits for a rebase or t…

## semantic p85 - q089: wrong document

- **Question:** Why can't I move origin/master by hand?
- **Evidence (03_remote-branches):** They're local references that you can't move; Git moves them for you whenever you do any network communication
- **First relevant rank:** >10
- **Top-1 retrieved (05_contributing):** $ git push origin master To john@githost:simplegit.git ! [rejected] master -> master (non-fast forward) error: failed to push some refs to 'john@githost:simplegit.git' In this case, John's push fails because of Jessica's earlier push of he…

## semantic p85 - q099: right document, wrong passage

- **Question:** What is an upstream branch and when does Git create a tracking branch?
- **Evidence (03_remote-branches):** Checking out a local branch from a remote-tracking branch automatically creates what is called a "tracking branch" (and the branch it tracks is called an "upstream branch"). Tracking branches are local branches that have a direct relationship to a remote branch.
- **First relevant rank:** 6
- **Top-1 retrieved (03_remote-branches):** $ git checkout -b sf origin/serverfix Branch sf set up to track remote branch serverfix from origin. Switched to a new branch 'sf' Now, your local branch sf will automatically pull from origin/serverfix. If you already have a local branch …

## semantic p85 - q100: wrong document

- **Question:** What does the status command report right after a fresh clone?
- **Evidence (02_recording-changes):** This means you have a clean working directory; in other words, none of your tracked files are modified.
- **First relevant rank:** >10
- **Top-1 retrieved (02_undoing):** The git status command reminds you: $ git add * $ git status On branch master Changes to be committed: (use "git restore --staged <file>..." to unstage) modified: CONTRIBUTING.md renamed: README.md -> README Right below the "Changes to be …

## semantic p85 - q104: right document, wrong passage

- **Question:** Do ignore files in subfolders affect the whole repository?
- **Evidence (02_recording-changes):** The rules in these nested .gitignore files apply only to the files under the directory where they are located.
- **First relevant rank:** 6
- **Top-1 retrieved (02_recording-changes):** The first line tells Git to ignore any files ending in ".o" or ".a" -- object and archive files that may be the product of building your code. The second line tells Git to ignore all files whose names end with a tilde (~), which is used by…

## semantic p85 - q115: right document, wrong passage

- **Question:** Why is creating a branch in Git instant while older tools take minutes?
- **Evidence (03_nutshell):** Because a branch in Git is actually a simple file that contains the 40 character SHA-1 checksum of the commit it points to, branches are cheap to create and destroy. Creating a new branch is as quick and simple as writing 41 bytes to a file (40 characters and a newline). This is in sharp contrast to the way most older…
- **First relevant rank:** 6
- **Top-1 retrieved (03_nutshell):** As you start making commits, you're given a master branch that points to the last commit you made. Every time you commit, the master branch pointer moves forward automatically. The "master" branch in Git is not a special branch. It is exac…

## semantic p85 - q124: wrong document

- **Question:** How hard is it to lose committed work, and what makes it safer still?
- **Evidence (01_what-is-git):** It is hard to get the system to do anything that is not undoable or to make it erase data in any way. As with any VCS, you can lose or mess up changes you haven't committed yet, but after you commit a snapshot into Git, it is very difficult to lose, especially if you regularly push your database to another repository.
- **First relevant rank:** >10
- **Top-1 retrieved (07_rewriting-history):** Don't push your work until you're happy with it One of the cardinal rules of Git is that, since so much work is local within your clone, you have a great deal of freedom to rewrite your history locally. However, once you push your work, it…

## semantic p85 - q125: wrong document

- **Question:** What are the three steps of the basic Git workflow?
- **Evidence (01_what-is-git):** 1. You modify files in your working tree. 2. You selectively stage just those changes you want to be part of your next commit, which adds only those changes to the staging area. 3. You do a commit, which takes the files as they are in the staging area and stores that snapshot permanently to your Git directory.
- **First relevant rank:** >10
- **Top-1 retrieved (07_reset):** $ tree . ├── README ├── Rakefile └── lib └── simplegit.rb 1 directory, 3 files The Workflow Git's typical workflow is to record snapshots of your project in successively better states, by manipulating these three trees. Git's typical workf…

## semantic p85 - q126: wrong document

- **Question:** Could a corrupted server be restored from a client's clone?
- **Evidence (02_getting-a-repository):** Every version of every file for the history of the project is pulled down by default when you run git clone. In fact, if your server disk gets corrupted, you can often use nearly any of the clones on any client to set the server back to the state it was in when it was cloned
- **First relevant rank:** >10
- **Top-1 retrieved (01_about-version-control):** However, this setup also has some serious downsides. The most obvious is the single point of failure that the centralized server represents. If that server goes down for an hour, then during that hour nobody can collaborate at all or save …
