# Failure cases: minilm, dense retrieval, selected configurations

A question counts as a miss when its first relevant chunk is not in the top 5.

## fixed 200 - q003: wrong document

- **Question:** From which Git release can the name of the initial branch be customised?
- **Evidence (01_first-time-setup):** From Git version 2.28 onwards, you can set a different name for the initial branch.
- **First relevant rank:** >10
- **Top-1 retrieved (02_recording-changes):** branch on the server. For now, that branch is always master, which is the default; you won't worry about it here. ch03-git-branching#ch03-git-branching will go over branches and references in detail. GitHub changed the default branch name …

## fixed 200 - q011: right document, wrong passage

- **Question:** What is the formal name for the area that holds what will go into the next commit?
- **Evidence (01_what-is-git):** Its technical name in Git parlance is the "index", but the phrase "staging area" works just as well.
- **First relevant rank:** >10
- **Top-1 retrieved (01_what-is-git):** you want to be part of your next commit, which adds only those changes to the staging area. 3. You do a commit, which takes the files as they are in the staging area and stores that snapshot permanently to your Git directory. If a particul…

## fixed 200 - q022: wrong document

- **Question:** Which URL styles can be used to clone, besides https?
- **Evidence (02_getting-a-repository):** you may also see git:// or user@server:path/to/repo.git, which uses the SSH transfer protocol.
- **First relevant rank:** 8
- **Top-1 retrieved (04_protocols):** The newer version is often referred to as the Smart HTTP protocol and the older way as Dumb HTTP. We'll cover the newer Smart HTTP protocol first. Smart HTTP Smart HTTP operates very similarly to the SSH or Git protocols but runs over stan…

## fixed 200 - q038: wrong document

- **Question:** Is it safe to amend a commit I have already shared with others?
- **Evidence (02_undoing):** Only amend commits that are still local and have not been pushed somewhere.
- **First relevant rank:** >10
- **Top-1 retrieved (07_rewriting-history):** you save and close the editor, the editor writes a new commit containing that updated commit message and makes it your new last commit. If, on the other hand, you want to change the actual content of your last commit, the process works bas…

## fixed 200 - q048: wrong document

- **Question:** After committing three files, how many objects are stored and of which kinds?
- **Evidence (03_nutshell):** Your Git repository now contains five objects: three blobs
- **First relevant rank:** 8
- **Top-1 retrieved (10_packfiles):** done. Delta compression using up to 8 threads. Compressing objects: 100% (14/14), done. Writing objects: 100% (18/18), done. Total 18 (delta 3), reused 0 (delta 0) If you look in your objects directory, you'll find that most of your object…

## fixed 200 - q052: wrong document

- **Question:** What makes a merge commit different from an ordinary commit?
- **Evidence (03_basic-branching-and-merging):** This is referred to as a merge commit, and is special in that it has more than one parent.
- **First relevant rank:** >10
- **Top-1 retrieved (07_signing):** only the latest commit is signed and valid and the previous commits are not. In Git 1.8.3 and later, git merge and git pull can be told to inspect and reject when merging a commit that does not carry a trusted GPG signature with the --veri…

## fixed 200 - q055: right document, wrong passage

- **Question:** Which two kinds of tags does Git support?
- **Evidence (02_tagging):** Git supports two types of tags: lightweight and annotated.
- **First relevant rank:** 7
- **Top-1 retrieved (02_tagging):** Tagging Like most VCSs, Git has the ability to tag specific points in a repository's history as being important. Typically, people use this functionality to mark release points (v1.0, v2.0 and so on). In this section, you'll learn how to l…

## fixed 200 - q057: right document, wrong passage

- **Question:** Does a plain push send my tags to the server?
- **Evidence (02_tagging):** By default, the git push command doesn't transfer tags to remote servers.
- **First relevant rank:** 7
- **Top-1 retrieved (02_tagging):** , done. Writing objects: 100% (1/1), 160 bytes | 0 bytes/s, done. Total 1 (delta 0), reused 0 (delta 0) To git@github.com:schacon/simplegit.git * [new tag] v1.4 -> v1.4 * [new tag] v1.4-lw -> v1.4-lw Now, when someone else clones or pulls …

## fixed 200 - q060: right document, wrong passage

- **Question:** What happens to a commit I make while sitting on a checked-out tag?
- **Evidence (02_tagging):** your new commit won't belong to any branch and will be unreachable, except by the exact commit hash
- **First relevant rank:** 10
- **Top-1 retrieved (02_tagging):** basically the commit checksum stored in a file -- no other information is kept. To create a lightweight tag, don't supply any of the -a, -s, or -m options, just provide a tag name: $ git tag v1.4-lw $ git tag v0.1 v1.3 v1.4 v1.4-lw v1.5 Th…

## fixed 200 - q066: wrong document

- **Question:** What does the star next to a branch name in the listing mean?
- **Evidence (03_branch-management):** it indicates the branch that you currently have checked out
- **First relevant rank:** >10
- **Top-1 retrieved (03_nutshell):** the directory and specifies which file names are stored as which blobs, and one commit with the pointer to that root tree and all the commit metadata. A commit and its tree If you make some changes and commit again, the next commit stores …

## fixed 200 - q068: right document, wrong passage

- **Question:** How do I delete a branch that still has unmerged work?
- **Evidence (03_branch-management):** If you really do want to delete the branch and lose that work, you can force it with -D
- **First relevant rank:** 6
- **Top-1 retrieved (03_branch-management):** in the readme The useful --merged and --no-merged options can filter this list to branches that you have or have not yet merged into the branch you're currently on. To see which branches are already merged into the branch you're on, you ca…

## fixed 200 - q069: right document, wrong passage

- **Question:** Is it fine to rename a branch my teammates are using?
- **Evidence (03_branch-management):** Do not rename branches that are still in use by other collaborators.
- **First relevant rank:** 9
- **Top-1 retrieved (03_branch-management):** branch-name remotes/origin/corrected-branch-name remotes/origin/main Notice that you're on the branch corrected-branch-name and it's available on the remote. However, the branch with the bad name is also still present there but you can del…

## fixed 200 - q074: wrong document

- **Question:** Does branching and merging involve contacting a server?
- **Evidence (03_workflows):** everything is being done only in your Git repository -- there is no communication with the server
- **First relevant rank:** >10
- **Top-1 retrieved (03_remote-branches):** essentially a git fetch immediately followed by a git merge in most cases. If you have a tracking branch set up as demonstrated in the last section, either by explicitly setting it or by having it created for you by the clone or checkout c…

## fixed 200 - q077: right document, wrong passage

- **Question:** What does rebasing do, in one sentence?
- **Evidence (03_rebasing):** you can take all the changes that were committed on one branch and replay them on a different branch.
- **First relevant rank:** 6
- **Top-1 retrieved (03_rebasing):** for this entire process looking like rbdiag_i: $ git branch -d client $ git branch -d server Final commit history The Perils of Rebasing Ahh, but the bliss of rebasing isn't without its drawbacks, which can be summed up in a single line: D…

## fixed 200 - q081: right document, wrong passage

- **Question:** How can I make pulling replay my commits rather than merge by default?
- **Evidence (03_rebasing):** you can set the pull.rebase config value
- **First relevant rank:** >10
- **Top-1 retrieved (03_rebasing):** to the main project. That way, the maintainer doesn't have to do any integration work -- just a fast-forward or a clean apply. Note that the snapshot pointed to by the final commit you end up with, whether it's the last of the rebased comm…

## fixed 200 - q084: right document, wrong passage

- **Question:** Step by step, how does a rebase work internally?
- **Evidence (03_rebasing):** This operation works by going to the common ancestor of the two branches (the one you're on and the one you're rebasing onto), getting the diff introduced by each commit of the branch you're on, saving those diffs to temporary files, resetting the current branch to the same commit as the branch you are rebasing onto, …
- **First relevant rank:** 10
- **Top-1 retrieved (03_rebasing):** to the main project. That way, the maintainer doesn't have to do any integration work -- just a fast-forward or a clean apply. Note that the snapshot pointed to by the final commit you end up with, whether it's the last of the rebased comm…

## fixed 200 - q087: wrong document

- **Question:** What is the argument for tidying up commits before merging them?
- **Evidence (03_rebasing):** The opposing point of view is that the commit history is the story of how your project was made. You wouldn't publish the first draft of a book, so why show your messy work?
- **First relevant rank:** >10
- **Top-1 retrieved (07_advanced-merging):** ===== puts 'hello mundo' >>>>>>> theirs end hello() If you like this format, you can set it as the default for future merge conflicts by setting the merge.conflictstyle setting to diff3. $ git config --global merge.conflictstyle diff3 The …

## fixed 200 - q089: right document, wrong passage

- **Question:** Why can't I move origin/master by hand?
- **Evidence (03_remote-branches):** They're local references that you can't move; Git moves them for you whenever you do any network communication
- **First relevant rank:** >10
- **Top-1 retrieved (03_remote-branches):** , neither does "origin". While "master" is the default name for a starting branch when you run git init which is the only reason it's widely used, "origin" is the default name for a remote when you run git clone. If you run git clone -o bo…

## fixed 200 - q091: right document, wrong passage

- **Question:** Are my local branches pushed to the server automatically?
- **Evidence (03_remote-branches):** Your local branches aren't automatically synchronized to the remotes you write to
- **First relevant rank:** >10
- **Top-1 retrieved (03_remote-branches):** your local branch sf will automatically pull from origin/serverfix. If you already have a local branch and want to set it to a remote branch you just pulled down, or want to change the upstream branch you're tracking, you can use the -u or…

## fixed 200 - q093: wrong document

- **Question:** After fetching a new remote branch do I get an editable local copy of it?
- **Evidence (03_remote-branches):** you don't automatically have local, editable copies of them
- **First relevant rank:** 8
- **Top-1 retrieved (02_remotes):** new work that has been pushed to that server since you cloned (or last fetched from) it. It's important to note that the git fetch command only downloads the data to your local repository -- it doesn't automatically merge it with any of yo…

## fixed 200 - q098: wrong document

- **Question:** Does fetching change the files in my working directory?
- **Evidence (03_remote-branches):** it will not modify your working directory at all.
- **First relevant rank:** >10
- **Top-1 retrieved (06_3-maintaining):** https://github.com/libgit2/libgit2.git fetch = +refs/heads/:refs/remotes/origin/ fetch = +refs/pull//head:refs/remotes/origin/pr/ That last line tells Git, "All the refs that look like refs/pull/123/head should be stored locally like refs/…

## fixed 200 - q100: wrong document

- **Question:** What does the status command report right after a fresh clone?
- **Evidence (02_recording-changes):** This means you have a clean working directory; in other words, none of your tracked files are modified.
- **First relevant rank:** >10
- **Top-1 retrieved (10_transfer-protocols):** server is done with its references listing. Now that it knows the server's state, your send-pack process determines what commits it has that the server doesn't. For each reference that this push will update, the send-pack process tells the…

## fixed 200 - q102: wrong document

- **Question:** What are glob patterns compared to?
- **Evidence (02_recording-changes):** Glob patterns are like simplified regular expressions that shells use.
- **First relevant rank:** 6
- **Top-1 retrieved (10_objects):** with commit or tree. Also, although the blob content can be nearly anything, the commit and tree content are very specifically formatted.

## fixed 200 - q105: wrong document

- **Question:** What does the verbose commit flag add to the message editor?
- **Evidence (02_recording-changes):** Doing so also puts the diff of your change in the editor so you can see exactly what changes you're committing.
- **First relevant rank:** 9
- **Top-1 retrieved (02_undoing):** -message editor fires up, but it already contains the message of your previous commit. You can edit the message the same as always, but it overwrites your previous commit. As an example, if you commit and then realize you forgot to stage t…

## fixed 200 - q106: wrong document

- **Question:** Which command opens diffs in a graphical or external viewer?
- **Evidence (02_recording-changes):** If you run git difftool instead of git diff
- **First relevant rank:** 9
- **Top-1 retrieved (08_attributes):** something like this: diff --git a/image.png b/image.png index 88839c4..4afcb7c 100644 --- a/image.png +++ b/image.png @@ -1,12 +1,12 @@ ExifTool Version Number : 7.74 -File Size : 70 kB -File Modification Date/Time : 2009:04:21 07:02:45-07…

## fixed 200 - q107: wrong document

- **Question:** How should I think about what git add really does?
- **Evidence (02_recording-changes):** git add is a multipurpose command -- you use it to begin tracking new files, to stage files, and to do other things like marking merge-conflicted files as resolved. It may be helpful to think of it more as "add precisely this content to the next commit" rather than "add this file to the project
- **First relevant rank:** >10
- **Top-1 retrieved (01_what-is-git):** What is Git? So, what is Git in a nutshell? This is an important section to absorb, because if you understand what Git is and the fundamentals of how it works, then using Git effectively will probably be much easier for you. As you learn G…

## fixed 200 - q110: wrong document

- **Question:** Why must I commit before switching branches?
- **Evidence (03_basic-branching-and-merging):** if your working directory or staging area has uncommitted changes that conflict with the branch you're checking out, Git won't let you switch branches.
- **First relevant rank:** >10
- **Top-1 retrieved (03_workflows):** - because your work is separated into silos where all the changes in that branch have to do with that topic, it's easier to see what has happened during code review and such. You can keep the changes there for minutes, days, or months, and…

## fixed 200 - q112: wrong document

- **Question:** How do I jump back to the branch I was on before?
- **Evidence (03_nutshell):** Return to your previously checked out branch: git switch -.
- **First relevant rank:** >10
- **Top-1 retrieved (07_rewriting-history):** that follow it. The further back in your repo's history you go, the more commits will need to be recreated. This can cause lots of merge conflicts if you have many commits later in the sequence that depend on the one you just deleted. If y…

## fixed 200 - q116: wrong document

- **Question:** What are the two effects of switching back to the master branch?
- **Evidence (03_nutshell):** That command did two things. It moved the HEAD pointer back to point to the master branch, and it reverted the files in your working directory back to the snapshot that master points to.
- **First relevant rank:** >10
- **Top-1 retrieved (03_branch-management):** no local master branch anymore, because it's renamed to the main branch. To let others see the new main branch, you need to push it to the remote. This makes the renamed branch available on the remote. $ git push --set-upstream origin main…

## fixed 200 - q121: right document, wrong passage

- **Question:** Why would someone build Git from source instead of using an installer?
- **Evidence (01_installing):** Some people may instead find it useful to install Git from source, because you'll get the most recent version. The binary installers tend to be a bit behind, though as Git has matured in recent years, this has made less of a difference.
- **First relevant rank:** >10
- **Top-1 retrieved (01_installing):** to be a bit behind, though as Git has matured in recent years, this has made less of a difference. If you do want to install Git from source, you need to have the following libraries that Git depends on: autotools, curl, zlib, openssl, exp…

## fixed 200 - q124: right document, wrong passage

- **Question:** How hard is it to lose committed work, and what makes it safer still?
- **Evidence (01_what-is-git):** It is hard to get the system to do anything that is not undoable or to make it erase data in any way. As with any VCS, you can lose or mess up changes you haven't committed yet, but after you commit a snapshot into Git, it is very difficult to lose, especially if you regularly push your database to another repository.
- **First relevant rank:** >10
- **Top-1 retrieved (01_what-is-git):** you commit a snapshot into Git, it is very difficult to lose, especially if you regularly push your database to another repository. This makes using Git a joy because we know we can experiment without the danger of severely screwing things…

## fixed 200 - q125: right document, wrong passage

- **Question:** What are the three steps of the basic Git workflow?
- **Evidence (01_what-is-git):** 1. You modify files in your working tree. 2. You selectively stage just those changes you want to be part of your next commit, which adds only those changes to the staging area. 3. You do a commit, which takes the files as they are in the staging area and stores that snapshot permanently to your Git directory.
- **First relevant rank:** >10
- **Top-1 retrieved (01_what-is-git):** the three main sections of a Git project: the working tree, the staging area, and the Git directory. Working tree, staging area, and Git directory The working tree is a single checkout of one version of the project. These files are pulled …

## sentence 200 - q013: right document, wrong passage

- **Question:** Which part of a Git project holds the metadata and the object database?
- **Evidence (01_what-is-git):** The Git directory is where Git stores the metadata and object database for your project.
- **First relevant rank:** 7
- **Top-1 retrieved (01_what-is-git):** Git has three main states that your files can reside in: modified, staged, and committed: - Modified means that you have changed the file but have not committed it to your database yet. - Staged means that you have marked a modified file i…

## sentence 200 - q022: wrong document

- **Question:** Which URL styles can be used to clone, besides https?
- **Evidence (02_getting-a-repository):** you may also see git:// or user@server:path/to/repo.git, which uses the SSH transfer protocol.
- **First relevant rank:** >10
- **Top-1 retrieved (04_protocols):** It has probably become the most popular way to use Git now, since it can be set up to both serve anonymously like the git:// protocol, and can also be pushed over with authentication and encryption like the SSH protocol. Instead of having …

## sentence 200 - q031: right document, wrong passage

- **Question:** Does Git remember that a file was renamed?
- **Evidence (02_recording-changes):** Unlike many other VCSs, Git doesn't explicitly track file movement.
- **First relevant rank:** >10
- **Top-1 retrieved (02_recording-changes):** If you rename a file in Git, no metadata is stored in Git that tells it you renamed the file. However, Git is pretty smart about figuring that out after the fact -- we'll deal with detecting file movement a bit later. Thus it's a bit confu…

## sentence 200 - q048: wrong document

- **Question:** After committing three files, how many objects are stored and of which kinds?
- **Evidence (03_nutshell):** Your Git repository now contains five objects: three blobs
- **First relevant rank:** >10
- **Top-1 retrieved (10_objects):** These three main Git objects -- the blob, the tree, and the commit -- are initially stored as separate files in your .git/objects directory. Here are all the objects in the example directory now, commented with what they store: $ find .git…

## sentence 200 - q051: wrong document

- **Question:** When does Git just move a pointer forward instead of creating a new commit while merging?
- **Evidence (03_basic-branching-and-merging):** there is no divergent work to merge together -- this is called a "fast-forward."
- **First relevant rank:** >10
- **Top-1 retrieved (07_advanced-merging):** This approach also won't work if any other commits have been created since the merge; moving the refs would effectively lose those changes. Reverse the commit If moving the branch pointers around isn't going to work for you, Git gives you …

## sentence 200 - q052: wrong document

- **Question:** What makes a merge commit different from an ordinary commit?
- **Evidence (03_basic-branching-and-merging):** This is referred to as a merge commit, and is special in that it has more than one parent.
- **First relevant rank:** >10
- **Top-1 retrieved (05_contributing):** In this environment, you can follow a workflow similar to what you might do when using Subversion or another centralized system. You still get the advantages of things like offline committing and vastly simpler branching and merging, but t…

## sentence 200 - q066: wrong document

- **Question:** What does the star next to a branch name in the listing mean?
- **Evidence (03_branch-management):** it indicates the branch that you currently have checked out
- **First relevant rank:** >10
- **Top-1 retrieved (02_remotes):** It also shows you which remote branches on the server you don't yet have, which remote branches you have that have been removed from the server, and multiple local branches that are able to merge automatically with their remote-tracking br…

## sentence 200 - q071: right document, wrong passage

- **Question:** Which branches are safe to remove with the lowercase delete flag?
- **Evidence (03_branch-management):** Branches on this list without the * in front of them are generally fine to delete with git branch -d; you've already incorporated their work into another branch, so you're not going to lose anything.
- **First relevant rank:** 6
- **Top-1 retrieved (03_branch-management):** Because it contains work that isn't merged in yet, trying to delete it with git branch -d will fail: $ git branch -d testing error: The branch 'testing' is not fully merged. If you are sure you want to delete it, run 'git branch -D testing…

## sentence 200 - q077: right document, wrong passage

- **Question:** What does rebasing do, in one sentence?
- **Evidence (03_rebasing):** you can take all the changes that were committed on one branch and replay them on a different branch.
- **First relevant rank:** >10
- **Top-1 retrieved (03_rebasing):** Ahh, but the bliss of rebasing isn't without its drawbacks, which can be summed up in a single line: Do not rebase commits that exist outside your repository and that people may have based work on. If you follow that guideline, you'll be f…

## sentence 200 - q080: wrong document

- **Question:** What is a patch-id?
- **Evidence (03_rebasing):** Git also calculates a checksum that is based just on the patch introduced with the commit.
- **First relevant rank:** 10
- **Top-1 retrieved (05_maintaining):** If you receive a patch over email that you need to integrate into your project, you need to apply the patch in your topic branch to evaluate it. There are two ways to apply an emailed patch: with git apply or with git am. Applying a Patch …

## sentence 200 - q081: right document, wrong passage

- **Question:** How can I make pulling replay my commits rather than merge by default?
- **Evidence (03_rebasing):** you can set the pull.rebase config value
- **First relevant rank:** >10
- **Top-1 retrieved (03_rebasing):** Rebasing replays changes from one line of work onto another in the order they were introduced, whereas merging takes the endpoints and merges them together. More Interesting Rebases You can also have your rebase replay on something other t…

## sentence 200 - q084: right document, wrong passage

- **Question:** Step by step, how does a rebase work internally?
- **Evidence (03_rebasing):** This operation works by going to the common ancestor of the two branches (the one you're on and the one you're rebasing onto), getting the diff introduced by each commit of the branch you're on, saving those diffs to temporary files, resetting the current branch to the same commit as the branch you are rebasing onto, …
- **First relevant rank:** >10
- **Top-1 retrieved (03_rebasing):** Rebasing replays changes from one line of work onto another in the order they were introduced, whereas merging takes the endpoints and merges them together. More Interesting Rebases You can also have your rebase replay on something other t…

## sentence 200 - q087: right document, wrong passage

- **Question:** What is the argument for tidying up commits before merging them?
- **Evidence (03_rebasing):** The opposing point of view is that the commit history is the story of how your project was made. You wouldn't publish the first draft of a book, so why show your messy work?
- **First relevant rank:** 6
- **Top-1 retrieved (03_rebasing):** If you or a partner does find it necessary at some point, make sure everyone knows to run git pull --rebase to try to make the pain after it happens a little bit simpler. Rebase vs. Merge Now that you've seen rebasing and merging in action…

## sentence 200 - q089: right document, wrong passage

- **Question:** Why can't I move origin/master by hand?
- **Evidence (03_remote-branches):** They're local references that you can't move; Git moves them for you whenever you do any network communication
- **First relevant rank:** >10
- **Top-1 retrieved (03_remote-branches):** ."origin" is not special Just like the branch name "master" does not have any special meaning in Git, neither does "origin". While "master" is the default name for a starting branch when you run git init which is the only reason it's widel…

## sentence 200 - q099: right document, wrong passage

- **Question:** What is an upstream branch and when does Git create a tracking branch?
- **Evidence (03_remote-branches):** Checking out a local branch from a remote-tracking branch automatically creates what is called a "tracking branch" (and the branch it tracks is called an "upstream branch"). Tracking branches are local branches that have a direct relationship to a remote branch.
- **First relevant rank:** >10
- **Top-1 retrieved (03_remote-branches):** Tracking branches are local branches that have a direct relationship to a remote branch. If you're on a tracking branch and type git pull, Git automatically knows which server to fetch from and which branch to merge in. When you clone a re…

## sentence 200 - q101: wrong document

- **Question:** Why do newer repositories often start on main instead of master?
- **Evidence (02_recording-changes):** GitHub changed the default branch name from master to main in mid-2020, and other Git hosts followed suit.
- **First relevant rank:** 8
- **Top-1 retrieved (05_maintaining):** This means master almost always moves forward, next is rebased occasionally, and seen is rebased even more often: Merging contributed topic branches into long-term integration branches When a topic branch has finally been merged into maste…

## sentence 200 - q105: wrong document

- **Question:** What does the verbose commit flag add to the message editor?
- **Evidence (02_recording-changes):** Doing so also puts the diff of your change in the editor so you can see exactly what changes you're committing.
- **First relevant rank:** >10
- **Top-1 retrieved (08_hooks):** The prepare-commit-msg hook is run before the commit message editor is fired up but after the default message is created. It lets you edit the default message before the commit author sees it. This hook takes a few parameters: the path to …

## sentence 200 - q107: wrong document

- **Question:** How should I think about what git add really does?
- **Evidence (02_recording-changes):** git add is a multipurpose command -- you use it to begin tracking new files, to stage files, and to do other things like marking merge-conflicted files as resolved. It may be helpful to think of it more as "add precisely this content to the next commit" rather than "add this file to the project
- **First relevant rank:** >10
- **Top-1 retrieved (10_plumbing-porcelain):** You'll now look at each of these sections in detail to see how Git operates.

## sentence 200 - q110: wrong document

- **Question:** Why must I commit before switching branches?
- **Evidence (03_basic-branching-and-merging):** if your working directory or staging area has uncommitted changes that conflict with the branch you're checking out, Git won't let you switch branches.
- **First relevant rank:** >10
- **Top-1 retrieved (05_contributing):** On a project for which you're not the maintainer, it's generally easier to have a branch like master always track origin/master and to do your work in topic branches that you can easily discard if they're rejected. Having work themes isola…

## sentence 200 - q112: wrong document

- **Question:** How do I jump back to the branch I was on before?
- **Evidence (03_nutshell):** Return to your previously checked out branch: git switch -.
- **First relevant rank:** >10
- **Top-1 retrieved (10_maintenance):** Date: Fri May 22 18:22:37 2009 -0700 Third commit commit ab1afef80fac8e34258ff41fc1b867c702daa24b Reflog: HEAD@{1} (Scott Chacon <schacon@gmail.com>) Reflog message: updating HEAD Author: Scott Chacon <schacon@gmail.com> Date: Fri May 22 1…

## sentence 200 - q115: right document, wrong passage

- **Question:** Why is creating a branch in Git instant while older tools take minutes?
- **Evidence (03_nutshell):** Because a branch in Git is actually a simple file that contains the 40 character SHA-1 checksum of the commit it points to, branches are cheap to create and destroy. Creating a new branch is as quick and simple as writing 41 bytes to a file (40 characters and a newline). This is in sharp contrast to the way most older…
- **First relevant rank:** 6
- **Top-1 retrieved (03_nutshell):** This can take several seconds or even minutes, depending on the size of the project, whereas in Git the process is always instantaneous. Also, because we're recording the parents when we commit, finding a proper merge base for merging is a…

## sentence 200 - q116: wrong document

- **Question:** What are the two effects of switching back to the master branch?
- **Evidence (03_nutshell):** That command did two things. It moved the HEAD pointer back to point to the master branch, and it reverted the files in your working directory back to the snapshot that master points to.
- **First relevant rank:** 10
- **Top-1 retrieved (05_maintaining):** This means master almost always moves forward, next is rebased occasionally, and seen is rebased even more often: Merging contributed topic branches into long-term integration branches When a topic branch has finally been merged into maste…

## sentence 200 - q123: wrong document

- **Question:** Can file contents change without Git noticing?
- **Evidence (01_what-is-git):** Everything in Git is checksummed before it is stored and is then referred to by that checksum. This means it's impossible to change the contents of any file or directory without Git knowing about it.
- **First relevant rank:** >10
- **Top-1 retrieved (08_attributes):** In addition, you get all this for very little overhead. 1.1.1. Local Version Control Systems Many people's version-control method of choice is to copy files into another directory (perhaps a time-stamped directory, if they're clever). This…

## sentence 200 - q125: wrong document

- **Question:** What are the three steps of the basic Git workflow?
- **Evidence (01_what-is-git):** 1. You modify files in your working tree. 2. You selectively stage just those changes you want to be part of your next commit, which adds only those changes to the staging area. 3. You do a commit, which takes the files as they are in the staging area and stores that snapshot permanently to your Git directory.
- **First relevant rank:** 6
- **Top-1 retrieved (10_plumbing-porcelain):** You'll now look at each of these sections in detail to see how Git operates.

## recursive 200 - q003: wrong document

- **Question:** From which Git release can the name of the initial branch be customised?
- **Evidence (01_first-time-setup):** From Git version 2.28 onwards, you can set a different name for the initial branch.
- **First relevant rank:** 8
- **Top-1 retrieved (02_recording-changes):** GitHub changed the default branch name from master to main in mid-2020, and other Git hosts followed suit. So you may find that the default branch name in some newly created repositories is main and not master. In addition, the default bra…

## recursive 200 - q011: wrong document

- **Question:** What is the formal name for the area that holds what will go into the next commit?
- **Evidence (01_what-is-git):** Its technical name in Git parlance is the "index", but the phrase "staging area" works just as well.
- **First relevant rank:** 10
- **Top-1 retrieved (07_reset):** The index is your proposed next commit. We've also been referring to this concept as Git's "Staging Area" as this is what Git looks at when you run git commit. Git populates this index with a list of all the file contents that were last ch…

## recursive 200 - q022: wrong document

- **Question:** Which URL styles can be used to clone, besides https?
- **Evidence (02_getting-a-repository):** you may also see git:// or user@server:path/to/repo.git, which uses the SSH transfer protocol.
- **First relevant rank:** >10
- **Top-1 retrieved (04_protocols):** In fact, for services like GitHub, the URL you use to view the repository online (for example, ^ (https://github.com/schacon/simplegit)) is the same URL you can use to clone and, if you have access, push over. Dumb HTTP

## recursive 200 - q044: right document, wrong passage

- **Question:** What exactly is a branch in Git's data model?
- **Evidence (03_nutshell):** A branch in Git is simply a lightweight movable pointer to one of these commits.
- **First relevant rank:** 6
- **Top-1 retrieved (03_nutshell):** Branches in a Nutshell To really understand the way Git does branching, we need to take a step back and examine how Git stores its data. As you may remember from ch01-getting-started#what_is_git_section, Git doesn't store data as a series …

## recursive 200 - q060: right document, wrong passage

- **Question:** What happens to a commit I make while sitting on a checked-out tag?
- **Evidence (02_tagging):** your new commit won't belong to any branch and will be unreachable, except by the exact commit hash
- **First relevant rank:** >10
- **Top-1 retrieved (02_tagging):** Tagging Later You can also tag commits after you've moved past them. Suppose your commit history looks like this:

## recursive 200 - q066: wrong document

- **Question:** What does the star next to a branch name in the listing mean?
- **Evidence (03_branch-management):** it indicates the branch that you currently have checked out
- **First relevant rank:** >10
- **Top-1 retrieved (03_nutshell):** How does Git know what branch you're currently on? It keeps a special pointer called HEAD. Note that this is a lot different than the concept of HEAD in other VCSs you may be used to, such as Subversion or CVS. In Git, this is a pointer to…

## recursive 200 - q077: right document, wrong passage

- **Question:** What does rebasing do, in one sentence?
- **Evidence (03_rebasing):** you can take all the changes that were committed on one branch and replay them on a different branch.
- **First relevant rank:** >10
- **Top-1 retrieved (03_rebasing):** The Perils of Rebasing Ahh, but the bliss of rebasing isn't without its drawbacks, which can be summed up in a single line: Do not rebase commits that exist outside your repository and that people may have based work on. If you follow that…

## recursive 200 - q080: wrong document

- **Question:** What is a patch-id?
- **Evidence (03_rebasing):** Git also calculates a checksum that is based just on the patch introduced with the commit.
- **First relevant rank:** >10
- **Top-1 retrieved (05_maintaining):** This modifies the files in your working directory. It's almost identical to running a patch -p1 command to apply the patch, although it's more paranoid and accepts fewer fuzzy matches than patch. It also handles file adds, deletes, and ren…

## recursive 200 - q081: right document, wrong passage

- **Question:** How can I make pulling replay my commits rather than merge by default?
- **Evidence (03_rebasing):** you can set the pull.rebase config value
- **First relevant rank:** >10
- **Top-1 retrieved (03_rebasing):** Note that the snapshot pointed to by the final commit you end up with, whether it's the last of the rebased commits for a rebase or the final merge commit after a merge, is the same snapshot -- it's only the history that is different. Reba…

## recursive 200 - q084: right document, wrong passage

- **Question:** Step by step, how does a rebase work internally?
- **Evidence (03_rebasing):** This operation works by going to the common ancestor of the two branches (the one you're on and the one you're rebasing onto), getting the diff introduced by each commit of the branch you're on, saving those diffs to temporary files, resetting the current branch to the same commit as the branch you are rebasing onto, …
- **First relevant rank:** >10
- **Top-1 retrieved (03_rebasing):** Note that the snapshot pointed to by the final commit you end up with, whether it's the last of the rebased commits for a rebase or the final merge commit after a merge, is the same snapshot -- it's only the history that is different. Reba…

## recursive 200 - q087: right document, wrong passage

- **Question:** What is the argument for tidying up commits before merging them?
- **Evidence (03_rebasing):** The opposing point of view is that the commit history is the story of how your project was made. You wouldn't publish the first draft of a book, so why show your messy work?
- **First relevant rank:** >10
- **Top-1 retrieved (03_rebasing):** If you or a partner does find it necessary at some point, make sure everyone knows to run git pull --rebase to try to make the pain after it happens a little bit simpler. Rebase vs. Merge Now that you've seen rebasing and merging in action…

## recursive 200 - q089: right document, wrong passage

- **Question:** Why can't I move origin/master by hand?
- **Evidence (03_remote-branches):** They're local references that you can't move; Git moves them for you whenever you do any network communication
- **First relevant rank:** >10
- **Top-1 retrieved (03_remote-branches):** ."origin" is not special Just like the branch name "master" does not have any special meaning in Git, neither does "origin". While "master" is the default name for a starting branch when you run git init which is the only reason it's widel…

## recursive 200 - q091: right document, wrong passage

- **Question:** Are my local branches pushed to the server automatically?
- **Evidence (03_remote-branches):** Your local branches aren't automatically synchronized to the remotes you write to
- **First relevant rank:** >10
- **Top-1 retrieved (03_remote-branches):** $ git checkout serverfix Branch serverfix set up to track remote branch serverfix from origin. Switched to a new branch 'serverfix' To set up a local branch with a different name than the remote branch, you can easily use the first version…

## recursive 200 - q093: wrong document

- **Question:** After fetching a new remote branch do I get an editable local copy of it?
- **Evidence (03_remote-branches):** you don't automatically have local, editable copies of them
- **First relevant rank:** 7
- **Top-1 retrieved (02_remotes):** If your current branch is set up to track a remote branch (see the next section and ch03-git-branching#ch03-git-branching for more information), you can use the git pull command to automatically fetch and then merge that remote branch into…

## recursive 200 - q099: right document, wrong passage

- **Question:** What is an upstream branch and when does Git create a tracking branch?
- **Evidence (03_remote-branches):** Checking out a local branch from a remote-tracking branch automatically creates what is called a "tracking branch" (and the branch it tracks is called an "upstream branch"). Tracking branches are local branches that have a direct relationship to a remote branch.
- **First relevant rank:** >10
- **Top-1 retrieved (03_remote-branches):** $ git branch -u origin/serverfix Branch serverfix set up to track remote branch serverfix from origin. Upstream shorthand When you have a tracking branch set up, you can reference its upstream branch with the @{upstream} or @{u} shorthand.…

## recursive 200 - q100: right document, wrong passage

- **Question:** What does the status command report right after a fresh clone?
- **Evidence (02_recording-changes):** This means you have a clean working directory; in other words, none of your tracked files are modified.
- **First relevant rank:** >10
- **Top-1 retrieved (02_recording-changes):** Untracked files are everything else -- any files in your working directory that were not in your last snapshot and are not in your staging area. When you first clone a repository, all of your files will be tracked and unmodified because Gi…

## recursive 200 - q105: wrong document

- **Question:** What does the verbose commit flag add to the message editor?
- **Evidence (02_recording-changes):** Doing so also puts the diff of your change in the editor so you can see exactly what changes you're committing.
- **First relevant rank:** >10
- **Top-1 retrieved (08_hooks):** The prepare-commit-msg hook is run before the commit message editor is fired up but after the default message is created. It lets you edit the default message before the commit author sees it. This hook takes a few parameters: the path to …

## recursive 200 - q107: wrong document

- **Question:** How should I think about what git add really does?
- **Evidence (02_recording-changes):** git add is a multipurpose command -- you use it to begin tracking new files, to stage files, and to do other things like marking merge-conflicted files as resolved. It may be helpful to think of it more as "add precisely this content to the next commit" rather than "add this file to the project
- **First relevant rank:** >10
- **Top-1 retrieved (01_what-is-git):** What is Git? So, what is Git in a nutshell? This is an important section to absorb, because if you understand what Git is and the fundamentals of how it works, then using Git effectively will probably be much easier for you. As you learn G…

## recursive 200 - q109: right document, wrong passage

- **Question:** What does git rm do beyond removing the file from disk?
- **Evidence (02_recording-changes):** To remove a file from Git, you have to remove it from your tracked files (more accurately, remove it from your staging area) and then commit. The git rm command does that, and also removes the file from your working directory so you don't see it as an untracked file the next time around.
- **First relevant rank:** >10
- **Top-1 retrieved (02_recording-changes):** If you simply remove the file from your working directory, it shows up under the "Changes not staged for commit" (that is, unstaged) area of your git status output: $ rm PROJECTS.md $ git status On branch master Your branch is up-to-date w…

## recursive 200 - q116: right document, wrong passage

- **Question:** What are the two effects of switching back to the master branch?
- **Evidence (03_nutshell):** That command did two things. It moved the HEAD pointer back to point to the master branch, and it reverted the files in your working directory back to the snapshot that master points to.
- **First relevant rank:** >10
- **Top-1 retrieved (03_nutshell):** The "master" branch in Git is not a special branch. It is exactly like any other branch. The only reason nearly every repository has one is that the git init command creates it by default and most people don't bother to change it. A branch…

## recursive 200 - q124: right document, wrong passage

- **Question:** How hard is it to lose committed work, and what makes it safer still?
- **Evidence (01_what-is-git):** It is hard to get the system to do anything that is not undoable or to make it erase data in any way. As with any VCS, you can lose or mess up changes you haven't committed yet, but after you commit a snapshot into Git, it is very difficult to lose, especially if you regularly push your database to another repository.
- **First relevant rank:** >10
- **Top-1 retrieved (01_what-is-git):** This also means that there is very little you can't do if you're offline or off VPN. If you get on an airplane or a train and want to do a little work, you can commit happily (to your local copy, remember?) until you get to a network conne…

## recursive 200 - q125: wrong document

- **Question:** What are the three steps of the basic Git workflow?
- **Evidence (01_what-is-git):** 1. You modify files in your working tree. 2. You selectively stage just those changes you want to be part of your next commit, which adds only those changes to the staging area. 3. You do a commit, which takes the files as they are in the staging area and stores that snapshot permanently to your Git directory.
- **First relevant rank:** 6
- **Top-1 retrieved (05_contributing):** All these questions can affect how you contribute effectively to a project and what workflows are preferred or available to you. We'll cover aspects of each of these in a series of use cases, moving from simple to more complex; you should …

## fixed_overlap 200+20 - q011: wrong document

- **Question:** What is the formal name for the area that holds what will go into the next commit?
- **Evidence (01_what-is-git):** Its technical name in Git parlance is the "index", but the phrase "staging area" works just as well.
- **First relevant rank:** >10
- **Top-1 retrieved (07_reset):** file, and indicate it in red. Git repository with changed file in the working directory If we run git status right now, we'll see the file in red as "Changes not staged for commit", because that entry differs between the index and the work…

## fixed_overlap 200+20 - q022: wrong document

- **Question:** Which URL styles can be used to clone, besides https?
- **Evidence (02_getting-a-repository):** you may also see git:// or user@server:path/to/repo.git, which uses the SSH transfer protocol.
- **First relevant rank:** >10
- **Top-1 retrieved (06_3-maintaining):** place, it also sets up a redirect from your URL to the new place. It will also redirect clones and fetches from Git, not just web requests.

## fixed_overlap 200+20 - q028: right document, wrong passage

- **Question:** How can a commit skip the explicit add step for files Git already follows?
- **Evidence (02_recording-changes):** Adding the -a option to the git commit command makes Git automatically stage every file that is already tracked before doing the commit
- **First relevant rank:** >10
- **Top-1 retrieved (02_recording-changes):** already tracked before doing the commit, letting you skip the git add part: $ git status On branch master Your branch is up-to-date with 'origin/master'. Changes not staged for commit: (use "git add <file>..." to update what will be commit…

## fixed_overlap 200+20 - q044: right document, wrong passage

- **Question:** What exactly is a branch in Git's data model?
- **Evidence (03_nutshell):** A branch in Git is simply a lightweight movable pointer to one of these commits.
- **First relevant rank:** >10
- **Top-1 retrieved (03_nutshell):** Branches in a Nutshell To really understand the way Git does branching, we need to take a step back and examine how Git stores its data. As you may remember from ch01-getting-started#what_is_git_section, Git doesn't store data as a series …

## fixed_overlap 200+20 - q051: wrong document

- **Question:** When does Git just move a pointer forward instead of creating a new commit while merging?
- **Evidence (03_basic-branching-and-merging):** there is no divergent work to merge together -- this is called a "fast-forward."
- **First relevant rank:** >10
- **Top-1 retrieved (05_contributing):** , 1 insertions(+), 0 deletions(-) As long as that local merge goes smoothly, John's updated history will now look like this: John's repository after merging origin/master At this point, John might want to test this new code to make sure no…

## fixed_overlap 200+20 - q052: wrong document

- **Question:** What makes a merge commit different from an ordinary commit?
- **Evidence (03_basic-branching-and-merging):** This is referred to as a merge commit, and is special in that it has more than one parent.
- **First relevant rank:** >10
- **Top-1 retrieved (05_contributing):** log --no-merges issue54..origin/master commit 738ee872852dfaa9d6634e0dea7a324040193016 Author: John Smith <jsmith@example.com> Date: Fri May 29 16:01:27 2009 -0700 Remove invalid default value The issue54..origin/master syntax is a log fil…

## fixed_overlap 200+20 - q054: wrong document

- **Question:** How do I tell Git that a conflicted file is now fixed?
- **Evidence (03_basic-branching-and-merging):** run git add on each file to mark it as resolved
- **First relevant rank:** 10
- **Top-1 retrieved (07_advanced-merging):** this though to give us much more specific context. If we add the --merge option to git log, it will only show the commits in either side of the merge that touch a file that's currently conflicted. $ git log --oneline --left-right --merge <…

## fixed_overlap 200+20 - q066: wrong document

- **Question:** What does the star next to a branch name in the listing mean?
- **Evidence (03_branch-management):** it indicates the branch that you currently have checked out
- **First relevant rank:** >10
- **Top-1 retrieved (03_nutshell):** . It is exactly like any other branch. The only reason nearly every repository has one is that the git init command creates it by default and most people don't bother to change it. A branch and its commit history Creating a New Branch What…

## fixed_overlap 200+20 - q071: right document, wrong passage

- **Question:** Which branches are safe to remove with the lowercase delete flag?
- **Evidence (03_branch-management):** Branches on this list without the * in front of them are generally fine to delete with git branch -d; you've already incorporated their work into another branch, so you're not going to lose anything.
- **First relevant rank:** 6
- **Top-1 retrieved (03_branch-management):** the old branch. After you've done all these tasks, and are certain the main branch performs just as the master branch, you can delete the master branch: $ git push origin --delete master

## fixed_overlap 200+20 - q077: wrong document

- **Question:** What does rebasing do, in one sentence?
- **Evidence (03_rebasing):** you can take all the changes that were committed on one branch and replay them on a different branch.
- **First relevant rank:** >10
- **Top-1 retrieved (06_2-contributing):** the target branch is (normally the master branch of the repository you forked), or you can merge the target branch into your branch. Most developers on GitHub will choose to do the latter, for the same reasons we just went over in the prev…

## fixed_overlap 200+20 - q080: wrong document

- **Question:** What is a patch-id?
- **Evidence (03_rebasing):** Git also calculates a checksum that is based just on the patch introduced with the commit.
- **First relevant rank:** 7
- **Top-1 retrieved (05_maintaining):** it doesn't work if the commit the patch says it was based on isn't in your repository. If you do have that commit -- if the patch was based on a public commit -- then the -3 option is generally much smarter about applying a conflicting pat…

## fixed_overlap 200+20 - q081: right document, wrong passage

- **Question:** How can I make pulling replay my commits rather than merge by default?
- **Evidence (03_rebasing):** you can set the pull.rebase config value
- **First relevant rank:** >10
- **Top-1 retrieved (03_rebasing):** apply cleanly on a remote branch -- perhaps in a project to which you're trying to contribute but that you don't maintain. In this case, you'd do your work in a branch and then rebase your work onto origin/master when you were ready to sub…

## fixed_overlap 200+20 - q084: right document, wrong passage

- **Question:** Step by step, how does a rebase work internally?
- **Evidence (03_rebasing):** This operation works by going to the common ancestor of the two branches (the one you're on and the one you're rebasing onto), getting the diff introduced by each commit of the branch you're on, saving those diffs to temporary files, resetting the current branch to the same commit as the branch you are rebasing onto, …
- **First relevant rank:** >10
- **Top-1 retrieved (03_rebasing):** together. More Interesting Rebases You can also have your rebase replay on something other than the rebase target branch. Take a history like rbdiag_e, for example. You branched a topic branch (server) to add some server-side functionality…

## fixed_overlap 200+20 - q089: right document, wrong passage

- **Question:** Why can't I move origin/master by hand?
- **Evidence (03_remote-branches):** They're local references that you can't move; Git moves them for you whenever you do any network communication
- **First relevant rank:** >10
- **Top-1 retrieved (03_remote-branches):** place as origin's master branch, so you have something to work from. ."origin" is not special Just like the branch name "master" does not have any special meaning in Git, neither does "origin". While "master" is the default name for a star…

## fixed_overlap 200+20 - q091: right document, wrong passage

- **Question:** Are my local branches pushed to the server automatically?
- **Evidence (03_remote-branches):** Your local branches aren't automatically synchronized to the remotes you write to
- **First relevant rank:** 7
- **Top-1 retrieved (03_remote-branches):** branch name: $ git checkout -b sf origin/serverfix Branch sf set up to track remote branch serverfix from origin. Switched to a new branch 'sf' Now, your local branch sf will automatically pull from origin/serverfix. If you already have a …

## fixed_overlap 200+20 - q092: wrong document

- **Question:** How can a local branch be pushed under a different name on the remote?
- **Evidence (03_remote-branches):** You can use this format to push a local branch into a remote branch that is named differently.
- **First relevant rank:** 9
- **Top-1 retrieved (02_remotes):** : dev-branch merges with remote dev-branch master merges with remote master Local refs configured for 'git push': dev-branch pushes to dev-branch (up to date) markdown-strip pushes to markdown-strip (up to date) master pushes to master (up…

## fixed_overlap 200+20 - q093: wrong document

- **Question:** After fetching a new remote branch do I get an editable local copy of it?
- **Evidence (03_remote-branches):** you don't automatically have local, editable copies of them
- **First relevant rank:** >10
- **Top-1 retrieved (02_remotes):** use them in much more detail in ch03-git-branching#ch03-git-branching. Fetching and Pulling from Your Remotes As you just saw, to get data from your remote projects, you can run: $ git fetch <remote> The command goes out to that remote pro…

## fixed_overlap 200+20 - q098: wrong document

- **Question:** Does fetching change the files in my working directory?
- **Evidence (03_remote-branches):** it will not modify your working directory at all.
- **First relevant rank:** >10
- **Top-1 retrieved (06_3-maintaining):** " Now, if you save that file, and do a git fetch: $ git fetch # … * [new ref] refs/pull/1/head -> origin/pr/1 * [new ref] refs/pull/2/head -> origin/pr/2 * [new ref] refs/pull/4/head -> origin/pr/4 # … Now all of the remote pull requests a…

## fixed_overlap 200+20 - q101: wrong document

- **Question:** Why do newer repositories often start on main instead of master?
- **Evidence (02_recording-changes):** GitHub changed the default branch name from master to main in mid-2020, and other Git hosts followed suit.
- **First relevant rank:** 6
- **Top-1 retrieved (05_maintaining):** pushed up so everyone can try the topics integrated together. Managing a complex series of parallel contributed topic branches If the topics still need work, they're merged into seen instead. When it's determined that they're totally stabl…

## fixed_overlap 200+20 - q104: right document, wrong passage

- **Question:** Do ignore files in subfolders affect the whole repository?
- **Evidence (02_recording-changes):** The rules in these nested .gitignore files apply only to the files under the directory where they are located.
- **First relevant rank:** >10
- **Top-1 retrieved (02_recording-changes):** .gitignore file: # ignore all .a files *.a # but do track lib.a, even though you're ignoring .a files above !lib.a # only ignore the TODO file in the current directory, not subdir/TODO /TODO # ignore all files in any directory named build …

## fixed_overlap 200+20 - q105: wrong document

- **Question:** What does the verbose commit flag add to the message editor?
- **Evidence (02_recording-changes):** Doing so also puts the diff of your change in the editor so you can see exactly what changes you're committing.
- **First relevant rank:** >10
- **Top-1 retrieved (08_config):** t will fire up Emacs to edit messages. `commit.template` If you set this to the path of a file on your system, Git will use that file as the default initial message when you commit. The value in creating a custom commit template is that yo…

## fixed_overlap 200+20 - q106: wrong document

- **Question:** Which command opens diffs in a graphical or external viewer?
- **Evidence (02_recording-changes):** If you run git difftool instead of git diff
- **First relevant rank:** >10
- **Top-1 retrieved (08_config):** , ul (underline), blink, and reverse (swap foreground and background). External Merge and Diff Tools Although Git has an internal implementation of diff, which is what we've been showing in this book, you can set up an external tool instea…

## fixed_overlap 200+20 - q110: wrong document

- **Question:** Why must I commit before switching branches?
- **Evidence (03_basic-branching-and-merging):** if your working directory or staging area has uncommitted changes that conflict with the branch you're checking out, Git won't let you switch branches.
- **First relevant rank:** >10
- **Top-1 retrieved (05_contributing):** er -- it tells them where the work was branched from, summarizes the commits, and identifies from where the new work is to be pulled. On a project for which you're not the maintainer, it's generally easier to have a branch like master alwa…

## fixed_overlap 200+20 - q112: wrong document

- **Question:** How do I jump back to the branch I was on before?
- **Evidence (03_nutshell):** Return to your previously checked out branch: git switch -.
- **First relevant rank:** >10
- **Top-1 retrieved (03_branch-management):** the old branch. After you've done all these tasks, and are certain the main branch performs just as the master branch, you can delete the master branch: $ git push origin --delete master

## fixed_overlap 200+20 - q114: right document, wrong passage

- **Question:** What happens to the default branch pointer as I commit, and is that branch special?
- **Evidence (03_nutshell):** As you start making commits, you're given a master branch that points to the last commit you made. Every time you commit, the master branch pointer moves forward automatically. The "master" branch in Git is not a special branch. It is exactly like any other branch.
- **First relevant rank:** >10
- **Top-1 retrieved (03_nutshell):** . It is exactly like any other branch. The only reason nearly every repository has one is that the git init command creates it by default and most people don't bother to change it. A branch and its commit history Creating a New Branch What…

## fixed_overlap 200+20 - q116: wrong document

- **Question:** What are the two effects of switching back to the master branch?
- **Evidence (03_nutshell):** That command did two things. It moved the HEAD pointer back to point to the master branch, and it reverted the files in your working directory back to the snapshot that master points to.
- **First relevant rank:** >10
- **Top-1 retrieved (05_maintaining):** pushed up so everyone can try the topics integrated together. Managing a complex series of parallel contributed topic branches If the topics still need work, they're merged into seen instead. When it's determined that they're totally stabl…

## fixed_overlap 200+20 - q124: right document, wrong passage

- **Question:** How hard is it to lose committed work, and what makes it safer still?
- **Evidence (01_what-is-git):** It is hard to get the system to do anything that is not undoable or to make it erase data in any way. As with any VCS, you can lose or mess up changes you haven't committed yet, but after you commit a snapshot into Git, it is very difficult to lose, especially if you regularly push your database to another repository.
- **First relevant rank:** >10
- **Top-1 retrieved (01_what-is-git):** to do it locally. This also means that there is very little you can't do if you're offline or off VPN. If you get on an airplane or a train and want to do a little work, you can commit happily (to your local copy, remember?) until you get …

## semantic p85 - q003: wrong document

- **Question:** From which Git release can the name of the initial branch be customised?
- **Evidence (01_first-time-setup):** From Git version 2.28 onwards, you can set a different name for the initial branch.
- **First relevant rank:** >10
- **Top-1 retrieved (02_recording-changes):** So you may find that the default branch name in some newly created repositories is main and not master. In addition, the default branch name can be changed (as you have seen in ch01-getting-started#_new_default_branch), so you may see a di…

## semantic p85 - q011: wrong document

- **Question:** What is the formal name for the area that holds what will go into the next commit?
- **Evidence (01_what-is-git):** Its technical name in Git parlance is the "index", but the phrase "staging area" works just as well.
- **First relevant rank:** 7
- **Top-1 retrieved (07_replace):** 622e88e9cbfbacfb75b5279245b9fb38dfea10cf ===== The commit-tree command is one of a set of commands that are commonly referred to as 'plumbing' commands. These are commands that are not generally meant to be used directly, but instead are u…

## semantic p85 - q028: right document, wrong passage

- **Question:** How can a commit skip the explicit add step for files Git already follows?
- **Evidence (02_recording-changes):** Adding the -a option to the git commit command makes Git automatically stage every file that is already tracked before doing the commit
- **First relevant rank:** >10
- **Top-1 retrieved (02_recording-changes):** Untracked files: (use "git add <file>..." to include in what will be committed) README nothing added to commit but untracked files present (use "git add" to track) You can see that your new README file is untracked, because it's under the …

## semantic p85 - q036: wrong document

- **Question:** How can I keep merge commits from cluttering the log output?
- **Evidence (02_viewing-history):** simply add the log option --no-merges
- **First relevant rank:** 10
- **Top-1 retrieved (07_advanced-merging):** At this point we can use the git clean command to clear out the extra files we created to do the manual merge but no longer need. $ git clean -f Removing hello.common.rb Removing hello.ours.rb Removing hello.theirs.rb Checking Out Conflict…

## semantic p85 - q041: wrong document

- **Question:** What is the standard nickname for the server a repository was cloned from?
- **Evidence (02_remotes):** origin -- that is the default name Git gives to the server you cloned from
- **First relevant rank:** >10
- **Top-1 retrieved (02_getting-a-repository):** We'll go over what these commands do in just a minute. At this point, you have a Git repository with tracked files and an initial commit. Cloning an Existing Repository If you want to get a copy of an existing Git repository -- for example…

## semantic p85 - q048: wrong document

- **Question:** After committing three files, how many objects are stored and of which kinds?
- **Evidence (03_nutshell):** Your Git repository now contains five objects: three blobs
- **First relevant rank:** 9
- **Top-1 retrieved (10_packfiles):** How does Git do this? When Git packs objects, it looks for files that are named and sized similarly, and stores just the deltas from one version of the file to the next. You can look into the packfile and see what Git did to save space. Th…

## semantic p85 - q052: wrong document

- **Question:** What makes a merge commit different from an ordinary commit?
- **Evidence (03_basic-branching-and-merging):** This is referred to as a merge commit, and is special in that it has more than one parent.
- **First relevant rank:** 6
- **Top-1 retrieved (07_advanced-merging):** Both sides of the merge added content to this file, but some of the commits modified the file in the same place that caused this conflict. Let's explore a couple of tools that you now have at your disposal to determine how this conflict ca…

## semantic p85 - q074: wrong document

- **Question:** Does branching and merging involve contacting a server?
- **Evidence (03_workflows):** everything is being done only in your Git repository -- there is no communication with the server
- **First relevant rank:** 8
- **Top-1 retrieved (03_remote-branches):** You could do that like this: $ git fetch --all; git branch -vv Pulling While the git fetch command will fetch all the changes on the server that you don't have yet, it will not modify your working directory at all. It will simply get the d…

## semantic p85 - q077: right document, wrong passage

- **Question:** What does rebasing do, in one sentence?
- **Evidence (03_rebasing):** you can take all the changes that were committed on one branch and replay them on a different branch.
- **First relevant rank:** >10
- **Top-1 retrieved (03_rebasing):** People in this camp use tools like rebase and filter-branch to rewrite their commits before they're merged into the mainline branch. They use tools like rebase and filter-branch, to tell the story in the way that's best for future readers.…

## semantic p85 - q079: right document, wrong passage

- **Question:** What is the main rule to follow when rebasing?
- **Evidence (03_rebasing):** Do not rebase commits that exist outside your repository and that people may have based work on.
- **First relevant rank:** >10
- **Top-1 retrieved (03_rebasing):** People in this camp use tools like rebase and filter-branch to rewrite their commits before they're merged into the mainline branch. They use tools like rebase and filter-branch, to tell the story in the way that's best for future readers.…

## semantic p85 - q080: wrong document

- **Question:** What is a patch-id?
- **Evidence (03_rebasing):** Git also calculates a checksum that is based just on the patch introduced with the commit.
- **First relevant rank:** >10
- **Top-1 retrieved (05_maintaining):** This modifies the files in your working directory. It's almost identical to running a patch -p1 command to apply the patch, although it's more paranoid and accepts fewer fuzzy matches than patch. It also handles file adds, deletes, and ren…

## semantic p85 - q081: wrong document

- **Question:** How can I make pulling replay my commits rather than merge by default?
- **Evidence (03_rebasing):** you can set the pull.rebase config value
- **First relevant rank:** >10
- **Top-1 retrieved (06_3-maintaining):** Branch pr/2 set up to track remote branch pr/2 from origin. Switched to a new branch 'pr/2' The eagle-eyed among you would note the head on the end of the remote portion of the refspec. There's also a refs/pull/#/merge ref on the GitHub si…

## semantic p85 - q084: wrong document

- **Question:** Step by step, how does a rebase work internally?
- **Evidence (03_rebasing):** This operation works by going to the common ancestor of the two branches (the one you're on and the one you're rebasing onto), getting the diff introduced by each commit of the branch you're on, saving those diffs to temporary files, resetting the current branch to the same commit as the branch you are rebasing onto, …
- **First relevant rank:** >10
- **Top-1 retrieved (07_replace):** You can read more about plumbing commands in ch10-git-internals#_plumbing_porcelain. ===== Creating a base commit using commit-tree OK, so now that we have a base commit, we can rebase the rest of our history on top of that with git rebase…

## semantic p85 - q087: wrong document

- **Question:** What is the argument for tidying up commits before merging them?
- **Evidence (03_rebasing):** The opposing point of view is that the commit history is the story of how your project was made. You wouldn't publish the first draft of a book, so why show your messy work?
- **First relevant rank:** >10
- **Top-1 retrieved (07_advanced-merging):** At this point we can use the git clean command to clear out the extra files we created to do the manual merge but no longer need. $ git clean -f Removing hello.common.rb Removing hello.ours.rb Removing hello.theirs.rb Checking Out Conflict…

## semantic p85 - q089: wrong document

- **Question:** Why can't I move origin/master by hand?
- **Evidence (03_remote-branches):** They're local references that you can't move; Git moves them for you whenever you do any network communication
- **First relevant rank:** >10
- **Top-1 retrieved (03_nutshell):** HEAD moves when you checkout That command did two things. It moved the HEAD pointer back to point to the master branch, and it reverted the files in your working directory back to the snapshot that master points to. This also means the cha…

## semantic p85 - q093: wrong document

- **Question:** After fetching a new remote branch do I get an editable local copy of it?
- **Evidence (03_remote-branches):** you don't automatically have local, editable copies of them
- **First relevant rank:** >10
- **Top-1 retrieved (02_remotes):** Fetching and Pulling from Your Remotes As you just saw, to get data from your remote projects, you can run: $ git fetch <remote> The command goes out to that remote project and pulls down all the data from that remote project that you don'…

## semantic p85 - q098: wrong document

- **Question:** Does fetching change the files in my working directory?
- **Evidence (03_remote-branches):** it will not modify your working directory at all.
- **First relevant rank:** >10
- **Top-1 retrieved (08_attributes):** 1.1.1. Local Version Control Systems Many people's version-control method of choice is to copy files into another directory (perhaps a time-stamped directory, if they're clever). This approach is very common because it is so simple, but it…

## semantic p85 - q099: wrong document

- **Question:** What is an upstream branch and when does Git create a tracking branch?
- **Evidence (03_remote-branches):** Checking out a local branch from a remote-tracking branch automatically creates what is called a "tracking branch" (and the branch it tracks is called an "upstream branch"). Tracking branches are local branches that have a direct relationship to a remote branch.
- **First relevant rank:** >10
- **Top-1 retrieved (03_nutshell):** As you start making commits, you're given a master branch that points to the last commit you made. Every time you commit, the master branch pointer moves forward automatically. The "master" branch in Git is not a special branch. It is exac…

## semantic p85 - q100: wrong document

- **Question:** What does the status command report right after a fresh clone?
- **Evidence (02_recording-changes):** This means you have a clean working directory; in other words, none of your tracked files are modified.
- **First relevant rank:** >10
- **Top-1 retrieved (02_getting-a-repository):** We'll go over what these commands do in just a minute. At this point, you have a Git repository with tracked files and an initial commit. Cloning an Existing Repository If you want to get a copy of an existing Git repository -- for example…

## semantic p85 - q101: wrong document

- **Question:** Why do newer repositories often start on main instead of master?
- **Evidence (02_recording-changes):** GitHub changed the default branch name from master to main in mid-2020, and other Git hosts followed suit.
- **First relevant rank:** >10
- **Top-1 retrieved (05_maintaining):** When new work is introduced by contributors, it's collected into topic branches in the maintainer's repository in a manner similar to what we've described (see merwf_f). At this point, the topics are evaluated to determine whether they're …

## semantic p85 - q107: wrong document

- **Question:** How should I think about what git add really does?
- **Evidence (02_recording-changes):** git add is a multipurpose command -- you use it to begin tracking new files, to stage files, and to do other things like marking merge-conflicted files as resolved. It may be helpful to think of it more as "add precisely this content to the next commit" rather than "add this file to the project
- **First relevant rank:** >10
- **Top-1 retrieved (07_bundling):** So, git bundle can be really useful for sharing or doing network-type operations when you don't have the proper network or shared repository to do so.

## semantic p85 - q110: wrong document

- **Question:** Why must I commit before switching branches?
- **Evidence (03_basic-branching-and-merging):** if your working directory or staging area has uncommitted changes that conflict with the branch you're checking out, Git won't let you switch branches.
- **First relevant rank:** >10
- **Top-1 retrieved (07_submodules):** ... Please move or remove them before you can switch branches. Aborting You can force it to switch with checkout -f, but be careful that you don't have unsaved changes in there as they could be overwritten with that command. $ git checkout…

## semantic p85 - q112: wrong document

- **Question:** How do I jump back to the branch I was on before?
- **Evidence (03_nutshell):** Return to your previously checked out branch: git switch -.
- **First relevant rank:** >10
- **Top-1 retrieved (03_rebasing):** The easiest way to integrate the branches, as we've already covered, is the merge command. It performs a three-way merge between the two latest branch snapshots (C3 and C4) and the most recent common ancestor of the two (C2), creating a ne…

## semantic p85 - q124: right document, wrong passage

- **Question:** How hard is it to lose committed work, and what makes it safer still?
- **Evidence (01_what-is-git):** It is hard to get the system to do anything that is not undoable or to make it erase data in any way. As with any VCS, you can lose or mess up changes you haven't committed yet, but after you commit a snapshot into Git, it is very difficult to lose, especially if you regularly push your database to another repository.
- **First relevant rank:** >10
- **Top-1 retrieved (01_what-is-git):** This also means that there is very little you can't do if you're offline or off VPN. If you get on an airplane or a train and want to do a little work, you can commit happily (to your local copy, remember?) until you get to a network conne…
