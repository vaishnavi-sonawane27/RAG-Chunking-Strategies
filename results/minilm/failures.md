# Failure cases: minilm, dense retrieval, selected configurations

A question counts as a miss when its first relevant chunk is not in the top 5.

## fixed 100 - q004: wrong document

- **Question:** Does skill with a graphical Git tool transfer to the terminal as readily as the reverse?
- **Evidence (01_command-line):** If you know how to run the command-line version, you can probably also figure out how to run the GUI version, while the opposite is not necessarily true.
- **First relevant rank:** >10
- **Top-1 retrieved (01_what-is-git):** What is Git? So, what is Git in a nutshell? This is an important section to absorb, because if you understand what Git is and the fundamentals of how it works, then using Git effectively will probably be much easier for you. As you learn G…

## fixed 100 - q005: wrong document

- **Question:** Which kind of Git interface can I count on every user already having?
- **Evidence (01_command-line):** all users will have the command-line tools installed and available.
- **First relevant rank:** >10
- **Top-1 retrieved (04_git-on-a-server):** to do to run a useful Git server to which several people have access -- just add SSH-able accounts on a server, and stick a bare repository somewhere that all those users have read and write access to. You're ready to go -- nothing else ne…

## fixed 100 - q012: wrong document

- **Question:** Which flag prints a brief list of a command's options instead of the whole manual?
- **Evidence (01_help):** In addition, if you don't need the full-blown manpage help, but just need a quick refresher on the available options for a Git command, you can ask for the more concise "help" output with the -h option, as in:
- **First relevant rank:** 10
- **Top-1 retrieved (07_interactive-staging):** ll go into more details on each of these as we get to more advanced usages of these commands.

## fixed 100 - q021: wrong document

- **Question:** Where does Git keep the record of what is queued up for the next commit?
- **Evidence (01_what-is-git):** The staging area is a file, generally contained in your Git directory, that stores information about what will go into your next commit.
- **First relevant rank:** >10
- **Top-1 retrieved (08_hooks):** commit hook runs. It doesn't take any parameters, but you can easily get the last commit by running git log -1 HEAD. Generally, this script is used for notification or something similar. Email Workflow Hooks You can set up three client-sid…

## fixed 100 - q026: right document, wrong passage

- **Question:** Can I choose a target folder name that differs from the project's own?
- **Evidence (02_getting-a-repository):** If you want to clone the repository into a directory named something other than libgit2, you can specify the new directory name as an additional argument:
- **First relevant rank:** >10
- **Top-1 retrieved (02_getting-a-repository):** you want to start controlling it with Git, you first need to go to that project's directory. If you've never done this, it looks a little different depending on which system you're running: for Linux: $ cd /home/user/my_project for macOS: …

## fixed 100 - q028: wrong document

- **Question:** I edited a file again after staging it; what do I have to do before committing?
- **Evidence (02_recording-changes):** If you modify a file after you run git add, you have to run git add again to stage the latest version of the file:
- **First relevant rank:** >10
- **Top-1 retrieved (02_undoing):** steps, and undo things with git restore instead of git reset. Unstaging a Staged File with git restore The next two sections demonstrate how to work with your staging area and working directory changes with git restore. The nice part is th…

## fixed 100 - q031: wrong document

- **Question:** Besides downloading new commits, what else does pulling do?
- **Evidence (02_remotes):** Running git pull generally fetches data from the server you originally cloned from and automatically tries to merge it into the code you're currently working on.
- **First relevant rank:** >10
- **Top-1 retrieved (06_3-maintaining):** Pull Requests can either come from a branch in a fork of your repository or they can come from another branch in the same repository. The only difference is that the ones in a fork are often from people where you can't push to their branch…

## fixed 100 - q038: wrong document

- **Question:** When is rewriting the most recent commit considered safe?
- **Evidence (02_undoing):** Only amend commits that are still local and have not been pushed somewhere.
- **First relevant rank:** >10
- **Top-1 retrieved (07_rewriting-history):** SHA-1 of the commit. It's like a very small rebase -- don't amend your last commit if you've already pushed it. An amended commit may (or may not) need an amended commit message When you amend a commit, you have the opportunity to change b…

## fixed 100 - q039: right document, wrong passage

- **Question:** Which Git release brought in a dedicated command for undoing file changes?
- **Evidence (02_undoing):** Git version 2.23.0 introduced a new command: git restore. It's basically an alternative to git reset which we just covered.
- **First relevant rank:** 10
- **Top-1 retrieved (02_undoing):** Undoing Things At any stage, you may want to undo something. Here, we'll review a few basic tools for undoing changes that you've made. Be careful, because you can't always undo some of these undos. This is one of the few areas in Git wher…

## fixed 100 - q041: right document, wrong passage

- **Question:** In what sequence are commits printed when no options are supplied?
- **Evidence (02_viewing-history):** By default, with no arguments, git log lists the commits made in that repository in reverse chronological order; that is, the most recent commits show up first.
- **First relevant rank:** 9
- **Top-1 retrieved (02_viewing-history):** a3f659402fe7563abf99ad00de2209e6 Initial commit The most interesting option value is format, which allows you to specify your own log output format. This is especially useful when you're generating output for machine parsing -- because you…

## fixed 100 - q045: right document, wrong passage

- **Question:** Why was no new snapshot needed when the hotfix work was integrated back into master?
- **Evidence (03_basic-branching-and-merging):** Because the commit C4 pointed to by the branch hotfix you merged in was directly ahead of the commit C2 you're on, Git simply moves the pointer forward.
- **First relevant rank:** 6
- **Top-1 retrieved (03_basic-branching-and-merging):** fix. master is fast-forwarded to hotfix After your super-important fix is deployed, you're ready to switch back to the work you were doing before you were interrupted. However, first you'll delete the hotfix branch, because you no longer n…

## fixed 100 - q046: right document, wrong passage

- **Question:** How can you get rid of a branch whose work has not been incorporated anywhere else?
- **Evidence (03_branch-management):** If you really do want to delete the branch and lose that work, you can force it with -D, as the helpful message points out.
- **First relevant rank:** >10
- **Top-1 retrieved (03_branch-management):** of them are generally fine to delete with git branch -d; you've already incorporated their work into another branch, so you're not going to lose anything. To see all the branches that contain work you haven't yet merged in, you can run git…

## fixed 100 - q047: wrong document

- **Question:** What does the asterisk shown beside one entry in the branch listing mean?
- **Evidence (03_branch-management):** Notice the * character that prefixes the master branch: it indicates the branch that you currently have checked out (i.e., the branch that HEAD points to).
- **First relevant rank:** >10
- **Top-1 retrieved (06_2-contributing):** it rendered like _eg_task_lists. Task lists rendered in a Markdown comment This is often used in Pull Requests to indicate what all you would like to get done on the branch before the Pull Request will be ready to merge. The really cool pa…

## fixed 100 - q053: wrong document

- **Question:** What does the rebase command do with work recorded on one branch?
- **Evidence (03_rebasing):** With the rebase command, you can take all the changes that were committed on one branch and replay them on a different branch.
- **First relevant rank:** >10
- **Top-1 retrieved (05_maintaining):** . This is useful if you have a number of commits on a topic branch and you want to integrate only one of them, or if you only have one commit on a topic branch and you'd prefer to cherry-pick it rather than run rebase. For example, suppose…

## fixed 100 - q054: wrong document

- **Question:** Which commits must never be rebased?
- **Evidence (03_rebasing):** Do not rebase commits that exist outside your repository and that people may have based work on.
- **First relevant rank:** >10
- **Top-1 retrieved (07_rewriting-history):** commit> to reword the commit message. # # These lines can be re-ordered; they are executed from top to bottom. # # If you remove a line here THAT COMMIT WILL BE LOST. # # However, if you remove everything, the rebase will be aborted. # # N…

## fixed 100 - q057: right document, wrong passage

- **Question:** What do local pointers such as origin/master actually stand for?
- **Evidence (03_remote-branches):** Remote-tracking branches are references to the state of remote branches.
- **First relevant rank:** >10
- **Top-1 retrieved (03_remote-branches):** .com. If you clone from this, Git's clone command automatically names it origin for you, pulls down all its data, creates a pointer to where its master branch is, and names it origin/master locally. Git also gives you your own local master…

## fixed 100 - q061: right document, wrong passage

- **Question:** In which folder does a user normally find their existing SSH keys?
- **Evidence (04_generating-ssh-key):** By default, a user's SSH keys are stored in that user's ~/.ssh directory.
- **First relevant rank:** 7
- **Top-1 retrieved (04_generating-ssh-key):** you have a key already by going to that directory and listing the contents: $ cd ~/.ssh $ ls authorized_keys2 id_dsa known_hosts config id_dsa.pub You're looking for a pair of files named something like id_dsa or id_rsa and a matching file…

## fixed 100 - q066: wrong document

- **Question:** Which port has to be opened if a firewall sits in front of the machine?
- **Evidence (04_git-daemon):** If you're running a firewall, you'll also need to punch a hole in it at port 9418 on the box you're setting this up on.
- **First relevant rank:** >10
- **Top-1 retrieved (04_protocols):** from it. The Cons The cons of this method are that shared access is generally more difficult to set up and reach from multiple locations than basic network access. If you want to push from your laptop when you're at home, you have to mount…

## fixed 100 - q075: wrong document

- **Question:** Which setting tells the build where your repositories live when generating the script?
- **Evidence (04_gitweb):** Notice that you have to tell the command where to find your Git repositories with the GITWEB_PROJECTROOT variable.
- **First relevant rank:** >10
- **Top-1 retrieved (08_hooks):** Git directory. In most projects, that's .git/hooks. When you initialize a new repository with git init, Git populates the hooks directory with a bunch of example scripts, many of which are useful by themselves; but they also document the i…

## fixed 100 - q078: wrong document

- **Question:** Why would someone running an internal server still put open source code on a public service?
- **Evidence (04_hosted):** you may still want to use a public hosting site for your open source code -- it's generally easier for the open source community to find and help you with.
- **First relevant rank:** 9
- **Top-1 retrieved (05_contributing):** In short, do as we say, not as we do. Private Small Team The simplest setup you're likely to encounter is a private project with one or two other developers. "Private," in this context, means closed-source -- not accessible to the outside …

## fixed 100 - q079: wrong document

- **Question:** How many transport mechanisms can move data, and which are they?
- **Evidence (04_protocols):** Git can use four distinct protocols to transfer data: Local, HTTP, Secure Shell (SSH) and Git.
- **First relevant rank:** 6
- **Top-1 retrieved (10_transfer-protocols):** 1d11a7 0032have 441b40d833fdfa93eb2908e52742248faf0ee993 0000 Again, this is the same format as above. The response to this request indicates success or failure, and includes the packfile. Protocols Summary This section contains a very bas…

## fixed 100 - q084: wrong document

- **Question:** Which bundled tool keeps a shared account confined to version-control operations?
- **Evidence (04_setting-up-server):** You can easily restrict the git user account to only Git-related activities with a limited shell tool called git-shell that comes with Git.
- **First relevant rank:** >10
- **Top-1 retrieved (01_about-version-control):** About Version Control What is "version control", and why should you care? Version control is a system that records changes to a file or set of files over time so that you can recall specific versions later. For the examples in this book, y…

## fixed 100 - q087: wrong document

- **Question:** Why does the group ownership of the repository directories need changing?
- **Evidence (04_smart-http):** You'll also need to set the Unix user group of the /srv/git directories to www-data so your web server can read- and write-access the repositories
- **First relevant rank:** >10
- **Top-1 retrieved (04_git-on-a-server):** :/srv/git/my_project.git If a user SSHs into a server and has write access to the /srv/git/my_project.git directory, they will also automatically have push access. Git will automatically add group write permissions to a repository properly…

## fixed 100 - q089: right document, wrong passage

- **Question:** Which Git command will list possible whitespace problems in your work before you make the commit?
- **Evidence (05_contributing):** Git provides an easy way to check for this -- before you commit, run git diff --check, which identifies possible whitespace errors and lists them for you.
- **First relevant rank:** >10
- **Top-1 retrieved (05_contributing):** possible whitespace errors and lists them for you. Output of git diff --check If you run that command before committing, you can tell if you're about to commit whitespace issues that may annoy other developers. Next, try to make each commi…

## fixed 100 - q091: wrong document

- **Question:** Why must a force flag be added when pushing a topic branch whose history you have just rewritten with a rebase?
- **Evidence (05_contributing):** Because you rebased the branch, you have to specify the -f to your push command in order to be able to replace the featureA branch on the server with a commit that isn't a descendant of it.
- **First relevant rank:** >10
- **Top-1 retrieved (05_maintaining):** . This is useful if you have a number of commits on a topic branch and you want to integrate only one of them, or if you only have one commit on a topic branch and you'd prefer to cherry-pick it rather than run rebase. For example, suppose…

## fixed 100 - q097: right document, wrong passage

- **Question:** When a mailed patch is applied, which parts of the email supply the commit's authorship and its message?
- **Evidence (05_maintaining):** The author information is taken from the email's From and Date headers, and the message of the commit is taken from the Subject and body (before the patch) of the email.
- **First relevant rank:** 7
- **Top-1 retrieved (05_maintaining):** ) of the email. For example, if this patch was applied from the mbox example above, the commit generated would look something like this: $ git log --pretty=fuller -1 commit 6c5e70b984a60b3cecd395edd5b48a7575bf58e0 Author: Jessica Smith <je…

## fixed 100 - q101: wrong document

- **Question:** What piece of information does GitHub use to attribute a commit to a particular member?
- **Evidence (06_1-setting-up-account):** The way that GitHub maps your Git commits to your user is by email address.
- **First relevant rank:** >10
- **Top-1 retrieved (10_environment):** Git commit object is usually done by git-commit-tree, which uses these environment variables as its primary source of information, falling back to configuration values only if these aren't present. GIT_AUTHOR_NAME is the human-readable nam…

## fixed 100 - q103: wrong document

- **Question:** Why is it worth giving each uploaded public key a label such as the machine it belongs to?
- **Evidence (06_1-setting-up-account):** You can name each of your keys (e.g. "My Laptop" or "Work Account") so that if you need to revoke a key later, you can easily tell which one you're looking for.
- **First relevant rank:** 7
- **Top-1 retrieved (10_refs):** public key as a blob object and then tagged it. You can view the public key by running this in a clone of the Git repository: $ git cat-file blob junio-gpg-pub The Linux kernel repository also has a non-commit-pointing tag object -- the fi…

## fixed 100 - q104: right document, wrong passage

- **Question:** After forking on GitHub, who owns the resulting copy and where does it sit?
- **Evidence (06_2-contributing):** When you "fork" a project, GitHub will make a copy of the project that is entirely yours; it lives in your namespace, and you can push to it.
- **First relevant rank:** 10
- **Top-1 retrieved (06_2-contributing):** Fork" button After a few seconds, you'll be taken to your new project page, with your own writeable copy of the code. The GitHub Flow GitHub is designed around a particular collaboration workflow, centered on Pull Requests. This flow works…

## fixed 100 - q116: right document, wrong passage

- **Question:** How does the generic hooks mechanism hand event data over to your own system?
- **Evidence (06_5-scripting):** You specify a URL and GitHub will post an HTTP payload to that URL on any event you want.
- **First relevant rank:** >10
- **Top-1 retrieved (06_5-scripting):** you have a nice developer console in the same screen where you set the hook up. You can see the last few deliveries that GitHub has tried to make for that webhook. For each hook you can dig down into when it was delivered, if it was succes…

## fixed 100 - q122: wrong document

- **Question:** Which numbered index slot holds the common ancestor of a conflicted file, and which one holds the incoming branch's copy?
- **Evidence (07_advanced-merging):** Stage 1 is the common ancestor, stage 2 is your version and stage 3 is from the MERGE_HEAD, the version you're merging in ("theirs").
- **First relevant rank:** >10
- **Top-1 retrieved (07_reset):** a6d12cb4b6f19... lib The Git cat-file and ls-tree commands are "plumbing" commands that are used for lower level things and not really used in day-to-day work, but they help us see what's going on here. The Index The index is your proposed…

## fixed 100 - q124: wrong document

- **Question:** Does Git work out automatically which refs belong in a bundle, or must I enumerate them?
- **Evidence (07_bundling):** With the bundle command you need to list out every reference or specific range of commits that you want to be included.
- **First relevant rank:** >10
- **Top-1 retrieved (10_maintenance):** refs/heads/master git/refs/tags/v1.0 git/refs/tags/v1.1 If you run git gc, you'll no longer have these files in the refs directory. Git will move them for the sake of efficiency into a file named .git/packed-refs that looks like this: $ ca…

## fixed 100 - q125: wrong document

- **Question:** What artifact does Git produce from the data a push would normally send across the network?
- **Evidence (07_bundling):** The bundle command will package up everything that would normally be pushed over the wire with a git push command into a binary file
- **First relevant rank:** >10
- **Top-1 retrieved (10_transfer-protocols):** and a pair for downloading data. Uploading Data To upload data to a remote process, Git uses the send-pack and receive-pack processes. The send-pack process runs on the client and connects to a receive-pack process on the remote side. SSH …

## fixed 100 - q126: wrong document

- **Question:** What goes wrong if someone packages only their newest couple of commits and the receiving repository lacks the earlier ones?
- **Evidence (07_bundling):** If the bundler had created a bundle of just the last two commits they had done, rather than all three, the original repository would not be able to import it, since it is missing requisite history.
- **First relevant rank:** 6
- **Top-1 retrieved (05_maintaining):** the commits as well. Although you may have legitimate merge issues, you know where in your history their work is based; a proper three-way merge is the default rather than having to supply a -3 and hope the patch was generated off a public…

## fixed 100 - q130: right document, wrong passage

- **Question:** Which credential helper ships with Git on Apple machines, and where does it keep the secrets?
- **Evidence (07_credentials):** If you're using macOS, Git comes with an "osxkeychain" mode, which caches credentials in the secure keychain that's attached to your system account.
- **First relevant rank:** >10
- **Top-1 retrieved (07_credentials):** -credential-store replies with the username and password we stored above. Here's what the ~/git.store file looks like: https://bob:s3cre7@mygithost It's just a series of lines, each of which contains a credential-decorated URL. The osxkeyc…

## fixed 100 - q132: right document, wrong passage

- **Question:** After tracking down the faulty revision, what command returns me to the checkout I had beforehand?
- **Evidence (07_debugging):** When you're finished, you should run git bisect reset to reset your HEAD to where you were before you started, or you'll end up in a weird state
- **First relevant rank:** >10
- **Top-1 retrieved (07_debugging):** you know the code worked, you'll likely turn to git bisect for help. The bisect command does a binary search through your commit history to help you identify as quickly as possible which commit introduced an issue. Let's say you just pushe…

## fixed 100 - q134: wrong document

- **Question:** What search technique does Git use to pin down the revision that introduced a regression?
- **Evidence (07_debugging):** The bisect command does a binary search through your commit history to help you identify as quickly as possible which commit introduced an issue.
- **First relevant rank:** 10
- **Top-1 retrieved (07_searching):** Searching With just about any size codebase, you'll often need to find where a function is called or defined, or display the history of a method. Git provides a couple of useful tools for looking through the code and commits stored in its …

## fixed 100 - q137: right document, wrong passage

- **Question:** Inside the menu-driven prompt, which letter or number takes a file back out of the staging area?
- **Evidence (07_interactive-staging):** If you want to unstage the TODO file at this point, you use the r or 3 (for revert) option
- **First relevant rank:** >10
- **Top-1 retrieved (07_interactive-staging):** ged changes on the right. After this comes a "Commands" section, which allows you to do a number of things like staging and unstaging files, staging parts of files, adding untracked files, and displaying diffs of what has been staged. Stag…

## fixed 100 - q138: right document, wrong passage

- **Question:** Which menu choice displays the changes already added to the staging area?
- **Evidence (07_interactive-staging):** To see the diff of what you've staged, you can use the d or 6 (for diff) command.
- **First relevant rank:** >10
- **Top-1 retrieved (07_interactive-staging):** [a]dd untracked 5: [p]atch 6: [d]iff 7: [q]uit 8: [h]elp What now> You can see that this command shows you a much different view of your staging area than you're probably used to -- basically, the same information you get with git status b…

## fixed 100 - q142: right document, wrong passage

- **Question:** When joining a short recent history to a long archived one, which two commits do you pair up?
- **Evidence (07_replace):** You can graft one history onto the other by "replacing" the earliest commit in the new line with the latest commit on the older one.
- **First relevant rank:** >10
- **Top-1 retrieved (07_replace):** > project-history/master Now the collaborator would have their recent commits in the master branch and the historical commits in the project-history/master branch. $ git log --oneline master e146b5f Fifth commit 81a708d Fourth commit 622e8…

## fixed 100 - q144: wrong document

- **Question:** Apart from the config flag, which directory can I create inside one repository to switch the feature on there?
- **Evidence (07_rerere):** You can also turn it on by creating the .git/rr-cache directory in a specific repository, but the config setting is clearer and enables that feature globally for you.
- **First relevant rank:** >10
- **Top-1 retrieved (04_git-on-a-server):** repository by itself, without a working directory, and creates a directory specifically for it alone. Putting the Bare Repository on a Server Now that you have a bare copy of your repository, all you need to do is put it on a server and se…

## fixed 100 - q148: right document, wrong passage

- **Question:** Between resetting and checking out a branch, which one relocates the branch pointer and which relocates HEAD?
- **Evidence (07_reset):** Whereas reset will move the branch that HEAD points to, checkout will move HEAD itself to point to another branch.
- **First relevant rank:** >10
- **Top-1 retrieved (07_reset):** HEAD points to it). If we run git reset master, develop itself will now point to the same commit that master does. If we instead run git checkout master, develop does not move, HEAD itself does. HEAD will now point to master. So, in both c…

## fixed 100 - q152: right document, wrong passage

- **Question:** How far back does Git's background record of where HEAD and branch tips have pointed normally reach?
- **Evidence (07_revision-selection):** One of the things Git does in the background while you're working away is keep a "reflog" -- a log of where your HEAD and branch references have been for the last few months.
- **First relevant rank:** >10
- **Top-1 retrieved (07_revision-selection):** pick): updating HEAD Every time your branch tip is updated for any reason, Git stores that information for you in this temporary history. You can use your reflog data to refer to older commits as well. For example, if you want to see the f…

## fixed 100 - q154: right document, wrong passage

- **Question:** What notation picks out the second parent of a merge commit such as d921970?
- **Evidence (07_revision-selection):** You can also specify a number after the ^ to identify which parent you want; for example, d921970^2 means "the second parent of d921970."
- **First relevant rank:** >10
- **Top-1 retrieved (07_revision-selection):** parent of d921970." This syntax is useful only for merge commits, which have more than one parent -- the first parent of a merge commit is from the branch you were on when you merged (frequently master), while the second parent of a merge …

## fixed 100 - q160: wrong document

- **Question:** How can you ask the log command to replay the whole evolution of a single function as patches?
- **Evidence (07_searching):** Simply run git log with the -L option, and it will show you the history of a function or line of code in your codebase.
- **First relevant rank:** >10
- **Top-1 retrieved (05_maintaining):** <schacon@gmail.com> CommitDate: Thu Apr 9 09:19:06 2009 -0700 Add limit to log function Limit log functionality to the first 20 The Commit information indicates the person who applied the patch and the time it was applied. The Author infor…

## fixed 100 - q162: wrong document

- **Question:** Which pickaxe-style log flag takes a regular expression rather than a fixed string?
- **Evidence (07_searching):** If you need to be more specific, you can provide a regular expression to search for with the -G option.
- **First relevant rank:** >10
- **Top-1 retrieved (10_environment):** 'log' '--graph' '--pretty=oneline' '--abbrev-commit' '--decorate' '--all' 20:12:49.879885 git.c:349 trace: built-in: git 'log' '--graph' '--pretty=oneline' '--abbrev-commit' '--decorate' '--all' 20:12:49

## fixed 100 - q168: wrong document

- **Question:** Since -u still skips files matched by ignore rules, what flag sweeps those in as well?
- **Evidence (07_stashing-cleaning):** including untracked files in the stash will still not include explicitly ignored files; to additionally include ignored files, use --all (or just -a).
- **First relevant rank:** >10
- **Top-1 retrieved (02_recording-changes):** b/z, a/b/c/z, and so on. Here is another example .gitignore file: # ignore all .a files *.a # but do track lib.a, even though you're ignoring .a files above !lib.a # only ignore the TODO file in the current directory, not subdir/TODO /TODO…

## fixed 100 - q170: right document, wrong passage

- **Question:** Which popular stash flag puts staged content into the saved entry yet still leaves that content ready for commit?
- **Evidence (07_stashing-cleaning):** The first option that is quite popular is the --keep-index option to the git stash command. This tells Git to not only include all staged content in the stash being created, but simultaneously leave it in the index.
- **First relevant rank:** 10
- **Top-1 retrieved (07_stashing-cleaning):** tracked files and staged changes -- and saves it on a stack of unfinished changes that you can reapply at any time (even on a different branch). Migrating to git stash push As of late October 2017, there has been extensive discussion on th…

## fixed 100 - q172: right document, wrong passage

- **Question:** What argument to clone fills in every subproject, including ones nested inside them, without extra steps?
- **Evidence (07_submodules):** If you pass --recurse-submodules to the git clone command, it will automatically initialize and update each submodule in the repository, including nested submodules if any of the submodules in the repository have submodules themselves.
- **First relevant rank:** 9
- **Top-1 retrieved (07_submodules):** have submodules themselves. $ git clone --recurse-submodules https://github.com/chaconinc/MainProject Cloning into 'MainProject'... remote: Counting objects: 14, done. remote: Compressing objects: 100% (13/13), done. remote: Total 14 (delt…

## fixed 100 - q178: wrong document

- **Question:** Which plumbing command loads another branch's top-level tree into your index and working files?
- **Evidence (07_subtree-merges):** You'll learn more about read-tree and its friends in ch10-git-internals#ch10-git-internals, but for now know that it reads the root tree of one branch into your current staging area and working directory.
- **First relevant rank:** >10
- **Top-1 retrieved (07_reset):** a6d12cb4b6f19... lib The Git cat-file and ls-tree commands are "plumbing" commands that are used for lower level things and not really used in day-to-day work, but they help us see what's going on here. The Index The index is your proposed…

## fixed 100 - q179: wrong document

- **Question:** Which two settings bring the vendored project's updates across with a ready-made commit message?
- **Evidence (07_subtree-merges):** To pull in the changes and prepopulate the commit message, use the --squash option, as well as the recursive merge strategy's -Xsubtree option.
- **First relevant rank:** >10
- **Top-1 retrieved (05_contributing):** with previous behavior -- this is a good guideline to follow. Write your commit message in the imperative: "Fix bug" and not "Fixed bug" or "Fixes bug." Here is a template you can follow, which we've lightly adapted from one originally wri…

## fixed 100 - q182: wrong document

- **Question:** Why might a content filter that works for you break for a colleague who clones the same project?
- **Evidence (08_attributes):** You have to be careful, though, because the .gitattributes file is committed and passed around with the project, but the driver (in this case, dater) isn't, so it won't work everywhere.
- **First relevant rank:** >10
- **Top-1 retrieved (05_distributed-workflows):** or repository, can accept code, and everyone synchronizes their work with it. A number of developers are nodes -- consumers of that hub -- and synchronize with that centralized location. Centralized workflow This means that if two develope…

## fixed 100 - q184: wrong document

- **Question:** Which configuration file is consulted first, and whose repositories does it affect?
- **Evidence (08_config):** The first place Git looks for these values is in the system-wide [path]/etc/gitconfig file, which contains settings that are applied to every user on the system and all of their repositories.
- **First relevant rank:** >10
- **Top-1 retrieved (01_first-time-setup):** or ~/.config/git/config file: Values specific personally to you, the user. You can make Git read and write to this file specifically by passing the --global option, and this affects all of the repositories you work with on your system. 3. …

## fixed 100 - q187: right document, wrong passage

- **Question:** When somebody pushes several branches at once, how many times does each of the two main receive-side scripts run?
- **Evidence (08_hooks):** The update script is very similar to the pre-receive script, except that it's run once for each branch the pusher is trying to update.
- **First relevant rank:** >10
- **Top-1 retrieved (08_hooks):** that it's run once for each branch the pusher is trying to update. If the pusher is trying to push to multiple branches, pre-receive runs only once, whereas update runs once per branch they're pushing to. Instead of reading from stdin, thi…

## fixed 100 - q189: wrong document

- **Question:** How many parameters does the server-side script used for this policy receive, and how frequently is it executed?
- **Evidence (08_policy):** The update hook runs once per branch being pushed and takes three arguments:
- **First relevant rank:** >10
- **Top-1 retrieved (08_config):** _enforced_policy.

## fixed 100 - q191: wrong document

- **Question:** Where does text printed by a server-side enforcement script end up?
- **Evidence (08_policy):** Anything your script echoes to stdout will be transferred to the client.
- **First relevant rank:** >10
- **Top-1 retrieved (08_hooks):** Side Hooks In addition to the client-side hooks, you can use a couple of important server-side hooks as a system administrator to enforce nearly any kind of policy for your project. These scripts run before and after pushes to the server. …

## fixed 100 - q195: wrong document

- **Question:** How many unpacked objects or how many pack files does it take before the automatic cleanup actually does work?
- **Evidence (10_maintenance):** You must have around 7,000 loose objects or more than 50 packfiles for Git to fire up a real gc command.
- **First relevant rank:** >10
- **Top-1 retrieved (10_packfiles):** , occasionally Git packs up several of these objects into a single binary file called a "packfile" in order to save space and be more efficient. Git does this if you have too many loose objects around, if you run the git gc command manuall…

## fixed 100 - q198: wrong document

- **Question:** How is the on-disk path of a stored object split up between folder name and file name?
- **Evidence (10_objects):** The subdirectory is named with the first 2 characters of the SHA-1, and the filename is the remaining 38 characters.
- **First relevant rank:** >10
- **Top-1 retrieved (10_plumbing-porcelain):** The objects directory stores all the content for your database, the refs directory stores pointers into commit objects in that data (branches, tags, remotes and more), the HEAD file points to the branch you currently have checked out, and …

## fixed 100 - q201: right document, wrong passage

- **Question:** Besides the automatic repacking Git performs on its own, how can someone trigger a repack deliberately?
- **Evidence (10_packfiles):** Git will occasionally repack your database automatically, always trying to save more space, but you can also manually repack at any time by running git gc by hand.
- **First relevant rank:** >10
- **Top-1 retrieved (10_packfiles):** also manually repack at any time by running git gc by hand.

## fixed 100 - q203: wrong document

- **Question:** What similarity does Git look for between objects when deciding which ones to store as differences?
- **Evidence (10_packfiles):** When Git packs objects, it looks for files that are named and sized similarly, and stores just the deltas from one version of the file to the next.
- **First relevant rank:** >10
- **Top-1 retrieved (07_revision-selection):** two objects whose SHA-1s are identical in the first 12 characters. A SHORT NOTE ABOUT SHA-1 A lot of people become concerned at some point that they will, by random happenstance, have two distinct objects in their repository that hash to t…

## fixed 100 - q208: right document, wrong passage

- **Question:** What does HEAD normally hold, and how does that differ from an ordinary ref?
- **Evidence (10_refs):** Usually the HEAD file is a symbolic reference to the branch you're currently on. By symbolic reference, we mean that unlike a normal reference, it contains a pointer to another reference.
- **First relevant rank:** >10
- **Top-1 retrieved (10_refs):** -ref HEAD refs/heads/test $ cat .git/HEAD ref: refs/heads/test You can't set a symbolic reference outside of the refs style: $ git symbolic-ref HEAD test fatal: Refusing to point HEAD outside of refs/ Tags We just finished discussing Git's…

## fixed 100 - q209: right document, wrong passage

- **Question:** Which pieces of data live inside a tag object, and which other object type is it closest to?
- **Evidence (10_refs):** The tag object is very much like a commit object -- it contains a tagger, a date, a message, and a pointer.
- **First relevant rank:** >10
- **Top-1 retrieved (10_refs):** contains a tagger, a date, a message, and a pointer. The main difference is that a tag object generally points to a commit rather than a tree. It's like a branch reference, but it never moves -- it always points to the same commit but give…

## fixed 100 - q212: wrong document

- **Question:** Why does pushing with nothing before the colon wipe out a branch upstream?
- **Evidence (10_refspec):** Because the refspec is <src>:<dst>, by leaving off the <src> part, this basically says to make the topic branch on the remote nothing, which deletes it.
- **First relevant rank:** >10
- **Top-1 retrieved (07_reset):** . Without Paths Running git checkout [branch] is pretty similar to running git reset --hard [branch] in that it updates all three trees for you to look like [branch], but there are two important differences. First, unlike reset --hard, che…

## sentence 100 - q004: wrong document

- **Question:** Does skill with a graphical Git tool transfer to the terminal as readily as the reverse?
- **Evidence (01_command-line):** If you know how to run the command-line version, you can probably also figure out how to run the GUI version, while the opposite is not necessarily true.
- **First relevant rank:** >10
- **Top-1 retrieved (10_plumbing-porcelain):** You'll now look at each of these sections in detail to see how Git operates.

## sentence 100 - q005: wrong document

- **Question:** Which kind of Git interface can I count on every user already having?
- **Evidence (01_command-line):** all users will have the command-line tools installed and available.
- **First relevant rank:** >10
- **Top-1 retrieved (04_setting-up-server):** With this method, you can quickly get a read/write Git server up and running for a handful of developers. You should note that currently all these users can also log into the server and get a shell as the git user. If you want to restrict …

## sentence 100 - q011: wrong document

- **Question:** Where can I talk to knowledgeable Git users live when the documentation is not enough?
- **Evidence (01_help):** If the manpages and this book aren't enough and you need in-person help, you can try the #git, #github, or #gitlab channels on the Libera Chat IRC server, which can be found at ^ (https://libera.chat/).
- **First relevant rank:** >10
- **Top-1 retrieved (04_git-on-a-server):** Now you're ready to collaborate on the same project. It's important to note that this is literally all you need to do to run a useful Git server to which several people have access -- just add SSH-able accounts on a server, and stick a bar…

## sentence 100 - q012: wrong document

- **Question:** Which flag prints a brief list of a command's options instead of the whole manual?
- **Evidence (01_help):** In addition, if you don't need the full-blown manpage help, but just need a quick refresher on the available options for a Git command, you can ask for the more concise "help" output with the -h option, as in:
- **First relevant rank:** >10
- **Top-1 retrieved (08_hooks):** If you're writing a script/hook that others will need to read, prefer the long versions of command-line flags; six months from now you'll thank us.

## sentence 100 - q021: wrong document

- **Question:** Where does Git keep the record of what is queued up for the next commit?
- **Evidence (01_what-is-git):** The staging area is a file, generally contained in your Git directory, that stores information about what will go into your next commit.
- **First relevant rank:** >10
- **Top-1 retrieved (08_hooks):** In the last section of this chapter, we'll demonstrate using this hook to check that your commit message is conformant to a required pattern. After the entire commit process is completed, the post-commit hook runs. It doesn't take any para…

## sentence 100 - q022: wrong document

- **Question:** How do I make a shortcut launch a program that isn't part of Git?
- **Evidence (02_aliases):** maybe you want to run an external command, rather than a Git subcommand. In that case, you start the command with a ! character.
- **First relevant rank:** 8
- **Top-1 retrieved (01_first-time-setup):** If you are using another editor, or a 32-bit version, please find specific instructions for how to set up your favorite editor with Git in C-git-commands#ch_core_editor. You may find, if you don't setup your editor like this, you get into …

## sentence 100 - q025: wrong document

- **Question:** After turning an existing folder into a repository, how do I record its current files?
- **Evidence (02_getting-a-repository):** You can accomplish that with a few git add commands that specify the files you want to track, followed by a git commit:
- **First relevant rank:** 10
- **Top-1 retrieved (02_recording-changes):** Recording Changes to the Repository At this point, you should have a bona fide Git repository on your local machine, and a checkout or working copy of all of its files in front of you. Typically, you'll want to start making changes and com…

## sentence 100 - q026: wrong document

- **Question:** Can I choose a target folder name that differs from the project's own?
- **Evidence (02_getting-a-repository):** If you want to clone the repository into a directory named something other than libgit2, you can specify the new directory name as an additional argument:
- **First relevant rank:** >10
- **Top-1 retrieved (04_gitlab):** You'll be asked for the project's name, which namespace it should belong to, and what its visibility level should be. Most of what you specify here isn't permanent, and can be changed later through the settings interface. Click "Create Pro…

## sentence 100 - q028: right document, wrong passage

- **Question:** I edited a file again after staging it; what do I have to do before committing?
- **Evidence (02_recording-changes):** If you modify a file after you run git add, you have to run git add again to stage the latest version of the file:
- **First relevant rank:** >10
- **Top-1 retrieved (02_recording-changes):** Remember that the commit records the snapshot you set up in your staging area. Anything you didn't stage is still sitting there modified; you can do another commit to add it to your history. Every time you perform a commit, you're recordin…

## sentence 100 - q030: wrong document

- **Question:** Which files in my working directory does Git consider untracked?
- **Evidence (02_recording-changes):** Untracked files are everything else -- any files in your working directory that were not in your last snapshot and are not in your staging area.
- **First relevant rank:** 6
- **Top-1 retrieved (07_stashing-cleaning):** To remove all the untracked files in your working directory, you can run git clean -f -d, which removes any files and also any subdirectories that become empty as a result. The -f means 'force' or "really do this," and is required if the G…

## sentence 100 - q031: wrong document

- **Question:** Besides downloading new commits, what else does pulling do?
- **Evidence (02_remotes):** Running git pull generally fetches data from the server you originally cloned from and automatically tries to merge it into the code you're currently working on.
- **First relevant rank:** >10
- **Top-1 retrieved (06_2-contributing):** This helps people break down Pull Requests into subtasks and helps other people track the progress of the branch. You can see an example of this in _task_list_progress. Task list summary in the Pull Request list These are incredibly useful…

## sentence 100 - q041: wrong document

- **Question:** In what sequence are commits printed when no options are supplied?
- **Evidence (02_viewing-history):** By default, with no arguments, git log lists the commits made in that repository in reverse chronological order; that is, the most recent commits show up first.
- **First relevant rank:** 6
- **Top-1 retrieved (07_rewriting-history):** # These lines can be re-ordered; they are executed from top to bottom. # # If you remove a line here THAT COMMIT WILL BE LOST. # # However, if you remove everything, the rebase will be aborted. # # Note that empty commits are commented out…

## sentence 100 - q045: right document, wrong passage

- **Question:** Why was no new snapshot needed when the hotfix work was integrated back into master?
- **Evidence (03_basic-branching-and-merging):** Because the commit C4 pointed to by the branch hotfix you merged in was directly ahead of the commit C2 you're on, Git simply moves the pointer forward.
- **First relevant rank:** >10
- **Top-1 retrieved (03_basic-branching-and-merging):** After your super-important fix is deployed, you're ready to switch back to the work you were doing before you were interrupted. However, first you'll delete the hotfix branch, because you no longer need it -- the master branch points at th…

## sentence 100 - q047: wrong document

- **Question:** What does the asterisk shown beside one entry in the branch listing mean?
- **Evidence (03_branch-management):** Notice the * character that prefixes the master branch: it indicates the branch that you currently have checked out (i.e., the branch that HEAD points to).
- **First relevant rank:** >10
- **Top-1 retrieved (03_nutshell):** This creates a new pointer to the same commit you're currently on. Two branches pointing into the same series of commits How does Git know what branch you're currently on? It keeps a special pointer called HEAD. Note that this is a lot dif…

## sentence 100 - q050: wrong document

- **Question:** Whose history does the log command display if you give it no extra arguments?
- **Evidence (03_nutshell):** by default, git log will only show commit history below the branch you've checked out.
- **First relevant rank:** >10
- **Top-1 retrieved (07_replace):** $ echo 'Get history from blah blah blah' | git commit-tree 9c68fdc^{tree} 622e88e9cbfbacfb75b5279245b9fb38dfea10cf ===== The commit-tree command is one of a set of commands that are commonly referred to as 'plumbing' commands.

## sentence 100 - q051: right document, wrong passage

- **Question:** Why are branches so inexpensive to make and throw away in Git?
- **Evidence (03_nutshell):** Because a branch in Git is actually a simple file that contains the 40 character SHA-1 checksum of the commit it points to, branches are cheap to create and destroy.
- **First relevant rank:** >10
- **Top-1 retrieved (03_nutshell):** The only reason nearly every repository has one is that the git init command creates it by default and most people don't bother to change it. A branch and its commit history Creating a New Branch What happens when you create a new branch? …

## sentence 100 - q053: right document, wrong passage

- **Question:** What does the rebase command do with work recorded on one branch?
- **Evidence (03_rebasing):** With the rebase command, you can take all the changes that were committed on one branch and replay them on a different branch.
- **First relevant rank:** >10
- **Top-1 retrieved (03_rebasing):** You can also have your rebase replay on something other than the rebase target branch. Take a history like rbdiag_e, for example. You branched a topic branch (server) to add some server-side functionality to your project, and made a commit…

## sentence 100 - q054: wrong document

- **Question:** Which commits must never be rebased?
- **Evidence (03_rebasing):** Do not rebase commits that exist outside your repository and that people may have based work on.
- **First relevant rank:** >10
- **Top-1 retrieved (07_rewriting-history):** # These lines can be re-ordered; they are executed from top to bottom. # # If you remove a line here THAT COMMIT WILL BE LOST. # # However, if you remove everything, the rebase will be aborted. # # Note that empty commits are commented out…

## sentence 100 - q057: right document, wrong passage

- **Question:** What do local pointers such as origin/master actually stand for?
- **Evidence (03_remote-branches):** Remote-tracking branches are references to the state of remote branches.
- **First relevant rank:** >10
- **Top-1 retrieved (03_remote-branches):** This may be a bit confusing, so let's look at an example. Let's say you have a Git server on your network at git.ourcompany.com. If you clone from this, Git's clone command automatically names it origin for you, pulls down all its data, cr…

## sentence 100 - q067: right document, wrong passage

- **Question:** What gives a developer the ability to send commits up, once they can log in over SSH?
- **Evidence (04_git-on-a-server):** If a user SSHs into a server and has write access to the /srv/git/my_project.git directory, they will also automatically have push access.
- **First relevant rank:** >10
- **Top-1 retrieved (04_git-on-a-server):** This doesn't affect the commit data in any way -- the SSH user you connect as doesn't affect the commits you've recorded. Another way to do it is to have your SSH server authenticate from an LDAP server or some other centralized authentica…

## sentence 100 - q073: right document, wrong passage

- **Question:** Which lightweight web server is usually already present on Linux, letting you launch the viewer with one command?
- **Evidence (04_gitweb):** On Linux machines, lighttpd is often installed, so you may be able to get it to run by typing git instaweb in your project directory.
- **First relevant rank:** 8
- **Top-1 retrieved (04_gitweb):** If you want to run the web interface on a server all the time for your team or for an open source project you're hosting, you'll need to set up the CGI script to be served by your normal web server. Some Linux distributions have a gitweb p…

## sentence 100 - q075: wrong document

- **Question:** Which setting tells the build where your repositories live when generating the script?
- **Evidence (04_gitweb):** Notice that you have to tell the command where to find your Git repositories with the GITWEB_PROJECTROOT variable.
- **First relevant rank:** >10
- **Top-1 retrieved (08_config):** The first place Git looks for these values is in the system-wide [path]/etc/gitconfig file, which contains settings that are applied to every user on the system and all of their repositories. If you pass the option --system to git config, …

## sentence 100 - q079: wrong document

- **Question:** How many transport mechanisms can move data, and which are they?
- **Evidence (04_protocols):** Git can use four distinct protocols to transfer data: Local, HTTP, Secure Shell (SSH) and Git.
- **First relevant rank:** 7
- **Top-1 retrieved (10_transfer-protocols):** The smart protocol is a more common method of transferring data, but it requires a process on the remote end that is intelligent about Git – it can read local data, figure out what the client has and needs, and generate a custom packfile f…

## sentence 100 - q083: wrong document

- **Question:** What has to be done on the machine itself each time a new project should be hosted?
- **Evidence (04_setting-up-server):** Note that someone must shell onto the machine and create a bare repository every time you want to add a project.
- **First relevant rank:** 7
- **Top-1 retrieved (05_maintaining):** Maintaining a Project In addition to knowing how to contribute effectively to a project, you'll likely need to know how to maintain one. This can consist of accepting and applying patches generated via format-patch and emailed to you, or i…

## sentence 100 - q084: wrong document

- **Question:** Which bundled tool keeps a shared account confined to version-control operations?
- **Evidence (04_setting-up-server):** You can easily restrict the git user account to only Git-related activities with a limited shell tool called git-shell that comes with Git.
- **First relevant rank:** >10
- **Top-1 retrieved (01_about-version-control):** About Version Control What is "version control", and why should you care? Version control is a system that records changes to a file or set of files over time so that you can recall specific versions later. For the examples in this book, y…

## sentence 100 - q087: wrong document

- **Question:** Why does the group ownership of the repository directories need changing?
- **Evidence (04_smart-http):** You'll also need to set the Unix user group of the /srv/git directories to www-data so your web server can read- and write-access the repositories
- **First relevant rank:** >10
- **Top-1 retrieved (04_git-on-a-server):** $ git clone user@git.example.com:/srv/git/my_project.git If a user SSHs into a server and has write access to the /srv/git/my_project.git directory, they will also automatically have push access. Git will automatically add group write perm…

## sentence 100 - q091: wrong document

- **Question:** Why must a force flag be added when pushing a topic branch whose history you have just rewritten with a rebase?
- **Evidence (05_contributing):** Because you rebased the branch, you have to specify the -f to your push command in order to be able to replace the featureA branch on the server with a commit that isn't a descendant of it.
- **First relevant rank:** >10
- **Top-1 retrieved (03_rebasing):** You can also have your rebase replay on something other than the rebase target branch. Take a history like rbdiag_e, for example. You branched a topic branch (server) to add some server-side functionality to your project, and made a commit…

## sentence 100 - q101: wrong document

- **Question:** What piece of information does GitHub use to attribute a commit to a particular member?
- **Evidence (06_1-setting-up-account):** The way that GitHub maps your Git commits to your user is by email address.
- **First relevant rank:** >10
- **Top-1 retrieved (02_viewing-history):** So, if you send in a patch to a project and one of the core members applies the patch, both of you get credit -- you as the author, and the core member as the committer. We'll cover this distinction a bit more in ch05-distributed-git#ch05-…

## sentence 100 - q103: wrong document

- **Question:** Why is it worth giving each uploaded public key a label such as the machine it belongs to?
- **Evidence (06_1-setting-up-account):** You can name each of your keys (e.g. "My Laptop" or "Work Account") so that if you need to revoke a key later, you can easily tell which one you're looking for.
- **First relevant rank:** >10
- **Top-1 retrieved (10_refs):** Notice that the object entry points to the commit SHA-1 value that you tagged. Also notice that it doesn't need to point to a commit; you can tag any Git object. In the Git source code, for example, the maintainer has added their GPG publi…

## sentence 100 - q104: right document, wrong passage

- **Question:** After forking on GitHub, who owns the resulting copy and where does it sit?
- **Evidence (06_2-contributing):** When you "fork" a project, GitHub will make a copy of the project that is entirely yours; it lives in your namespace, and you can push to it.
- **First relevant rank:** 9
- **Top-1 retrieved (06_2-contributing):** To fork a project, visit the project page and click the "Fork" button at the top-right of the page. The "Fork" button After a few seconds, you'll be taken to your new project page, with your own writeable copy of the code. The GitHub Flow …

## sentence 100 - q116: wrong document

- **Question:** How does the generic hooks mechanism hand event data over to your own system?
- **Evidence (06_5-scripting):** You specify a URL and GitHub will post an HTTP payload to that URL on any event you want.
- **First relevant rank:** >10
- **Top-1 retrieved (08_hooks):** The hooks are all stored in the hooks subdirectory of the Git directory. In most projects, that's .git/hooks. When you initialize a new repository with git init, Git populates the hooks directory with a bunch of example scripts, many of wh…

## sentence 100 - q122: wrong document

- **Question:** Which numbered index slot holds the common ancestor of a conflicted file, and which one holds the incoming branch's copy?
- **Evidence (07_advanced-merging):** Stage 1 is the common ancestor, stage 2 is your version and stage 3 is from the MERGE_HEAD, the version you're merging in ("theirs").
- **First relevant rank:** >10
- **Top-1 retrieved (07_reset):** The Git cat-file and ls-tree commands are "plumbing" commands that are used for lower level things and not really used in day-to-day work, but they help us see what's going on here. The Index The index is your proposed next commit. We've a…

## sentence 100 - q124: right document, wrong passage

- **Question:** Does Git work out automatically which refs belong in a bundle, or must I enumerate them?
- **Evidence (07_bundling):** With the bundle command you need to list out every reference or specific range of commits that you want to be included.
- **First relevant rank:** >10
- **Top-1 retrieved (07_bundling):** When she gets the bundle, she can inspect it to see what it contains before she imports it into her repository. The first command is the bundle verify command that will make sure the file is actually a valid Git bundle and that you have al…

## sentence 100 - q125: wrong document

- **Question:** What artifact does Git produce from the data a push would normally send across the network?
- **Evidence (07_bundling):** The bundle command will package up everything that would normally be pushed over the wire with a git push command into a binary file
- **First relevant rank:** >10
- **Top-1 retrieved (10_transfer-protocols):** To upload data to a remote process, Git uses the send-pack and receive-pack processes. The send-pack process runs on the client and connects to a receive-pack process on the remote side. SSH For example, say you run git push origin master …

## sentence 100 - q128: right document, wrong passage

- **Question:** Am I restricted to the helpers shipped with Git, or can my own program serve credentials?
- **Evidence (07_credentials):** Given that git-credential-store and friends are separate programs from Git, it's not much of a leap to realize that any program can be a Git credential helper.
- **First relevant rank:** >10
- **Top-1 retrieved (07_credentials):** Git even allows you to configure several helpers. When looking for credentials for a particular host, Git will query them in order, and stop after the first answer is provided. When saving credentials, Git will send the username and passwo…

## sentence 100 - q132: right document, wrong passage

- **Question:** After tracking down the faulty revision, what command returns me to the checkout I had beforehand?
- **Evidence (07_debugging):** When you're finished, you should run git bisect reset to reset your HEAD to where you were before you started, or you'll end up in a weird state
- **First relevant rank:** >10
- **Top-1 retrieved (07_debugging):** [b047b02ea83310a70fd603dc8cd7a6cd13d15c04] Secure this thing Now you're on another commit, halfway between the one you just tested and your bad commit. You run your test again and find that this commit is broken, so you tell Git that with …

## sentence 100 - q134: wrong document

- **Question:** What search technique does Git use to pin down the revision that introduced a regression?
- **Evidence (07_debugging):** The bisect command does a binary search through your commit history to help you identify as quickly as possible which commit introduced an issue.
- **First relevant rank:** >10
- **Top-1 retrieved (07_searching):** Git ships with a command called grep that allows you to easily search through any committed tree, the working directory, or even the index for a string or regular expression. For the examples that follow, we'll search through the source co…

## sentence 100 - q137: right document, wrong passage

- **Question:** Inside the menu-driven prompt, which letter or number takes a file back out of the staging area?
- **Evidence (07_interactive-staging):** If you want to unstage the TODO file at this point, you use the r or 3 (for revert) option
- **First relevant rank:** >10
- **Top-1 retrieved (07_interactive-staging):** After this comes a "Commands" section, which allows you to do a number of things like staging and unstaging files, staging parts of files, adding untracked files, and displaying diffs of what has been staged. Staging and Unstaging Files If…

## sentence 100 - q138: right document, wrong passage

- **Question:** Which menu choice displays the changes already added to the staging area?
- **Evidence (07_interactive-staging):** To see the diff of what you've staged, you can use the d or 6 (for diff) command.
- **First relevant rank:** >10
- **Top-1 retrieved (07_interactive-staging):** You can see that this command shows you a much different view of your staging area than you're probably used to -- basically, the same information you get with git status but a bit more succinct and informative. It lists the changes you've…

## sentence 100 - q139: wrong document

- **Question:** Which two command-line switches make the add command open its menu-driven prompt?
- **Evidence (07_interactive-staging):** If you run git add with the -i or --interactive option, Git enters an interactive shell mode, displaying something like this
- **First relevant rank:** 8
- **Top-1 retrieved (07_submodules):** This is obviously a simplified example, but hopefully it gives you an idea of how this may be useful. Useful Aliases You may want to set up some aliases for some of these commands as they can be quite long and you can't set configuration o…

## sentence 100 - q142: right document, wrong passage

- **Question:** When joining a short recent history to a long archived one, which two commits do you pair up?
- **Evidence (07_replace):** You can graft one history onto the other by "replacing" the earliest commit in the new line with the latest commit on the older one.
- **First relevant rank:** 7
- **Top-1 retrieved (07_replace):** 945704c Second commit c1822cf First commit We want to break this up into two lines of history. One line goes from commit one to commit four - that will be the historical one. The second line will just be commits four and five - that will b…

## sentence 100 - q144: wrong document

- **Question:** Apart from the config flag, which directory can I create inside one repository to switch the feature on there?
- **Evidence (07_rerere):** You can also turn it on by creating the .git/rr-cache directory in a specific repository, but the config setting is clearer and enables that feature globally for you.
- **First relevant rank:** >10
- **Top-1 retrieved (04_git-on-a-server):** This is roughly equivalent to something like: $ cp -Rf my_project/.git my_project.git There are a couple of minor differences in the configuration file but, for your purpose, this is close to the same thing. It takes the Git repository by …

## sentence 100 - q148: right document, wrong passage

- **Question:** Between resetting and checking out a branch, which one relocates the branch pointer and which relocates HEAD?
- **Evidence (07_reset):** Whereas reset will move the branch that HEAD points to, checkout will move HEAD itself to point to another branch.
- **First relevant rank:** 9
- **Top-1 retrieved (07_reset):** If we instead run git checkout master, develop does not move, HEAD itself does. HEAD will now point to master. So, in both cases we're moving HEAD to point to commit A, but how we do so is very different. reset will move the branch HEAD po…

## sentence 100 - q152: right document, wrong passage

- **Question:** How far back does Git's background record of where HEAD and branch tips have pointed normally reach?
- **Evidence (07_revision-selection):** One of the things Git does in the background while you're working away is keep a "reflog" -- a log of where your HEAD and branch references have been for the last few months.
- **First relevant rank:** >10
- **Top-1 retrieved (07_revision-selection):** If you run a git push and your current branch is tracking origin/master, the commits listed by git log origin/master..HEAD are the commits that will be transferred to the server. You can also leave off one side of the syntax to have Git as…

## sentence 100 - q154: right document, wrong passage

- **Question:** What notation picks out the second parent of a merge commit such as d921970?
- **Evidence (07_revision-selection):** You can also specify a number after the ^ to identify which parent you want; for example, d921970^2 means "the second parent of d921970."
- **First relevant rank:** >10
- **Top-1 retrieved (07_revision-selection):** This syntax is useful only for merge commits, which have more than one parent -- the first parent of a merge commit is from the branch you were on when you merged (frequently master), while the second parent of a merge commit is from the b…

## sentence 100 - q158: right document, wrong passage

- **Question:** Which instruction word in the rebase script melds a commit into the one before it and asks you to join their log messages?
- **Evidence (07_rewriting-history):** If, instead of "pick" or "edit", you specify "squash", Git applies both that change and the change directly before it and makes you merge the commit messages together.
- **First relevant rank:** >10
- **Top-1 retrieved (07_rewriting-history):** Use -c <commit> to reword the commit message. # # These lines can be re-ordered; they are executed from top to bottom. # # If you remove a line here THAT COMMIT WILL BE LOST. # # However, if you remove everything, the rebase will be aborte…

## sentence 100 - q160: wrong document

- **Question:** How can you ask the log command to replay the whole evolution of a single function as patches?
- **Evidence (07_searching):** Simply run git log with the -L option, and it will show you the history of a function or line of code in your codebase.
- **First relevant rank:** >10
- **Top-1 retrieved (05_contributing):** 0001-add-limit-to-log-function.patch 0002-increase-log-output-to-30-from-25.patch The format-patch command prints out the names of the patch files it creates. The -M switch tells Git to look for renames. The files end up looking like this:…

## sentence 100 - q162: wrong document

- **Question:** Which pickaxe-style log flag takes a regular expression rather than a fixed string?
- **Evidence (07_searching):** If you need to be more specific, you can provide a regular expression to search for with the -G option.
- **First relevant rank:** >10
- **Top-1 retrieved (02_viewing-history):** Option values include oneline, short, full, fuller, and format (where you specify your own format). | --oneline | Shorthand for --pretty=oneline --abbrev-commit used together. |================================ Limiting Log Output

## sentence 100 - q164: wrong document

- **Question:** From which release can merging and pulling be made to reject unsigned incoming commits, and with what argument?
- **Evidence (07_signing):** In Git 1.8.3 and later, git merge and git pull can be told to inspect and reject when merging a commit that does not carry a trusted GPG signature with the --verify-signatures command.
- **First relevant rank:** 6
- **Top-1 retrieved (06_2-contributing):** Adding commits to an existing Pull Request doesn't trigger a notification, so once Tony has pushed his corrections he decides to leave a comment to inform the project owner that he made the requested change. Pull Request final An interesti…

## sentence 100 - q166: right document, wrong passage

- **Question:** Which configuration entry records which GPG key Git should reach for when it signs things?
- **Evidence (07_signing):** Once you have a private key to sign with, you can configure Git to use it for signing things by setting the user.signingkey config setting.
- **First relevant rank:** >10
- **Top-1 retrieved (07_signing):** gpg: Good signature from "Scott Chacon (Git signing key) <schacon@gmail.com>" Author: Scott Chacon <schacon@gmail.com> Date: Wed Jun 4 19:49:17 2014 -0700 Signed commit Additionally, you can configure git log to check any signatures it fin…

## sentence 100 - q168: wrong document

- **Question:** Since -u still skips files matched by ignore rules, what flag sweeps those in as well?
- **Evidence (07_stashing-cleaning):** including untracked files in the stash will still not include explicitly ignored files; to additionally include ignored files, use --all (or just -a).
- **First relevant rank:** >10
- **Top-1 retrieved (01_help):** --ignore-errors just skip files which cannot be added because of errors --ignore-missing check if - even missing - files are ignored in dry run --sparse allow updating entries outside of the sparse-checkout cone --chmod (+|-)x override the…

## sentence 100 - q170: wrong document

- **Question:** Which popular stash flag puts staged content into the saved entry yet still leaves that content ready for commit?
- **Evidence (07_stashing-cleaning):** The first option that is quite popular is the --keep-index option to the git stash command. This tells Git to not only include all staged content in the stash being created, but simultaneously leave it in the index.
- **First relevant rank:** 10
- **Top-1 retrieved (01_what-is-git):** You do a commit, which takes the files as they are in the staging area and stores that snapshot permanently to your Git directory. If a particular version of a file is in the Git directory, it's considered committed. If it has been modifie…

## sentence 100 - q174: right document, wrong passage

- **Question:** Which tracked configuration file records the pairing of a subproject's URL with the local folder it sits in?
- **Evidence (07_submodules):** First you should notice the new .gitmodules file. This is a configuration file that stores the mapping between the project's URL and the local subdirectory you've pulled it into:
- **First relevant rank:** >10
- **Top-1 retrieved (07_submodules):** path = DbConnector url = https://github.com/chaconinc/DbConnector If you have multiple submodules, you'll have multiple entries in this file. It's important to note that this file is version-controlled with your other files, like your .git…

## sentence 100 - q175: right document, wrong passage

- **Question:** Why can work you commit inside a subproject vanish when the superproject later refreshes it?
- **Evidence (07_submodules):** With no working branch tracking changes, that means even if you commit changes to the submodule, those changes will quite possibly be lost the next time you run git submodule update.
- **First relevant rank:** >10
- **Top-1 retrieved (07_submodules):** There is a special situation that can happen when pulling superproject updates: it could be that the upstream repository has changed the URL of the submodule in the .gitmodules file in one of the commits you pull. This can happen for examp…

## sentence 100 - q178: wrong document

- **Question:** Which plumbing command loads another branch's top-level tree into your index and working files?
- **Evidence (07_subtree-merges):** You'll learn more about read-tree and its friends in ch10-git-internals#ch10-git-internals, but for now know that it reads the root tree of one branch into your current staging area and working directory.
- **First relevant rank:** >10
- **Top-1 retrieved (07_reset):** The Git cat-file and ls-tree commands are "plumbing" commands that are used for lower level things and not really used in day-to-day work, but they help us see what's going on here. The Index The index is your proposed next commit. We've a…

## sentence 100 - q179: wrong document

- **Question:** Which two settings bring the vendored project's updates across with a ready-made commit message?
- **Evidence (07_subtree-merges):** To pull in the changes and prepopulate the commit message, use the --squash option, as well as the recursive merge strategy's -Xsubtree option.
- **First relevant rank:** >10
- **Top-1 retrieved (08_hooks):** You can do things like check for code style (run lint or something equivalent), check for trailing whitespace (the default hook does exactly this), or check for appropriate documentation on new methods. The prepare-commit-msg hook is run b…

## sentence 100 - q182: wrong document

- **Question:** Why might a content filter that works for you break for a colleague who clones the same project?
- **Evidence (08_attributes):** You have to be careful, though, because the .gitattributes file is committed and passed around with the project, but the driver (in this case, dater) isn't, so it won't work everywhere.
- **First relevant rank:** >10
- **Top-1 retrieved (05_maintaining):** This way, when people clone your project's repository, they can either check out master to build the latest stable version and keep up to date on that easily, or they can check out develop, which is the more cutting-edge content. You can a…

## sentence 100 - q189: wrong document

- **Question:** How many parameters does the server-side script used for this policy receive, and how frequently is it executed?
- **Evidence (08_policy):** The update hook runs once per branch being pushed and takes three arguments:
- **First relevant rank:** >10
- **Top-1 retrieved (08_hooks):** It takes the same stdin data as the pre-receive hook. Examples include emailing a list, notifying a continuous integration server, or updating a ticket-tracking system – you can even parse the commit messages to see if any tickets need to …

## sentence 100 - q191: wrong document

- **Question:** Where does text printed by a server-side enforcement script end up?
- **Evidence (08_policy):** Anything your script echoes to stdout will be transferred to the client.
- **First relevant rank:** >10
- **Top-1 retrieved (10_transfer-protocols):** The first line also has a list of the server's capabilities (here, report-status, delete-refs, and some others, including the client identifier). The data is transmitted in chunks. Each chunk starts with a 4-character hex value specifying …

## sentence 100 - q195: wrong document

- **Question:** How many unpacked objects or how many pack files does it take before the automatic cleanup actually does work?
- **Evidence (10_maintenance):** You must have around 7,000 loose objects or more than 50 packfiles for Git to fire up a real gc command.
- **First relevant rank:** >10
- **Top-1 retrieved (10_packfiles):** To see what happens, you can manually ask Git to pack up the objects by calling the git gc command: $ git gc Counting objects: 18, done. Delta compression using up to 8 threads. Compressing objects: 100% (14/14), done. Writing objects: 100…

## sentence 100 - q203: wrong document

- **Question:** What similarity does Git look for between objects when deciding which ones to store as differences?
- **Evidence (10_packfiles):** When Git packs objects, it looks for files that are named and sized similarly, and stores just the deltas from one version of the file to the next.
- **First relevant rank:** >10
- **Top-1 retrieved (07_revision-selection):** A lot of people become concerned at some point that they will, by random happenstance, have two distinct objects in their repository that hash to the same SHA-1 value. What then? If you do happen to commit an object that hashes to the same…

## sentence 100 - q210: wrong document

- **Question:** What does the leading plus sign in front of a mapping authorise Git to do?
- **Evidence (10_refspec):** The + tells Git to update the reference even if it isn't a fast-forward.
- **First relevant rank:** >10
- **Top-1 retrieved (07_credentials):** Git's root command for the credential-helper system is git credential, which takes a command as an argument, and then more input through stdin. This might be easier to understand with an example. Let's say that a credential helper has been…

## sentence 100 - q212: wrong document

- **Question:** Why does pushing with nothing before the colon wipe out a branch upstream?
- **Evidence (10_refspec):** Because the refspec is <src>:<dst>, by leaving off the <src> part, this basically says to make the topic branch on the remote nothing, which deletes it.
- **First relevant rank:** >10
- **Top-1 retrieved (05_contributing):** 1 files changed, 4 insertions(+), 0 deletions(-) At this point, Jessica wants to push all of this merged "featureB" work back to the server, but she doesn't want to simply push her own featureB branch. Rather, since Josie has already start…

## recursive 100 - q004: wrong document

- **Question:** Does skill with a graphical Git tool transfer to the terminal as readily as the reverse?
- **Evidence (01_command-line):** If you know how to run the command-line version, you can probably also figure out how to run the GUI version, while the opposite is not necessarily true.
- **First relevant rank:** >10
- **Top-1 retrieved (01_what-is-git):** What is Git?

## recursive 100 - q005: wrong document

- **Question:** Which kind of Git interface can I count on every user already having?
- **Evidence (01_command-line):** all users will have the command-line tools installed and available.
- **First relevant rank:** >10
- **Top-1 retrieved (04_git-on-a-server):** It's important to note that this is literally all you need to do to run a useful Git server to which several people have access -- just add SSH-able accounts on a server, and stick a bare repository somewhere that all those users have read…

## recursive 100 - q008: wrong document

- **Question:** What is a brand new repository's first branch named if I never configure it?
- **Evidence (01_first-time-setup):** By default Git will create a branch called master when you create a new repository with git init.
- **First relevant rank:** 8
- **Top-1 retrieved (10_refs):** It's like a branch reference, but it never moves -- it always points to the same commit but gives it a friendlier name.

## recursive 100 - q011: right document, wrong passage

- **Question:** Where can I talk to knowledgeable Git users live when the documentation is not enough?
- **Evidence (01_help):** If the manpages and this book aren't enough and you need in-person help, you can try the #git, #github, or #gitlab channels on the Libera Chat IRC server, which can be found at ^ (https://libera.chat/).
- **First relevant rank:** >10
- **Top-1 retrieved (01_help):** These channels are regularly filled with hundreds of people who are all very knowledgeable about Git and are often willing to help.

## recursive 100 - q012: wrong document

- **Question:** Which flag prints a brief list of a command's options instead of the whole manual?
- **Evidence (01_help):** In addition, if you don't need the full-blown manpage help, but just need a quick refresher on the available options for a Git command, you can ask for the more concise "help" output with the -h option, as in:
- **First relevant rank:** >10
- **Top-1 retrieved (08_hooks):** If you're writing a script/hook that others will need to read, prefer the long versions of command-line flags; six months from now you'll thank us.

## recursive 100 - q021: wrong document

- **Question:** Where does Git keep the record of what is queued up for the next commit?
- **Evidence (01_what-is-git):** The staging area is a file, generally contained in your Git directory, that stores information about what will go into your next commit.
- **First relevant rank:** >10
- **Top-1 retrieved (08_hooks):** After the entire commit process is completed, the post-commit hook runs. It doesn't take any parameters, but you can easily get the last commit by running git log -1 HEAD. Generally, this script is used for notification or something simila…

## recursive 100 - q025: wrong document

- **Question:** After turning an existing folder into a repository, how do I record its current files?
- **Evidence (02_getting-a-repository):** You can accomplish that with a few git add commands that specify the files you want to track, followed by a git commit:
- **First relevant rank:** >10
- **Top-1 retrieved (02_recording-changes):** Recording Changes to the Repository At this point, you should have a bona fide Git repository on your local machine, and a checkout or working copy of all of its files in front of you. Typically, you'll want to start making changes and com…

## recursive 100 - q026: wrong document

- **Question:** Can I choose a target folder name that differs from the project's own?
- **Evidence (02_getting-a-repository):** If you want to clone the repository into a directory named something other than libgit2, you can specify the new directory name as an additional argument:
- **First relevant rank:** >10
- **Top-1 retrieved (07_rewriting-history):** Suppose you've done an import from another source control system and have subdirectories that make no sense (trunk, tags, and so on). If you want to make the trunk subdirectory be the new project root for every commit, filter-branch can he…

## recursive 100 - q028: right document, wrong passage

- **Question:** I edited a file again after staging it; what do I have to do before committing?
- **Evidence (02_recording-changes):** If you modify a file after you run git add, you have to run git add again to stage the latest version of the file:
- **First relevant rank:** >10
- **Top-1 retrieved (02_recording-changes):** Remember that the commit records the snapshot you set up in your staging area. Anything you didn't stage is still sitting there modified; you can do another commit to add it to your history. Every time you perform a commit, you're recordin…

## recursive 100 - q031: wrong document

- **Question:** Besides downloading new commits, what else does pulling do?
- **Evidence (02_remotes):** Running git pull generally fetches data from the server you originally cloned from and automatically tries to merge it into the code you're currently working on.
- **First relevant rank:** >10
- **Top-1 retrieved (06_2-contributing):** It's important to understand that many projects don't really think of Pull Requests as queues of perfect patches that should apply cleanly in order, as most mailing list-based projects think of patch series contributions. Most GitHub proje…

## recursive 100 - q038: right document, wrong passage

- **Question:** When is rewriting the most recent commit considered safe?
- **Evidence (02_undoing):** Only amend commits that are still local and have not been pushed somewhere.
- **First relevant rank:** 7
- **Top-1 retrieved (02_undoing):** It's important to understand that when you're amending your last commit, you're not so much fixing it as replacing it entirely with a new, improved commit that pushes the old commit out of the way and puts the new commit in its place. Effe…

## recursive 100 - q041: wrong document

- **Question:** In what sequence are commits printed when no options are supplied?
- **Evidence (02_viewing-history):** By default, with no arguments, git log lists the commits made in that repository in reverse chronological order; that is, the most recent commits show up first.
- **First relevant rank:** 7
- **Top-1 retrieved (07_revision-selection):** For the sake of brevity and clarity in these examples, the letters of the commit objects from the diagram are used in place of the actual log output in the order that they would display:

## recursive 100 - q044: right document, wrong passage

- **Question:** Which snapshots are combined when the current commit is not a direct ancestor of the branch being brought in?
- **Evidence (03_basic-branching-and-merging):** Git does a simple three-way merge, using the two snapshots pointed to by the branch tips and the common ancestor of the two.
- **First relevant rank:** 9
- **Top-1 retrieved (03_basic-branching-and-merging):** Three snapshots used in a typical merge Instead of just moving the branch pointer forward, Git creates a new snapshot that results from this three-way merge and automatically creates a new commit that points to it. This is referred to as a…

## recursive 100 - q045: right document, wrong passage

- **Question:** Why was no new snapshot needed when the hotfix work was integrated back into master?
- **Evidence (03_basic-branching-and-merging):** Because the commit C4 pointed to by the branch hotfix you merged in was directly ahead of the commit C2 you're on, Git simply moves the pointer forward.
- **First relevant rank:** >10
- **Top-1 retrieved (03_basic-branching-and-merging):** This looks a bit different than the hotfix merge you did earlier. In this case, your development history has diverged from some older point. Because the commit on the branch you're on isn't a direct ancestor of the branch you're merging in…

## recursive 100 - q047: wrong document

- **Question:** What does the asterisk shown beside one entry in the branch listing mean?
- **Evidence (03_branch-management):** Notice the * character that prefixes the master branch: it indicates the branch that you currently have checked out (i.e., the branch that HEAD points to).
- **First relevant rank:** 7
- **Top-1 retrieved (10_refs):** It's like a branch reference, but it never moves -- it always points to the same commit but gives it a friendlier name.

## recursive 100 - q050: wrong document

- **Question:** Whose history does the log command display if you give it no extra arguments?
- **Evidence (03_nutshell):** by default, git log will only show commit history below the branch you've checked out.
- **First relevant rank:** >10
- **Top-1 retrieved (07_replace):** $ echo 'Get history from blah blah blah' | git commit-tree 9c68fdc^{tree} 622e88e9cbfbacfb75b5279245b9fb38dfea10cf

## recursive 100 - q053: right document, wrong passage

- **Question:** What does the rebase command do with work recorded on one branch?
- **Evidence (03_rebasing):** With the rebase command, you can take all the changes that were committed on one branch and replay them on a different branch.
- **First relevant rank:** >10
- **Top-1 retrieved (03_rebasing):** You can also have your rebase replay on something other than the rebase target branch. Take a history like rbdiag_e, for example. You branched a topic branch (server) to add some server-side functionality to your project, and made a commit…

## recursive 100 - q054: wrong document

- **Question:** Which commits must never be rebased?
- **Evidence (03_rebasing):** Do not rebase commits that exist outside your repository and that people may have based work on.
- **First relevant rank:** >10
- **Top-1 retrieved (07_rewriting-history):** # If you remove a line here THAT COMMIT WILL BE LOST. # # However, if you remove everything, the rebase will be aborted. # # Note that empty commits are commented out

## recursive 100 - q057: right document, wrong passage

- **Question:** What do local pointers such as origin/master actually stand for?
- **Evidence (03_remote-branches):** Remote-tracking branches are references to the state of remote branches.
- **First relevant rank:** >10
- **Top-1 retrieved (03_remote-branches):** This may be a bit confusing, so let's look at an example. Let's say you have a Git server on your network at git.ourcompany.com. If you clone from this, Git's clone command automatically names it origin for you, pulls down all its data, cr…

## recursive 100 - q061: right document, wrong passage

- **Question:** In which folder does a user normally find their existing SSH keys?
- **Evidence (04_generating-ssh-key):** By default, a user's SSH keys are stored in that user's ~/.ssh directory.
- **First relevant rank:** >10
- **Top-1 retrieved (04_generating-ssh-key):** $ cd ~/.ssh $ ls authorized_keys2 id_dsa known_hosts config id_dsa.pub

## recursive 100 - q066: wrong document

- **Question:** Which port has to be opened if a firewall sits in front of the machine?
- **Evidence (04_git-daemon):** If you're running a firewall, you'll also need to punch a hole in it at port 9418 on the box you're setting this up on.
- **First relevant rank:** >10
- **Top-1 retrieved (04_protocols):** Behind big corporate firewalls, this obscure port is commonly blocked.

## recursive 100 - q073: wrong document

- **Question:** Which lightweight web server is usually already present on Linux, letting you launch the viewer with one command?
- **Evidence (04_gitweb):** On Linux machines, lighttpd is often installed, so you may be able to get it to run by typing git instaweb in your project directory.
- **First relevant rank:** 10
- **Top-1 retrieved (04_smart-http):** You can do this with nearly any CGI-capable web server, so go with the one that you know best.

## recursive 100 - q075: wrong document

- **Question:** Which setting tells the build where your repositories live when generating the script?
- **Evidence (04_gitweb):** Notice that you have to tell the command where to find your Git repositories with the GITWEB_PROJECTROOT variable.
- **First relevant rank:** >10
- **Top-1 retrieved (01_first-time-setup):** 2. ~/.gitconfig or ~/.config/git/config file: Values specific personally to you, the user. You can make Git read and write to this file specifically by passing the --global option, and this affects all of the repositories you work with on …

## recursive 100 - q079: wrong document

- **Question:** How many transport mechanisms can move data, and which are they?
- **Evidence (04_protocols):** Git can use four distinct protocols to transfer data: Local, HTTP, Secure Shell (SSH) and Git.
- **First relevant rank:** 7
- **Top-1 retrieved (10_transfer-protocols):** There are two sets of processes for transferring data: a pair for uploading data and a pair for downloading data.

## recursive 100 - q083: wrong document

- **Question:** What has to be done on the machine itself each time a new project should be hosted?
- **Evidence (04_setting-up-server):** Note that someone must shell onto the machine and create a bare repository every time you want to add a project.
- **First relevant rank:** 8
- **Top-1 retrieved (05_maintaining):** Maintaining a Project

## recursive 100 - q084: wrong document

- **Question:** Which bundled tool keeps a shared account confined to version-control operations?
- **Evidence (04_setting-up-server):** You can easily restrict the git user account to only Git-related activities with a limited shell tool called git-shell that comes with Git.
- **First relevant rank:** >10
- **Top-1 retrieved (01_about-version-control):** Distributed Version Control Systems

## recursive 100 - q085: right document, wrong passage

- **Question:** What essentially has to be turned on to offer the smarter HTTP service?
- **Evidence (04_smart-http):** Setting up Smart HTTP is basically just enabling a CGI script that is provided with Git called git-http-backend on the server.
- **First relevant rank:** 8
- **Top-1 retrieved (04_smart-http):** Smart HTTP

## recursive 100 - q087: wrong document

- **Question:** Why does the group ownership of the repository directories need changing?
- **Evidence (04_smart-http):** You'll also need to set the Unix user group of the /srv/git directories to www-data so your web server can read- and write-access the repositories
- **First relevant rank:** >10
- **Top-1 retrieved (04_git-on-a-server):** If a user SSHs into a server and has write access to the /srv/git/my_project.git directory, they will also automatically have push access. Git will automatically add group write permissions to a repository properly if you run the git init …

## recursive 100 - q091: wrong document

- **Question:** Why must a force flag be added when pushing a topic branch whose history you have just rewritten with a rebase?
- **Evidence (05_contributing):** Because you rebased the branch, you have to specify the -f to your push command in order to be able to replace the featureA branch on the server with a commit that isn't a descendant of it.
- **First relevant rank:** >10
- **Top-1 retrieved (03_rebasing):** You can also have your rebase replay on something other than the rebase target branch. Take a history like rbdiag_e, for example. You branched a topic branch (server) to add some server-side functionality to your project, and made a commit…

## recursive 100 - q093: right document, wrong passage

- **Question:** In the integration-manager model, must a contributor sit idle until their submission is taken in?
- **Evidence (05_distributed-workflows):** Contributors don't have to wait for the project to incorporate their changes -- each party can work at their own pace.
- **First relevant rank:** 6
- **Top-1 retrieved (05_distributed-workflows):** 1. The project maintainer pushes to their public repository. 2. A contributor clones that repository and makes changes. 3. The contributor pushes to their own public copy. 4. The contributor sends the maintainer an email asking them to pul…

## recursive 100 - q101: wrong document

- **Question:** What piece of information does GitHub use to attribute a commit to a particular member?
- **Evidence (06_1-setting-up-account):** The way that GitHub maps your Git commits to your user is by email address.
- **First relevant rank:** >10
- **Top-1 retrieved (02_viewing-history):** You may be wondering what the difference is between author and committer. The author is the person who originally wrote the work, whereas the committer is the person who last applied the work. So, if you send in a patch to a project and on…

## recursive 100 - q103: wrong document

- **Question:** Why is it worth giving each uploaded public key a label such as the machine it belongs to?
- **Evidence (06_1-setting-up-account):** You can name each of your keys (e.g. "My Laptop" or "Work Account") so that if you need to revoke a key later, you can easily tell which one you're looking for.
- **First relevant rank:** >10
- **Top-1 retrieved (04_git-daemon):** If you're running this on a server outside your firewall, it should be used only for projects that are publicly visible to the world. If the server you're running it on is inside your firewall, you might use it for projects that a large nu…

## recursive 100 - q104: right document, wrong passage

- **Question:** After forking on GitHub, who owns the resulting copy and where does it sit?
- **Evidence (06_2-contributing):** When you "fork" a project, GitHub will make a copy of the project that is entirely yours; it lives in your namespace, and you can push to it.
- **First relevant rank:** >10
- **Top-1 retrieved (06_2-contributing):** To fork a project, visit the project page and click the "Fork" button at the top-right of the page. The "Fork" button After a few seconds, you'll be taken to your new project page, with your own writeable copy of the code. The GitHub Flow

## recursive 100 - q119: wrong document

- **Question:** Whose status does a Pull Request report, and what does it do if that one failed?
- **Evidence (06_5-scripting):** You can also see that the Pull Request takes the status of the last commit on the branch and warns you if it is a failure.
- **First relevant rank:** >10
- **Top-1 retrieved (06_3-maintaining):** There are a few things to notice about this email. It will give you a small diffstat -- a list of files that have changed in the Pull Request and by how much. It gives you a link to the Pull Request on GitHub. It also gives you a few URLs …

## recursive 100 - q122: wrong document

- **Question:** Which numbered index slot holds the common ancestor of a conflicted file, and which one holds the incoming branch's copy?
- **Evidence (07_advanced-merging):** Stage 1 is the common ancestor, stage 2 is your version and stage 3 is from the MERGE_HEAD, the version you're merging in ("theirs").
- **First relevant rank:** 7
- **Top-1 retrieved (07_reset):** The Git cat-file and ls-tree commands are "plumbing" commands that are used for lower level things and not really used in day-to-day work, but they help us see what's going on here. The Index The index is your proposed next commit. We've a…

## recursive 100 - q124: wrong document

- **Question:** Does Git work out automatically which refs belong in a bundle, or must I enumerate them?
- **Evidence (07_bundling):** With the bundle command you need to list out every reference or specific range of commits that you want to be included.
- **First relevant rank:** >10
- **Top-1 retrieved (10_maintenance):** If you run git gc, you'll no longer have these files in the refs directory. Git will move them for the sake of efficiency into a file named .git/packed-refs that looks like this:

## recursive 100 - q125: wrong document

- **Question:** What artifact does Git produce from the data a push would normally send across the network?
- **Evidence (07_bundling):** The bundle command will package up everything that would normally be pushed over the wire with a git push command into a binary file
- **First relevant rank:** >10
- **Top-1 retrieved (04_protocols):** The Git Protocol

## recursive 100 - q130: right document, wrong passage

- **Question:** Which credential helper ships with Git on Apple machines, and where does it keep the secrets?
- **Evidence (07_credentials):** If you're using macOS, Git comes with an "osxkeychain" mode, which caches credentials in the secure keychain that's attached to your system account.
- **First relevant rank:** >10
- **Top-1 retrieved (07_credentials):** The credential system is actually invoking a program that's separate from Git itself; which one and how depends on the credential.helper configuration value. There are several forms it can take:

## recursive 100 - q132: wrong document

- **Question:** After tracking down the faulty revision, what command returns me to the checkout I had beforehand?
- **Evidence (07_debugging):** When you're finished, you should run git bisect reset to reset your HEAD to where you were before you started, or you'll end up in a weird state
- **First relevant rank:** >10
- **Top-1 retrieved (10_maintenance):** It looks like the bottom commit is the one you lost, so you can recover it by creating a new branch at that commit. For example, you can start a branch named recover-branch at that commit (ab1afef):

## recursive 100 - q134: wrong document

- **Question:** What search technique does Git use to pin down the revision that introduced a regression?
- **Evidence (07_debugging):** The bisect command does a binary search through your commit history to help you identify as quickly as possible which commit introduced an issue.
- **First relevant rank:** >10
- **Top-1 retrieved (07_searching):** Git ships with a command called grep that allows you to easily search through any committed tree, the working directory, or even the index for a string or regular expression. For the examples that follow, we'll search through the source co…

## recursive 100 - q137: right document, wrong passage

- **Question:** Inside the menu-driven prompt, which letter or number takes a file back out of the staging area?
- **Evidence (07_interactive-staging):** If you want to unstage the TODO file at this point, you use the r or 3 (for revert) option
- **First relevant rank:** >10
- **Top-1 retrieved (07_interactive-staging):** After this comes a "Commands" section, which allows you to do a number of things like staging and unstaging files, staging parts of files, adding untracked files, and displaying diffs of what has been staged. Staging and Unstaging Files If…

## recursive 100 - q138: right document, wrong passage

- **Question:** Which menu choice displays the changes already added to the staging area?
- **Evidence (07_interactive-staging):** To see the diff of what you've staged, you can use the d or 6 (for diff) command.
- **First relevant rank:** >10
- **Top-1 retrieved (07_interactive-staging):** You can see that this command shows you a much different view of your staging area than you're probably used to -- basically, the same information you get with git status but a bit more succinct and informative. It lists the changes you've…

## recursive 100 - q139: wrong document

- **Question:** Which two command-line switches make the add command open its menu-driven prompt?
- **Evidence (07_interactive-staging):** If you run git add with the -i or --interactive option, Git enters an interactive shell mode, displaying something like this
- **First relevant rank:** >10
- **Top-1 retrieved (08_config):** The three that are turned on by default are blank-at-eol, which looks for spaces at the end of a line; blank-at-eof, which notices blank lines at the end of a file; and space-before-tab, which looks for spaces before tabs at the beginning …

## recursive 100 - q144: wrong document

- **Question:** Apart from the config flag, which directory can I create inside one repository to switch the feature on there?
- **Evidence (07_rerere):** You can also turn it on by creating the .git/rr-cache directory in a specific repository, but the config setting is clearer and enables that feature globally for you.
- **First relevant rank:** >10
- **Top-1 retrieved (04_git-on-a-server):** There are a couple of minor differences in the configuration file but, for your purpose, this is close to the same thing. It takes the Git repository by itself, without a working directory, and creates a directory specifically for it alone…

## recursive 100 - q152: right document, wrong passage

- **Question:** How far back does Git's background record of where HEAD and branch tips have pointed normally reach?
- **Evidence (07_revision-selection):** One of the things Git does in the background while you're working away is keep a "reflog" -- a log of where your HEAD and branch references have been for the last few months.
- **First relevant rank:** >10
- **Top-1 retrieved (07_revision-selection):** Every time your branch tip is updated for any reason, Git stores that information for you in this temporary history. You can use your reflog data to refer to older commits as well. For example, if you want to see the fifth prior value of t…

## recursive 100 - q158: right document, wrong passage

- **Question:** Which instruction word in the rebase script melds a commit into the one before it and asks you to join their log messages?
- **Evidence (07_rewriting-history):** If, instead of "pick" or "edit", you specify "squash", Git applies both that change and the change directly before it and makes you merge the commit messages together.
- **First relevant rank:** >10
- **Top-1 retrieved (07_rewriting-history):** # If you remove a line here THAT COMMIT WILL BE LOST. # # However, if you remove everything, the rebase will be aborted. # # Note that empty commits are commented out

## recursive 100 - q160: right document, wrong passage

- **Question:** How can you ask the log command to replay the whole evolution of a single function as patches?
- **Evidence (07_searching):** Simply run git log with the -L option, and it will show you the history of a function or line of code in your codebase.
- **First relevant rank:** >10
- **Top-1 retrieved (07_searching):** For example, if we wanted to see every change made to the function git_deflate_bound in the zlib.c file, we could run git log -L :git_deflate_bound:zlib.c. This will try to figure out what the bounds of that function are and then look thro…

## recursive 100 - q162: right document, wrong passage

- **Question:** Which pickaxe-style log flag takes a regular expression rather than a fixed string?
- **Evidence (07_searching):** If you need to be more specific, you can provide a regular expression to search for with the -G option.
- **First relevant rank:** >10
- **Top-1 retrieved (07_searching):** You can also search for complex combinations of strings with the --and flag, which ensures that multiple matches must occur in the same line of text.

## recursive 100 - q166: right document, wrong passage

- **Question:** Which configuration entry records which GPG key Git should reach for when it signs things?
- **Evidence (07_signing):** Once you have a private key to sign with, you can configure Git to use it for signing things by setting the user.signingkey config setting.
- **First relevant rank:** 7
- **Top-1 retrieved (07_signing):** $ gpg --list-keys /Users/schacon/.gnupg/pubring.gpg --------------------------------- pub 2048R/0A46826A 2014-06-04 uid Scott Chacon (Git signing key) <schacon@gmail.com>

## recursive 100 - q172: right document, wrong passage

- **Question:** What argument to clone fills in every subproject, including ones nested inside them, without extra steps?
- **Evidence (07_submodules):** If you pass --recurse-submodules to the git clone command, it will automatically initialize and update each submodule in the repository, including nested submodules if any of the submodules in the repository have submodules themselves.
- **First relevant rank:** 6
- **Top-1 retrieved (07_submodules):** $ git clone --recurse-submodules https://github.com/chaconinc/MainProject Cloning into 'MainProject'... remote: Counting objects: 14, done. remote: Compressing objects: 100% (13/13), done. remote: Total 14 (delta 1), reused 13 (delta 0) Un…

## recursive 100 - q174: right document, wrong passage

- **Question:** Which tracked configuration file records the pairing of a subproject's URL with the local folder it sits in?
- **Evidence (07_submodules):** First you should notice the new .gitmodules file. This is a configuration file that stores the mapping between the project's URL and the local subdirectory you've pulled it into:
- **First relevant rank:** 8
- **Top-1 retrieved (07_submodules):** This is pretty cool as we can actually see the log of commits that we're about to commit to in our submodule. Once committed, you can see this information after the fact as well when you run git log -p.

## recursive 100 - q175: right document, wrong passage

- **Question:** Why can work you commit inside a subproject vanish when the superproject later refreshes it?
- **Evidence (07_submodules):** With no working branch tracking changes, that means even if you commit changes to the submodule, those changes will quite possibly be lost the next time you run git submodule update.
- **First relevant rank:** >10
- **Top-1 retrieved (07_submodules):** There is a special situation that can happen when pulling superproject updates: it could be that the upstream repository has changed the URL of the submodule in the .gitmodules file in one of the commits you pull. This can happen for examp…

## recursive 100 - q176: wrong document

- **Question:** Since ordinary diff will not compare the vendored folder against the branch it came from, what must you use instead?
- **Evidence (07_subtree-merges):** you must run git diff-tree with the branch you want to compare to:
- **First relevant rank:** >10
- **Top-1 retrieved (06_2-contributing):** See ch05-distributed-git#_what_is_introduced for more about this type of diff.

## recursive 100 - q178: wrong document

- **Question:** Which plumbing command loads another branch's top-level tree into your index and working files?
- **Evidence (07_subtree-merges):** You'll learn more about read-tree and its friends in ch10-git-internals#ch10-git-internals, but for now know that it reads the root tree of one branch into your current staging area and working directory.
- **First relevant rank:** >10
- **Top-1 retrieved (07_reset):** The Git cat-file and ls-tree commands are "plumbing" commands that are used for lower level things and not really used in day-to-day work, but they help us see what's going on here. The Index The index is your proposed next commit. We've a…

## recursive 100 - q179: wrong document

- **Question:** Which two settings bring the vendored project's updates across with a ready-made commit message?
- **Evidence (07_subtree-merges):** To pull in the changes and prepopulate the commit message, use the --squash option, as well as the recursive merge strategy's -Xsubtree option.
- **First relevant rank:** >10
- **Top-1 retrieved (08_hooks):** The prepare-commit-msg hook is run before the commit message editor is fired up but after the default message is created. It lets you edit the default message before the commit author sees it. This hook takes a few parameters: the path to …

## recursive 100 - q180: wrong document

- **Question:** Where do you declare that particular paths should be run through scripts on checkout and on staging, and what are those two processing steps named?
- **Evidence (08_attributes):** In the .gitattributes file, you can set a filter for particular paths and then set up scripts that will process files just before they're checked out ("smudge", see filters_a) and just before they're staged ("clean", see filters_b).
- **First relevant rank:** 6
- **Top-1 retrieved (07_interactive-staging):** With these basic commands, you can use the interactive add mode to deal with your staging area a little more easily. Staging Patches

## recursive 100 - q182: wrong document

- **Question:** Why might a content filter that works for you break for a colleague who clones the same project?
- **Evidence (08_attributes):** You have to be careful, though, because the .gitattributes file is committed and passed around with the project, but the driver (in this case, dater) isn't, so it won't work everywhere.
- **First relevant rank:** >10
- **Top-1 retrieved (05_contributing):** The second developer, Jessica, does the same thing -- clones the repository and commits a change:

## recursive 100 - q189: wrong document

- **Question:** How many parameters does the server-side script used for this policy receive, and how frequently is it executed?
- **Evidence (08_policy):** The update hook runs once per branch being pushed and takes three arguments:
- **First relevant rank:** >10
- **Top-1 retrieved (06_5-scripting):** This also has the added advantage of increasing your rate limit. Without authenticating, you will be limited to 60 requests per hour. If you authenticate you can make up to 5,000 requests per hour.

## recursive 100 - q191: wrong document

- **Question:** Where does text printed by a server-side enforcement script end up?
- **Evidence (08_policy):** Anything your script echoes to stdout will be transferred to the client.
- **First relevant rank:** >10
- **Top-1 retrieved (07_credentials):** If the protocol, host, and username from known match this line, the program prints the results to stdout and exits.

## recursive 100 - q194: wrong document

- **Question:** Which variable supplies fallback locations to search when an object is missing from the main object store?
- **Evidence (10_environment):** GIT_ALTERNATE_OBJECT_DIRECTORIES is a colon-separated list (formatted like /dir/one:/dir/two:…) which tells Git where to check for objects if they aren't in GIT_OBJECT_DIRECTORY.
- **First relevant rank:** >10
- **Top-1 retrieved (01_help):** -A, --all add changes from all tracked and untracked files --ignore-removal ignore paths removed in the working tree (same as --no-all) --refresh don't add, only refresh the index --ignore-errors just skip files which cannot be added becau…

## recursive 100 - q195: wrong document

- **Question:** How many unpacked objects or how many pack files does it take before the automatic cleanup actually does work?
- **Evidence (10_maintenance):** You must have around 7,000 loose objects or more than 50 packfiles for Git to fire up a real gc command.
- **First relevant rank:** >10
- **Top-1 retrieved (10_packfiles):** The other files are your new packfile and an index. The packfile is a single file containing the contents of all the objects that were removed from your filesystem. The index is a file that contains offsets into that packfile so you can qu…

## recursive 100 - q203: wrong document

- **Question:** What similarity does Git look for between objects when deciding which ones to store as differences?
- **Evidence (10_packfiles):** When Git packs objects, it looks for files that are named and sized similarly, and stores just the deltas from one version of the file to the next.
- **First relevant rank:** >10
- **Top-1 retrieved (10_objects):** The next type of Git object we'll examine is the tree, which solves the problem of storing the filename and also allows you to store a group of files together. Git stores content in a manner similar to a UNIX filesystem, but a bit simplifi…

## recursive 100 - q210: wrong document

- **Question:** What does the leading plus sign in front of a mapping authorise Git to do?
- **Evidence (10_refspec):** The + tells Git to update the reference even if it isn't a fast-forward.
- **First relevant rank:** >10
- **Top-1 retrieved (05_maintaining):** They can use that key to verify all your signed tags. Also, if you include instructions in the tag message, running git show <tag> will let you give the end user more specific instructions about tag verification. Generating a Build Number

## recursive 100 - q212: wrong document

- **Question:** Why does pushing with nothing before the colon wipe out a branch upstream?
- **Evidence (10_refspec):** Because the refspec is <src>:<dst>, by leaving off the <src> part, this basically says to make the topic branch on the remote nothing, which deletes it.
- **First relevant rank:** >10
- **Top-1 retrieved (05_contributing):** This is called a refspec. See ch10-git-internals#_refspec for a more detailed discussion of Git refspecs and different things you can do with them. Also notice the -u flag; this is short for --set-upstream, which configures the branches fo…

## fixed_overlap 200+80 - q005: wrong document

- **Question:** Which kind of Git interface can I count on every user already having?
- **Evidence (01_command-line):** all users will have the command-line tools installed and available.
- **First relevant rank:** >10
- **Top-1 retrieved (08_config):** review: Git uses a series of configuration files to determine non-default behavior that you may want. The first place Git looks for these values is in the system-wide [path]/etc/gitconfig file, which contains settings that are applied to e…

## fixed_overlap 200+80 - q008: wrong document

- **Question:** What is a brand new repository's first branch named if I never configure it?
- **Evidence (01_first-time-setup):** By default Git will create a branch called master when you create a new repository with git init.
- **First relevant rank:** >10
- **Top-1 retrieved (03_remote-branches):** make sure they accurately represent the state of the remote repository. Think of them as bookmarks, to remind you where the branches in your remote repositories were the last time you connected to them. Remote-tracking branch names take th…

## fixed_overlap 200+80 - q012: wrong document

- **Question:** Which flag prints a brief list of a command's options instead of the whole manual?
- **Evidence (01_help):** In addition, if you don't need the full-blown manpage help, but just need a quick refresher on the available options for a Git command, you can ask for the more concise "help" output with the -h option, as in:
- **First relevant rank:** >10
- **Top-1 retrieved (02_viewing-history):** output will become more interesting as we go through branching and merging in the next chapter. Those are only some simple output-formatting options to git log -- there are many more. log_options lists the options we've covered so far, as …

## fixed_overlap 200+80 - q019: wrong document

- **Question:** Do everyday Git commands have to reach another machine to do their work?
- **Evidence (01_what-is-git):** Most operations in Git need only local files and resources to operate -- generally no information is needed from another computer on your network.
- **First relevant rank:** 6
- **Top-1 retrieved (02_getting-a-repository):** these commands do in just a minute. At this point, you have a Git repository with tracked files and an initial commit. Cloning an Existing Repository If you want to get a copy of an existing Git repository -- for example, a project you'd l…

## fixed_overlap 200+80 - q021: wrong document

- **Question:** Where does Git keep the record of what is queued up for the next commit?
- **Evidence (01_what-is-git):** The staging area is a file, generally contained in your Git directory, that stores information about what will go into your next commit.
- **First relevant rank:** >10
- **Top-1 retrieved (10_objects):** Git does when you run the git add and git commit commands -- it stores blobs for the files that have changed, updates the index, writes out trees, and writes commit objects that reference the top-level trees and the commits that came immed…

## fixed_overlap 200+80 - q026: wrong document

- **Question:** Can I choose a target folder name that differs from the project's own?
- **Evidence (02_getting-a-repository):** If you want to clone the repository into a directory named something other than libgit2, you can specify the new directory name as an additional argument:
- **First relevant rank:** >10
- **Top-1 retrieved (10_environment):** file (non-bare repositories only). GIT_OBJECT_DIRECTORY can be used to specify the location of the directory that usually resides at .git/objects. GIT_ALTERNATE_OBJECT_DIRECTORIES is a colon-separated list (formatted like /dir/one:/dir/two…

## fixed_overlap 200+80 - q028: wrong document

- **Question:** I edited a file again after staging it; what do I have to do before committing?
- **Evidence (02_recording-changes):** If you modify a file after you run git add, you have to run git add again to stage the latest version of the file:
- **First relevant rank:** >10
- **Top-1 retrieved (02_undoing):** new commit in its place. Effectively, it's as if the previous commit never happened, and it won't show up in your repository history. The obvious value to amending commits is to make minor improvements to your last commit, without clutteri…

## fixed_overlap 200+80 - q031: wrong document

- **Question:** Besides downloading new commits, what else does pulling do?
- **Evidence (02_remotes):** Running git pull generally fetches data from the server you originally cloned from and automatically tries to merge it into the code you're currently working on.
- **First relevant rank:** >10
- **Top-1 retrieved (05_contributing):** pulled. For instance, if Jessica wants to send John a pull request, and she's done two commits on the topic branch she just pushed, she can run this: $ git request-pull origin/master myfork The following changes since commit 1edee6b1d61823…

## fixed_overlap 200+80 - q032: right document, wrong passage

- **Question:** What else gets thrown away when I drop a remote from my repository?
- **Evidence (02_remotes):** Once you delete the reference to a remote this way, all remote-tracking branches and configuration settings associated with that remote are also deleted.
- **First relevant rank:** 9
- **Top-1 retrieved (02_remotes):** are no longer valid, manage various remote branches and define them as being tracked or not, and more. In this section, we'll cover some of these remote-management skills. Remote repositories can be on your local machine. It is entirely po…

## fixed_overlap 200+80 - q044: wrong document

- **Question:** Which snapshots are combined when the current commit is not a direct ancestor of the branch being brought in?
- **Evidence (03_basic-branching-and-merging):** Git does a simple three-way merge, using the two snapshots pointed to by the branch tips and the common ancestor of the two.
- **First relevant rank:** >10
- **Top-1 retrieved (10_objects):** 6601ebc7a059dd55cfe9 Each of the three commit objects points to one of the three snapshot trees you created. Oddly enough, you have a real Git history now that you can view with the git log command, if you run it on the last commit SHA-1: …

## fixed_overlap 200+80 - q046: right document, wrong passage

- **Question:** How can you get rid of a branch whose work has not been incorporated anywhere else?
- **Evidence (03_branch-management):** If you really do want to delete the branch and lose that work, you can force it with -D, as the helpful message points out.
- **First relevant rank:** >10
- **Top-1 retrieved (03_branch-management):** see which branches are already merged into the branch you're on, you can run git branch --merged: $ git branch --merged iss53 - master Because you already merged in iss53 earlier, you see it in your list. Branches on this list without the …

## fixed_overlap 200+80 - q047: wrong document

- **Question:** What does the asterisk shown beside one entry in the branch listing mean?
- **Evidence (03_branch-management):** Notice the * character that prefixes the master branch: it indicates the branch that you currently have checked out (i.e., the branch that HEAD points to).
- **First relevant rank:** >10
- **Top-1 retrieved (03_nutshell):** , this is a pointer to the local branch you're currently on. In this case, you're still on master. The git branch command only created a new branch -- it didn't switch to that branch. HEAD pointing to a branch You can easily see this by ru…

## fixed_overlap 200+80 - q050: wrong document

- **Question:** Whose history does the log command display if you give it no extra arguments?
- **Evidence (03_nutshell):** by default, git log will only show commit history below the branch you've checked out.
- **First relevant rank:** >10
- **Top-1 retrieved (07_revision-selection):** history If you have a UNIX or Linux background, you can think of the reflog as Git's version of shell history, which emphasizes that what's there is clearly relevant only for you and your "session", and has nothing to do with anyone else w…

## fixed_overlap 200+80 - q051: wrong document

- **Question:** Why are branches so inexpensive to make and throw away in Git?
- **Evidence (03_nutshell):** Because a branch in Git is actually a simple file that contains the 40 character SHA-1 checksum of the commit it points to, branches are cheap to create and destroy.
- **First relevant rank:** >10
- **Top-1 retrieved (03_workflows):** levels of stability. Some larger projects also have a proposed or pu (proposed updates) branch that has integrated branches that may not be ready to go into the next or master branch. The idea is that your branches are at various levels of…

## fixed_overlap 200+80 - q053: right document, wrong passage

- **Question:** What does the rebase command do with work recorded on one branch?
- **Evidence (03_rebasing):** With the rebase command, you can take all the changes that were committed on one branch and replay them on a different branch.
- **First relevant rank:** >10
- **Top-1 retrieved (03_rebasing):** to the main project. That way, the maintainer doesn't have to do any integration work -- just a fast-forward or a clean apply. Note that the snapshot pointed to by the final commit you end up with, whether it's the last of the rebased comm…

## fixed_overlap 200+80 - q054: wrong document

- **Question:** Which commits must never be rebased?
- **Evidence (03_rebasing):** Do not rebase commits that exist outside your repository and that people may have based work on.
- **First relevant rank:** >10
- **Top-1 retrieved (07_rewriting-history):** are executed from top to bottom. # # If you remove a line here THAT COMMIT WILL BE LOST. # # However, if you remove everything, the rebase will be aborted. # # Note that empty commits are commented out It's important to note that these com…

## fixed_overlap 200+80 - q057: right document, wrong passage

- **Question:** What do local pointers such as origin/master actually stand for?
- **Evidence (03_remote-branches):** Remote-tracking branches are references to the state of remote branches.
- **First relevant rank:** >10
- **Top-1 retrieved (03_remote-branches):** 53 branch, but the branch on the server would be represented by the remote-tracking branch origin/iss53. This may be a bit confusing, so let's look at an example. Let's say you have a Git server on your network at git.ourcompany.com. If yo…

## fixed_overlap 200+80 - q058: right document, wrong passage

- **Question:** Is any network traffic involved while you create branches and combine them?
- **Evidence (03_workflows):** When you're branching and merging, everything is being done only in your Git repository -- there is no communication with the server.
- **First relevant rank:** >10
- **Top-1 retrieved (03_workflows):** levels of stability. Some larger projects also have a proposed or pu (proposed updates) branch that has integrated branches that may not be ready to go into the next or master branch. The idea is that your branches are at various levels of…

## fixed_overlap 200+80 - q059: wrong document

- **Question:** What is held in the proposed-updates branch that some bigger projects keep?
- **Evidence (03_workflows):** Some larger projects also have a proposed or pu (proposed updates) branch that has integrated branches that may not be ready to go into the next or master branch.
- **First relevant rank:** 6
- **Top-1 retrieved (05_maintaining):** _c), you merge it into develop (merwf_d); then, when you tag a release, you fast-forward master to wherever the now-stable develop branch is (merwf_e). Before a topic branch merge After a topic branch merge After a project release This way…

## fixed_overlap 200+80 - q063: wrong document

- **Question:** What difference does the -o flag make when a passphrase is chosen during key generation?
- **Evidence (04_generating-ssh-key):** if you do use a password, make sure to add the -o option; it saves the private key in a format that is more resistant to brute-force password cracking than is the default format.
- **First relevant rank:** >10
- **Top-1 retrieved (02_viewing-history):** format |================================ | Specifier | Description of Output | %H | Commit hash | %h | Abbreviated commit hash | %T | Tree hash | %t | Abbreviated tree hash | %P | Parent hashes | %p | Abbreviated parent hashes | %an | Auth…

## fixed_overlap 200+80 - q065: wrong document

- **Question:** Which command registers the service so it comes up when the machine boots?
- **Evidence (04_git-daemon):** you'll run systemctl enable git-daemon to automatically start the service on boot
- **First relevant rank:** 8
- **Top-1 retrieved (08_hooks):** ` The post-receive hook runs after the entire process is completed and can be used to update other services or notify users. It takes the same stdin data as the pre-receive hook. Examples include emailing a list, notifying a continuous int…

## fixed_overlap 200+80 - q066: wrong document

- **Question:** Which port has to be opened if a firewall sits in front of the machine?
- **Evidence (04_git-daemon):** If you're running a firewall, you'll also need to punch a hole in it at port 9418 on the box you're setting this up on.
- **First relevant rank:** >10
- **Top-1 retrieved (04_protocols):** can clone the repo (although this is often exactly what you want). It's also probably the most difficult protocol to set up. It must run its own daemon, which requires xinetd or systemd configuration or the like, which isn't always a walk …

## fixed_overlap 200+80 - q067: right document, wrong passage

- **Question:** What gives a developer the ability to send commits up, once they can log in over SSH?
- **Evidence (04_git-on-a-server):** If a user SSHs into a server and has write access to the /srv/git/my_project.git directory, they will also automatically have push access.
- **First relevant rank:** >10
- **Top-1 retrieved (04_git-on-a-server):** and that's how you're accessing the server. There are a few ways you can give access to everyone on your team. The first is to set up accounts for everybody, which is straightforward but can be cumbersome. You may not want to run adduser (…

## fixed_overlap 200+80 - q068: wrong document

- **Question:** Which flag makes the initialization set group write permissions correctly?
- **Evidence (04_git-on-a-server):** Git will automatically add group write permissions to a repository properly if you run the git init command with the --shared option.
- **First relevant rank:** >10
- **Top-1 retrieved (08_policy):** hook look at those rules, see what files are being introduced for all the commits being pushed, and determine whether the user doing the push has access to update all those files. The first thing you'll do is write your ACL. Here you'll us…

## fixed_overlap 200+80 - q075: wrong document

- **Question:** Which setting tells the build where your repositories live when generating the script?
- **Evidence (04_gitweb):** Notice that you have to tell the command where to find your Git repositories with the GITWEB_PROJECTROOT variable.
- **First relevant rank:** >10
- **Top-1 retrieved (01_first-time-setup):** --global option, and this affects all of the repositories you work with on your system. 3. config file in the Git directory (that is, .git/config) of whatever repository you're currently using: Specific to that single repository. You can f…

## fixed_overlap 200+80 - q079: wrong document

- **Question:** How many transport mechanisms can move data, and which are they?
- **Evidence (04_protocols):** Git can use four distinct protocols to transfer data: Local, HTTP, Secure Shell (SSH) and Git.
- **First relevant rank:** >10
- **Top-1 retrieved (10_transfer-protocols):** , this is the same format as above. The response to this request indicates success or failure, and includes the packfile. Protocols Summary This section contains a very basic overview of the transfer protocols. The protocol includes many o…

## fixed_overlap 200+80 - q083: wrong document

- **Question:** What has to be done on the machine itself each time a new project should be hosted?
- **Evidence (04_setting-up-server):** Note that someone must shell onto the machine and create a bare repository every time you want to add a project.
- **First relevant rank:** >10
- **Top-1 retrieved (06_3-maintaining):** Maintaining a Project Now that we're comfortable contributing to a project, let's look at the other side: creating, maintaining and administering your own project. Creating a New Repository Let's create a new repository to share our projec…

## fixed_overlap 200+80 - q084: wrong document

- **Question:** Which bundled tool keeps a shared account confined to version-control operations?
- **Evidence (04_setting-up-server):** You can easily restrict the git user account to only Git-related activities with a limited shell tool called git-shell that comes with Git.
- **First relevant rank:** >10
- **Top-1 retrieved (01_about-version-control):** .gnu.org/software/rcs/) works by keeping patch sets (that is, the differences between files) in a special format on disk; it can then re-create what any file looked like at any point in time by adding up all the patches. Centralized Versio…

## fixed_overlap 200+80 - q087: wrong document

- **Question:** Why does the group ownership of the repository directories need changing?
- **Evidence (04_smart-http):** You'll also need to set the Unix user group of the /srv/git directories to www-data so your web server can read- and write-access the repositories
- **First relevant rank:** >10
- **Top-1 retrieved (06_4-managing-organization):** " icon at the top-right of any GitHub page, and select "New organization" from the menu. The "New organization" menu item First you'll need to name your organization and provide an email address for a main point of contact for the group. T…

## fixed_overlap 200+80 - q091: wrong document

- **Question:** Why must a force flag be added when pushing a topic branch whose history you have just rewritten with a rebase?
- **Evidence (05_contributing):** Because you rebased the branch, you have to specify the -f to your push command in order to be able to replace the featureA branch on the server with a commit that isn't a descendant of it.
- **First relevant rank:** >10
- **Top-1 retrieved (03_rebasing):** together. More Interesting Rebases You can also have your rebase replay on something other than the rebase target branch. Take a history like rbdiag_e, for example. You branched a topic branch (server) to add some server-side functionality…

## fixed_overlap 200+80 - q094: wrong document

- **Question:** What two roles can one and the same developer fill under Git, unlike in a centralized tool?
- **Evidence (05_distributed-workflows):** In Git, however, every developer is potentially both a node and a hub
- **First relevant rank:** 9
- **Top-1 retrieved (05_contributing):** branch), and merge that work into your master branch when it's ready to be integrated. When you want to share that work, you fetch and merge your master from origin/master if it has changed, and finally push to the master branch on the ser…

## fixed_overlap 200+80 - q097: wrong document

- **Question:** When a mailed patch is applied, which parts of the email supply the commit's authorship and its message?
- **Evidence (05_maintaining):** The author information is taken from the email's From and Date headers, and the message of the commit is taken from the Subject and body (before the patch) of the email.
- **First relevant rank:** 7
- **Top-1 retrieved (02_viewing-history):** cn | Committer name | %ce | Committer email | %cd | Committer date | %cr | Committer date, relative | %s | Subject |================================ You may be wondering what the difference is between author and committer. The author is th…

## fixed_overlap 200+80 - q101: wrong document

- **Question:** What piece of information does GitHub use to attribute a commit to a particular member?
- **Evidence (06_1-setting-up-account):** The way that GitHub maps your Git commits to your user is by email address.
- **First relevant rank:** >10
- **Top-1 retrieved (02_viewing-history):** cn | Committer name | %ce | Committer email | %cd | Committer date | %cr | Committer date, relative | %s | Subject |================================ You may be wondering what the difference is between author and committer. The author is th…

## fixed_overlap 200+80 - q103: wrong document

- **Question:** Why is it worth giving each uploaded public key a label such as the machine it belongs to?
- **Evidence (06_1-setting-up-account):** You can name each of your keys (e.g. "My Laptop" or "Work Account") so that if you need to revoke a key later, you can easily tell which one you're looking for.
- **First relevant rank:** >10
- **Top-1 retrieved (10_refs):** Also notice that it doesn't need to point to a commit; you can tag any Git object. In the Git source code, for example, the maintainer has added their GPG public key as a blob object and then tagged it. You can view the public key by runni…

## fixed_overlap 200+80 - q116: wrong document

- **Question:** How does the generic hooks mechanism hand event data over to your own system?
- **Evidence (06_5-scripting):** You specify a URL and GitHub will post an HTTP payload to that URL on any event you want.
- **First relevant rank:** 9
- **Top-1 retrieved (08_hooks):** Git Hooks Like many other Version Control Systems, Git has a way to fire off custom scripts when certain important actions occur. There are two groups of these hooks: client-side and server-side. Client-side hooks are triggered by operatio…

## fixed_overlap 200+80 - q122: wrong document

- **Question:** Which numbered index slot holds the common ancestor of a conflicted file, and which one holds the incoming branch's copy?
- **Evidence (07_advanced-merging):** Stage 1 is the common ancestor, stage 2 is your version and stage 3 is from the MERGE_HEAD, the version you're merging in ("theirs").
- **First relevant rank:** >10
- **Top-1 retrieved (07_reset):** structure. There are a few cases where the index doesn't exactly act like a tree, but for our purposes it is easier to think about it this way for now. Git as a system manages and manipulates three trees in its normal operation: |=========…

## fixed_overlap 200+80 - q124: wrong document

- **Question:** Does Git work out automatically which refs belong in a bundle, or must I enumerate them?
- **Evidence (07_bundling):** With the bundle command you need to list out every reference or specific range of commits that you want to be included.
- **First relevant rank:** >10
- **Top-1 retrieved (10_maintenance):** packlimit config settings, respectively. The other thing gc will do is pack up your references into a single file. Suppose your repository contains the following branches and tags: $ find .git/refs -type f git/refs/heads/experiment git/ref…

## fixed_overlap 200+80 - q125: wrong document

- **Question:** What artifact does Git produce from the data a push would normally send across the network?
- **Evidence (07_bundling):** The bundle command will package up everything that would normally be pushed over the wire with a git push command into a binary file
- **First relevant rank:** >10
- **Top-1 retrieved (10_transfer-protocols):** the client and connects to a receive-pack process on the remote side. SSH For example, say you run git push origin master in your project, and origin is defined as a URL that uses the SSH protocol. Git fires up the send-pack process, which…

## fixed_overlap 200+80 - q132: wrong document

- **Question:** After tracking down the faulty revision, what command returns me to the checkout I had beforehand?
- **Evidence (07_debugging):** When you're finished, you should run git bisect reset to reset your HEAD to where you were before you started, or you'll end up in a weird state
- **First relevant rank:** 10
- **Top-1 retrieved (10_maintenance):** 7c702daa24b Reflog: HEAD@{1} (Scott Chacon <schacon@gmail.com>) Reflog message: updating HEAD Author: Scott Chacon <schacon@gmail.com> Date: Fri May 22 18:15:24 2009 -0700 Modify repo.rb a bit It looks like the bottom commit is the one you…

## fixed_overlap 200+80 - q134: wrong document

- **Question:** What search technique does Git use to pin down the revision that introduced a regression?
- **Evidence (07_debugging):** The bisect command does a binary search through your commit history to help you identify as quickly as possible which commit introduced an issue.
- **First relevant rank:** >10
- **Top-1 retrieved (07_searching):** Searching With just about any size codebase, you'll often need to find where a function is called or defined, or display the history of a method. Git provides a couple of useful tools for looking through the code and commits stored in its …

## fixed_overlap 200+80 - q137: wrong document

- **Question:** Inside the menu-driven prompt, which letter or number takes a file back out of the staging area?
- **Evidence (07_interactive-staging):** If you want to unstage the TODO file at this point, you use the r or 3 (for revert) option
- **First relevant rank:** >10
- **Top-1 retrieved (02_undoing):** what happens when you do this and how to recover if you're on the receiving end read _rebase_peril. Unstaging a Staged File The next two sections demonstrate how to work with your staging area and working directory changes. The nice part i…

## fixed_overlap 200+80 - q138: right document, wrong passage

- **Question:** Which menu choice displays the changes already added to the staging area?
- **Evidence (07_interactive-staging):** To see the diff of what you've staged, you can use the d or 6 (for diff) command.
- **First relevant rank:** >10
- **Top-1 retrieved (07_interactive-staging):** see that this command shows you a much different view of your staging area than you're probably used to -- basically, the same information you get with git status but a bit more succinct and informative. It lists the changes you've staged …

## fixed_overlap 200+80 - q139: wrong document

- **Question:** Which two command-line switches make the add command open its menu-driven prompt?
- **Evidence (07_interactive-staging):** If you run git add with the -i or --interactive option, Git enters an interactive shell mode, displaying something like this
- **First relevant rank:** >10
- **Top-1 retrieved (01_first-time-setup):** ride this with a different name or email address for specific projects, you can run the command without the --global option when you're in that project. Many of the GUI tools will help you do this when you first run them. Your Editor Now t…

## fixed_overlap 200+80 - q142: right document, wrong passage

- **Question:** When joining a short recent history to a long archived one, which two commits do you pair up?
- **Evidence (07_replace):** You can graft one history onto the other by "replacing" the earliest commit in the new line with the latest commit on the older one.
- **First relevant rank:** 8
- **Top-1 retrieved (07_replace):** commit 945704c Second commit c1822cf First commit Creating a new history branch Now we can push the new history branch to the master branch of our new repository: $ git remote add project-history https://github.com/schacon/project-history …

## fixed_overlap 200+80 - q144: wrong document

- **Question:** Apart from the config flag, which directory can I create inside one repository to switch the feature on there?
- **Evidence (07_rerere):** You can also turn it on by creating the .git/rr-cache directory in a specific repository, but the config setting is clearer and enables that feature globally for you.
- **First relevant rank:** >10
- **Top-1 retrieved (06_3-maintaining):** or see by default, you can change that in your repository's settings page under the "Options" tab. Change the default branch for a project Simply change the default branch in the dropdown and that will be the default for all major operatio…

## fixed_overlap 200+80 - q152: wrong document

- **Question:** How far back does Git's background record of where HEAD and branch tips have pointed normally reach?
- **Evidence (07_revision-selection):** One of the things Git does in the background while you're working away is keep a "reflog" -- a log of where your HEAD and branch references have been for the last few months.
- **First relevant rank:** >10
- **Top-1 retrieved (07_reset):** ========================= The HEAD HEAD is the pointer to the current branch reference, which is in turn a pointer to the last commit made on that branch. That means HEAD will be the parent of the next commit that is created. It's generall…

## fixed_overlap 200+80 - q158: right document, wrong passage

- **Question:** Which instruction word in the rebase script melds a commit into the one before it and asks you to join their log messages?
- **Evidence (07_rewriting-history):** If, instead of "pick" or "edit", you specify "squash", Git applies both that change and the change directly before it and makes you merge the commit messages together.
- **First relevant rank:** >10
- **Top-1 retrieved (07_rewriting-history):** d, drop <commit> = remove commit # l, label <label> = label current HEAD with a name # t, reset <label> = reset HEAD to a label # m, merge [-C <commit> | -c <commit>] <label> [# <oneline>] # . create a merge commit using the original merge…

## fixed_overlap 200+80 - q162: wrong document

- **Question:** Which pickaxe-style log flag takes a regular expression rather than a fixed string?
- **Evidence (07_searching):** If you need to be more specific, you can provide a regular expression to search for with the -G option.
- **First relevant rank:** >10
- **Top-1 retrieved (05_contributing):** out a bunch of log information looking something like this for each patch you're sending: (mbox) Adding cc: Jessica Smith <jessica@example.com> from \line 'From: Jessica Smith <jessica@example.com>' OK. Log says: Sendmail: /usr/sbin/sendma…

## fixed_overlap 200+80 - q164: wrong document

- **Question:** From which release can merging and pulling be made to reject unsigned incoming commits, and with what argument?
- **Evidence (07_signing):** In Git 1.8.3 and later, git merge and git pull can be told to inspect and reject when merging a commit that does not carry a trusted GPG signature with the --verify-signatures command.
- **First relevant rank:** >10
- **Top-1 retrieved (06_3-maintaining):** merge commit even if a fast-forward merge was possible. This means that no matter what, every time you hit the merge button, a merge commit is created. As you can see in _merge_button, GitHub gives you all of this information if you click …

## fixed_overlap 200+80 - q168: wrong document

- **Question:** Since -u still skips files matched by ignore rules, what flag sweeps those in as well?
- **Evidence (07_stashing-cleaning):** including untracked files in the stash will still not include explicitly ignored files; to additionally include ignored files, use --all (or just -a).
- **First relevant rank:** >10
- **Top-1 retrieved (02_recording-changes):** zero or more characters; [abc] matches any character inside the brackets (in this case a, b, or c); a question mark (?) matches a single character; and brackets enclosing characters separated by a hyphen ([0-9]) matches any character betwe…

## fixed_overlap 200+80 - q170: right document, wrong passage

- **Question:** Which popular stash flag puts staged content into the saved entry yet still leaves that content ready for commit?
- **Evidence (07_stashing-cleaning):** The first option that is quite popular is the --keep-index option to the git stash command. This tells Git to not only include all staged content in the stash being created, but simultaneously leave it in the index.
- **First relevant rank:** >10
- **Top-1 retrieved (07_stashing-cleaning):** apply at any time (even on a different branch). Migrating to git stash push As of late October 2017, there has been extensive discussion on the Git mailing list, wherein the command git stash save is being deprecated in favour of the exist…

## fixed_overlap 200+80 - q175: right document, wrong passage

- **Question:** Why can work you commit inside a subproject vanish when the superproject later refreshes it?
- **Evidence (07_submodules):** With no working branch tracking changes, that means even if you commit changes to the submodule, those changes will quite possibly be lost the next time you run git submodule update.
- **First relevant rank:** 9
- **Top-1 retrieved (07_submodules):** the submodule project changes its hosting platform. In that case, it is possible for git pull --recurse-submodules, or git submodule update, to fail if the superproject references a submodule commit that is not found in the submodule remot…

## fixed_overlap 200+80 - q178: wrong document

- **Question:** Which plumbing command loads another branch's top-level tree into your index and working files?
- **Evidence (07_subtree-merges):** You'll learn more about read-tree and its friends in ch10-git-internals#ch10-git-internals, but for now know that it reads the root tree of one branch into your current staging area and working directory.
- **First relevant rank:** >10
- **Top-1 retrieved (07_reset):** ums for each file in the HEAD snapshot: $ git cat-file -p HEAD tree cfda3bf379e4f8dba8717dee55aab78aef7f4daf author Scott Chacon 1301511835 -0700 committer Scott Chacon 1301511835 -0700 initial commit $ git ls-tree -r HEAD 100644 blob a906…

## fixed_overlap 200+80 - q179: wrong document

- **Question:** Which two settings bring the vendored project's updates across with a ready-made commit message?
- **Evidence (07_subtree-merges):** To pull in the changes and prepopulate the commit message, use the --squash option, as well as the recursive merge strategy's -Xsubtree option.
- **First relevant rank:** >10
- **Top-1 retrieved (05_contributing):** the changeset concisely, followed by a blank line, followed by a more detailed explanation. The Git project requires that the more detailed explanation include your motivation for the change and contrast its implementation with previous be…

## fixed_overlap 200+80 - q182: wrong document

- **Question:** Why might a content filter that works for you break for a colleague who clones the same project?
- **Evidence (08_attributes):** You have to be careful, though, because the .gitattributes file is committed and passed around with the project, but the driver (in this case, dater) isn't, so it won't work everywhere.
- **First relevant rank:** >10
- **Top-1 retrieved (01_about-version-control):** is where Distributed Version Control Systems (DVCSs) step in. In a DVCS (such as Git, Mercurial or Darcs), clients don't just check out the latest snapshot of the files; rather, they fully mirror the repository, including its full history.…

## fixed_overlap 200+80 - q184: wrong document

- **Question:** Which configuration file is consulted first, and whose repositories does it affect?
- **Evidence (08_config):** The first place Git looks for these values is in the system-wide [path]/etc/gitconfig file, which contains settings that are applied to every user on the system and all of their repositories.
- **First relevant rank:** 6
- **Top-1 retrieved (10_plumbing-porcelain):** is where almost everything that Git stores and manipulates is located. If you want to back up or clone your repository, copying this single directory elsewhere gives you nearly everything you need. This entire chapter basically deals with …

## fixed_overlap 200+80 - q189: wrong document

- **Question:** How many parameters does the server-side script used for this policy receive, and how frequently is it executed?
- **Evidence (08_policy):** The update hook runs once per branch being pushed and takes three arguments:
- **First relevant rank:** >10
- **Top-1 retrieved (10_transfer-protocols):** a list of the server's capabilities (here, report-status, delete-refs, and some others, including the client identifier). The data is transmitted in chunks. Each chunk starts with a 4-character hex value specifying how long the chunk is (i…

## fixed_overlap 200+80 - q191: wrong document

- **Question:** Where does text printed by a server-side enforcement script end up?
- **Evidence (08_policy):** Anything your script echoes to stdout will be transferred to the client.
- **First relevant rank:** >10
- **Top-1 retrieved (10_transfer-protocols):** a list of the server's capabilities (here, report-status, delete-refs, and some others, including the client identifier). The data is transmitted in chunks. Each chunk starts with a 4-character hex value specifying how long the chunk is (i…

## fixed_overlap 200+80 - q194: wrong document

- **Question:** Which variable supplies fallback locations to search when an object is missing from the main object store?
- **Evidence (10_environment):** GIT_ALTERNATE_OBJECT_DIRECTORIES is a colon-separated list (formatted like /dir/one:/dir/two:…) which tells Git where to check for objects if they aren't in GIT_OBJECT_DIRECTORY.
- **First relevant rank:** >10
- **Top-1 retrieved (10_packfiles):** delta 3), reused 0 (delta 0) If you look in your objects directory, you'll find that most of your objects are gone, and a new pair of files has appeared: $ find .git/objects -type f git/objects/bd/9dbf5aae1a3862dd1526723246b20206e5fc37 git…

## fixed_overlap 200+80 - q195: wrong document

- **Question:** How many unpacked objects or how many pack files does it take before the automatic cleanup actually does work?
- **Evidence (10_maintenance):** You must have around 7,000 loose objects or more than 50 packfiles for Git to fire up a real gc command.
- **First relevant rank:** 10
- **Top-1 retrieved (10_packfiles):** delta 3), reused 0 (delta 0) If you look in your objects directory, you'll find that most of your objects are gone, and a new pair of files has appeared: $ find .git/objects -type f git/objects/bd/9dbf5aae1a3862dd1526723246b20206e5fc37 git…

## fixed_overlap 200+80 - q198: right document, wrong passage

- **Question:** How is the on-disk path of a stored object split up between folder name and file name?
- **Evidence (10_objects):** The subdirectory is named with the first 2 characters of the SHA-1, and the filename is the remaining 38 characters.
- **First relevant rank:** 7
- **Top-1 retrieved (10_objects):** ; plus, you aren't storing the filename in your system -- just the content. This object type is called a blob. You can have Git tell you the object type of any object in Git, given its SHA-1 key, with git cat-file -t: $ git cat-file -t 1f7…

## fixed_overlap 200+80 - q201: wrong document

- **Question:** Besides the automatic repacking Git performs on its own, how can someone trigger a repack deliberately?
- **Evidence (10_packfiles):** Git will occasionally repack your database automatically, always trying to save more space, but you can also manually repack at any time by running git gc by hand.
- **First relevant rank:** >10
- **Top-1 retrieved (08_hooks):** working tree changes. The pre-push hook runs during git push, after the remote refs have been updated but before any objects have been transferred. It receives the name and location of the remote as parameters, and a list of to-be-updated …

## fixed_overlap 200+80 - q203: wrong document

- **Question:** What similarity does Git look for between objects when deciding which ones to store as differences?
- **Evidence (10_packfiles):** When Git packs objects, it looks for files that are named and sized similarly, and stores just the deltas from one version of the file to the next.
- **First relevant rank:** >10
- **Top-1 retrieved (10_objects):** Git Objects Git is a content-addressable filesystem. Great. What does that mean? It means that at the core of Git is a simple key-value data store. What this means is that you can insert any kind of content into a Git repository, for which…

## fixed_overlap 200+80 - q210: wrong document

- **Question:** What does the leading plus sign in front of a mapping authorise Git to do?
- **Evidence (10_refspec):** The + tells Git to update the reference even if it isn't a fast-forward.
- **First relevant rank:** >10
- **Top-1 retrieved (10_environment):** override prefixes are disabled as well. GIT_ICASE_PATHSPECS sets all pathspecs to work in a case-insensitive manner. Committing The final creation of a Git commit object is usually done by git-commit-tree, which uses these environment vari…

## fixed_overlap 200+80 - q212: wrong document

- **Question:** Why does pushing with nothing before the colon wipe out a branch upstream?
- **Evidence (10_refspec):** Because the refspec is <src>:<dst>, by leaving off the <src> part, this basically says to make the topic branch on the remote nothing, which deletes it.
- **First relevant rank:** >10
- **Top-1 retrieved (07_replace):** t commit-tree 9c68fdc^{tree} 622e88e9cbfbacfb75b5279245b9fb38dfea10cf ===== The commit-tree command is one of a set of commands that are commonly referred to as 'plumbing' commands. These are commands that are not generally meant to be use…

## semantic p95 - q005: wrong document

- **Question:** Which kind of Git interface can I count on every user already having?
- **Evidence (01_command-line):** all users will have the command-line tools installed and available.
- **First relevant rank:** >10
- **Top-1 retrieved (04_git-daemon):** If you're running a firewall, you'll also need to punch a hole in it at port 9418 on the box you're setting this up on. You can daemonize this process a number of ways, depending on the operating system you're running. Since systemd is the…

## semantic p95 - q012: wrong document

- **Question:** Which flag prints a brief list of a command's options instead of the whole manual?
- **Evidence (01_help):** In addition, if you don't need the full-blown manpage help, but just need a quick refresher on the available options for a Git command, you can ask for the more concise "help" output with the -h option, as in:
- **First relevant rank:** >10
- **Top-1 retrieved (07_interactive-staging):** We'll go into more details on each of these as we get to more advanced usages of these commands.

## semantic p95 - q018: right document, wrong passage

- **Question:** Which libraries do I need before compiling Git myself?
- **Evidence (01_installing):** If you do want to install Git from source, you need to have the following libraries that Git depends on: autotools, curl, zlib, openssl, expat, and libiconv.
- **First relevant rank:** >10
- **Top-1 retrieved (01_installing):** Installing on Linux If you want to install the basic Git tools on Linux via a binary installer, you can generally do so through the package management tool that comes with your distribution. If you're on Fedora (or any closely-related RPM-…

## semantic p95 - q019: wrong document

- **Question:** Do everyday Git commands have to reach another machine to do their work?
- **Evidence (01_what-is-git):** Most operations in Git need only local files and resources to operate -- generally no information is needed from another computer on your network.
- **First relevant rank:** 7
- **Top-1 retrieved (03_remote-branches):** If you do some work on your local master branch, and, in the meantime, someone else pushes to git.ourcompany.com and updates its master branch, then your histories move forward differently. Also, as long as you stay out of contact with you…

## semantic p95 - q021: wrong document

- **Question:** Where does Git keep the record of what is queued up for the next commit?
- **Evidence (01_what-is-git):** The staging area is a file, generally contained in your Git directory, that stores information about what will go into your next commit.
- **First relevant rank:** >10
- **Top-1 retrieved (10_maintenance):** The trick is finding that latest commit SHA-1 – it's not like you've memorized it, right? Often, the quickest way is to use a tool called git reflog. As you're working, Git silently records what your HEAD is every time you change it. Each …

## semantic p95 - q025: wrong document

- **Question:** After turning an existing folder into a repository, how do I record its current files?
- **Evidence (02_getting-a-repository):** You can accomplish that with a few git add commands that specify the files you want to track, followed by a git commit:
- **First relevant rank:** 6
- **Top-1 retrieved (02_recording-changes):** Recording Changes to the Repository At this point, you should have a bona fide Git repository on your local machine, and a checkout or working copy of all of its files in front of you. Typically, you'll want to start making changes and com…

## semantic p95 - q026: wrong document

- **Question:** Can I choose a target folder name that differs from the project's own?
- **Evidence (02_getting-a-repository):** If you want to clone the repository into a directory named something other than libgit2, you can specify the new directory name as an additional argument:
- **First relevant rank:** >10
- **Top-1 retrieved (03_branch-management):** topicA featureB Changing a branch name Do not rename branches that are still in use by other collaborators. Do not rename a branch like master/main/mainline without having read the section _changing_master. Suppose you have a branch that i…

## semantic p95 - q028: wrong document

- **Question:** I edited a file again after staging it; what do I have to do before committing?
- **Evidence (02_recording-changes):** If you modify a file after you run git add, you have to run git add again to stage the latest version of the file:
- **First relevant rank:** >10
- **Top-1 retrieved (02_undoing):** For more on what happens when you do this and how to recover if you're on the receiving end read _rebase_peril. Unstaging a Staged File The next two sections demonstrate how to work with your staging area and working directory changes. The…

## semantic p95 - q030: right document, wrong passage

- **Question:** Which files in my working directory does Git consider untracked?
- **Evidence (02_recording-changes):** Untracked files are everything else -- any files in your working directory that were not in your last snapshot and are not in your staging area.
- **First relevant rank:** 6
- **Top-1 retrieved (02_recording-changes):** 1 file changed, 5 insertions(+), 0 deletions(-) Notice how you don't have to run git add on the CONTRIBUTING.md file in this case before you commit. That's because the -a flag includes all changed files. This is convenient, but be careful;…

## semantic p95 - q031: wrong document

- **Question:** Besides downloading new commits, what else does pulling do?
- **Evidence (02_remotes):** Running git pull generally fetches data from the server you originally cloned from and automatically tries to merge it into the code you're currently working on.
- **First relevant rank:** >10
- **Top-1 retrieved (06_3-maintaining):** For these examples, let's assume you are "tonychacon" and you've created a new Arduino code project named "fade". Email Notifications Someone comes along and makes a change to your code and sends you a Pull Request. You should get an email…

## semantic p95 - q034: right document, wrong passage

- **Question:** Do my tags travel to the server automatically when I push?
- **Evidence (02_tagging):** By default, the git push command doesn't transfer tags to remote servers.
- **First relevant rank:** >10
- **Top-1 retrieved (02_tagging):** To git@github.com:schacon/simplegit.git * [new tag] v1.5 -> v1.5 If you have a lot of tags that you want to push up at once, you can also use the --tags option to the git push command. This will transfer all of your tags to the remote serv…

## semantic p95 - q040: right document, wrong passage

- **Question:** How do I track down commits where a particular piece of text appeared or vanished?
- **Evidence (02_viewing-history):** Another really helpful filter is the -S option (colloquially referred to as Git's "pickaxe" option), which takes a string and shows only those commits that changed the number of occurrences of that string.
- **First relevant rank:** >10
- **Top-1 retrieved (02_viewing-history):** Viewing the Commit History After you have created several commits, or if you have cloned a repository with an existing commit history, you'll probably want to look back to see what has happened. The most basic and powerful tool to do this …

## semantic p95 - q041: wrong document

- **Question:** In what sequence are commits printed when no options are supplied?
- **Evidence (02_viewing-history):** By default, with no arguments, git log lists the commits made in that repository in reverse chronological order; that is, the most recent commits show up first.
- **First relevant rank:** >10
- **Top-1 retrieved (07_replace):** 622e88e9cbfbacfb75b5279245b9fb38dfea10cf ===== The commit-tree command is one of a set of commands that are commonly referred to as 'plumbing' commands. These are commands that are not generally meant to be used directly, but instead are u…

## semantic p95 - q044: wrong document

- **Question:** Which snapshots are combined when the current commit is not a direct ancestor of the branch being brought in?
- **Evidence (03_basic-branching-and-merging):** Git does a simple three-way merge, using the two snapshots pointed to by the branch tips and the common ancestor of the two.
- **First relevant rank:** >10
- **Top-1 retrieved (07_reset):** |================================ | Tree | Role | HEAD | Last commit snapshot, next parent | Index | Proposed next commit snapshot | Working Directory | Sandbox |================================

## semantic p95 - q047: wrong document

- **Question:** What does the asterisk shown beside one entry in the branch listing mean?
- **Evidence (03_branch-management):** Notice the * character that prefixes the master branch: it indicates the branch that you currently have checked out (i.e., the branch that HEAD points to).
- **First relevant rank:** >10
- **Top-1 retrieved (07_replace):** 622e88e9cbfbacfb75b5279245b9fb38dfea10cf ===== The commit-tree command is one of a set of commands that are commonly referred to as 'plumbing' commands. These are commands that are not generally meant to be used directly, but instead are u…

## semantic p95 - q050: wrong document

- **Question:** Whose history does the log command display if you give it no extra arguments?
- **Evidence (03_nutshell):** by default, git log will only show commit history below the branch you've checked out.
- **First relevant rank:** >10
- **Top-1 retrieved (07_revision-selection):** If you have a UNIX or Linux background, you can think of the reflog as Git's version of shell history, which emphasizes that what's there is clearly relevant only for you and your "session", and has nothing to do with anyone else who might…

## semantic p95 - q051: wrong document

- **Question:** Why are branches so inexpensive to make and throw away in Git?
- **Evidence (03_nutshell):** Because a branch in Git is actually a simple file that contains the 40 character SHA-1 checksum of the commit it points to, branches are cheap to create and destroy.
- **First relevant rank:** 8
- **Top-1 retrieved (03_workflows):** Some larger projects also have a proposed or pu (proposed updates) branch that has integrated branches that may not be ready to go into the next or master branch. The idea is that your branches are at various levels of stability; when they…

## semantic p95 - q053: right document, wrong passage

- **Question:** What does the rebase command do with work recorded on one branch?
- **Evidence (03_rebasing):** With the rebase command, you can take all the changes that were committed on one branch and replay them on a different branch.
- **First relevant rank:** >10
- **Top-1 retrieved (03_rebasing):** When you rebase stuff, you're abandoning existing commits and creating new ones that are similar but different. If you push commits somewhere and others pull them down and base work on them, and then you rewrite those commits with git reba…

## semantic p95 - q055: right document, wrong passage

- **Question:** Do branches you create on your own machine reach the server by themselves?
- **Evidence (03_remote-branches):** Your local branches aren't automatically synchronized to the remotes you write to -- you have to explicitly push the branches you want to share.
- **First relevant rank:** >10
- **Top-1 retrieved (03_remote-branches):** If you have a branch named serverfix that you want to work on with others, you can push it up the same way you pushed your first branch. Run git push <remote> <branch>: $ git push origin serverfix

## semantic p95 - q057: wrong document

- **Question:** What do local pointers such as origin/master actually stand for?
- **Evidence (03_remote-branches):** Remote-tracking branches are references to the state of remote branches.
- **First relevant rank:** 8
- **Top-1 retrieved (03_nutshell):** As you start making commits, you're given a master branch that points to the last commit you made. Every time you commit, the master branch pointer moves forward automatically. The "master" branch in Git is not a special branch. It is exac…

## semantic p95 - q058: right document, wrong passage

- **Question:** Is any network traffic involved while you create branches and combine them?
- **Evidence (03_workflows):** When you're branching and merging, everything is being done only in your Git repository -- there is no communication with the server.
- **First relevant rank:** >10
- **Top-1 retrieved (03_workflows):** Some larger projects also have a proposed or pu (proposed updates) branch that has integrated branches that may not be ready to go into the next or master branch. The idea is that your branches are at various levels of stability; when they…

## semantic p95 - q063: wrong document

- **Question:** What difference does the -o flag make when a passphrase is chosen during key generation?
- **Evidence (04_generating-ssh-key):** if you do use a password, make sure to add the -o option; it saves the private key in a format that is more resistant to brute-force password cracking than is the default format.
- **First relevant rank:** >10
- **Top-1 retrieved (10_environment):** The command is interpreted by the shell, and extra command-line arguments can be used with ssh, such as GIT_SSH_COMMAND="ssh -i ~/.ssh/my_key" git clone git@example.com:my/repo. GIT_ASKPASS is an override for the core.askpass configuration…

## semantic p95 - q066: wrong document

- **Question:** Which port has to be opened if a firewall sits in front of the machine?
- **Evidence (04_git-daemon):** If you're running a firewall, you'll also need to punch a hole in it at port 9418 on the box you're setting this up on.
- **First relevant rank:** >10
- **Top-1 retrieved (07_debugging):** Secure this thing :040000 040000 40ee3e7821b895e52c1695092db9bdc4c61d1730 f24d3c6ebcfc639b1a3814550e62d60b8e68a8e4 M config

## semantic p95 - q067: right document, wrong passage

- **Question:** What gives a developer the ability to send commits up, once they can log in over SSH?
- **Evidence (04_git-on-a-server):** If a user SSHs into a server and has write access to the /srv/git/my_project.git directory, they will also automatically have push access.
- **First relevant rank:** >10
- **Top-1 retrieved (04_git-on-a-server):** A second method is to create a single 'git' user account on the machine, ask every user who is to have write access to send you an SSH public key, and add that key to the ~/.ssh/authorized_keys file of that new 'git' account. At that point…

## semantic p95 - q068: wrong document

- **Question:** Which flag makes the initialization set group write permissions correctly?
- **Evidence (04_git-on-a-server):** Git will automatically add group write permissions to a repository properly if you run the git init command with the --shared option.
- **First relevant rank:** >10
- **Top-1 retrieved (01_help):** --chmod (+|-)x override the executable bit of the listed files --pathspec-from-file <file> read pathspec from file --pathspec-file-nul with --pathspec-from-file, pathspec elements are separated with NUL character

## semantic p95 - q075: wrong document

- **Question:** Which setting tells the build where your repositories live when generating the script?
- **Evidence (04_gitweb):** Notice that you have to tell the command where to find your Git repositories with the GITWEB_PROJECTROOT variable.
- **First relevant rank:** >10
- **Top-1 retrieved (06_3-maintaining):** Not only does this move the repository along with all its watchers and stars to another place, it also sets up a redirect from your URL to the new place. It will also redirect clones and fetches from Git, not just web requests.

## semantic p95 - q079: wrong document

- **Question:** How many transport mechanisms can move data, and which are they?
- **Evidence (04_protocols):** Git can use four distinct protocols to transfer data: Local, HTTP, Secure Shell (SSH) and Git.
- **First relevant rank:** >10
- **Top-1 retrieved (10_transfer-protocols):** This is very similar to invoking git-upload-pack over an SSH connection, but the second exchange is performed as a separate request: => POST $GIT_URL/git-upload-pack HTTP/1.0 0032want 0a53e9ddeaddad63ad106860237bbf53411d11a7 0032have 441b4…

## semantic p95 - q083: wrong document

- **Question:** What has to be done on the machine itself each time a new project should be hosted?
- **Evidence (04_setting-up-server):** Note that someone must shell onto the machine and create a bare repository every time you want to add a project.
- **First relevant rank:** >10
- **Top-1 retrieved (06_3-maintaining):** Maintaining a Project Now that we're comfortable contributing to a project, let's look at the other side: creating, maintaining and administering your own project. Creating a New Repository Let's create a new repository to share our projec…

## semantic p95 - q084: wrong document

- **Question:** Which bundled tool keeps a shared account confined to version-control operations?
- **Evidence (04_setting-up-server):** You can easily restrict the git user account to only Git-related activities with a limited shell tool called git-shell that comes with Git.
- **First relevant rank:** >10
- **Top-1 retrieved (01_about-version-control):** Local Version Control Systems Many people's version-control method of choice is to copy files into another directory (perhaps a time-stamped directory, if they're clever). This approach is very common because it is so simple, but it is als…

## semantic p95 - q087: wrong document

- **Question:** Why does the group ownership of the repository directories need changing?
- **Evidence (04_smart-http):** You'll also need to set the Unix user group of the /srv/git directories to www-data so your web server can read- and write-access the repositories
- **First relevant rank:** >10
- **Top-1 retrieved (04_gitlab):** Groups A GitLab group is a collection of projects, along with data about how users can access those projects. Each group has a project namespace (the same way that users do), so if the group +training+ has a project +materials+, its URL wo…

## semantic p95 - q098: wrong document

- **Question:** Which long-running branches does the Git project itself keep, and what is each one for?
- **Evidence (05_maintaining):** The Git project has four long-running branches: master, next, and seen (formerly 'pu' -- proposed updates) for new work, and maint for maintenance backports.
- **First relevant rank:** >10
- **Top-1 retrieved (03_workflows):** Some larger projects also have a proposed or pu (proposed updates) branch that has integrated branches that may not be ready to go into the next or master branch. The idea is that your branches are at various levels of stability; when they…

## semantic p95 - q101: wrong document

- **Question:** What piece of information does GitHub use to attribute a commit to a particular member?
- **Evidence (06_1-setting-up-account):** The way that GitHub maps your Git commits to your user is by email address.
- **First relevant rank:** >10
- **Top-1 retrieved (02_viewing-history):** You may be wondering what the difference is between author and committer. The author is the person who originally wrote the work, whereas the committer is the person who last applied the work. So, if you send in a patch to a project and on…

## semantic p95 - q103: wrong document

- **Question:** Why is it worth giving each uploaded public key a label such as the machine it belongs to?
- **Evidence (06_1-setting-up-account):** You can name each of your keys (e.g. "My Laptop" or "Work Account") so that if you need to revoke a key later, you can easily tell which one you're looking for.
- **First relevant rank:** >10
- **Top-1 retrieved (07_replace):** e146b5f14e79d4935160c0e83fb9ebe526b8da0d commit refs/heads/master c6e1e95051d41771a649f3145423f8809d1a74d4 commit refs/remotes/history/master e146b5f14e79d4935160c0e83fb9ebe526b8da0d commit refs/remotes/origin/HEAD e146b5f14e79d4935160c0e8…

## semantic p95 - q105: right document, wrong passage

- **Question:** Is it a good idea to force push over the branch an open Pull Request points at when tidying it up?
- **Evidence (06_2-contributing):** If you absolutely wish to rebase the branch to clean it up, you can certainly do so, but it is highly encouraged to not force push over the branch that the Pull Request is already opened on.
- **First relevant rank:** 6
- **Top-1 retrieved (06_2-contributing):** The other thing you'll notice is that GitHub checks to see if the Pull Request merges cleanly and provides a button to do the merge for you on the server. This button only shows up if you have write access to the repository and a trivial m…

## semantic p95 - q116: wrong document

- **Question:** How does the generic hooks mechanism hand event data over to your own system?
- **Evidence (06_5-scripting):** You specify a URL and GitHub will post an HTTP payload to that URL on any event you want.
- **First relevant rank:** >10
- **Top-1 retrieved (08_hooks):** Git Hooks Like many other Version Control Systems, Git has a way to fire off custom scripts when certain important actions occur. There are two groups of these hooks: client-side and server-side. Client-side hooks are triggered by operatio…

## semantic p95 - q122: wrong document

- **Question:** Which numbered index slot holds the common ancestor of a conflicted file, and which one holds the incoming branch's copy?
- **Evidence (07_advanced-merging):** Stage 1 is the common ancestor, stage 2 is your version and stage 3 is from the MERGE_HEAD, the version you're merging in ("theirs").
- **First relevant rank:** >10
- **Top-1 retrieved (07_reset):** The Index The index is your proposed next commit. We've also been referring to this concept as Git's "Staging Area" as this is what Git looks at when you run git commit. Git populates this index with a list of all the file contents that we…

## semantic p95 - q124: wrong document

- **Question:** Does Git work out automatically which refs belong in a bundle, or must I enumerate them?
- **Evidence (07_bundling):** With the bundle command you need to list out every reference or specific range of commits that you want to be included.
- **First relevant rank:** >10
- **Top-1 retrieved (06_3-maintaining):** url = https://github.com/libgit2/libgit2.git fetch = +refs/heads/:refs/remotes/origin/ fetch = +refs/pull//head:refs/remotes/origin/pr/ That last line tells Git, "All the refs that look like refs/pull/123/head should be stored locally like…

## semantic p95 - q125: wrong document

- **Question:** What artifact does Git produce from the data a push would normally send across the network?
- **Evidence (07_bundling):** The bundle command will package up everything that would normally be pushed over the wire with a git push command into a binary file
- **First relevant rank:** 10
- **Top-1 retrieved (10_transfer-protocols):** The Smart Protocol The dumb protocol is simple but a bit inefficient, and it can't handle writing of data from the client to the server. The smart protocol is a more common method of transferring data, but it requires a process on the remo…

## semantic p95 - q129: right document, wrong passage

- **Question:** If more than one helper is configured, which one's answer does Git end up using for a given host?
- **Evidence (07_credentials):** When looking for credentials for a particular host, Git will query them in order, and stop after the first answer is provided.
- **First relevant rank:** >10
- **Top-1 retrieved (07_credentials):** So the helpers described above are actually named git-credential-cache, git-credential-store, and so on, and we can configure them to take command-line arguments. The general form for this is "git-credential-foo [args] <action>." The stdin…

## semantic p95 - q130: right document, wrong passage

- **Question:** Which credential helper ships with Git on Apple machines, and where does it keep the secrets?
- **Evidence (07_credentials):** If you're using macOS, Git comes with an "osxkeychain" mode, which caches credentials in the secure keychain that's attached to your system account.
- **First relevant rank:** >10
- **Top-1 retrieved (07_credentials):** It's just a series of lines, each of which contains a credential-decorated URL. The osxkeychain and wincred helpers use the native format of their backing stores, while cache uses its own in-memory format (which no other process can read).…

## semantic p95 - q132: wrong document

- **Question:** After tracking down the faulty revision, what command returns me to the checkout I had beforehand?
- **Evidence (07_debugging):** When you're finished, you should run git bisect reset to reset your HEAD to where you were before you started, or you'll end up in a weird state
- **First relevant rank:** 7
- **Top-1 retrieved (07_reset):** It would be exactly like git reset --hard [branch] file (if reset would let you run that) -- it's not working-directory safe, and it does not move HEAD. Also, like git reset and git add, checkout will accept a --patch option to allow you t…

## semantic p95 - q134: wrong document

- **Question:** What search technique does Git use to pin down the revision that introduced a regression?
- **Evidence (07_debugging):** The bisect command does a binary search through your commit history to help you identify as quickly as possible which commit introduced an issue.
- **First relevant rank:** 7
- **Top-1 retrieved (07_searching):** The git grep command has a few advantages over normal searching commands like grep and ack. The first is that it's really fast, the second is that you can search through any tree in Git, not just the working directory. As we saw in the abo…

## semantic p95 - q135: right document, wrong passage

- **Question:** Which annotation flag tracks down where a block of code lived before it was copied into the current file?
- **Evidence (07_debugging):** If you pass -C to git blame, Git analyzes the file you're annotating and tries to figure out where snippets of code within it originally came from if they were copied from elsewhere.
- **First relevant rank:** >10
- **Top-1 retrieved (07_debugging):** Debugging with Git In addition to being primarily for version control, Git also provides a couple commands to help you debug your source code projects. Because Git is designed to handle nearly any type of content, these tools are pretty ge…

## semantic p95 - q137: wrong document

- **Question:** Inside the menu-driven prompt, which letter or number takes a file back out of the staging area?
- **Evidence (07_interactive-staging):** If you want to unstage the TODO file at this point, you use the r or 3 (for revert) option
- **First relevant rank:** >10
- **Top-1 retrieved (02_undoing):** For more on what happens when you do this and how to recover if you're on the receiving end read _rebase_peril. Unstaging a Staged File The next two sections demonstrate how to work with your staging area and working directory changes. The…

## semantic p95 - q138: wrong document

- **Question:** Which menu choice displays the changes already added to the staging area?
- **Evidence (07_interactive-staging):** To see the diff of what you've staged, you can use the d or 6 (for diff) command.
- **First relevant rank:** 10
- **Top-1 retrieved (02_recording-changes):** If you are starting to work on a particular area, feel free to submit a PR that highlights your work in progress (and note in the PR title that it's That command compares what is in your working directory with what is in your staging area.…

## semantic p95 - q139: right document, wrong passage

- **Question:** Which two command-line switches make the add command open its menu-driven prompt?
- **Evidence (07_interactive-staging):** If you run git add with the -i or --interactive option, Git enters an interactive shell mode, displaying something like this
- **First relevant rank:** >10
- **Top-1 retrieved (07_interactive-staging):** We'll go into more details on each of these as we get to more advanced usages of these commands.

## semantic p95 - q142: right document, wrong passage

- **Question:** When joining a short recent history to a long archived one, which two commits do you pair up?
- **Evidence (07_replace):** You can graft one history onto the other by "replacing" the earliest commit in the new line with the latest commit on the older one.
- **First relevant rank:** >10
- **Top-1 retrieved (07_replace):** Let's try this out. Let's take an existing repository, split it into two repositories, one recent and one historical, and then we'll see how we can recombine them without modifying the recent repositories SHA-1 values via replace. We'll us…

## semantic p95 - q143: right document, wrong passage

- **Question:** Which low-level command turns a tree into a fresh commit object that has no parent?
- **Evidence (07_replace):** We can create our base commit using the commit-tree command, which just takes a tree and will give us a brand new, parentless commit object SHA-1 back.
- **First relevant rank:** >10
- **Top-1 retrieved (07_replace):** 622e88e9cbfbacfb75b5279245b9fb38dfea10cf ===== The commit-tree command is one of a set of commands that are commonly referred to as 'plumbing' commands. These are commands that are not generally meant to be used directly, but instead are u…

## semantic p95 - q144: wrong document

- **Question:** Apart from the config flag, which directory can I create inside one repository to switch the feature on there?
- **Evidence (07_rerere):** You can also turn it on by creating the .git/rr-cache directory in a specific repository, but the config setting is clearer and enables that feature globally for you.
- **First relevant rank:** >10
- **Top-1 retrieved (06_3-maintaining):** Not only does this move the repository along with all its watchers and stars to another place, it also sets up a redirect from your URL to the new place. It will also redirect clones and fetches from Git, not just web requests.

## semantic p95 - q146: wrong document

- **Question:** What three words is the odd-looking name of Git's conflict-memory feature short for?
- **Evidence (07_rerere):** The name stands for "reuse recorded resolution" and, as the name implies, it allows you to ask Git to remember how you've resolved a hunk conflict
- **First relevant rank:** 10
- **Top-1 retrieved (05_maintaining):** Rerere If you're doing lots of merging and rebasing, or you're maintaining a long-lived topic branch, Git has a feature called "rerere" that can help. Rerere stands for "reuse recorded resolution" -- it's a way of shortcutting manual confl…

## semantic p95 - q148: right document, wrong passage

- **Question:** Between resetting and checking out a branch, which one relocates the branch pointer and which relocates HEAD?
- **Evidence (07_reset):** Whereas reset will move the branch that HEAD points to, checkout will move HEAD itself to point to another branch.
- **First relevant rank:** >10
- **Top-1 retrieved (07_reset):** Let's now walk through exactly what reset does when you call it. It directly manipulates these three trees in a simple and predictable way. It does up to three basic operations. Step 1: Move HEAD The first thing reset will do is move what …

## semantic p95 - q152: wrong document

- **Question:** How far back does Git's background record of where HEAD and branch tips have pointed normally reach?
- **Evidence (07_revision-selection):** One of the things Git does in the background while you're working away is keep a "reflog" -- a log of where your HEAD and branch references have been for the last few months.
- **First relevant rank:** 10
- **Top-1 retrieved (07_reset):** The HEAD HEAD is the pointer to the current branch reference, which is in turn a pointer to the last commit made on that branch. That means HEAD will be the parent of the next commit that is created. It's generally simplest to think of HEA…

## semantic p95 - q156: wrong document

- **Question:** After an import leaves junk top-level folders, how can an inner folder like trunk be promoted to the project root throughout history?
- **Evidence (07_rewriting-history):** If you want to make the trunk subdirectory be the new project root for every commit, filter-branch can help you do that, too:
- **First relevant rank:** >10
- **Top-1 retrieved (07_stashing-cleaning):** Stashing and Cleaning Often, when you've been working on part of your project, things are in a messy state and you want to switch branches for a bit to work on something else. The problem is, you don't want to do a commit of half-done work…

## semantic p95 - q162: wrong document

- **Question:** Which pickaxe-style log flag takes a regular expression rather than a fixed string?
- **Evidence (07_searching):** If you need to be more specific, you can provide a regular expression to search for with the -G option.
- **First relevant rank:** >10
- **Top-1 retrieved (02_viewing-history):** This is especially useful when you're generating output for machine parsing -- because you specify the format explicitly, you know it won't change with updates to Git: $ git log --pretty=format:"%h - %an, %ar : %s"

## semantic p95 - q164: wrong document

- **Question:** From which release can merging and pulling be made to reject unsigned incoming commits, and with what argument?
- **Evidence (07_signing):** In Git 1.8.3 and later, git merge and git pull can be told to inspect and reject when merging a commit that does not carry a trusted GPG signature with the --verify-signatures command.
- **First relevant rank:** >10
- **Top-1 retrieved (06_2-contributing):** When code is proposed with a Pull Request and the maintainers or community suggest a change, the patch series is generally not re-rolled, but instead the difference is pushed as a new commit to the branch, moving the conversation forward w…

## semantic p95 - q166: wrong document

- **Question:** Which configuration entry records which GPG key Git should reach for when it signs things?
- **Evidence (07_signing):** Once you have a private key to sign with, you can configure Git to use it for signing things by setting the user.signingkey config setting.
- **First relevant rank:** >10
- **Top-1 retrieved (08_config):** `user.signingkey` If you're making signed annotated tags (as discussed in ch07-git-tools#_signing), setting your GPG signing key as a configuration setting makes things easier. Set your key ID like so: $ git config --global user.signingkey…

## semantic p95 - q168: wrong document

- **Question:** Since -u still skips files matched by ignore rules, what flag sweeps those in as well?
- **Evidence (07_stashing-cleaning):** including untracked files in the stash will still not include explicitly ignored files; to additionally include ignored files, use --all (or just -a).
- **First relevant rank:** 8
- **Top-1 retrieved (01_help):** --refresh don't add, only refresh the index --ignore-errors just skip files which cannot be added because of errors --ignore-missing check if - even missing - files are ignored in dry run --sparse allow updating entries outside of the spar…

## semantic p95 - q169: right document, wrong passage

- **Question:** Which clean invocation discards untracked files and also any folders left empty by the deletion?
- **Evidence (07_stashing-cleaning):** To remove all the untracked files in your working directory, you can run git clean -f -d, which removes any files and also any subdirectories that become empty as a result.
- **First relevant rank:** >10
- **Top-1 retrieved (07_stashing-cleaning):** build.TMP test.o - Commands *** 1: clean 2: filter by pattern 3: select by numbers 4: ask each 5: quit 6: help What now> This way you can step through each file individually or specify patterns for deletion interactively. There is a quirky…

## semantic p95 - q176: wrong document

- **Question:** Since ordinary diff will not compare the vendored folder against the branch it came from, what must you use instead?
- **Evidence (07_subtree-merges):** you must run git diff-tree with the branch you want to compare to:
- **First relevant rank:** 9
- **Top-1 retrieved (08_config):** External Merge and Diff Tools Although Git has an internal implementation of diff, which is what we've been showing in this book, you can set up an external tool instead. You can also set up a graphical merge-conflict-resolution tool inste…

## semantic p95 - q178: wrong document

- **Question:** Which plumbing command loads another branch's top-level tree into your index and working files?
- **Evidence (07_subtree-merges):** You'll learn more about read-tree and its friends in ch10-git-internals#ch10-git-internals, but for now know that it reads the root tree of one branch into your current staging area and working directory.
- **First relevant rank:** >10
- **Top-1 retrieved (07_reset):** 100644 blob a906cb2a4a904a152... README 100644 blob 8f94139338f9404f2... Rakefile 040000 tree 99f1a6d12cb4b6f19... lib The Git cat-file and ls-tree commands are "plumbing" commands that are used for lower level things and not really used i…

## semantic p95 - q179: wrong document

- **Question:** Which two settings bring the vendored project's updates across with a ready-made commit message?
- **Evidence (07_subtree-merges):** To pull in the changes and prepopulate the commit message, use the --squash option, as well as the recursive merge strategy's -Xsubtree option.
- **First relevant rank:** >10
- **Top-1 retrieved (07_rewriting-history):** Don't include any commit you've already pushed to a central server -- doing so will confuse other developers by providing an alternate version of the same change. Running this command gives you a list of commits in your text editor that lo…

## semantic p95 - q180: wrong document

- **Question:** Where do you declare that particular paths should be run through scripts on checkout and on staging, and what are those two processing steps named?
- **Evidence (08_attributes):** In the .gitattributes file, you can set a filter for particular paths and then set up scripts that will process files just before they're checked out ("smudge", see filters_a) and just before they're staged ("clean", see filters_b).
- **First relevant rank:** 6
- **Top-1 retrieved (01_what-is-git):** You modify files in your working tree. 2. You selectively stage just those changes you want to be part of your next commit, which adds only those changes to the staging area. 3. You do a commit, which takes the files as they are in the sta…

## semantic p95 - q182: wrong document

- **Question:** Why might a content filter that works for you break for a colleague who clones the same project?
- **Evidence (08_attributes):** You have to be careful, though, because the .gitattributes file is committed and passed around with the project, but the driver (in this case, dater) isn't, so it won't work everywhere.
- **First relevant rank:** >10
- **Top-1 retrieved (03_rebasing):** When you rebase stuff, you're abandoning existing commits and creating new ones that are similar but different. If you push commits somewhere and others pull them down and base work on them, and then you rewrite those commits with git reba…

## semantic p95 - q183: wrong document

- **Question:** In what time unit is the numeric value of the mistyped-command correction delay expressed?
- **Evidence (08_config):** help.autocorrect is actually an integer which represents tenths of a second.
- **First relevant rank:** >10
- **Top-1 retrieved (07_searching):** If you're interested in the context of a search string, you can display the enclosing method or function for each matching string with either of the -p or --show-function options: $ git grep -p gmtime_r *.c date.c=static int match_multi_nu…

## semantic p95 - q184: wrong document

- **Question:** Which configuration file is consulted first, and whose repositories does it affect?
- **Evidence (08_config):** The first place Git looks for these values is in the system-wide [path]/etc/gitconfig file, which contains settings that are applied to every user on the system and all of their repositories.
- **First relevant rank:** 7
- **Top-1 retrieved (10_plumbing-porcelain):** $ ls -F1 config description HEAD hooks/ info/ objects/ refs/ Depending on your version of Git, you may see some additional content there, but this is a fresh git init repository -- it's what you see by default. The description file is used…

## semantic p95 - q187: wrong document

- **Question:** When somebody pushes several branches at once, how many times does each of the two main receive-side scripts run?
- **Evidence (08_hooks):** The update script is very similar to the pre-receive script, except that it's run once for each branch the pusher is trying to update.
- **First relevant rank:** >10
- **Top-1 retrieved (03_remote-branches):** remote: Counting objects: 7, done. remote: Compressing objects: 100% (2/2), done. remote: Total 3 (delta 0), reused 3 (delta 0) Unpacking objects: 100% (3/3), done. From https://github.com/schacon/simplegit * [new branch] serverfix -> orig…

## semantic p95 - q191: right document, wrong passage

- **Question:** Where does text printed by a server-side enforcement script end up?
- **Evidence (08_policy):** Anything your script echoes to stdout will be transferred to the client.
- **First relevant rank:** >10
- **Top-1 retrieved (08_policy):** An Example Git-Enforced Policy In this section, you'll use what you've learned to establish a Git workflow that checks for a custom commit message format, and allows only certain users to modify certain subdirectories in a project. You'll …

## semantic p95 - q194: wrong document

- **Question:** Which variable supplies fallback locations to search when an object is missing from the main object store?
- **Evidence (10_environment):** GIT_ALTERNATE_OBJECT_DIRECTORIES is a colon-separated list (formatted like /dir/one:/dir/two:…) which tells Git where to check for objects if they aren't in GIT_OBJECT_DIRECTORY.
- **First relevant rank:** >10
- **Top-1 retrieved (07_revision-selection):** What then? If you do happen to commit an object that hashes to the same SHA-1 value as a previous different object in your repository, Git will see the previous object already in your Git database, assume it was already written and simply …

## semantic p95 - q198: right document, wrong passage

- **Question:** How is the on-disk path of a stored object split up between folder name and file name?
- **Evidence (10_objects):** The subdirectory is named with the first 2 characters of the SHA-1, and the filename is the remaining 38 characters.
- **First relevant rank:** >10
- **Top-1 retrieved (10_objects):** => true >> FileUtils.mkdir_p(File.dirname(path)) => ".git/objects/bd" >> File.open(path, 'w') { |f| f.write zlib_content }

## semantic p95 - q199: wrong document

- **Question:** Is an object's checksum computed over its payload alone, or over something more?
- **Evidence (10_objects):** Git concatenates the header and the original content and then calculates the SHA-1 checksum of that new content.
- **First relevant rank:** >10
- **Top-1 retrieved (01_what-is-git):** This functionality is built into Git at the lowest levels and is integral to its philosophy. You can't lose information in transit or get file corruption without Git being able to detect it. The mechanism that Git uses for this checksummin…

## semantic p95 - q203: wrong document

- **Question:** What similarity does Git look for between objects when deciding which ones to store as differences?
- **Evidence (10_packfiles):** When Git packs objects, it looks for files that are named and sized similarly, and stores just the deltas from one version of the file to the next.
- **First relevant rank:** >10
- **Top-1 retrieved (10_objects):** $ git cat-file -t 1f7a7a472abf3dd9643fd615f6da379c4acb3e3a blob Tree Objects The next type of Git object we'll examine is the tree, which solves the problem of storing the filename and also allows you to store a group of files together. Gi…

## semantic p95 - q204: wrong document

- **Question:** Among the core pieces of a repository, what are the respective jobs of HEAD and of the index?
- **Evidence (10_plumbing-porcelain):** the HEAD file points to the branch you currently have checked out, and the index file is where Git stores your staging area information.
- **First relevant rank:** >10
- **Top-1 retrieved (07_reset):** The HEAD HEAD is the pointer to the current branch reference, which is in turn a pointer to the last commit made on that branch. That means HEAD will be the parent of the next commit that is created. It's generally simplest to think of HEA…

## semantic p95 - q208: wrong document

- **Question:** What does HEAD normally hold, and how does that differ from an ordinary ref?
- **Evidence (10_refs):** Usually the HEAD file is a symbolic reference to the branch you're currently on. By symbolic reference, we mean that unlike a normal reference, it contains a pointer to another reference.
- **First relevant rank:** 8
- **Top-1 retrieved (07_reset):** The HEAD HEAD is the pointer to the current branch reference, which is in turn a pointer to the last commit made on that branch. That means HEAD will be the parent of the next commit that is created. It's generally simplest to think of HEA…

## semantic p95 - q209: wrong document

- **Question:** Which pieces of data live inside a tag object, and which other object type is it closest to?
- **Evidence (10_refs):** The tag object is very much like a commit object -- it contains a tagger, a date, a message, and a pointer.
- **First relevant rank:** >10
- **Top-1 retrieved (02_tagging):** Listing tag wildcards requires -l or --list option If you want just the entire list of tags, running the command git tag implicitly assumes you want a listing and provides one; the use of -l or --list in this case is optional. If, however,…

## semantic p95 - q210: wrong document

- **Question:** What does the leading plus sign in front of a mapping authorise Git to do?
- **Evidence (10_refspec):** The + tells Git to update the reference even if it isn't a fast-forward.
- **First relevant rank:** >10
- **Top-1 retrieved (10_environment):** GIT_LITERAL_PATHSPECS disables both of the above behaviors; no wildcard characters will work, and the override prefixes are disabled as well. GIT_ICASE_PATHSPECS sets all pathspecs to work in a case-insensitive manner. Committing The final…

## semantic p95 - q212: wrong document

- **Question:** Why does pushing with nothing before the colon wipe out a branch upstream?
- **Evidence (10_refspec):** Because the refspec is <src>:<dst>, by leaving off the <src> part, this basically says to make the topic branch on the remote nothing, which deletes it.
- **First relevant rank:** >10
- **Top-1 retrieved (07_replace):** 622e88e9cbfbacfb75b5279245b9fb38dfea10cf ===== The commit-tree command is one of a set of commands that are commonly referred to as 'plumbing' commands. These are commands that are not generally meant to be used directly, but instead are u…
