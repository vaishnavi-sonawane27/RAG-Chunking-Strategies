# Failure cases: bge-small, dense retrieval, headline configurations

A question counts as a miss when its first relevant chunk is not in the top 5.

## fixed - q002: right document, wrong passage

- **Question:** Which flag makes git config store a value for my user account across all my repositories?
- **Evidence (01_first-time-setup):** You can make Git read and write to this file specifically by passing the --global option
- **First relevant rank:** 8
- **Top-1 retrieved (01_first-time-setup):** config <key>: $ git config user.name John Doe Since Git might read the same configuration variable value from more than one file, it's possible that you have an unexpected value for one of these values and you don't know why. In cases like…

## fixed - q013: wrong document

- **Question:** Which part of a Git project holds the metadata and the object database?
- **Evidence (01_what-is-git):** The Git directory is where Git stores the metadata and object database for your project.
- **First relevant rank:** 7
- **Top-1 retrieved (10_objects):** tree 1 git/objects/fa/49b077972391ad58037050f2a75f74e3671e92 # new.txt git/objects/fd/f4fc3344e67ab068f836878b6c4951e3b15f3d # commit 1 If you follow all the internal pointers, you get an object graph something like this: All the reachable…

## fixed - q022: wrong document

- **Question:** Which URL styles can be used to clone, besides https?
- **Evidence (02_getting-a-repository):** you may also see git:// or user@server:path/to/repo.git, which uses the SSH transfer protocol.
- **First relevant rank:** 8
- **Top-1 retrieved (04_protocols):** like GitHub, the URL you use to view the repository online (for example, ^ (https://github.com/schacon/simplegit)) is the same URL you can use to clone and, if you have access, push over. Dumb HTTP If the server does not respond with a Git…

## fixed - q028: right document, wrong passage

- **Question:** How can a commit skip the explicit add step for files Git already follows?
- **Evidence (02_recording-changes):** Adding the -a option to the git commit command makes Git automatically stage every file that is already tracked before doing the commit
- **First relevant rank:** >10
- **Top-1 retrieved (02_recording-changes):** you skip the git add part: $ git status On branch master Your branch is up-to-date with 'origin/master'. Changes not staged for commit: (use "git add <file>..." to update what will be committed) (use "git checkout -- <file>..." to discard …

## fixed - q033: wrong document

- **Question:** In what order does the history command list commits when run without options?
- **Evidence (02_viewing-history):** lists the commits made in that repository in reverse chronological order
- **First relevant rank:** >10
- **Top-1 retrieved (07_rewriting-history):** # Note that empty commits are commented out It's important to note that these commits are listed in the opposite order than you normally see them using the log command. If you run a log, you see something like this: $ git log --pretty=form…

## fixed - q057: right document, wrong passage

- **Question:** Does a plain push send my tags to the server?
- **Evidence (02_tagging):** By default, the git push command doesn't transfer tags to remote servers.
- **First relevant rank:** >10
- **Top-1 retrieved (02_tagging):** to a shared server after you have created them. This process is just like sharing remote branches -- you can run git push origin <tagname>. $ git push origin v1.5 Counting objects: 14, done. Delta compression using up to 8 threads. Compres…

## fixed - q060: right document, wrong passage

- **Question:** What happens to a commit I make while sitting on a checked-out tag?
- **Evidence (02_tagging):** your new commit won't belong to any branch and will be unreachable, except by the exact commit hash
- **First relevant rank:** >10
- **Top-1 retrieved (02_tagging):** date the commit was tagged, and the annotation message before showing the commit information. Lightweight Tags Another way to tag commits is with a lightweight tag. This is basically the commit checksum stored in a file -- no other informa…

## fixed - q066: wrong document

- **Question:** What does the star next to a branch name in the listing mean?
- **Evidence (03_branch-management):** it indicates the branch that you currently have checked out
- **First relevant rank:** 7
- **Top-1 retrieved (02_recording-changes):** the command tells you which branch you're on and informs you that it has not diverged from the same branch on the server. For now, that branch is always master, which is the default; you won't worry about it here. ch03-git-branching#ch03-g…

## fixed - q071: wrong document

- **Question:** Which branches are safe to remove with the lowercase delete flag?
- **Evidence (03_branch-management):** Branches on this list without the * in front of them are generally fine to delete with git branch -d; you've already incorporated their work into another branch, so you're not going to lose anything.
- **First relevant rank:** 10
- **Top-1 retrieved (08_config):** denies any deletion of branches or tags -- no user can do it. To remove remote branches, you must remove the ref files from the server manually. There are also more interesting ways to do this on a per-user basis via ACLs, as you'll learn …

## fixed - q074: wrong document

- **Question:** Does branching and merging involve contacting a server?
- **Evidence (03_workflows):** everything is being done only in your Git repository -- there is no communication with the server
- **First relevant rank:** >10
- **Top-1 retrieved (03_basic-branching-and-merging):** Basic Branching and Merging Let's go through a simple example of branching and merging with a workflow that you might use in the real world. You'll follow these steps: - Do some work on a website. - Create a branch for a new user story you…

## fixed - q077: right document, wrong passage

- **Question:** What does rebasing do, in one sentence?
- **Evidence (03_rebasing):** you can take all the changes that were committed on one branch and replay them on a different branch.
- **First relevant rank:** >10
- **Top-1 retrieved (03_rebasing):** Rebasing In Git, there are two main ways to integrate changes from one branch into another: the merge and the rebase. In this section you'll learn what rebasing is, how to do it, why it's a pretty amazing tool, and in what cases you won't …

## fixed - q081: right document, wrong passage

- **Question:** How can I make pulling replay my commits rather than merge by default?
- **Evidence (03_rebasing):** you can set the pull.rebase config value
- **First relevant rank:** >10
- **Top-1 retrieved (03_rebasing):** were ready to submit your patches to the main project. That way, the maintainer doesn't have to do any integration work -- just a fast-forward or a clean apply. Note that the snapshot pointed to by the final commit you end up with, whether…

## fixed - q084: right document, wrong passage

- **Question:** Step by step, how does a rebase work internally?
- **Evidence (03_rebasing):** This operation works by going to the common ancestor of the two branches (the one you're on and the one you're rebasing onto), getting the diff introduced by each commit of the branch you're on, saving those diffs to temporary files, resetting the current branch to the same commit as the branch you are rebasing onto, …
- **First relevant rank:** >10
- **Top-1 retrieved (03_rebasing):** make --rebase the default, you can set the pull.rebase config value with something like git config --global pull.rebase true. If you only ever rebase commits that have never left your own computer, you'll be just fine. If you rebase commit…

## fixed - q089: wrong document

- **Question:** Why can't I move origin/master by hand?
- **Evidence (03_remote-branches):** They're local references that you can't move; Git moves them for you whenever you do any network communication
- **First relevant rank:** >10
- **Top-1 retrieved (05_contributing):** origin/master is reachable from Jessica's master branch, so she should be able to successfully push (assuming John hasn't pushed even more changes in the meantime): $ git push origin master ... To jessica@githost:simplegit.git 72bbc59..805…

## fixed - q092: wrong document

- **Question:** How can a local branch be pushed under a different name on the remote?
- **Evidence (03_remote-branches):** You can use this format to push a local branch into a remote branch that is named differently.
- **First relevant rank:** >10
- **Top-1 retrieved (03_branch-management):** like master/main/mainline without having read the section _changing_master. Suppose you have a branch that is called bad-branch-name and you want to change it to corrected-branch-name, while keeping all history. You also want to change the…

## fixed - q093: wrong document

- **Question:** After fetching a new remote branch do I get an editable local copy of it?
- **Evidence (03_remote-branches):** you don't automatically have local, editable copies of them
- **First relevant rank:** 9
- **Top-1 retrieved (02_remotes):** issue-43 new (next fetch will store in remotes/origin) issue-45 new (next fetch will store in remotes/origin) refs/remotes/origin/issue-11 stale (use 'git remote prune' to remove) Local branches configured for 'git pull': dev-branch merges…

## fixed - q112: wrong document

- **Question:** How do I jump back to the branch I was on before?
- **Evidence (03_nutshell):** Return to your previously checked out branch: git switch -.
- **First relevant rank:** >10
- **Top-1 retrieved (07_rewriting-history):** will be returned to the state it was in before you started the rebase. If you finish a rebase and decide it's not what you want, you can use git reflog to recover an earlier version of your branch. See ch10-git-internals#_data_recovery for…

## fixed - q123: wrong document

- **Question:** Can file contents change without Git noticing?
- **Evidence (01_what-is-git):** Everything in Git is checksummed before it is stored and is then referred to by that checksum. This means it's impossible to change the contents of any file or directory without Git knowing about it.
- **First relevant rank:** 9
- **Top-1 retrieved (02_undoing):** how to do that, too. In the last example output, the unstaged area looks like this: Changes not staged for commit: (use "git add <file>..." to update what will be committed) (use "git checkout -- <file>..." to discard changes in working di…

## fixed - q125: wrong document

- **Question:** What are the three steps of the basic Git workflow?
- **Evidence (01_what-is-git):** 1. You modify files in your working tree. 2. You selectively stage just those changes you want to be part of your next commit, which adds only those changes to the staging area. 3. You do a commit, which takes the files as they are in the staging area and stores that snapshot permanently to your Git directory.
- **First relevant rank:** 6
- **Top-1 retrieved (05_contributing):** section, we covered multiple workflows, and talked about the differences between working as part of a small team on closed-source projects vs contributing to a big public project. You know to check for white-space errors before committing,…

## fixed - q127: wrong document

- **Question:** If a maintainer applies my patch, who is credited as author and who as committer?
- **Evidence (02_viewing-history):** The author is the person who originally wrote the work, whereas the committer is the person who last applied the work. So, if you send in a patch to a project and one of the core members applies the patch, both of you get credit -- you as the author, and the core member as the committer.
- **First relevant rank:** 7
- **Top-1 retrieved (05_maintaining):** If the contributor is a Git user and was good enough to use the format-patch command to generate their patch, then your job is easier because the patch contains author information and a commit message for you. If you can, encourage your co…

## sentence - q022: wrong document

- **Question:** Which URL styles can be used to clone, besides https?
- **Evidence (02_getting-a-repository):** you may also see git:// or user@server:path/to/repo.git, which uses the SSH transfer protocol.
- **First relevant rank:** 7
- **Top-1 retrieved (04_protocols):** In fact, for services like GitHub, the URL you use to view the repository online (for example, ^ (https://github.com/schacon/simplegit)) is the same URL you can use to clone and, if you have access, push over. Dumb HTTP If the server does …

## sentence - q030: right document, wrong passage

- **Question:** How do I stop Git tracking a file but leave it on my disk?
- **Evidence (02_recording-changes):** keep the file in your working tree but remove it from your staging area
- **First relevant rank:** 10
- **Top-1 retrieved (02_recording-changes):** In other words, you may want to keep the file on your hard drive but not have Git track it anymore. This is particularly useful if you forgot to add something to your .gitignore file and accidentally staged it, like a large log file or a b…

## sentence - q036: wrong document

- **Question:** How can I keep merge commits from cluttering the log output?
- **Evidence (02_viewing-history):** simply add the log option --no-merges
- **First relevant rank:** 6
- **Top-1 retrieved (07_advanced-merging):** We can further simplify this though to give us much more specific context. If we add the --merge option to git log, it will only show the commits in either side of the merge that touch a file that's currently conflicted. $ git log --onelin…

## sentence - q048: wrong document

- **Question:** After committing three files, how many objects are stored and of which kinds?
- **Evidence (03_nutshell):** Your Git repository now contains five objects: three blobs
- **First relevant rank:** >10
- **Top-1 retrieved (10_packfiles):** Packfiles If you followed all of the instructions in the example from the previous section, you should now have a test Git repository with 11 objects -- four blobs, three trees, three commits, and one tag: $ find .git/objects -type f git/o…

## sentence - q051: wrong document

- **Question:** When does Git just move a pointer forward instead of creating a new commit while merging?
- **Evidence (03_basic-branching-and-merging):** there is no divergent work to merge together -- this is called a "fast-forward."
- **First relevant rank:** >10
- **Top-1 retrieved (07_advanced-merging):** This approach also won't work if any other commits have been created since the merge; moving the refs would effectively lose those changes. Reverse the commit If moving the branch pointers around isn't going to work for you, Git gives you …

## sentence - q054: right document, wrong passage

- **Question:** How do I tell Git that a conflicted file is now fixed?
- **Evidence (03_basic-branching-and-merging):** run git add on each file to mark it as resolved
- **First relevant rank:** 10
- **Top-1 retrieved (03_basic-branching-and-merging):** If you want to see which files are unmerged at any point after a merge conflict, you can run git status: $ git status On branch master You have unmerged paths. (fix conflicts and run "git commit") Unmerged paths: (use "git add <file>..." t…

## sentence - q061: right document, wrong passage

- **Question:** Can I label an older commit I forgot to mark as a release?
- **Evidence (02_tagging):** You can also tag commits after you've moved past them.
- **First relevant rank:** 9
- **Top-1 retrieved (02_tagging):** Suppose your commit history looks like this: $ git log --pretty=oneline 15027957951b64cf874c3557a0f3547bd83b3ff6 Merge branch 'experiment' a6b4c97498bd301d84096da251c98a07c7723e65 Create write support 0d52aaab4479697da7686c15f77a3d64d91651…

## sentence - q066: wrong document

- **Question:** What does the star next to a branch name in the listing mean?
- **Evidence (03_branch-management):** it indicates the branch that you currently have checked out
- **First relevant rank:** 8
- **Top-1 retrieved (03_remote-branches):** This will list out your local branches with more information including what each branch is tracking and if your local branch is ahead, behind or both. $ git branch -vv iss53 7e424c3 [origin/iss53: ahead 2] Add forgotten brackets master 1ae…

## sentence - q071: right document, wrong passage

- **Question:** Which branches are safe to remove with the lowercase delete flag?
- **Evidence (03_branch-management):** Branches on this list without the * in front of them are generally fine to delete with git branch -d; you've already incorporated their work into another branch, so you're not going to lose anything.
- **First relevant rank:** >10
- **Top-1 retrieved (03_branch-management):** Because it contains work that isn't merged in yet, trying to delete it with git branch -d will fail: $ git branch -d testing error: The branch 'testing' is not fully merged. If you are sure you want to delete it, run 'git branch -D testing…

## sentence - q077: right document, wrong passage

- **Question:** What does rebasing do, in one sentence?
- **Evidence (03_rebasing):** you can take all the changes that were committed on one branch and replay them on a different branch.
- **First relevant rank:** >10
- **Top-1 retrieved (03_rebasing):** Let's look at an example of how rebasing work that you've made public can cause problems. Suppose you clone from a central server and then do some work off that. Your commit history looks like this: Clone a repository, and base some work o…

## sentence - q081: wrong document

- **Question:** How can I make pulling replay my commits rather than merge by default?
- **Evidence (03_rebasing):** you can set the pull.rebase config value
- **First relevant rank:** >10
- **Top-1 retrieved (07_advanced-merging):** This approach also won't work if any other commits have been created since the merge; moving the refs would effectively lose those changes. Reverse the commit If moving the branch pointers around isn't going to work for you, Git gives you …

## sentence - q084: right document, wrong passage

- **Question:** Step by step, how does a rebase work internally?
- **Evidence (03_rebasing):** This operation works by going to the common ancestor of the two branches (the one you're on and the one you're rebasing onto), getting the diff introduced by each commit of the branch you're on, saving those diffs to temporary files, resetting the current branch to the same commit as the branch you are rebasing onto, …
- **First relevant rank:** >10
- **Top-1 retrieved (03_rebasing):** If you examine the log of a rebased branch, it looks like a linear history: it appears that all the work happened in series, even when it originally happened in parallel. Often, you'll do this to make sure your commits apply cleanly on a r…

## sentence - q089: wrong document

- **Question:** Why can't I move origin/master by hand?
- **Evidence (03_remote-branches):** They're local references that you can't move; Git moves them for you whenever you do any network communication
- **First relevant rank:** >10
- **Top-1 retrieved (05_contributing):** Now origin/master is reachable from Jessica's master branch, so she should be able to successfully push (assuming John hasn't pushed even more changes in the meantime): $ git push origin master ... To jessica@githost:simplegit.git 72bbc59.…

## sentence - q092: wrong document

- **Question:** How can a local branch be pushed under a different name on the remote?
- **Evidence (03_remote-branches):** You can use this format to push a local branch into a remote branch that is named differently.
- **First relevant rank:** 7
- **Top-1 retrieved (02_remotes):** master merges with remote master Local refs configured for 'git push': dev-branch pushes to dev-branch (up to date) markdown-strip pushes to markdown-strip (up to date) master pushes to master (up to date) This command shows which branch i…

## sentence - q101: wrong document

- **Question:** Why do newer repositories often start on main instead of master?
- **Evidence (02_recording-changes):** GitHub changed the default branch name from master to main in mid-2020, and other Git hosts followed suit.
- **First relevant rank:** >10
- **Top-1 retrieved (03_remote-branches):** Git also gives you your own local master branch starting at the same place as origin's master branch, so you have something to work from. ."origin" is not special Just like the branch name "master" does not have any special meaning in Git,…

## sentence - q104: wrong document

- **Question:** Do ignore files in subfolders affect the whole repository?
- **Evidence (02_recording-changes):** The rules in these nested .gitignore files apply only to the files under the directory where they are located.
- **First relevant rank:** >10
- **Top-1 retrieved (07_stashing-cleaning):** By default, git stash will stash only modified and staged tracked files. If you specify --include-untracked or -u, Git will include untracked files in the stash being created. However, including untracked files in the stash will still not …

## sentence - q107: wrong document

- **Question:** How should I think about what git add really does?
- **Evidence (02_recording-changes):** git add is a multipurpose command -- you use it to begin tracking new files, to stage files, and to do other things like marking merge-conflicted files as resolved. It may be helpful to think of it more as "add precisely this content to the next commit" rather than "add this file to the project
- **First relevant rank:** 10
- **Top-1 retrieved (01_help):** In addition, if you don't need the full-blown manpage help, but just need a quick refresher on the available options for a Git command, you can ask for the more concise "help" output with the -h option, as in: $ git add -h usage: git add […

## sentence - q112: wrong document

- **Question:** How do I jump back to the branch I was on before?
- **Evidence (03_nutshell):** Return to your previously checked out branch: git switch -.
- **First relevant rank:** >10
- **Top-1 retrieved (07_rewriting-history):** If you finish a rebase and decide it's not what you want, you can use git reflog to recover an earlier version of your branch. See ch10-git-internals#_data_recovery for more information on the reflog command. Drew DeVault made a practical …

## sentence - q116: right document, wrong passage

- **Question:** What are the two effects of switching back to the master branch?
- **Evidence (03_nutshell):** That command did two things. It moved the HEAD pointer back to point to the master branch, and it reverted the files in your working directory back to the snapshot that master points to.
- **First relevant rank:** >10
- **Top-1 retrieved (03_nutshell):** It essentially rewinds the work you've done in your testing branch so you can go in a different direction. Switching branches changes files in your working directory It's important to note that when you switch branches in Git, files in you…

## sentence - q125: wrong document

- **Question:** What are the three steps of the basic Git workflow?
- **Evidence (01_what-is-git):** 1. You modify files in your working tree. 2. You selectively stage just those changes you want to be part of your next commit, which adds only those changes to the staging area. 3. You do a commit, which takes the files as they are in the staging area and stores that snapshot permanently to your Git directory.
- **First relevant rank:** >10
- **Top-1 retrieved (07_reset):** Git's typical workflow is to record snapshots of your project in successively better states, by manipulating these three trees. Git's typical workflow Let's visualize this process: say you go into a new directory with a single file in it. …

## recursive - q002: right document, wrong passage

- **Question:** Which flag makes git config store a value for my user account across all my repositories?
- **Evidence (01_first-time-setup):** You can make Git read and write to this file specifically by passing the --global option
- **First relevant rank:** >10
- **Top-1 retrieved (01_first-time-setup):** Since Git might read the same configuration variable value from more than one file, it's possible that you have an unexpected value for one of these values and you don't know why. In cases like that, you can query Git as to the origin for …

## recursive - q017: right document, wrong passage

- **Question:** In a distributed system, why does losing the server not mean losing the history?
- **Evidence (01_about-version-control):** Every clone is really a full backup of all the data.
- **First relevant rank:** >10
- **Top-1 retrieved (01_about-version-control):** If the hard disk the central database is on becomes corrupted, and proper backups haven't been kept, you lose absolutely everything -- the entire history of the project except whatever single snapshots people happen to have on their local …

## recursive - q022: wrong document

- **Question:** Which URL styles can be used to clone, besides https?
- **Evidence (02_getting-a-repository):** you may also see git:// or user@server:path/to/repo.git, which uses the SSH transfer protocol.
- **First relevant rank:** >10
- **Top-1 retrieved (04_protocols):** In fact, for services like GitHub, the URL you use to view the repository online (for example, ^ (https://github.com/schacon/simplegit)) is the same URL you can use to clone and, if you have access, push over. Dumb HTTP

## recursive - q033: wrong document

- **Question:** In what order does the history command list commits when run without options?
- **Evidence (02_viewing-history):** lists the commits made in that repository in reverse chronological order
- **First relevant rank:** 7
- **Top-1 retrieved (07_rewriting-history):** Running this command gives you a list of commits in your text editor that looks something like this: pick f7f3f6d Change my name a bit pick 310154e Update README formatting and add blame pick a5f4a0d Add cat-file

## recursive - q041: wrong document

- **Question:** What is the standard nickname for the server a repository was cloned from?
- **Evidence (02_remotes):** origin -- that is the default name Git gives to the server you cloned from
- **First relevant rank:** >10
- **Top-1 retrieved (04_protocols):** In fact, for services like GitHub, the URL you use to view the repository online (for example, ^ (https://github.com/schacon/simplegit)) is the same URL you can use to clone and, if you have access, push over. Dumb HTTP

## recursive - q052: wrong document

- **Question:** What makes a merge commit different from an ordinary commit?
- **Evidence (03_basic-branching-and-merging):** This is referred to as a merge commit, and is special in that it has more than one parent.
- **First relevant rank:** >10
- **Top-1 retrieved (07_advanced-merging):** Now that you know how to create a merge commit, you'll probably make some by mistake. One of the great things about working with Git is that it's okay to make mistakes, because it's possible (and in many cases easy) to fix them. Merge comm…

## recursive - q054: wrong document

- **Question:** How do I tell Git that a conflicted file is now fixed?
- **Evidence (03_basic-branching-and-merging):** run git add on each file to mark it as resolved
- **First relevant rank:** >10
- **Top-1 retrieved (07_rerere):** You should notice the new line Recorded preimage for FILE in there. Otherwise it should look exactly like a normal merge conflict. At this point, rerere can tell us a few things. Normally, you might run git status at this point to see what…

## recursive - q074: wrong document

- **Question:** Does branching and merging involve contacting a server?
- **Evidence (03_workflows):** everything is being done only in your Git repository -- there is no communication with the server
- **First relevant rank:** >10
- **Top-1 retrieved (05_contributing):** In this environment, you can follow a workflow similar to what you might do when using Subversion or another centralized system. You still get the advantages of things like offline committing and vastly simpler branching and merging, but t…

## recursive - q077: right document, wrong passage

- **Question:** What does rebasing do, in one sentence?
- **Evidence (03_rebasing):** you can take all the changes that were committed on one branch and replay them on a different branch.
- **First relevant rank:** >10
- **Top-1 retrieved (03_rebasing):** Rebasing In Git, there are two main ways to integrate changes from one branch into another: the merge and the rebase. In this section you'll learn what rebasing is, how to do it, why it's a pretty amazing tool, and in what cases you won't …

## recursive - q079: wrong document

- **Question:** What is the main rule to follow when rebasing?
- **Evidence (03_rebasing):** Do not rebase commits that exist outside your repository and that people may have based work on.
- **First relevant rank:** >10
- **Top-1 retrieved (07_rerere):** This same tactic can be used if you want to keep a branch rebased so you don't have to deal with the same rebasing conflicts each time you do it. Or if you want to take a branch that you merged and fixed a bunch of conflicts and then decid…

## recursive - q081: right document, wrong passage

- **Question:** How can I make pulling replay my commits rather than merge by default?
- **Evidence (03_rebasing):** you can set the pull.rebase config value
- **First relevant rank:** >10
- **Top-1 retrieved (03_rebasing):** Note that the snapshot pointed to by the final commit you end up with, whether it's the last of the rebased commits for a rebase or the final merge commit after a merge, is the same snapshot -- it's only the history that is different. Reba…

## recursive - q084: wrong document

- **Question:** Step by step, how does a rebase work internally?
- **Evidence (03_rebasing):** This operation works by going to the common ancestor of the two branches (the one you're on and the one you're rebasing onto), getting the diff introduced by each commit of the branch you're on, saving those diffs to temporary files, resetting the current branch to the same commit as the branch you are rebasing onto, …
- **First relevant rank:** >10
- **Top-1 retrieved (07_rewriting-history):** Notice the reverse order. The interactive rebase gives you a script that it's going to run. It will start at the commit you specify on the command line (HEAD~3) and replay the changes introduced in each of these commits from top to bottom.…

## recursive - q087: right document, wrong passage

- **Question:** What is the argument for tidying up commits before merging them?
- **Evidence (03_rebasing):** The opposing point of view is that the commit history is the story of how your project was made. You wouldn't publish the first draft of a book, so why show your messy work?
- **First relevant rank:** >10
- **Top-1 retrieved (03_rebasing):** Now, to the question of whether merging or rebasing is better: hopefully you'll see that it's not that simple. Git is a powerful tool, and allows you to do many things to and with your history, but every team and every project is different…

## recursive - q089: wrong document

- **Question:** Why can't I move origin/master by hand?
- **Evidence (03_remote-branches):** They're local references that you can't move; Git moves them for you whenever you do any network communication
- **First relevant rank:** >10
- **Top-1 retrieved (05_contributing):** Now origin/master is reachable from Jessica's master branch, so she should be able to successfully push (assuming John hasn't pushed even more changes in the meantime): $ git push origin master ... To jessica@githost:simplegit.git 72bbc59.…

## recursive - q091: wrong document

- **Question:** Are my local branches pushed to the server automatically?
- **Evidence (03_remote-branches):** Your local branches aren't automatically synchronized to the remotes you write to
- **First relevant rank:** 9
- **Top-1 retrieved (02_remotes):** This command shows which branch is automatically pushed to when you run git push while on certain branches. It also shows you which remote branches on the server you don't yet have, which remote branches you have that have been removed fro…

## recursive - q100: right document, wrong passage

- **Question:** What does the status command report right after a fresh clone?
- **Evidence (02_recording-changes):** This means you have a clean working directory; in other words, none of your tracked files are modified.
- **First relevant rank:** >10
- **Top-1 retrieved (02_recording-changes):** The main tool you use to determine which files are in which state is the git status command. If you run this command directly after a clone, you should see something like this: $ git status On branch master Your branch is up-to-date with '…

## recursive - q104: right document, wrong passage

- **Question:** Do ignore files in subfolders affect the whole repository?
- **Evidence (02_recording-changes):** The rules in these nested .gitignore files apply only to the files under the directory where they are located.
- **First relevant rank:** >10
- **Top-1 retrieved (02_recording-changes):** Here is another example .gitignore file: # ignore all .a files *.a # but do track lib.a, even though you're ignoring .a files above !lib.a # only ignore the TODO file in the current directory, not subdir/TODO /TODO # ignore all files in an…

## recursive - q105: wrong document

- **Question:** What does the verbose commit flag add to the message editor?
- **Evidence (02_recording-changes):** Doing so also puts the diff of your change in the editor so you can see exactly what changes you're committing.
- **First relevant rank:** >10
- **Top-1 retrieved (07_rewriting-history):** The command above loads the previous commit message into an editor session, where you can make changes to the message, save those changes and exit. When you save and close the editor, the editor writes a new commit containing that updated …

## recursive - q107: right document, wrong passage

- **Question:** How should I think about what git add really does?
- **Evidence (02_recording-changes):** git add is a multipurpose command -- you use it to begin tracking new files, to stage files, and to do other things like marking merge-conflicted files as resolved. It may be helpful to think of it more as "add precisely this content to the next commit" rather than "add this file to the project
- **First relevant rank:** 9
- **Top-1 retrieved (02_recording-changes):** You can tell that it's staged because it's under the "Changes to be committed" heading. If you commit at this point, the version of the file at the time you ran git add is what will be in the subsequent historical snapshot. You may recall …

## recursive - q112: wrong document

- **Question:** How do I jump back to the branch I was on before?
- **Evidence (03_nutshell):** Return to your previously checked out branch: git switch -.
- **First relevant rank:** >10
- **Top-1 retrieved (07_subtree-merges):** We just switched back to your master branch, and we pull the rack_branch branch into the rack subdirectory of our master branch of our main project:

## recursive - q116: wrong document

- **Question:** What are the two effects of switching back to the master branch?
- **Evidence (03_nutshell):** That command did two things. It moved the HEAD pointer back to point to the master branch, and it reverted the files in your working directory back to the snapshot that master points to.
- **First relevant rank:** 9
- **Top-1 retrieved (03_basic-branching-and-merging):** For now, let's assume you've committed all your changes, so you can switch back to your master branch:

## recursive - q119: right document, wrong passage

- **Question:** Why does the book use the terminal instead of graphical clients?
- **Evidence (01_command-line):** the command line is the only place you can run all Git commands
- **First relevant rank:** >10
- **Top-1 retrieved (01_command-line):** If you know how to run the command-line version, you can probably also figure out how to run the GUI version, while the opposite is not necessarily true. Also, while your choice of graphical client is a matter of personal taste, all users …

## recursive - q125: wrong document

- **Question:** What are the three steps of the basic Git workflow?
- **Evidence (01_what-is-git):** 1. You modify files in your working tree. 2. You selectively stage just those changes you want to be part of your next commit, which adds only those changes to the staging area. 3. You do a commit, which takes the files as they are in the staging area and stores that snapshot permanently to your Git directory.
- **First relevant rank:** >10
- **Top-1 retrieved (07_reset):** $ tree . ├── README ├── Rakefile └── lib └── simplegit.rb 1 directory, 3 files The Workflow Git's typical workflow is to record snapshots of your project in successively better states, by manipulating these three trees. Git's typical workf…

## fixed_overlap - q022: wrong document

- **Question:** Which URL styles can be used to clone, besides https?
- **Evidence (02_getting-a-repository):** you may also see git:// or user@server:path/to/repo.git, which uses the SSH transfer protocol.
- **First relevant rank:** >10
- **Top-1 retrieved (04_protocols):** Git by default runs the appropriate command (git update-server-info) to make HTTP fetching and cloning work properly. This command is run when you push to this repository (over SSH perhaps); then, other people can clone via something like:…

## fixed_overlap - q048: wrong document

- **Question:** After committing three files, how many objects are stored and of which kinds?
- **Evidence (03_nutshell):** Your Git repository now contains five objects: three blobs
- **First relevant rank:** 8
- **Top-1 retrieved (10_objects):** are initially stored as separate files in your .git/objects directory. Here are all the objects in the example directory now, commented with what they store: $ find .git/objects -type f git/objects/01/55eb4229851634a0f03eb265b69f5a2d56f341…

## fixed_overlap - q052: wrong document

- **Question:** What makes a merge commit different from an ordinary commit?
- **Evidence (03_basic-branching-and-merging):** This is referred to as a merge commit, and is special in that it has more than one parent.
- **First relevant rank:** >10
- **Top-1 retrieved (07_revision-selection):** of a merge commit is from the branch you were on when you merged (frequently master), while the second parent of a merge commit is from the branch that was merged (say, topic): $ git show d921970^ commit 1c002dd4b536e7479fe34593e72e6c6c181…

## fixed_overlap - q060: right document, wrong passage

- **Question:** What happens to a commit I make while sitting on a checked-out tag?
- **Evidence (02_tagging):** your new commit won't belong to any branch and will be unreachable, except by the exact commit hash
- **First relevant rank:** 10
- **Top-1 retrieved (02_tagging):** commit checksum stored in a file -- no other information is kept. To create a lightweight tag, don't supply any of the -a, -s, or -m options, just provide a tag name: $ git tag v1.4-lw $ git tag v0.1 v1.3 v1.4 v1.4-lw v1.5 This time, if yo…

## fixed_overlap - q071: wrong document

- **Question:** Which branches are safe to remove with the lowercase delete flag?
- **Evidence (03_branch-management):** Branches on this list without the * in front of them are generally fine to delete with git branch -d; you've already incorporated their work into another branch, so you're not going to lose anything.
- **First relevant rank:** 7
- **Top-1 retrieved (08_config):** the user to delete the branch and then push it back up with the new reference. To avoid this, set receive.denyDeletes to true: $ git config --system receive.denyDeletes true This denies any deletion of branches or tags -- no user can do it…

## fixed_overlap - q077: right document, wrong passage

- **Question:** What does rebasing do, in one sentence?
- **Evidence (03_rebasing):** you can take all the changes that were committed on one branch and replay them on a different branch.
- **First relevant rank:** >10
- **Top-1 retrieved (03_rebasing):** the integration, but rebasing makes for a cleaner history. If you examine the log of a rebased branch, it looks like a linear history: it appears that all the work happened in series, even when it originally happened in parallel. Often, yo…

## fixed_overlap - q079: right document, wrong passage

- **Question:** What is the main rule to follow when rebasing?
- **Evidence (03_rebasing):** Do not rebase commits that exist outside your repository and that people may have based work on.
- **First relevant rank:** 10
- **Top-1 retrieved (03_rebasing):** on a project, you may need a record of all your missteps and dead-end paths, but when it's time to show your work to the world, you may want to tell a more coherent story of how to get from A to B. People in this camp use tools like rebase…

## fixed_overlap - q080: wrong document

- **Question:** What is a patch-id?
- **Evidence (03_rebasing):** Git also calculates a checksum that is based just on the patch introduced with the commit.
- **First relevant rank:** >10
- **Top-1 retrieved (05_maintaining):** If the contributor is a Git user and was good enough to use the format-patch command to generate their patch, then your job is easier because the patch contains author information and a commit message for you. If you can, encourage your co…

## fixed_overlap - q081: right document, wrong passage

- **Question:** How can I make pulling replay my commits rather than merge by default?
- **Evidence (03_rebasing):** you can set the pull.rebase config value
- **First relevant rank:** 8
- **Top-1 retrieved (03_rebasing):** that the snapshot pointed to by the final commit you end up with, whether it's the last of the rebased commits for a rebase or the final merge commit after a merge, is the same snapshot -- it's only the history that is different. Rebasing …

## fixed_overlap - q084: right document, wrong passage

- **Question:** Step by step, how does a rebase work internally?
- **Evidence (03_rebasing):** This operation works by going to the common ancestor of the two branches (the one you're on and the one you're rebasing onto), getting the diff introduced by each commit of the branch you're on, saving those diffs to temporary files, resetting the current branch to the same commit as the branch you are rebasing onto, …
- **First relevant rank:** 9
- **Top-1 retrieved (03_rebasing):** the integration, but rebasing makes for a cleaner history. If you examine the log of a rebased branch, it looks like a linear history: it appears that all the work happened in series, even when it originally happened in parallel. Often, yo…

## fixed_overlap - q089: wrong document

- **Question:** Why can't I move origin/master by hand?
- **Evidence (03_remote-branches):** They're local references that you can't move; Git moves them for you whenever you do any network communication
- **First relevant rank:** >10
- **Top-1 retrieved (06_2-contributing):** master, pull from progit, then push to origin -- all of those operations are valid with this setup. So you'll have to take care never to commit directly to master, since that branch effectively belongs to the upstream repository.

## fixed_overlap - q091: wrong document

- **Question:** Are my local branches pushed to the server automatically?
- **Evidence (03_remote-branches):** Your local branches aren't automatically synchronized to the remotes you write to
- **First relevant rank:** 7
- **Top-1 retrieved (03_workflows):** remember when you're doing all this that these branches are completely local. When you're branching and merging, everything is being done only in your Git repository -- there is no communication with the server.

## fixed_overlap - q101: wrong document

- **Question:** Why do newer repositories often start on main instead of master?
- **Evidence (02_recording-changes):** GitHub changed the default branch name from master to main in mid-2020, and other Git hosts followed suit.
- **First relevant rank:** >10
- **Top-1 retrieved (03_branch-management):** one will need to update their code and/or configuration. - Update any test-runner configuration files. - Adjust build and release scripts. - Redirect settings on your repo host for things like the repo's default branch, merge rules, and ot…

## fixed_overlap - q107: wrong document

- **Question:** How should I think about what git add really does?
- **Evidence (02_recording-changes):** git add is a multipurpose command -- you use it to begin tracking new files, to stage files, and to do other things like marking merge-conflicted files as resolved. It may be helpful to think of it more as "add precisely this content to the next commit" rather than "add this file to the project
- **First relevant rank:** >10
- **Top-1 retrieved (01_help):** knowledgeable about Git and are often willing to help. In addition, if you don't need the full-blown manpage help, but just need a quick refresher on the available options for a Git command, you can ask for the more concise "help" output w…

## fixed_overlap - q110: wrong document

- **Question:** Why must I commit before switching branches?
- **Evidence (03_basic-branching-and-merging):** if your working directory or staging area has uncommitted changes that conflict with the branch you're checking out, Git won't let you switch branches.
- **First relevant rank:** >10
- **Top-1 retrieved (03_nutshell):** size of the project, whereas in Git the process is always instantaneous. Also, because we're recording the parents when we commit, finding a proper merge base for merging is automatically done for us and is generally very easy to do. These…

## fixed_overlap - q112: wrong document

- **Question:** How do I jump back to the branch I was on before?
- **Evidence (03_nutshell):** Return to your previously checked out branch: git switch -.
- **First relevant rank:** >10
- **Top-1 retrieved (07_rewriting-history):** will be returned to the state it was in before you started the rebase. If you finish a rebase and decide it's not what you want, you can use git reflog to recover an earlier version of your branch. See ch10-git-internals#_data_recovery for…

## fixed_overlap - q116: wrong document

- **Question:** What are the two effects of switching back to the master branch?
- **Evidence (03_nutshell):** That command did two things. It moved the HEAD pointer back to point to the master branch, and it reverted the files in your working directory back to the snapshot that master points to.
- **First relevant rank:** >10
- **Top-1 retrieved (03_basic-branching-and-merging):** won't let you switch branches. It's best to have a clean working state when you switch branches. There are ways to get around this (namely, stashing and commit amending) that we'll cover later on, in ch07-git-tools#_git_stashing. For now, …

## fixed_overlap - q124: wrong document

- **Question:** How hard is it to lose committed work, and what makes it safer still?
- **Evidence (01_what-is-git):** It is hard to get the system to do anything that is not undoable or to make it erase data in any way. As with any VCS, you can lose or mess up changes you haven't committed yet, but after you commit a snapshot into Git, it is very difficult to lose, especially if you regularly push your database to another repository.
- **First relevant rank:** >10
- **Top-1 retrieved (01_about-version-control):** is the single point of failure that the centralized server represents. If that server goes down for an hour, then during that hour nobody can collaborate at all or save versioned changes to anything they're working on. If the hard disk the…

## fixed_overlap - q125: wrong document

- **Question:** What are the three steps of the basic Git workflow?
- **Evidence (01_what-is-git):** 1. You modify files in your working tree. 2. You selectively stage just those changes you want to be part of your next commit, which adds only those changes to the staging area. 3. You do a commit, which takes the files as they are in the staging area and stores that snapshot permanently to your Git directory.
- **First relevant rank:** 9
- **Top-1 retrieved (05_contributing):** and what workflows are preferred or available to you. We'll cover aspects of each of these in a series of use cases, moving from simple to more complex; you should be able to construct the specific workflows you need in practice from these…

## fixed_overlap - q128: right document, wrong passage

- **Question:** What does the stat option add underneath each log entry?
- **Evidence (02_viewing-history):** As you can see, the --stat option prints below each commit entry a list of modified files, how many files were changed, and how many lines in those files were added and removed. It also puts a summary of the information at the end.
- **First relevant rank:** 6
- **Top-1 retrieved (02_viewing-history):** we've covered so far, as well as some other common formatting options that may be useful, along with how they change the output of the log command. Common options to git log |================================ | Option | Description | -p | S…

## semantic - q003: wrong document

- **Question:** From which Git release can the name of the initial branch be customised?
- **Evidence (01_first-time-setup):** From Git version 2.28 onwards, you can set a different name for the initial branch.
- **First relevant rank:** >10
- **Top-1 retrieved (03_branch-management):** Now we'll take a brief look at where we are now: $ git branch --all - corrected-branch-name main remotes/origin/bad-branch-name remotes/origin/corrected-branch-name remotes/origin/main Notice that you're on the branch corrected-branch-name…

## semantic - q013: wrong document

- **Question:** Which part of a Git project holds the metadata and the object database?
- **Evidence (01_what-is-git):** The Git directory is where Git stores the metadata and object database for your project.
- **First relevant rank:** >10
- **Top-1 retrieved (10_objects):** $ cd test $ find .git/objects git/objects git/objects/info git/objects/pack $ find .git/objects -type f Git has initialized the objects directory and created pack and info subdirectories in it, but there are no regular files. Now, let's us…

## semantic - q014: right document, wrong passage

- **Question:** What goes wrong with the habit of duplicating project folders by hand as a backup scheme?
- **Evidence (01_about-version-control):** It is easy to forget which directory you're in and accidentally write to the wrong file or copy over files you don't mean to.
- **First relevant rank:** >10
- **Top-1 retrieved (01_about-version-control):** The most obvious is the single point of failure that the centralized server represents. If that server goes down for an hour, then during that hour nobody can collaborate at all or save versioned changes to anything they're working on. If …

## semantic - q022: wrong document

- **Question:** Which URL styles can be used to clone, besides https?
- **Evidence (02_getting-a-repository):** you may also see git:// or user@server:path/to/repo.git, which uses the SSH transfer protocol.
- **First relevant rank:** 7
- **Top-1 retrieved (04_protocols):** The Cons Due to the lack of TLS or other cryptography, cloning over git:// might lead to an arbitrary code execution vulnerability, and should therefore be avoided unless you know what you are doing. - If you run git clone git://example.co…

## semantic - q028: right document, wrong passage

- **Question:** How can a commit skip the explicit add step for files Git already follows?
- **Evidence (02_recording-changes):** Adding the -a option to the git commit command makes Git automatically stage every file that is already tracked before doing the commit
- **First relevant rank:** 7
- **Top-1 retrieved (02_recording-changes):** You can tell that it's staged because it's under the "Changes to be committed" heading. If you commit at this point, the version of the file at the time you ran git add is what will be in the subsequent historical snapshot. You may recall …

## semantic - q033: wrong document

- **Question:** In what order does the history command list commits when run without options?
- **Evidence (02_viewing-history):** lists the commits made in that repository in reverse chronological order
- **First relevant rank:** >10
- **Top-1 retrieved (07_rewriting-history):** There is another history-rewriting option that you can use if you need to rewrite a larger number of commits in some scriptable way -- for instance, changing your email address globally or removing a file from every commit. The command is …

## semantic - q041: wrong document

- **Question:** What is the standard nickname for the server a repository was cloned from?
- **Evidence (02_remotes):** origin -- that is the default name Git gives to the server you cloned from
- **First relevant rank:** >10
- **Top-1 retrieved (04_git-on-a-server):** This is generally straightforward to do. In order to clone your repository to create a new bare repository, you run the clone command with the --bare option. By convention, bare repository directory names end with the suffix .git, like so:…

## semantic - q047: wrong document

- **Question:** Is the default branch special compared with other branches?
- **Evidence (03_nutshell):** The only reason nearly every repository has one is that the git init command creates it by default
- **First relevant rank:** 6
- **Top-1 retrieved (02_recording-changes):** Finally, the command tells you which branch you're on and informs you that it has not diverged from the same branch on the server. For now, that branch is always master, which is the default; you won't worry about it here. ch03-git-branchi…

## semantic - q048: wrong document

- **Question:** After committing three files, how many objects are stored and of which kinds?
- **Evidence (03_nutshell):** Your Git repository now contains five objects: three blobs
- **First relevant rank:** >10
- **Top-1 retrieved (10_packfiles):** Counting objects: 18, done. Delta compression using up to 8 threads. Compressing objects: 100% (14/14), done. Writing objects: 100% (18/18), done. Total 18 (delta 3), reused 0 (delta 0) If you look in your objects directory, you'll find th…

## semantic - q052: wrong document

- **Question:** What makes a merge commit different from an ordinary commit?
- **Evidence (03_basic-branching-and-merging):** This is referred to as a merge commit, and is special in that it has more than one parent.
- **First relevant rank:** >10
- **Top-1 retrieved (07_advanced-merging):** You can see that there is no difference between the branch we were on and the result of the merge. This can often be useful to basically trick Git into thinking that a branch is already merged when doing a merge later on. For example, say …

## semantic - q057: right document, wrong passage

- **Question:** Does a plain push send my tags to the server?
- **Evidence (02_tagging):** By default, the git push command doesn't transfer tags to remote servers.
- **First relevant rank:** >10
- **Top-1 retrieved (02_tagging):** You will have to explicitly push tags to a shared server after you have created them. This process is just like sharing remote branches -- you can run git push origin <tagname>. $ git push origin v1.5

## semantic - q066: wrong document

- **Question:** What does the star next to a branch name in the listing mean?
- **Evidence (03_branch-management):** it indicates the branch that you currently have checked out
- **First relevant rank:** 7
- **Top-1 retrieved (02_recording-changes):** Finally, the command tells you which branch you're on and informs you that it has not diverged from the same branch on the server. For now, that branch is always master, which is the default; you won't worry about it here. ch03-git-branchi…

## semantic - q080: wrong document

- **Question:** What is a patch-id?
- **Evidence (03_rebasing):** Git also calculates a checksum that is based just on the patch introduced with the commit.
- **First relevant rank:** >10
- **Top-1 retrieved (05_maintaining):** You can see that it applied cleanly and automatically created the new commit for you. The author information is taken from the email's From and Date headers, and the message of the commit is taken from the Subject and body (before the patc…

## semantic - q081: right document, wrong passage

- **Question:** How can I make pulling replay my commits rather than merge by default?
- **Evidence (03_rebasing):** you can set the pull.rebase config value
- **First relevant rank:** >10
- **Top-1 retrieved (03_rebasing):** Note that the snapshot pointed to by the final commit you end up with, whether it's the last of the rebased commits for a rebase or the final merge commit after a merge, is the same snapshot -- it's only the history that is different. Reba…

## semantic - q084: right document, wrong passage

- **Question:** Step by step, how does a rebase work internally?
- **Evidence (03_rebasing):** This operation works by going to the common ancestor of the two branches (the one you're on and the one you're rebasing onto), getting the diff introduced by each commit of the branch you're on, saving those diffs to temporary files, resetting the current branch to the same commit as the branch you are rebasing onto, …
- **First relevant rank:** 7
- **Top-1 retrieved (03_rebasing):** When you rebase stuff, you're abandoning existing commits and creating new ones that are similar but different. If you push commits somewhere and others pull them down and base work on them, and then you rewrite those commits with git reba…

## semantic - q089: wrong document

- **Question:** Why can't I move origin/master by hand?
- **Evidence (03_remote-branches):** They're local references that you can't move; Git moves them for you whenever you do any network communication
- **First relevant rank:** >10
- **Top-1 retrieved (05_contributing):** The issue54..origin/master syntax is a log filter that asks Git to display only those commits that are on the latter branch (in this case origin/master) and that are not on the first branch (in this case issue54). We'll go over this syntax…

## semantic - q092: wrong document

- **Question:** How can a local branch be pushed under a different name on the remote?
- **Evidence (03_remote-branches):** You can use this format to push a local branch into a remote branch that is named differently.
- **First relevant rank:** >10
- **Top-1 retrieved (02_remotes):** refs/remotes/origin/issue-11 stale (use 'git remote prune' to remove) Local branches configured for 'git pull': dev-branch merges with remote dev-branch master merges with remote master Local refs configured for 'git push': dev-branch push…

## semantic - q093: wrong document

- **Question:** After fetching a new remote branch do I get an editable local copy of it?
- **Evidence (03_remote-branches):** you don't automatically have local, editable copies of them
- **First relevant rank:** 7
- **Top-1 retrieved (06_3-maintaining):** Now all of the remote pull requests are represented locally with refs that act much like tracking branches; they're read-only, and they update when you do a fetch. This makes it super easy to try the code from a pull request locally: $ git…

## semantic - q098: wrong document

- **Question:** Does fetching change the files in my working directory?
- **Evidence (03_remote-branches):** it will not modify your working directory at all.
- **First relevant rank:** 9
- **Top-1 retrieved (02_recording-changes):** ?? LICENSE.txt New files that aren't tracked have a ?? next to them, new files that have been added to the staging area have an A, modified files have an M and so on. There are two columns to the output -- the left-hand column indicates th…

## semantic - q099: wrong document

- **Question:** What is an upstream branch and when does Git create a tracking branch?
- **Evidence (03_remote-branches):** Checking out a local branch from a remote-tracking branch automatically creates what is called a "tracking branch" (and the branch it tracks is called an "upstream branch"). Tracking branches are local branches that have a direct relationship to a remote branch.
- **First relevant rank:** 9
- **Top-1 retrieved (03_nutshell):** Your Git repository now contains five objects: three blobs (each representing the contents of one of the three files), one tree that lists the contents of the directory and specifies which file names are stored as which blobs, and one comm…

## semantic - q100: wrong document

- **Question:** What does the status command report right after a fresh clone?
- **Evidence (02_recording-changes):** This means you have a clean working directory; in other words, none of your tracked files are modified.
- **First relevant rank:** >10
- **Top-1 retrieved (07_reset):** At this point, if we run git status, we will see the file in green under "Changes to be committed" because the index and HEAD differ -- that is, our proposed next commit is now different from our last commit. Finally, we run git commit to …

## semantic - q101: wrong document

- **Question:** Why do newer repositories often start on main instead of master?
- **Evidence (02_recording-changes):** GitHub changed the default branch name from master to main in mid-2020, and other Git hosts followed suit.
- **First relevant rank:** 9
- **Top-1 retrieved (03_remote-branches):** While "master" is the default name for a starting branch when you run git init which is the only reason it's widely used, "origin" is the default name for a remote when you run git clone. If you run git clone -o booyah instead, then you wi…

## semantic - q112: wrong document

- **Question:** How do I jump back to the branch I was on before?
- **Evidence (03_nutshell):** Return to your previously checked out branch: git switch -.
- **First relevant rank:** >10
- **Top-1 retrieved (07_reset):** You can run git reset --soft HEAD~2 to move the HEAD branch back to an older commit (the most recent commit you want to keep): Moving HEAD with soft reset And then simply run git commit again: Git repository with squashed commit Now you ca…

## semantic - q124: wrong document

- **Question:** How hard is it to lose committed work, and what makes it safer still?
- **Evidence (01_what-is-git):** It is hard to get the system to do anything that is not undoable or to make it erase data in any way. As with any VCS, you can lose or mess up changes you haven't committed yet, but after you commit a snapshot into Git, it is very difficult to lose, especially if you regularly push your database to another repository.
- **First relevant rank:** >10
- **Top-1 retrieved (01_about-version-control):** The most obvious is the single point of failure that the centralized server represents. If that server goes down for an hour, then during that hour nobody can collaborate at all or save versioned changes to anything they're working on. If …

## semantic - q125: wrong document

- **Question:** What are the three steps of the basic Git workflow?
- **Evidence (01_what-is-git):** 1. You modify files in your working tree. 2. You selectively stage just those changes you want to be part of your next commit, which adds only those changes to the staging area. 3. You do a commit, which takes the files as they are in the staging area and stores that snapshot permanently to your Git directory.
- **First relevant rank:** 9
- **Top-1 retrieved (07_reset):** $ tree . ├── README ├── Rakefile └── lib └── simplegit.rb 1 directory, 3 files The Workflow Git's typical workflow is to record snapshots of your project in successively better states, by manipulating these three trees. Git's typical workf…

## semantic - q126: wrong document

- **Question:** Could a corrupted server be restored from a client's clone?
- **Evidence (02_getting-a-repository):** Every version of every file for the history of the project is pulled down by default when you run git clone. In fact, if your server disk gets corrupted, you can often use nearly any of the clones on any client to set the server back to the state it was in when it was cloned
- **First relevant rank:** >10
- **Top-1 retrieved (01_about-version-control):** The most obvious is the single point of failure that the centralized server represents. If that server goes down for an hour, then during that hour nobody can collaborate at all or save versioned changes to anything they're working on. If …

## semantic - q128: right document, wrong passage

- **Question:** What does the stat option add underneath each log entry?
- **Evidence (02_viewing-history):** As you can see, the --stat option prints below each commit entry a list of modified files, how many files were changed, and how many lines in those files were added and removed. It also puts a summary of the information at the end.
- **First relevant rank:** >10
- **Top-1 retrieved (02_viewing-history):** This option changes the log output to formats other than the default. A few prebuilt option values are available for you to use. The oneline value for this option prints each commit on a single line, which is useful if you're looking at a …
