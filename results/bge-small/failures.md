# Failure cases: bge-small, dense retrieval, selected configurations

A question counts as a miss when its first relevant chunk is not in the top 5.

## fixed 200 - q005: wrong document

- **Question:** Which kind of Git interface can I count on every user already having?
- **Evidence (01_command-line):** all users will have the command-line tools installed and available.
- **First relevant rank:** >10
- **Top-1 retrieved (05_contributing):** Contributing to a Project The main difficulty with describing how to contribute to a project are the numerous variations on how to do that. Because Git is very flexible, people can and do work together in many ways, and it's problematic to…

## fixed 200 - q008: wrong document

- **Question:** What is a brand new repository's first branch named if I never configure it?
- **Evidence (01_first-time-setup):** By default Git will create a branch called master when you create a new repository with git init.
- **First relevant rank:** >10
- **Top-1 retrieved (02_recording-changes):** branch on the server. For now, that branch is always master, which is the default; you won't worry about it here. ch03-git-branching#ch03-git-branching will go over branches and references in detail. GitHub changed the default branch name …

## fixed 200 - q012: wrong document

- **Question:** Which flag prints a brief list of a command's options instead of the whole manual?
- **Evidence (01_help):** In addition, if you don't need the full-blown manpage help, but just need a quick refresher on the available options for a Git command, you can ask for the more concise "help" output with the -h option, as in:
- **First relevant rank:** >10
- **Top-1 retrieved (02_viewing-history):** options lists the options we've covered so far, as well as some other common formatting options that may be useful, along with how they change the output of the log command. Common options to git log |================================ | Opt…

## fixed 200 - q019: wrong document

- **Question:** Do everyday Git commands have to reach another machine to do their work?
- **Evidence (01_what-is-git):** Most operations in Git need only local files and resources to operate -- generally no information is needed from another computer on your network.
- **First relevant rank:** >10
- **Top-1 retrieved (04_protocols):** The Protocols Git can use four distinct protocols to transfer data: Local, HTTP, Secure Shell (SSH) and Git. Here we'll discuss what they are and in what basic circumstances you would want (or not want) to use them. Local Protocol The most…

## fixed 200 - q021: wrong document

- **Question:** Where does Git keep the record of what is queued up for the next commit?
- **Evidence (01_what-is-git):** The staging area is a file, generally contained in your Git directory, that stores information about what will go into your next commit.
- **First relevant rank:** >10
- **Top-1 retrieved (02_recording-changes):** Recording Changes to the Repository At this point, you should have a bona fide Git repository on your local machine, and a checkout or working copy of all of its files in front of you. Typically, you'll want to start making changes and com…

## fixed 200 - q026: wrong document

- **Question:** Can I choose a target folder name that differs from the project's own?
- **Evidence (02_getting-a-repository):** If you want to clone the repository into a directory named something other than libgit2, you can specify the new directory name as an additional argument:
- **First relevant rank:** >10
- **Top-1 retrieved (07_subtree-merges):** project in our rack_branch branch and our own project in the master branch. If you check out one and then the other, you can see that they have different project roots: $ ls AUTHORS KNOWN-ISSUES Rakefile contrib lib COPYING README bin exam…

## fixed 200 - q028: wrong document

- **Question:** I edited a file again after staging it; what do I have to do before committing?
- **Evidence (02_recording-changes):** If you modify a file after you run git add, you have to run git add again to stage the latest version of the file:
- **First relevant rank:** >10
- **Top-1 retrieved (01_what-is-git):** you want to be part of your next commit, which adds only those changes to the staging area. 3. You do a commit, which takes the files as they are in the staging area and stores that snapshot permanently to your Git directory. If a particul…

## fixed 200 - q030: right document, wrong passage

- **Question:** Which files in my working directory does Git consider untracked?
- **Evidence (02_recording-changes):** Untracked files are everything else -- any files in your working directory that were not in your last snapshot and are not in your staging area.
- **First relevant rank:** 6
- **Top-1 retrieved (02_recording-changes):** , you see your untracked file like so: $ echo 'My Project' > README $ git status On branch master Your branch is up-to-date with 'origin/master'. Untracked files: (use "git add <file>..." to include in what will be committed) README nothin…

## fixed 200 - q031: right document, wrong passage

- **Question:** Besides downloading new commits, what else does pulling do?
- **Evidence (02_remotes):** Running git pull generally fetches data from the server you originally cloned from and automatically tries to merge it into the code you're currently working on.
- **First relevant rank:** >10
- **Top-1 retrieved (02_remotes):** new work that has been pushed to that server since you cloned (or last fetched from) it. It's important to note that the git fetch command only downloads the data to your local repository -- it doesn't automatically merge it with any of yo…

## fixed 200 - q038: wrong document

- **Question:** When is rewriting the most recent commit considered safe?
- **Evidence (02_undoing):** Only amend commits that are still local and have not been pushed somewhere.
- **First relevant rank:** 6
- **Top-1 retrieved (07_rewriting-history):** is that, since so much work is local within your clone, you have a great deal of freedom to rewrite your history locally. However, once you push your work, it is a different story entirely, and you should consider pushed work as final unle…

## fixed 200 - q040: right document, wrong passage

- **Question:** How do I track down commits where a particular piece of text appeared or vanished?
- **Evidence (02_viewing-history):** Another really helpful filter is the -S option (colloquially referred to as Git's "pickaxe" option), which takes a string and shows only those commits that changed the number of occurrences of that string.
- **First relevant rank:** >10
- **Top-1 retrieved (02_viewing-history):** with a commit message containing the string. | -S | Only show commits adding or removing code matching the string. |================================ For example, if you want to see which commits modifying test files in the Git source code …

## fixed 200 - q045: right document, wrong passage

- **Question:** Why was no new snapshot needed when the hotfix work was integrated back into master?
- **Evidence (03_basic-branching-and-merging):** Because the commit C4 pointed to by the branch hotfix you merged in was directly ahead of the commit C2 you're on, Git simply moves the pointer forward.
- **First relevant rank:** 8
- **Top-1 retrieved (03_basic-branching-and-merging):** fix. master is fast-forwarded to hotfix After your super-important fix is deployed, you're ready to switch back to the work you were doing before you were interrupted. However, first you'll delete the hotfix branch, because you no longer n…

## fixed 200 - q046: right document, wrong passage

- **Question:** How can you get rid of a branch whose work has not been incorporated anywhere else?
- **Evidence (03_branch-management):** If you really do want to delete the branch and lose that work, you can force it with -D, as the helpful message points out.
- **First relevant rank:** >10
- **Top-1 retrieved (03_branch-management):** in the readme The useful --merged and --no-merged options can filter this list to branches that you have or have not yet merged into the branch you're currently on. To see which branches are already merged into the branch you're on, you ca…

## fixed 200 - q050: wrong document

- **Question:** Whose history does the log command display if you give it no extra arguments?
- **Evidence (03_nutshell):** by default, git log will only show commit history below the branch you've checked out.
- **First relevant rank:** >10
- **Top-1 retrieved (02_viewing-history):** 32f8ecbe6306e7e7 Author: Scott Chacon <schacon@gee-mail.com> Date: Sat Mar 15 16:40:33 2008 -0700 Remove unnecessary test commit a11bef06a3f659402fe7563abf99ad00de2209e6 Author: Scott Chacon <schacon@gee-mail.com> Date: Sat Mar 15 10:31:28…

## fixed 200 - q057: right document, wrong passage

- **Question:** What do local pointers such as origin/master actually stand for?
- **Evidence (03_remote-branches):** Remote-tracking branches are references to the state of remote branches.
- **First relevant rank:** >10
- **Top-1 retrieved (03_remote-branches):** , neither does "origin". While "master" is the default name for a starting branch when you run git init which is the only reason it's widely used, "origin" is the default name for a remote when you run git clone. If you run git clone -o bo…

## fixed 200 - q058: right document, wrong passage

- **Question:** Is any network traffic involved while you create branches and combine them?
- **Evidence (03_workflows):** When you're branching and merging, everything is being done only in your Git repository -- there is no communication with the server.
- **First relevant rank:** >10
- **Top-1 retrieved (03_workflows):** Branching Workflows Now that you have the basics of branching and merging down, what can or should you do with them? In this section, we'll cover some common workflows that this lightweight branching makes possible, so you can decide if yo…

## fixed 200 - q059: wrong document

- **Question:** What is held in the proposed-updates branch that some bigger projects keep?
- **Evidence (03_workflows):** Some larger projects also have a proposed or pu (proposed updates) branch that has integrated branches that may not be ready to go into the next or master branch.
- **First relevant rank:** >10
- **Top-1 retrieved (05_maintaining):** a while, you fast-forward your master branch. Large-Merging Workflows The Git project has four long-running branches: master, next, and seen (formerly 'pu' -- proposed updates) for new work, and maint for maintenance backports. When new wo…

## fixed 200 - q067: wrong document

- **Question:** What gives a developer the ability to send commits up, once they can log in over SSH?
- **Evidence (04_git-on-a-server):** If a user SSHs into a server and has write access to the /srv/git/my_project.git directory, they will also automatically have push access.
- **First relevant rank:** >10
- **Top-1 retrieved (10_transfer-protocols):** and a pair for downloading data. Uploading Data To upload data to a remote process, Git uses the send-pack and receive-pack processes. The send-pack process runs on the client and connects to a receive-pack process on the remote side. SSH …

## fixed 200 - q068: wrong document

- **Question:** Which flag makes the initialization set group write permissions correctly?
- **Evidence (04_git-on-a-server):** Git will automatically add group write permissions to a repository properly if you run the git init command with the --shared option.
- **First relevant rank:** >10
- **Top-1 retrieved (08_config):** global core.pager '' If you run that, Git will print the entire output of all commands, no matter how long they are. `user.signingkey` If you're making signed annotated tags (as discussed in ch07-git-tools#_signing), setting your GPG signi…

## fixed 200 - q081: right document, wrong passage

- **Question:** What is the drawback of serving a project only over Secure Shell?
- **Evidence (04_protocols):** The negative aspect of SSH is that it doesn't support anonymous access to your Git repository.
- **First relevant rank:** 6
- **Top-1 retrieved (04_protocols):** your machine, even in a read-only capacity, which doesn't make SSH conducive to open source projects for which people might simply want to clone your repository to examine it. If you're using it only within your corporate network, SSH may …

## fixed 200 - q083: wrong document

- **Question:** What has to be done on the machine itself each time a new project should be hosted?
- **Evidence (04_setting-up-server):** Note that someone must shell onto the machine and create a bare repository every time you want to add a project.
- **First relevant rank:** >10
- **Top-1 retrieved (06_3-maintaining):** Maintaining a Project Now that we're comfortable contributing to a project, let's look at the other side: creating, maintaining and administering your own project. Creating a New Repository Let's create a new repository to share our projec…

## fixed 200 - q084: wrong document

- **Question:** Which bundled tool keeps a shared account confined to version-control operations?
- **Evidence (04_setting-up-server):** You can easily restrict the git user account to only Git-related activities with a limited shell tool called git-shell that comes with Git.
- **First relevant rank:** >10
- **Top-1 retrieved (05_contributing):** In short, do as we say, not as we do. Private Small Team The simplest setup you're likely to encounter is a private project with one or two other developers. "Private," in this context, means closed-source -- not accessible to the outside …

## fixed 200 - q087: wrong document

- **Question:** Why does the group ownership of the repository directories need changing?
- **Evidence (04_smart-http):** You'll also need to set the Unix user group of the /srv/git directories to www-data so your web server can read- and write-access the repositories
- **First relevant rank:** >10
- **Top-1 retrieved (05_distributed-workflows):** your fork for everyone to see. One of the main advantages of this approach is that you can continue to work, and the maintainer of the main repository can pull in your changes at any time. Contributors don't have to wait for the project to…

## fixed 200 - q089: wrong document

- **Question:** Which Git command will list possible whitespace problems in your work before you make the commit?
- **Evidence (05_contributing):** Git provides an easy way to check for this -- before you commit, run git diff --check, which identifies possible whitespace errors and lists them for you.
- **First relevant rank:** 7
- **Top-1 retrieved (08_config):** issues when you run a git diff command and try to color them so you can possibly fix them before you commit. It will also use these values to help you when you apply patches with git apply. When you're applying patches, you can ask Git to …

## fixed 200 - q091: right document, wrong passage

- **Question:** Why must a force flag be added when pushing a topic branch whose history you have just rewritten with a rebase?
- **Evidence (05_contributing):** Because you rebased the branch, you have to specify the -f to your push command in order to be able to replace the featureA branch on the server with a commit that isn't a descendant of it.
- **First relevant rank:** 9
- **Top-1 retrieved (05_contributing):** and to do your work in topic branches that you can easily discard if they're rejected. Having work themes isolated into topic branches also makes it easier for you to rebase your work if the tip of the main repository has moved in the mean…

## fixed 200 - q097: wrong document

- **Question:** When a mailed patch is applied, which parts of the email supply the commit's authorship and its message?
- **Evidence (05_maintaining):** The author information is taken from the email's From and Date headers, and the message of the commit is taken from the Subject and body (before the patch) of the email.
- **First relevant rank:** 9
- **Top-1 retrieved (02_viewing-history):** cn | Committer name | %ce | Committer email | %cd | Committer date | %cr | Committer date, relative | %s | Subject |================================ You may be wondering what the difference is between author and committer. The author is th…

## fixed 200 - q101: wrong document

- **Question:** What piece of information does GitHub use to attribute a commit to a particular member?
- **Evidence (06_1-setting-up-account):** The way that GitHub maps your Git commits to your user is by email address.
- **First relevant rank:** >10
- **Top-1 retrieved (10_environment):** Git commit object is usually done by git-commit-tree, which uses these environment variables as its primary source of information, falling back to configuration values only if these aren't present. GIT_AUTHOR_NAME is the human-readable nam…

## fixed 200 - q103: wrong document

- **Question:** Why is it worth giving each uploaded public key a label such as the machine it belongs to?
- **Evidence (06_1-setting-up-account):** You can name each of your keys (e.g. "My Laptop" or "Work Account") so that if you need to revoke a key later, you can easily tell which one you're looking for.
- **First relevant rank:** 10
- **Top-1 retrieved (10_refs):** public key as a blob object and then tagged it. You can view the public key by running this in a clone of the Git repository: $ git cat-file blob junio-gpg-pub The Linux kernel repository also has a non-commit-pointing tag object -- the fi…

## fixed 200 - q124: wrong document

- **Question:** Does Git work out automatically which refs belong in a bundle, or must I enumerate them?
- **Evidence (07_bundling):** With the bundle command you need to list out every reference or specific range of commits that you want to be included.
- **First relevant rank:** 9
- **Top-1 retrieved (06_3-maintaining):** https://github.com/libgit2/libgit2.git fetch = +refs/heads/:refs/remotes/origin/ fetch = +refs/pull//head:refs/remotes/origin/pr/ That last line tells Git, "All the refs that look like refs/pull/123/head should be stored locally like refs/…

## fixed 200 - q126: wrong document

- **Question:** What goes wrong if someone packages only their newest couple of commits and the receiving repository lacks the earlier ones?
- **Evidence (07_bundling):** If the bundler had created a bundle of just the last two commits they had done, rather than all three, the original repository would not be able to import it, since it is missing requisite history.
- **First relevant rank:** >10
- **Top-1 retrieved (07_debugging):** , and it turns out you can reproduce the issue, but you can't figure out what is going wrong. You can bisect the code to find out. First you run git bisect start to get things going, and then you use git bisect bad to tell the system that …

## fixed 200 - q129: right document, wrong passage

- **Question:** If more than one helper is configured, which one's answer does Git end up using for a given host?
- **Evidence (07_credentials):** When looking for credentials for a particular host, Git will query them in order, and stop after the first answer is provided.
- **First relevant rank:** 6
- **Top-1 retrieved (07_credentials):** https host=mygithost username=bob password=s3cre7 Since its name starts with "git-", we can use the simple syntax for the configuration value: $ git config --global credential.helper 'read-only --file /mnt/shared/creds' As you can see, ext…

## fixed 200 - q130: right document, wrong passage

- **Question:** Which credential helper ships with Git on Apple machines, and where does it keep the secrets?
- **Evidence (07_credentials):** If you're using macOS, Git comes with an "osxkeychain" mode, which caches credentials in the secure keychain that's attached to your system account.
- **First relevant rank:** 8
- **Top-1 retrieved (07_credentials):** = store --file /mnt/thumbdrive/.git-credentials helper = cache --timeout 30000 Under the Hood How does this all work? Git's root command for the credential-helper system is git credential, which takes a command as an argument, and then mor…

## fixed 200 - q132: wrong document

- **Question:** After tracking down the faulty revision, what command returns me to the checkout I had beforehand?
- **Evidence (07_debugging):** When you're finished, you should run git bisect reset to reset your HEAD to where you were before you started, or you'll end up in a weird state
- **First relevant rank:** >10
- **Top-1 retrieved (02_undoing):** been reverted. ===== It's important to understand that git checkout \-- <file> is a dangerous command. Any local changes you made to that file are gone -- Git just replaced that file with the last staged or committed version. Don't ever us…

## fixed 200 - q138: right document, wrong passage

- **Question:** Which menu choice displays the changes already added to the staging area?
- **Evidence (07_interactive-staging):** To see the diff of what you've staged, you can use the d or 6 (for diff) command.
- **First relevant rank:** 6
- **Top-1 retrieved (07_interactive-staging):** [a]dd untracked 5: [p]atch 6: [d]iff 7: [q]uit 8: [h]elp What now> You can see that this command shows you a much different view of your staging area than you're probably used to -- basically, the same information you get with git status b…

## fixed 200 - q139: wrong document

- **Question:** Which two command-line switches make the add command open its menu-driven prompt?
- **Evidence (07_interactive-staging):** If you run git add with the -i or --interactive option, Git enters an interactive shell mode, displaying something like this
- **First relevant rank:** 8
- **Top-1 retrieved (01_first-time-setup):** notepad++.exe' -multiInst -notabbar -nosession -noPlugin" Vim, Emacs and Notepad++ are popular text editors often used by developers on Unix-based systems like Linux and macOS or a Windows system. If you are using another editor, or a 32-b…

## fixed 200 - q142: right document, wrong passage

- **Question:** When joining a short recent history to a long archived one, which two commits do you pair up?
- **Evidence (07_replace):** You can graft one history onto the other by "replacing" the earliest commit in the new line with the latest commit on the older one.
- **First relevant rank:** >10
- **Top-1 retrieved (07_replace):** would normally have to do to join them together (because the parentage affects the SHA-1s). Let's try this out. Let's take an existing repository, split it into two repositories, one recent and one historical, and then we'll see how we can…

## fixed 200 - q143: right document, wrong passage

- **Question:** Which low-level command turns a tree into a fresh commit object that has no parent?
- **Evidence (07_replace):** We can create our base commit using the commit-tree command, which just takes a tree and will give us a brand new, parentless commit object SHA-1 back.
- **First relevant rank:** >10
- **Top-1 retrieved (07_replace):** f ===== The commit-tree command is one of a set of commands that are commonly referred to as 'plumbing' commands. These are commands that are not generally meant to be used directly, but instead are used by other Git commands to do smaller…

## fixed 200 - q144: wrong document

- **Question:** Apart from the config flag, which directory can I create inside one repository to switch the feature on there?
- **Evidence (07_rerere):** You can also turn it on by creating the .git/rr-cache directory in a specific repository, but the config setting is clearer and enables that feature globally for you.
- **First relevant rank:** >10
- **Top-1 retrieved (10_plumbing-porcelain):** , but rather to be used as building blocks for new tools and custom scripts. When you run git init in a new or existing directory, Git creates the .git directory, which is where almost everything that Git stores and manipulates is located.…

## fixed 200 - q145: wrong document

- **Question:** What repeated routine lets a long-lived topic branch stay mergeable without littering history with interim merge commits?
- **Evidence (07_rerere):** With rerere enabled, you can attempt the occasional merge, resolve the conflicts, then back out of the merge.
- **First relevant rank:** >10
- **Top-1 retrieved (07_advanced-merging):** : $ git merge topic Already up-to-date. There's nothing in topic that isn't already reachable from master. What's worse, if you add work to topic and merge again, Git will only bring in the changes since the reverted merge: History with a …

## fixed 200 - q146: wrong document

- **Question:** What three words is the odd-looking name of Git's conflict-memory feature short for?
- **Evidence (07_rerere):** The name stands for "reuse recorded resolution" and, as the name implies, it allows you to ask Git to remember how you've resolved a hunk conflict
- **First relevant rank:** 9
- **Top-1 retrieved (05_maintaining):** your topic branch and drop the commits you didn't want to pull in. Rerere If you're doing lots of merging and rebasing, or you're maintaining a long-lived topic branch, Git has a feature called "rerere" that can help. Rerere stands for "re…

## fixed 200 - q152: wrong document

- **Question:** How far back does Git's background record of where HEAD and branch tips have pointed normally reach?
- **Evidence (07_revision-selection):** One of the things Git does in the background while you're working away is keep a "reflog" -- a log of where your HEAD and branch references have been for the last few months.
- **First relevant rank:** >10
- **Top-1 retrieved (07_reset):** ==== | Tree | Role | HEAD | Last commit snapshot, next parent | Index | Proposed next commit snapshot | Working Directory | Sandbox |================================ The HEAD HEAD is the pointer to the current branch reference, which is in…

## fixed 200 - q161: right document, wrong passage

- **Question:** Which grep flag demands that two separate patterns both appear on the very same line?
- **Evidence (07_searching):** You can also search for complex combinations of strings with the --and flag, which ensures that multiple matches must occur in the same line of text.
- **First relevant rank:** >10
- **Top-1 retrieved (07_searching):** 1.8.0 (we'll throw in the --break and --heading options which help split up the output into a more readable format): $ git grep --break --heading \ -n -e '#define' --and \( -e LINK -e BUF_MAX \) v1.8.0 v1.8.0:builtin/index-pack.c 62:#defin…

## fixed 200 - q162: right document, wrong passage

- **Question:** Which pickaxe-style log flag takes a regular expression rather than a fixed string?
- **Evidence (07_searching):** If you need to be more specific, you can provide a regular expression to search for with the -G option.
- **First relevant rank:** 6
- **Top-1 retrieved (07_searching):** exists, but when it existed or was introduced. The git log command has a number of powerful tools for finding specific commits by the content of their messages or even the content of the diff they introduce. If, for example, we want to fin…

## fixed 200 - q166: right document, wrong passage

- **Question:** Which configuration entry records which GPG key Git should reach for when it signs things?
- **Evidence (07_signing):** Once you have a private key to sign with, you can configure Git to use it for signing things by setting the user.signingkey config setting.
- **First relevant rank:** 7
- **Top-1 retrieved (07_signing):** -05-04 If you run git show on that tag, you can see your GPG signature attached to it: $ git show v1.5 tag v1.5 Tagger: Ben Straub <ben@straub.cc> Date: Sat May 3 20:29:41 2014 -0700 my signed 1.5 tag -----BEGIN PGP SIGNATURE----- Version:…

## fixed 200 - q168: right document, wrong passage

- **Question:** Since -u still skips files matched by ignore rules, what flag sweeps those in as well?
- **Evidence (07_stashing-cleaning):** including untracked files in the stash will still not include explicitly ignored files; to additionally include ignored files, use --all (or just -a).
- **First relevant rank:** >10
- **Top-1 retrieved (07_stashing-cleaning):** re or other ignore files will not be removed. If you want to remove those files too, such as to remove all .o files generated from a build so you can do a fully clean build, you can add a -x to the clean command. $ git status -s M lib/simp…

## fixed 200 - q176: wrong document

- **Question:** Since ordinary diff will not compare the vendored folder against the branch it came from, what must you use instead?
- **Evidence (07_subtree-merges):** you must run git diff-tree with the branch you want to compare to:
- **First relevant rank:** >10
- **Top-1 retrieved (08_config):** /extDiff #!/bin/sh [ $# -eq 7 ] && /usr/local/bin/extMerge "$2" "$5" You also need to make sure these tools are executable: $ sudo chmod +x /usr/local/bin/extMerge $ sudo chmod +x /usr/local/bin/extDiff Now you can set up your config file …

## fixed 200 - q178: wrong document

- **Question:** Which plumbing command loads another branch's top-level tree into your index and working files?
- **Evidence (07_subtree-merges):** You'll learn more about read-tree and its friends in ch10-git-internals#ch10-git-internals, but for now know that it reads the root tree of one branch into your current staging area and working directory.
- **First relevant rank:** >10
- **Top-1 retrieved (07_reset):** , which is more of a behind the scenes command that shows you what your index currently looks like. The index is not technically a tree structure -- it's actually implemented as a flattened manifest -- but for our purposes it's close enoug…

## fixed 200 - q179: wrong document

- **Question:** Which two settings bring the vendored project's updates across with a ready-made commit message?
- **Evidence (07_subtree-merges):** To pull in the changes and prepopulate the commit message, use the --squash option, as well as the recursive merge strategy's -Xsubtree option.
- **First relevant rank:** >10
- **Top-1 retrieved (05_contributing):** "Fixed bug" or "Fixes bug." This convention matches up with commit messages generated by commands like git merge and git revert. Further paragraphs come after blank lines. - Bullet points are okay, too - Typically a hyphen or asterisk is u…

## fixed 200 - q183: wrong document

- **Question:** In what time unit is the numeric value of the mistyped-command correction delay expressed?
- **Evidence (08_config):** help.autocorrect is actually an integer which represents tenths of a second.
- **First relevant rank:** 9
- **Top-1 retrieved (07_debugging):** = 066b7ed955808 (Michal Marek 2014-07-04 14:29:30 +0200 79) else 066b7ed955808 (Michal Marek 2014-07-04 14:29:30 +0200 80) quiet=quiet_ 066b7ed955808 (Michal Marek 2014-07-04 14:29:30 +0200 81) Q = @ 066b7ed955808 (Michal Marek 2014-07-04 …

## fixed 200 - q184: wrong document

- **Question:** Which configuration file is consulted first, and whose repositories does it affect?
- **Evidence (08_config):** The first place Git looks for these values is in the system-wide [path]/etc/gitconfig file, which contains settings that are applied to every user on the system and all of their repositories.
- **First relevant rank:** >10
- **Top-1 retrieved (01_first-time-setup):** First-Time Git Setup Now that you have Git on your system, you'll want to do a few things to customize your Git environment. You should have to do these things only once on any given computer; they'll stick around between upgrades. You can…

## fixed 200 - q191: right document, wrong passage

- **Question:** Where does text printed by a server-side enforcement script end up?
- **Evidence (08_policy):** Anything your script echoes to stdout will be transferred to the client.
- **First relevant rank:** >10
- **Top-1 retrieved (08_policy):** An Example Git-Enforced Policy In this section, you'll use what you've learned to establish a Git workflow that checks for a custom commit message format, and allows only certain users to modify certain subdirectories in a project. You'll …

## fixed 200 - q192: right document, wrong passage

- **Question:** What combination of thresholds makes Git give up on a sluggish HTTP transfer?
- **Evidence (10_environment):** If the data rate of an HTTP operation is lower than GIT_HTTP_LOW_SPEED_LIMIT bytes per second for longer than GIT_HTTP_LOW_SPEED_TIME seconds, Git will abort that operation.
- **First relevant rank:** >10
- **Top-1 retrieved (10_environment):** .git/objects/pack/.tmp-49190-pack' 20:18:23.584728 trace.c:414 performance: 0.000910000 s: git command: 'git' 'prune-packed' 20:18:23.605218 trace.c:414 performance: 0.017972000 s: git command: 'git' 'update-server-info' 20:18:23.606342 tr…

## fixed 200 - q195: right document, wrong passage

- **Question:** How many unpacked objects or how many pack files does it take before the automatic cleanup actually does work?
- **Evidence (10_maintenance):** You must have around 7,000 loose objects or more than 50 packfiles for Git to fire up a real gc command.
- **First relevant rank:** 7
- **Top-1 retrieved (10_maintenance):** gc Counting objects: 17, done. Delta compression using up to 8 threads. Compressing objects: 100% (13/13), done. Writing objects: 100% (17/17), done. Total 17 (delta 1), reused 10 (delta 0) You can run the count-objects command to quickly …

## fixed 200 - q198: right document, wrong passage

- **Question:** How is the on-disk path of a stored object split up between folder name and file name?
- **Evidence (10_objects):** The subdirectory is named with the first 2 characters of the SHA-1, and the filename is the remaining 38 characters.
- **First relevant rank:** >10
- **Top-1 retrieved (10_objects):** be processed from stdin; otherwise, the command would expect a filename argument at the end of the command containing the content to be used. The output from the above command is a 40-character checksum hash. This is the SHA-1 hash -- a ch…

## fixed 200 - q201: wrong document

- **Question:** Besides the automatic repacking Git performs on its own, how can someone trigger a repack deliberately?
- **Evidence (10_packfiles):** Git will occasionally repack your database automatically, always trying to save more space, but you can also manually repack at any time by running git gc by hand.
- **First relevant rank:** >10
- **Top-1 retrieved (08_policy):** Because hooks aren't transferred with a clone of a project, you must distribute these scripts some other way and then have your users copy them to their .git/hooks directory and make them executable. You can distribute these hooks within t…

## fixed 200 - q203: wrong document

- **Question:** What similarity does Git look for between objects when deciding which ones to store as differences?
- **Evidence (10_packfiles):** When Git packs objects, it looks for files that are named and sized similarly, and stores just the deltas from one version of the file to the next.
- **First relevant rank:** >10
- **Top-1 retrieved (01_what-is-git):** CVS, Subversion, Perforce, and so on) think of the information they store as a set of files and the changes made to each file over time (this is commonly described as delta-based version control). Storing data as changes to a base version …

## fixed 200 - q208: right document, wrong passage

- **Question:** What does HEAD normally hold, and how does that differ from an ordinary ref?
- **Evidence (10_refs):** Usually the HEAD file is a symbolic reference to the branch you're currently on. By symbolic reference, we mean that unlike a normal reference, it contains a pointer to another reference.
- **First relevant rank:** >10
- **Top-1 retrieved (10_refs):** -ref HEAD refs/heads/test $ cat .git/HEAD ref: refs/heads/test You can't set a symbolic reference outside of the refs style: $ git symbolic-ref HEAD test fatal: Refusing to point HEAD outside of refs/ Tags We just finished discussing Git's…

## fixed 200 - q210: wrong document

- **Question:** What does the leading plus sign in front of a mapping authorise Git to do?
- **Evidence (10_refspec):** The + tells Git to update the reference even if it isn't a fast-forward.
- **First relevant rank:** 8
- **Top-1 retrieved (02_aliases):** 3329c7aebe598c2246a8e6af90d04646 Author: Josh Goebel <dreamer3@example.com> Date: Tue Aug 26 19:48:51 2008 +0800 Test for current head Signed-off-by: Scott Chacon <schacon@example.com> As you can tell, Git simply replaces the new command w…

## fixed 200 - q212: wrong document

- **Question:** Why does pushing with nothing before the colon wipe out a branch upstream?
- **Evidence (10_refspec):** Because the refspec is <src>:<dst>, by leaving off the <src> part, this basically says to make the topic branch on the remote nothing, which deletes it.
- **First relevant rank:** >10
- **Top-1 retrieved (06_2-contributing):** push it back up to the same branch you opened the Pull Request on. For example, let's say that in the "tonychacon" example we were using before, the original author made a change that would create a conflict in the Pull Request. Let's go t…

## sentence 200 - q005: wrong document

- **Question:** Which kind of Git interface can I count on every user already having?
- **Evidence (01_command-line):** all users will have the command-line tools installed and available.
- **First relevant rank:** >10
- **Top-1 retrieved (05_contributing):** Contributing to a Project The main difficulty with describing how to contribute to a project are the numerous variations on how to do that. Because Git is very flexible, people can and do work together in many ways, and it's problematic to…

## sentence 200 - q012: wrong document

- **Question:** Which flag prints a brief list of a command's options instead of the whole manual?
- **Evidence (01_help):** In addition, if you don't need the full-blown manpage help, but just need a quick refresher on the available options for a Git command, you can ask for the more concise "help" output with the -h option, as in:
- **First relevant rank:** 10
- **Top-1 retrieved (08_config):** If your team has a commit-message policy, then putting a template for that policy on your system and configuring Git to use it by default can help increase the chance of that policy being followed regularly. `core.pager` This setting deter…

## sentence 200 - q019: wrong document

- **Question:** Do everyday Git commands have to reach another machine to do their work?
- **Evidence (01_what-is-git):** Most operations in Git need only local files and resources to operate -- generally no information is needed from another computer on your network.
- **First relevant rank:** >10
- **Top-1 retrieved (04_setting-up-server):** If you're running it internally, and you set up DNS for gitserver to point to that server, then you can use the commands pretty much as is (assuming that myproject is an existing project with files in it): # on John's computer $ cd myproje…

## sentence 200 - q021: wrong document

- **Question:** Where does Git keep the record of what is queued up for the next commit?
- **Evidence (01_what-is-git):** The staging area is a file, generally contained in your Git directory, that stores information about what will go into your next commit.
- **First relevant rank:** >10
- **Top-1 retrieved (03_nutshell):** Your Git repository now contains five objects: three blobs (each representing the contents of one of the three files), one tree that lists the contents of the directory and specifies which file names are stored as which blobs, and one comm…

## sentence 200 - q028: wrong document

- **Question:** I edited a file again after staging it; what do I have to do before committing?
- **Evidence (02_recording-changes):** If you modify a file after you run git add, you have to run git add again to stage the latest version of the file:
- **First relevant rank:** >10
- **Top-1 retrieved (02_undoing):** The obvious value to amending commits is to make minor improvements to your last commit, without cluttering your repository history with commit messages of the form, "Oops, forgot to add a file" or "Darn, fixing a typo in last commit". Onl…

## sentence 200 - q030: wrong document

- **Question:** Which files in my working directory does Git consider untracked?
- **Evidence (02_recording-changes):** Untracked files are everything else -- any files in your working directory that were not in your last snapshot and are not in your staging area.
- **First relevant rank:** 10
- **Top-1 retrieved (07_stashing-cleaning):** To remove all the untracked files in your working directory, you can run git clean -f -d, which removes any files and also any subdirectories that become empty as a result. The -f means 'force' or "really do this," and is required if the G…

## sentence 200 - q031: wrong document

- **Question:** Besides downloading new commits, what else does pulling do?
- **Evidence (02_remotes):** Running git pull generally fetches data from the server you originally cloned from and automatically tries to merge it into the code you're currently working on.
- **First relevant rank:** 6
- **Top-1 retrieved (03_remote-branches):** While the git fetch command will fetch all the changes on the server that you don't have yet, it will not modify your working directory at all. It will simply get the data for you and let you merge it yourself. However, there is a command …

## sentence 200 - q039: right document, wrong passage

- **Question:** Which Git release brought in a dedicated command for undoing file changes?
- **Evidence (02_undoing):** Git version 2.23.0 introduced a new command: git restore. It's basically an alternative to git reset which we just covered.
- **First relevant rank:** 7
- **Top-1 retrieved (02_undoing):** (use "git reset HEAD <file>..." to unstage) renamed: README.md -> README Changes not staged for commit: (use "git add <file>..." to update what will be committed) (use "git checkout -- <file>..." to discard changes in working directory) mo…

## sentence 200 - q044: wrong document

- **Question:** Which snapshots are combined when the current commit is not a direct ancestor of the branch being brought in?
- **Evidence (03_basic-branching-and-merging):** Git does a simple three-way merge, using the two snapshots pointed to by the branch tips and the common ancestor of the two.
- **First relevant rank:** >10
- **Top-1 retrieved (05_contributing):** The end snapshot should be identical no matter which order she chooses; only the history will be different. She chooses to merge the issue54 branch first: $ git merge issue54 Updating fbff5bc..4af4298 Fast forward README | 1 + lib/simplegi…

## sentence 200 - q050: wrong document

- **Question:** Whose history does the log command display if you give it no extra arguments?
- **Evidence (03_nutshell):** by default, git log will only show commit history below the branch you've checked out.
- **First relevant rank:** >10
- **Top-1 retrieved (07_searching):** If, for example, we want to find out when the ZLIB_BUF_MAX constant was originally introduced, we can use the -S option (colloquially referred to as the Git "pickaxe" option) to tell Git to show us only those commits that changed the numbe…

## sentence 200 - q057: right document, wrong passage

- **Question:** What do local pointers such as origin/master actually stand for?
- **Evidence (03_remote-branches):** Remote-tracking branches are references to the state of remote branches.
- **First relevant rank:** >10
- **Top-1 retrieved (03_remote-branches):** ."origin" is not special Just like the branch name "master" does not have any special meaning in Git, neither does "origin". While "master" is the default name for a starting branch when you run git init which is the only reason it's widel…

## sentence 200 - q058: right document, wrong passage

- **Question:** Is any network traffic involved while you create branches and combine them?
- **Evidence (03_workflows):** When you're branching and merging, everything is being done only in your Git repository -- there is no communication with the server.
- **First relevant rank:** >10
- **Top-1 retrieved (03_workflows):** Branching Workflows Now that you have the basics of branching and merging down, what can or should you do with them? In this section, we'll cover some common workflows that this lightweight branching makes possible, so you can decide if yo…

## sentence 200 - q067: right document, wrong passage

- **Question:** What gives a developer the ability to send commits up, once they can log in over SSH?
- **Evidence (04_git-on-a-server):** If a user SSHs into a server and has write access to the /srv/git/my_project.git directory, they will also automatically have push access.
- **First relevant rank:** >10
- **Top-1 retrieved (04_git-on-a-server):** You may not want to run adduser (or the possible alternative useradd) and have to set temporary passwords for every new user. A second method is to create a single 'git' user account on the machine, ask every user who is to have write acce…

## sentence 200 - q075: wrong document

- **Question:** Which setting tells the build where your repositories live when generating the script?
- **Evidence (04_gitweb):** Notice that you have to tell the command where to find your Git repositories with the GITWEB_PROJECTROOT variable.
- **First relevant rank:** >10
- **Top-1 retrieved (10_environment):** Environment Variables Git always runs inside a bash shell, and uses a number of shell environment variables to determine how it behaves. Occasionally, it comes in handy to know what these are, and how they can be used to make Git behave th…

## sentence 200 - q081: right document, wrong passage

- **Question:** What is the drawback of serving a project only over Secure Shell?
- **Evidence (04_protocols):** The negative aspect of SSH is that it doesn't support anonymous access to your Git repository.
- **First relevant rank:** 10
- **Top-1 retrieved (04_protocols):** It uses the same data-transfer mechanism as the SSH protocol but without the encryption and authentication overhead. The Cons Due to the lack of TLS or other cryptography, cloning over git:// might lead to an arbitrary code execution vulne…

## sentence 200 - q083: wrong document

- **Question:** What has to be done on the machine itself each time a new project should be hosted?
- **Evidence (04_setting-up-server):** Note that someone must shell onto the machine and create a bare repository every time you want to add a project.
- **First relevant rank:** >10
- **Top-1 retrieved (06_3-maintaining):** Maintaining a Project Now that we're comfortable contributing to a project, let's look at the other side: creating, maintaining and administering your own project. Creating a New Repository Let's create a new repository to share our projec…

## sentence 200 - q084: wrong document

- **Question:** Which bundled tool keeps a shared account confined to version-control operations?
- **Evidence (04_setting-up-server):** You can easily restrict the git user account to only Git-related activities with a limited shell tool called git-shell that comes with Git.
- **First relevant rank:** >10
- **Top-1 retrieved (05_distributed-workflows):** This is a very common workflow with hub-based tools like GitHub or GitLab, where it's easy to fork a project and push your changes into your fork for everyone to see. One of the main advantages of this approach is that you can continue to …

## sentence 200 - q087: wrong document

- **Question:** Why does the group ownership of the repository directories need changing?
- **Evidence (04_smart-http):** You'll also need to set the Unix user group of the /srv/git directories to www-data so your web server can read- and write-access the repositories
- **First relevant rank:** >10
- **Top-1 retrieved (06_4-managing-organization):** Follow these steps and you'll soon be the owner of a brand-new organization. Like personal accounts, organizations are free if everything you plan to store there will be open source. As an owner in an organization, when you fork a reposito…

## sentence 200 - q091: right document, wrong passage

- **Question:** Why must a force flag be added when pushing a topic branch whose history you have just rewritten with a rebase?
- **Evidence (05_contributing):** Because you rebased the branch, you have to specify the -f to your push command in order to be able to replace the featureA branch on the server with a commit that isn't a descendant of it.
- **First relevant rank:** >10
- **Top-1 retrieved (05_contributing):** On a project for which you're not the maintainer, it's generally easier to have a branch like master always track origin/master and to do your work in topic branches that you can easily discard if they're rejected. Having work themes isola…

## sentence 200 - q101: wrong document

- **Question:** What piece of information does GitHub use to attribute a commit to a particular member?
- **Evidence (06_1-setting-up-account):** The way that GitHub maps your Git commits to your user is by email address.
- **First relevant rank:** >10
- **Top-1 retrieved (02_viewing-history):** So, if you send in a patch to a project and one of the core members applies the patch, both of you get credit -- you as the author, and the core member as the committer. We'll cover this distinction a bit more in ch05-distributed-git#ch05-…

## sentence 200 - q103: wrong document

- **Question:** Why is it worth giving each uploaded public key a label such as the machine it belongs to?
- **Evidence (06_1-setting-up-account):** You can name each of your keys (e.g. "My Laptop" or "Work Account") so that if you need to revoke a key later, you can easily tell which one you're looking for.
- **First relevant rank:** >10
- **Top-1 retrieved (05_maintaining):** If you do sign your tags, you may have the problem of distributing the public PGP key used to sign your tags. The maintainer of the Git project has solved this issue by including their public key as a blob in the repository and then adding…

## sentence 200 - q124: wrong document

- **Question:** Does Git work out automatically which refs belong in a bundle, or must I enumerate them?
- **Evidence (07_bundling):** With the bundle command you need to list out every reference or specific range of commits that you want to be included.
- **First relevant rank:** >10
- **Top-1 retrieved (06_3-maintaining):** That last line tells Git, "All the refs that look like refs/pull/123/head should be stored locally like refs/remotes/origin/pr/123." Now, if you save that file, and do a git fetch: $ git fetch # … * [new ref] refs/pull/1/head -> origin/pr/…

## sentence 200 - q126: wrong document

- **Question:** What goes wrong if someone packages only their newest couple of commits and the receiving repository lacks the earlier ones?
- **Evidence (07_bundling):** If the bundler had created a bundle of just the last two commits they had done, rather than all three, the original repository would not be able to import it, since it is missing requisite history.
- **First relevant rank:** 8
- **Top-1 retrieved (07_debugging):** If it does, then it was introduced sometime before this middle commit; if it doesn't, then the problem was introduced sometime after the middle commit. It turns out there is no issue here, and you tell Git that by typing git bisect good an…

## sentence 200 - q129: wrong document

- **Question:** If more than one helper is configured, which one's answer does Git end up using for a given host?
- **Evidence (07_credentials):** When looking for credentials for a particular host, Git will query them in order, and stop after the first answer is provided.
- **First relevant rank:** >10
- **Top-1 retrieved (04_hosted):** Third Party Hosted Options If you don't want to go through all of the work involved in setting up your own Git server, you have several options for hosting your Git projects on an external dedicated hosting site. Doing so offers a number o…

## sentence 200 - q130: right document, wrong passage

- **Question:** Which credential helper ships with Git on Apple machines, and where does it keep the secrets?
- **Evidence (07_credentials):** If you're using macOS, Git comes with an "osxkeychain" mode, which caches credentials in the secure keychain that's attached to your system account.
- **First relevant rank:** 10
- **Top-1 retrieved (07_credentials):** It's just a series of lines, each of which contains a credential-decorated URL. The osxkeychain and wincred helpers use the native format of their backing stores, while cache uses its own in-memory format (which no other process can read).…

## sentence 200 - q132: wrong document

- **Question:** After tracking down the faulty revision, what command returns me to the checkout I had beforehand?
- **Evidence (07_debugging):** When you're finished, you should run git bisect reset to reset your HEAD to where you were before you started, or you'll end up in a weird state
- **First relevant rank:** >10
- **Top-1 retrieved (02_undoing):** It tells you pretty explicitly how to discard the changes you've made. Let's do what it says: $ git checkout -- CONTRIBUTING.md $ git status On branch master Changes to be committed: (use "git reset HEAD <file>..." to unstage) renamed: REA…

## sentence 200 - q138: right document, wrong passage

- **Question:** Which menu choice displays the changes already added to the staging area?
- **Evidence (07_interactive-staging):** To see the diff of what you've staged, you can use the d or 6 (for diff) command.
- **First relevant rank:** 8
- **Top-1 retrieved (07_interactive-staging):** 1: [s]tatus 2: [u]pdate 3: [r]evert 4: [a]dd untracked 5: [p]atch 6: [d]iff 7: [q]uit 8: [h]elp What now> You can see that this command shows you a much different view of your staging area than you're probably used to -- basically, the sam…

## sentence 200 - q139: wrong document

- **Question:** Which two command-line switches make the add command open its menu-driven prompt?
- **Evidence (07_interactive-staging):** If you run git add with the -i or --interactive option, Git enters an interactive shell mode, displaying something like this
- **First relevant rank:** 9
- **Top-1 retrieved (08_config):** If you're programming on Windows and working with people who are not (or vice-versa), you'll probably run into line-ending issues at some point. This is because Windows uses both a carriage-return character and a linefeed character for new…

## sentence 200 - q142: right document, wrong passage

- **Question:** When joining a short recent history to a long archived one, which two commits do you pair up?
- **Evidence (07_replace):** You can graft one history onto the other by "replacing" the earliest commit in the new line with the latest commit on the older one.
- **First relevant rank:** >10
- **Top-1 retrieved (07_replace):** This is nice because it means that you don't actually have to rewrite every commit in the new history, as you would normally have to do to join them together (because the parentage affects the SHA-1s). Let's try this out. Let's take an exi…

## sentence 200 - q143: right document, wrong passage

- **Question:** Which low-level command turns a tree into a fresh commit object that has no parent?
- **Evidence (07_replace):** We can create our base commit using the commit-tree command, which just takes a tree and will give us a brand new, parentless commit object SHA-1 back.
- **First relevant rank:** 10
- **Top-1 retrieved (07_replace):** $ echo 'Get history from blah blah blah' | git commit-tree 9c68fdc^{tree} 622e88e9cbfbacfb75b5279245b9fb38dfea10cf ===== The commit-tree command is one of a set of commands that are commonly referred to as 'plumbing' commands. These are co…

## sentence 200 - q144: wrong document

- **Question:** Apart from the config flag, which directory can I create inside one repository to switch the feature on there?
- **Evidence (07_rerere):** You can also turn it on by creating the .git/rr-cache directory in a specific repository, but the config setting is clearer and enables that feature globally for you.
- **First relevant rank:** >10
- **Top-1 retrieved (10_plumbing-porcelain):** Many of these commands aren't meant to be used manually on the command line, but rather to be used as building blocks for new tools and custom scripts. When you run git init in a new or existing directory, Git creates the .git directory, w…

## sentence 200 - q145: wrong document

- **Question:** What repeated routine lets a long-lived topic branch stay mergeable without littering history with interim merge commits?
- **Evidence (07_rerere):** With rerere enabled, you can attempt the occasional merge, resolve the conflicts, then back out of the merge.
- **First relevant rank:** >10
- **Top-1 retrieved (05_contributing):** Now, each of your topics is contained within a silo -- similar to a patch queue -- that you can rewrite, rebase, and modify without the topics interfering or interdepending on each other, like so: Initial commit history with featureB work …

## sentence 200 - q146: wrong document

- **Question:** What three words is the odd-looking name of Git's conflict-memory feature short for?
- **Evidence (07_rerere):** The name stands for "reuse recorded resolution" and, as the name implies, it allows you to ask Git to remember how you've resolved a hunk conflict
- **First relevant rank:** 7
- **Top-1 retrieved (07_advanced-merging):** This can be useful if you want to reset the markers and try to resolve them again. You can pass --conflict either diff3 or merge (which is the default). If you pass it diff3, Git will use a slightly different version of conflict markers, n…

## sentence 200 - q148: right document, wrong passage

- **Question:** Between resetting and checking out a branch, which one relocates the branch pointer and which relocates HEAD?
- **Evidence (07_reset):** Whereas reset will move the branch that HEAD points to, checkout will move HEAD itself to point to another branch.
- **First relevant rank:** >10
- **Top-1 retrieved (07_reset):** HEAD will now point to master. So, in both cases we're moving HEAD to point to commit A, but how we do so is very different. reset will move the branch HEAD points to, checkout moves HEAD itself. git checkout and git reset With Paths The o…

## sentence 200 - q150: right document, wrong passage

- **Question:** Which of the three usual stages is omitted when a filename is handed to the reset command?
- **Evidence (07_reset):** If you specify a path, reset will skip step 1, and limit the remainder of its actions to a specific file or set of files.
- **First relevant rank:** >10
- **Top-1 retrieved (07_reset):** | reset [commit] | REF | YES | NO | YES | reset --hard [commit] | REF | YES | YES | NO | checkout <commit> | HEAD | YES | YES | YES | File Level | | | | | reset [commit] <paths> | NO | YES | NO | YES | checkout [commit] <paths> | NO | YES …

## sentence 200 - q152: right document, wrong passage

- **Question:** How far back does Git's background record of where HEAD and branch tips have pointed normally reach?
- **Evidence (07_revision-selection):** One of the things Git does in the background while you're working away is keep a "reflog" -- a log of where your HEAD and branch references have been for the last few months.
- **First relevant rank:** 8
- **Top-1 retrieved (07_revision-selection):** 95df984 HEAD@{4}: commit: # This is a combination of two commits. 1c36188 HEAD@{5}: rebase -i (squash): updating HEAD 7e05da5 HEAD@{6}: rebase -i (pick): updating HEAD Every time your branch tip is updated for any reason, Git stores that i…

## sentence 200 - q166: right document, wrong passage

- **Question:** Which configuration entry records which GPG key Git should reach for when it signs things?
- **Evidence (07_signing):** Once you have a private key to sign with, you can configure Git to use it for signing things by setting the user.signingkey config setting.
- **First relevant rank:** 9
- **Top-1 retrieved (07_signing):** To see and verify these signatures, there is also a --show-signature option to git log. $ git log --show-signature -1 commit 5c3386cf54bba0a33a32da706aa52bc0155503c2 gpg: Signature made Wed Jun 4 19:49:17 2014 PDT using RSA key ID 0A46826A…

## sentence 200 - q168: right document, wrong passage

- **Question:** Since -u still skips files matched by ignore rules, what flag sweeps those in as well?
- **Evidence (07_stashing-cleaning):** including untracked files in the stash will still not include explicitly ignored files; to additionally include ignored files, use --all (or just -a).
- **First relevant rank:** 7
- **Top-1 retrieved (07_stashing-cleaning):** To remove all the untracked files in your working directory, you can run git clean -f -d, which removes any files and also any subdirectories that become empty as a result. The -f means 'force' or "really do this," and is required if the G…

## sentence 200 - q172: right document, wrong passage

- **Question:** What argument to clone fills in every subproject, including ones nested inside them, without extra steps?
- **Evidence (07_submodules):** If you pass --recurse-submodules to the git clone command, it will automatically initialize and update each submodule in the repository, including nested submodules if any of the submodules in the repository have submodules themselves.
- **First relevant rank:** 6
- **Top-1 retrieved (07_submodules):** That is a special mode in Git that basically means you're recording a commit as a directory entry rather than a subdirectory or a file. Lastly, push these changes: $ git push origin master Cloning a Project with Submodules Here we'll clone…

## sentence 200 - q175: right document, wrong passage

- **Question:** Why can work you commit inside a subproject vanish when the superproject later refreshes it?
- **Evidence (07_submodules):** With no working branch tracking changes, that means even if you commit changes to the submodule, those changes will quite possibly be lost the next time you run git submodule update.
- **First relevant rank:** 10
- **Top-1 retrieved (07_submodules):** This can happen for example if the submodule project changes its hosting platform. In that case, it is possible for git pull --recurse-submodules, or git submodule update, to fail if the superproject references a submodule commit that is n…

## sentence 200 - q178: wrong document

- **Question:** Which plumbing command loads another branch's top-level tree into your index and working files?
- **Evidence (07_subtree-merges):** You'll learn more about read-tree and its friends in ch10-git-internals#ch10-git-internals, but for now know that it reads the root tree of one branch into your current staging area and working directory.
- **First relevant rank:** 6
- **Top-1 retrieved (07_reset):** 100644 47c6340d6459e05787f644c2447d2595f5d3a54b 0 lib/simplegit.rb Again, here we're using git ls-files, which is more of a behind the scenes command that shows you what your index currently looks like. The index is not technically a tree …

## sentence 200 - q179: wrong document

- **Question:** Which two settings bring the vendored project's updates across with a ready-made commit message?
- **Evidence (07_subtree-merges):** To pull in the changes and prepopulate the commit message, use the --squash option, as well as the recursive merge strategy's -Xsubtree option.
- **First relevant rank:** >10
- **Top-1 retrieved (08_hooks):** The prepare-commit-msg hook is run before the commit message editor is fired up but after the default message is created. It lets you edit the default message before the commit author sees it. This hook takes a few parameters: the path to …

## sentence 200 - q182: wrong document

- **Question:** Why might a content filter that works for you break for a colleague who clones the same project?
- **Evidence (08_attributes):** You have to be careful, though, because the .gitattributes file is committed and passed around with the project, but the driver (in this case, dater) isn't, so it won't work everywhere.
- **First relevant rank:** >10
- **Top-1 retrieved (05_distributed-workflows):** To contribute to that project, you create your own public clone of the project and push your changes to it. Then, you can send a request to the maintainer of the main project to pull in your changes. The maintainer can then add your reposi…

## sentence 200 - q183: wrong document

- **Question:** In what time unit is the numeric value of the mistyped-command correction delay expressed?
- **Evidence (08_config):** help.autocorrect is actually an integer which represents tenths of a second.
- **First relevant rank:** 8
- **Top-1 retrieved (06_2-contributing):** [-delay(1000);-]{+delay(3000);+} // wait for a second } $ git commit -a -m 'Change delay to 3 seconds' <5> [slow-blink 5ca509d] Change delay to 3 seconds 1 file changed, 2 insertions(+), 2 deletions(-) $ git push origin slow-blink <6> User…

## sentence 200 - q184: wrong document

- **Question:** Which configuration file is consulted first, and whose repositories does it affect?
- **Evidence (08_config):** The first place Git looks for these values is in the system-wide [path]/etc/gitconfig file, which contains settings that are applied to every user on the system and all of their repositories.
- **First relevant rank:** 10
- **Top-1 retrieved (01_first-time-setup):** First-Time Git Setup Now that you have Git on your system, you'll want to do a few things to customize your Git environment. You should have to do these things only once on any given computer; they'll stick around between upgrades. You can…

## sentence 200 - q191: right document, wrong passage

- **Question:** Where does text printed by a server-side enforcement script end up?
- **Evidence (08_policy):** Anything your script echoes to stdout will be transferred to the client.
- **First relevant rank:** >10
- **Top-1 retrieved (08_policy):** if !$regex.match(message) puts "[POLICY] Your message is not formatted correctly" exit 1 end end end check_message_format Putting that in your update script will reject updates that contain commits that have messages that don't adhere to y…

## sentence 200 - q194: wrong document

- **Question:** Which variable supplies fallback locations to search when an object is missing from the main object store?
- **Evidence (10_environment):** GIT_ALTERNATE_OBJECT_DIRECTORIES is a colon-separated list (formatted like /dir/one:/dir/two:…) which tells Git where to check for objects if they aren't in GIT_OBJECT_DIRECTORY.
- **First relevant rank:** >10
- **Top-1 retrieved (10_transfer-protocols):** => GET objects/cf/da3bf379e4f8dba8717dee55aab78aef7f4daf (404 - Not Found) Oops – it looks like that tree object isn't in loose format on the server, so you get a 404 response back. There are a couple of reasons for this – the object could…

## sentence 200 - q195: wrong document

- **Question:** How many unpacked objects or how many pack files does it take before the automatic cleanup actually does work?
- **Evidence (10_maintenance):** You must have around 7,000 loose objects or more than 50 packfiles for Git to fire up a real gc command.
- **First relevant rank:** >10
- **Top-1 retrieved (10_packfiles):** The objects that remain are the blobs that aren't pointed to by any commit -- in this case, the "what is up, doc?" example and the "test content" example blobs you created earlier. Because you never added them to any commits, they're consi…

## sentence 200 - q198: right document, wrong passage

- **Question:** How is the on-disk path of a stored object split up between folder name and file name?
- **Evidence (10_objects):** The subdirectory is named with the first 2 characters of the SHA-1, and the filename is the remaining 38 characters.
- **First relevant rank:** >10
- **Top-1 retrieved (10_objects):** These three main Git objects -- the blob, the tree, and the commit -- are initially stored as separate files in your .git/objects directory. Here are all the objects in the example directory now, commented with what they store: $ find .git…

## sentence 200 - q199: wrong document

- **Question:** Is an object's checksum computed over its payload alone, or over something more?
- **Evidence (10_objects):** Git concatenates the header and the original content and then calculates the SHA-1 checksum of that new content.
- **First relevant rank:** >10
- **Top-1 retrieved (08_config):** Git is capable of making sure every object received during a push still matches its SHA-1 checksum and points to valid objects. However, it doesn't do this by default; it's a fairly expensive operation, and might slow down the operation, e…

## sentence 200 - q201: wrong document

- **Question:** Besides the automatic repacking Git performs on its own, how can someone trigger a repack deliberately?
- **Evidence (10_packfiles):** Git will occasionally repack your database automatically, always trying to save more space, but you can also manually repack at any time by running git gc by hand.
- **First relevant rank:** >10
- **Top-1 retrieved (08_hooks):** It receives the name and location of the remote as parameters, and a list of to-be-updated refs through stdin. You can use it to validate a set of ref updates before a push occurs (a non-zero exit code will abort the push). Git occasionall…

## sentence 200 - q209: wrong document

- **Question:** Which pieces of data live inside a tag object, and which other object type is it closest to?
- **Evidence (10_refs):** The tag object is very much like a commit object -- it contains a tagger, a date, a message, and a pointer.
- **First relevant rank:** >10
- **Top-1 retrieved (10_objects):** git/objects/fa/49b077972391ad58037050f2a75f74e3671e92 # new.txt git/objects/fd/f4fc3344e67ab068f836878b6c4951e3b15f3d # commit 1 If you follow all the internal pointers, you get an object graph something like this: All the reachable object…

## sentence 200 - q210: wrong document

- **Question:** What does the leading plus sign in front of a mapping authorise Git to do?
- **Evidence (10_refspec):** The + tells Git to update the reference even if it isn't a fast-forward.
- **First relevant rank:** >10
- **Top-1 retrieved (02_aliases):** commit 66938dae3329c7aebe598c2246a8e6af90d04646 Author: Josh Goebel <dreamer3@example.com> Date: Tue Aug 26 19:48:51 2008 +0800 Test for current head Signed-off-by: Scott Chacon <schacon@example.com> As you can tell, Git simply replaces th…

## recursive 200 - q005: wrong document

- **Question:** Which kind of Git interface can I count on every user already having?
- **Evidence (01_command-line):** all users will have the command-line tools installed and available.
- **First relevant rank:** >10
- **Top-1 retrieved (07_credentials):** Git even allows you to configure several helpers. When looking for credentials for a particular host, Git will query them in order, and stop after the first answer is provided. When saving credentials, Git will send the username and passwo…

## recursive 200 - q008: wrong document

- **Question:** What is a brand new repository's first branch named if I never configure it?
- **Evidence (01_first-time-setup):** By default Git will create a branch called master when you create a new repository with git init.
- **First relevant rank:** >10
- **Top-1 retrieved (02_recording-changes):** GitHub changed the default branch name from master to main in mid-2020, and other Git hosts followed suit. So you may find that the default branch name in some newly created repositories is main and not master. In addition, the default bra…

## recursive 200 - q021: wrong document

- **Question:** Where does Git keep the record of what is queued up for the next commit?
- **Evidence (01_what-is-git):** The staging area is a file, generally contained in your Git directory, that stores information about what will go into your next commit.
- **First relevant rank:** >10
- **Top-1 retrieved (10_objects):** Amazing. You've just done the low-level operations to build up a Git history without using any of the front end commands. This is essentially what Git does when you run the git add and git commit commands -- it stores blobs for the files t…

## recursive 200 - q022: wrong document

- **Question:** How do I make a shortcut launch a program that isn't part of Git?
- **Evidence (02_aliases):** maybe you want to run an external command, rather than a Git subcommand. In that case, you start the command with a ! character.
- **First relevant rank:** >10
- **Top-1 retrieved (07_interactive-staging):** It's also possible for Git to stage certain parts of files and not the rest. For example, if you make two changes to your simplegit.rb file and want to stage one of them and not the other, doing so is very easy in Git. From the same intera…

## recursive 200 - q026: wrong document

- **Question:** Can I choose a target folder name that differs from the project's own?
- **Evidence (02_getting-a-repository):** If you want to clone the repository into a directory named something other than libgit2, you can specify the new directory name as an additional argument:
- **First relevant rank:** >10
- **Top-1 retrieved (02_recording-changes):** Often, you'll have a class of files that you don't want Git to automatically add or even show you as being untracked. These are generally automatically generated files such as log files or files produced by your build system. In such cases…

## recursive 200 - q028: right document, wrong passage

- **Question:** I edited a file again after staging it; what do I have to do before committing?
- **Evidence (02_recording-changes):** If you modify a file after you run git add, you have to run git add again to stage the latest version of the file:
- **First relevant rank:** >10
- **Top-1 retrieved (02_recording-changes):** Now that your staging area is set up the way you want it, you can commit your changes. Remember that anything that is still unstaged -- any files you have created or modified that you haven't run git add on since you edited them -- won't g…

## recursive 200 - q031: wrong document

- **Question:** Besides downloading new commits, what else does pulling do?
- **Evidence (02_remotes):** Running git pull generally fetches data from the server you originally cloned from and automatically tries to merge it into the code you're currently working on.
- **First relevant rank:** 7
- **Top-1 retrieved (03_remote-branches):** While the git fetch command will fetch all the changes on the server that you don't have yet, it will not modify your working directory at all. It will simply get the data for you and let you merge it yourself. However, there is a command …

## recursive 200 - q039: right document, wrong passage

- **Question:** Which Git release brought in a dedicated command for undoing file changes?
- **Evidence (02_undoing):** Git version 2.23.0 introduced a new command: git restore. It's basically an alternative to git reset which we just covered.
- **First relevant rank:** >10
- **Top-1 retrieved (02_undoing):** ===== It's important to understand that git checkout \-- <file> is a dangerous command. Any local changes you made to that file are gone -- Git just replaced that file with the last staged or committed version. Don't ever use this command …

## recursive 200 - q045: right document, wrong passage

- **Question:** Why was no new snapshot needed when the hotfix work was integrated back into master?
- **Evidence (03_basic-branching-and-merging):** Because the commit C4 pointed to by the branch hotfix you merged in was directly ahead of the commit C2 you're on, Git simply moves the pointer forward.
- **First relevant rank:** >10
- **Top-1 retrieved (03_basic-branching-and-merging):** You can run your tests, make sure the hotfix is what you want, and finally merge the hotfix branch back into your master branch to deploy to production. You do this with the git merge command: $ git checkout master $ git merge hotfix Updat…

## recursive 200 - q053: wrong document

- **Question:** What does the rebase command do with work recorded on one branch?
- **Evidence (03_rebasing):** With the rebase command, you can take all the changes that were committed on one branch and replay them on a different branch.
- **First relevant rank:** 6
- **Top-1 retrieved (05_maintaining):** Other maintainers prefer to rebase or cherry-pick contributed work on top of their master branch, rather than merging it in, to keep a mostly linear history. When you have work in a topic branch and have determined that you want to integra…

## recursive 200 - q057: right document, wrong passage

- **Question:** What do local pointers such as origin/master actually stand for?
- **Evidence (03_remote-branches):** Remote-tracking branches are references to the state of remote branches.
- **First relevant rank:** >10
- **Top-1 retrieved (03_remote-branches):** ."origin" is not special Just like the branch name "master" does not have any special meaning in Git, neither does "origin". While "master" is the default name for a starting branch when you run git init which is the only reason it's widel…

## recursive 200 - q058: right document, wrong passage

- **Question:** Is any network traffic involved while you create branches and combine them?
- **Evidence (03_workflows):** When you're branching and merging, everything is being done only in your Git repository -- there is no communication with the server.
- **First relevant rank:** >10
- **Top-1 retrieved (03_workflows):** Branching Workflows Now that you have the basics of branching and merging down, what can or should you do with them? In this section, we'll cover some common workflows that this lightweight branching makes possible, so you can decide if yo…

## recursive 200 - q065: wrong document

- **Question:** Which command registers the service so it comes up when the machine boots?
- **Evidence (04_git-daemon):** you'll run systemctl enable git-daemon to automatically start the service on boot
- **First relevant rank:** 6
- **Top-1 retrieved (06_5-scripting):** There are dozens of services you can choose from, most of them integrations into other commercial and open source systems. Most of them are for Continuous Integration services, bug and issue trackers, chat room systems and documentation sy…

## recursive 200 - q067: wrong document

- **Question:** What gives a developer the ability to send commits up, once they can log in over SSH?
- **Evidence (04_git-on-a-server):** If a user SSHs into a server and has write access to the /srv/git/my_project.git directory, they will also automatically have push access.
- **First relevant rank:** 10
- **Top-1 retrieved (10_transfer-protocols):** For example, say you run git push origin master in your project, and origin is defined as a URL that uses the SSH protocol. Git fires up the send-pack process, which initiates a connection over SSH to your server. It tries to run a command…

## recursive 200 - q083: wrong document

- **Question:** What has to be done on the machine itself each time a new project should be hosted?
- **Evidence (04_setting-up-server):** Note that someone must shell onto the machine and create a bare repository every time you want to add a project.
- **First relevant rank:** 9
- **Top-1 retrieved (06_3-maintaining):** Maintaining a Project Now that we're comfortable contributing to a project, let's look at the other side: creating, maintaining and administering your own project. Creating a New Repository Let's create a new repository to share our projec…

## recursive 200 - q084: wrong document

- **Question:** Which bundled tool keeps a shared account confined to version-control operations?
- **Evidence (04_setting-up-server):** You can easily restrict the git user account to only Git-related activities with a limited shell tool called git-shell that comes with Git.
- **First relevant rank:** >10
- **Top-1 retrieved (04_gitlab):** Another, more decoupled way of collaboration is by using merge requests. This feature enables any user that can see a project to contribute to it in a controlled way. Users with direct access can simply create a branch, push commits to it,…

## recursive 200 - q087: wrong document

- **Question:** Why does the group ownership of the repository directories need changing?
- **Evidence (04_smart-http):** You'll also need to set the Unix user group of the /srv/git directories to www-data so your web server can read- and write-access the repositories
- **First relevant rank:** >10
- **Top-1 retrieved (06_4-managing-organization):** Follow these steps and you'll soon be the owner of a brand-new organization. Like personal accounts, organizations are free if everything you plan to store there will be open source. As an owner in an organization, when you fork a reposito…

## recursive 200 - q091: right document, wrong passage

- **Question:** Why must a force flag be added when pushing a topic branch whose history you have just rewritten with a rebase?
- **Evidence (05_contributing):** Because you rebased the branch, you have to specify the -f to your push command in order to be able to replace the featureA branch on the server with a commit that isn't a descendant of it.
- **First relevant rank:** >10
- **Top-1 retrieved (05_contributing):** On a project for which you're not the maintainer, it's generally easier to have a branch like master always track origin/master and to do your work in topic branches that you can easily discard if they're rejected. Having work themes isola…

## recursive 200 - q093: right document, wrong passage

- **Question:** In the integration-manager model, must a contributor sit idle until their submission is taken in?
- **Evidence (05_distributed-workflows):** Contributors don't have to wait for the project to incorporate their changes -- each party can work at their own pace.
- **First relevant rank:** 10
- **Top-1 retrieved (05_distributed-workflows):** This is a variant of a multiple-repository workflow. It's generally used by huge projects with hundreds of collaborators; one famous example is the Linux kernel. Various integration managers are in charge of certain parts of the repository…

## recursive 200 - q101: wrong document

- **Question:** What piece of information does GitHub use to attribute a commit to a particular member?
- **Evidence (06_1-setting-up-account):** The way that GitHub maps your Git commits to your user is by email address.
- **First relevant rank:** >10
- **Top-1 retrieved (10_environment):** GIT_ICASE_PATHSPECS sets all pathspecs to work in a case-insensitive manner. Committing The final creation of a Git commit object is usually done by git-commit-tree, which uses these environment variables as its primary source of informati…

## recursive 200 - q103: wrong document

- **Question:** Why is it worth giving each uploaded public key a label such as the machine it belongs to?
- **Evidence (06_1-setting-up-account):** You can name each of your keys (e.g. "My Laptop" or "Work Account") so that if you need to revoke a key later, you can easily tell which one you're looking for.
- **First relevant rank:** >10
- **Top-1 retrieved (05_maintaining):** If you do sign your tags, you may have the problem of distributing the public PGP key used to sign your tags. The maintainer of the Git project has solved this issue by including their public key as a blob in the repository and then adding…

## recursive 200 - q124: wrong document

- **Question:** Does Git work out automatically which refs belong in a bundle, or must I enumerate them?
- **Evidence (07_bundling):** With the bundle command you need to list out every reference or specific range of commits that you want to be included.
- **First relevant rank:** >10
- **Top-1 retrieved (06_3-maintaining):** That last line tells Git, "All the refs that look like refs/pull/123/head should be stored locally like refs/remotes/origin/pr/123." Now, if you save that file, and do a git fetch: $ git fetch # … * [new ref] refs/pull/1/head -> origin/pr/…

## recursive 200 - q125: wrong document

- **Question:** What artifact does Git produce from the data a push would normally send across the network?
- **Evidence (07_bundling):** The bundle command will package up everything that would normally be pushed over the wire with a git push command into a binary file
- **First relevant rank:** 6
- **Top-1 retrieved (10_transfer-protocols):** For example, say you run git push origin master in your project, and origin is defined as a URL that uses the SSH protocol. Git fires up the send-pack process, which initiates a connection over SSH to your server. It tries to run a command…

## recursive 200 - q130: right document, wrong passage

- **Question:** Which credential helper ships with Git on Apple machines, and where does it keep the secrets?
- **Evidence (07_credentials):** If you're using macOS, Git comes with an "osxkeychain" mode, which caches credentials in the secure keychain that's attached to your system account.
- **First relevant rank:** >10
- **Top-1 retrieved (07_credentials):** Git even allows you to configure several helpers. When looking for credentials for a particular host, Git will query them in order, and stop after the first answer is provided. When saving credentials, Git will send the username and passwo…

## recursive 200 - q132: wrong document

- **Question:** After tracking down the faulty revision, what command returns me to the checkout I had beforehand?
- **Evidence (07_debugging):** When you're finished, you should run git bisect reset to reset your HEAD to where you were before you started, or you'll end up in a weird state
- **First relevant rank:** >10
- **Top-1 retrieved (07_reset):** The other way to run checkout is with a file path, which, like reset, does not move HEAD. It is just like git reset [branch] file in that it updates the index with that file at that commit, but it also overwrites the file in the working di…

## recursive 200 - q137: right document, wrong passage

- **Question:** Inside the menu-driven prompt, which letter or number takes a file back out of the staging area?
- **Evidence (07_interactive-staging):** If you want to unstage the TODO file at this point, you use the r or 3 (for revert) option
- **First relevant rank:** 7
- **Top-1 retrieved (07_interactive-staging):** If you type u or 2 (for update) at the What now> prompt, you're prompted for which files you want to stage: What now> u staged unstaged path 1: unchanged +0/-1 TODO 2: unchanged +1/-1 index.html 3: unchanged +5/-1 lib/simplegit.rb Update>>…

## recursive 200 - q139: wrong document

- **Question:** Which two command-line switches make the add command open its menu-driven prompt?
- **Evidence (07_interactive-staging):** If you run git add with the -i or --interactive option, Git enters an interactive shell mode, displaying something like this
- **First relevant rank:** >10
- **Top-1 retrieved (01_command-line):** So we will expect you to know how to open Terminal in macOS or Command Prompt or PowerShell in Windows. If you don't know what we're talking about here, you may need to stop and research that quickly so that you can follow the rest of the …

## recursive 200 - q143: right document, wrong passage

- **Question:** Which low-level command turns a tree into a fresh commit object that has no parent?
- **Evidence (07_replace):** We can create our base commit using the commit-tree command, which just takes a tree and will give us a brand new, parentless commit object SHA-1 back.
- **First relevant rank:** >10
- **Top-1 retrieved (07_replace):** $ echo 'Get history from blah blah blah' | git commit-tree 9c68fdc^{tree} 622e88e9cbfbacfb75b5279245b9fb38dfea10cf ===== The commit-tree command is one of a set of commands that are commonly referred to as 'plumbing' commands. These are co…

## recursive 200 - q144: wrong document

- **Question:** Apart from the config flag, which directory can I create inside one repository to switch the feature on there?
- **Evidence (07_rerere):** You can also turn it on by creating the .git/rr-cache directory in a specific repository, but the config setting is clearer and enables that feature globally for you.
- **First relevant rank:** >10
- **Top-1 retrieved (04_git-on-a-server):** $ git clone --bare my_project my_project.git Cloning into bare repository 'my_project.git'... done. You should now have a copy of the Git directory data in your my_project.git directory. This is roughly equivalent to something like: $ cp -…

## recursive 200 - q145: wrong document

- **Question:** What repeated routine lets a long-lived topic branch stay mergeable without littering history with interim merge commits?
- **Evidence (07_rerere):** With rerere enabled, you can attempt the occasional merge, resolve the conflicts, then back out of the merge.
- **First relevant rank:** >10
- **Top-1 retrieved (05_contributing):** Now, each of your topics is contained within a silo -- similar to a patch queue -- that you can rewrite, rebase, and modify without the topics interfering or interdepending on each other, like so: Initial commit history with featureB work …

## recursive 200 - q146: right document, wrong passage

- **Question:** What three words is the odd-looking name of Git's conflict-memory feature short for?
- **Evidence (07_rerere):** The name stands for "reuse recorded resolution" and, as the name implies, it allows you to ask Git to remember how you've resolved a hunk conflict
- **First relevant rank:** 6
- **Top-1 retrieved (07_rerere):** $ git diff diff --cc hello.rb index a440db6,54336ba..0000000 --- a/hello.rb +++ b/hello.rb @@@ -1,7 -1,7 +1,7 @@@ #! /usr/bin/env ruby def hello - puts 'hola world' - puts 'hello mundo' ++ puts 'hola mundo' end Automatically resolved merge…

## recursive 200 - q148: right document, wrong passage

- **Question:** Between resetting and checking out a branch, which one relocates the branch pointer and which relocates HEAD?
- **Evidence (07_reset):** Whereas reset will move the branch that HEAD points to, checkout will move HEAD itself to point to another branch.
- **First relevant rank:** >10
- **Top-1 retrieved (07_reset):** 1. Move the branch HEAD points to (stop here if --soft). 2. Make the index look like HEAD (stop here unless --hard). 3. Make the working directory look like the index. Reset With a Path That covers the behavior of reset in its basic form, …

## recursive 200 - q152: right document, wrong passage

- **Question:** How far back does Git's background record of where HEAD and branch tips have pointed normally reach?
- **Evidence (07_revision-selection):** One of the things Git does in the background while you're working away is keep a "reflog" -- a log of where your HEAD and branch references have been for the last few months.
- **First relevant rank:** 10
- **Top-1 retrieved (07_revision-selection):** Every time your branch tip is updated for any reason, Git stores that information for you in this temporary history. You can use your reflog data to refer to older commits as well. For example, if you want to see the fifth prior value of t…

## recursive 200 - q156: wrong document

- **Question:** After an import leaves junk top-level folders, how can an inner folder like trunk be promoted to the project root throughout history?
- **Evidence (07_rewriting-history):** If you want to make the trunk subdirectory be the new project root for every commit, filter-branch can help you do that, too:
- **First relevant rank:** >10
- **Top-1 retrieved (07_subtree-merges):** In this case, we want to pull the Rack project into our master project as a subdirectory. We can do that in Git with git read-tree. You'll learn more about read-tree and its friends in ch10-git-internals#ch10-git-internals, but for now kno…

## recursive 200 - q158: right document, wrong passage

- **Question:** Which instruction word in the rebase script melds a commit into the one before it and asks you to join their log messages?
- **Evidence (07_rewriting-history):** If, instead of "pick" or "edit", you specify "squash", Git applies both that change and the change directly before it and makes you merge the commit messages together.
- **First relevant rank:** >10
- **Top-1 retrieved (07_rewriting-history):** # Rebase 710f0f8..a5f4a0d onto 710f0f8 # # Commands: # p, pick <commit> = use commit # r, reword <commit> = use commit, but edit the commit message # e, edit <commit> = use commit, but stop for amending # s, squash <commit> = use commit, b…

## recursive 200 - q160: right document, wrong passage

- **Question:** How can you ask the log command to replay the whole evolution of a single function as patches?
- **Evidence (07_searching):** Simply run git log with the -L option, and it will show you the history of a function or line of code in your codebase.
- **First relevant rank:** >10
- **Top-1 retrieved (07_searching):** For example, if we wanted to see every change made to the function git_deflate_bound in the zlib.c file, we could run git log -L :git_deflate_bound:zlib.c. This will try to figure out what the bounds of that function are and then look thro…

## recursive 200 - q164: wrong document

- **Question:** From which release can merging and pulling be made to reject unsigned incoming commits, and with what argument?
- **Evidence (07_signing):** In Git 1.8.3 and later, git merge and git pull can be told to inspect and reject when merging a commit that does not carry a trusted GPG signature with the --verify-signatures command.
- **First relevant rank:** >10
- **Top-1 retrieved (08_policy):** The downside to this approach is the whining that will inevitably result when your users' commit pushes are rejected. Having their carefully crafted work rejected at the last minute can be extremely frustrating and confusing; and furthermo…

## recursive 200 - q166: right document, wrong passage

- **Question:** Which configuration entry records which GPG key Git should reach for when it signs things?
- **Evidence (07_signing):** Once you have a private key to sign with, you can configure Git to use it for signing things by setting the user.signingkey config setting.
- **First relevant rank:** 10
- **Top-1 retrieved (07_signing):** $ git merge --verify-signatures -S signed-branch Commit 13ad65e has a good GPG signature by Scott Chacon (Git signing key) <schacon@gmail.com> You need a passphrase to unlock the secret key for user: "Scott Chacon (Git signing key) <schaco…

## recursive 200 - q175: right document, wrong passage

- **Question:** Why can work you commit inside a subproject vanish when the superproject later refreshes it?
- **Evidence (07_submodules):** With no working branch tracking changes, that means even if you commit changes to the submodule, those changes will quite possibly be lost the next time you run git submodule update.
- **First relevant rank:** 7
- **Top-1 retrieved (07_submodules):** There is a special situation that can happen when pulling superproject updates: it could be that the upstream repository has changed the URL of the submodule in the .gitmodules file in one of the commits you pull. This can happen for examp…

## recursive 200 - q178: wrong document

- **Question:** Which plumbing command loads another branch's top-level tree into your index and working files?
- **Evidence (07_subtree-merges):** You'll learn more about read-tree and its friends in ch10-git-internals#ch10-git-internals, but for now know that it reads the root tree of one branch into your current staging area and working directory.
- **First relevant rank:** 10
- **Top-1 retrieved (07_reset):** $ git cat-file -p HEAD tree cfda3bf379e4f8dba8717dee55aab78aef7f4daf author Scott Chacon 1301511835 -0700 committer Scott Chacon 1301511835 -0700 initial commit $ git ls-tree -r HEAD 100644 blob a906cb2a4a904a152... README 100644 blob 8f94…

## recursive 200 - q179: wrong document

- **Question:** Which two settings bring the vendored project's updates across with a ready-made commit message?
- **Evidence (07_subtree-merges):** To pull in the changes and prepopulate the commit message, use the --squash option, as well as the recursive merge strategy's -Xsubtree option.
- **First relevant rank:** >10
- **Top-1 retrieved (08_hooks):** The prepare-commit-msg hook is run before the commit message editor is fired up but after the default message is created. It lets you edit the default message before the commit author sees it. This hook takes a few parameters: the path to …

## recursive 200 - q182: wrong document

- **Question:** Why might a content filter that works for you break for a colleague who clones the same project?
- **Evidence (08_attributes):** You have to be careful, though, because the .gitattributes file is committed and passed around with the project, but the driver (in this case, dater) isn't, so it won't work everywhere.
- **First relevant rank:** >10
- **Top-1 retrieved (04_gitlab):** Another, more decoupled way of collaboration is by using merge requests. This feature enables any user that can see a project to contribute to it in a controlled way. Users with direct access can simply create a branch, push commits to it,…

## recursive 200 - q183: wrong document

- **Question:** In what time unit is the numeric value of the mistyped-command correction delay expressed?
- **Evidence (08_config):** help.autocorrect is actually an integer which represents tenths of a second.
- **First relevant rank:** >10
- **Top-1 retrieved (07_searching):** compat/mingw.h:206:struct tm *gmtime_r(const time_t *timep, struct tm *result); date.c:482: if (gmtime_r(&now, &now_tm)) date.c:545: if (gmtime_r(&time, tm)) { date.c:758: / gmtime_r() in match_digit() may have clobbered it / git-compat-ut…

## recursive 200 - q184: wrong document

- **Question:** Which configuration file is consulted first, and whose repositories does it affect?
- **Evidence (08_config):** The first place Git looks for these values is in the system-wide [path]/etc/gitconfig file, which contains settings that are applied to every user on the system and all of their repositories.
- **First relevant rank:** >10
- **Top-1 retrieved (05_distributed-workflows):** This is a variant of a multiple-repository workflow. It's generally used by huge projects with hundreds of collaborators; one famous example is the Linux kernel. Various integration managers are in charge of certain parts of the repository…

## recursive 200 - q191: right document, wrong passage

- **Question:** Where does text printed by a server-side enforcement script end up?
- **Evidence (08_policy):** Anything your script echoes to stdout will be transferred to the client.
- **First relevant rank:** >10
- **Top-1 retrieved (08_policy):** An Example Git-Enforced Policy In this section, you'll use what you've learned to establish a Git workflow that checks for a custom commit message format, and allows only certain users to modify certain subdirectories in a project. You'll …

## recursive 200 - q194: wrong document

- **Question:** Which variable supplies fallback locations to search when an object is missing from the main object store?
- **Evidence (10_environment):** GIT_ALTERNATE_OBJECT_DIRECTORIES is a colon-separated list (formatted like /dir/one:/dir/two:…) which tells Git where to check for objects if they aren't in GIT_OBJECT_DIRECTORY.
- **First relevant rank:** >10
- **Top-1 retrieved (10_packfiles):** If you look in your objects directory, you'll find that most of your objects are gone, and a new pair of files has appeared: $ find .git/objects -type f git/objects/bd/9dbf5aae1a3862dd1526723246b20206e5fc37 git/objects/d6/70460b4b4aece5915…

## recursive 200 - q195: wrong document

- **Question:** How many unpacked objects or how many pack files does it take before the automatic cleanup actually does work?
- **Evidence (10_maintenance):** You must have around 7,000 loose objects or more than 50 packfiles for Git to fire up a real gc command.
- **First relevant rank:** >10
- **Top-1 retrieved (10_packfiles):** The objects that remain are the blobs that aren't pointed to by any commit -- in this case, the "what is up, doc?" example and the "test content" example blobs you created earlier. Because you never added them to any commits, they're consi…

## recursive 200 - q198: wrong document

- **Question:** How is the on-disk path of a stored object split up between folder name and file name?
- **Evidence (10_objects):** The subdirectory is named with the first 2 characters of the SHA-1, and the filename is the remaining 38 characters.
- **First relevant rank:** 8
- **Top-1 retrieved (10_packfiles):** The objects that remain are the blobs that aren't pointed to by any commit -- in this case, the "what is up, doc?" example and the "test content" example blobs you created earlier. Because you never added them to any commits, they're consi…

## recursive 200 - q201: wrong document

- **Question:** Besides the automatic repacking Git performs on its own, how can someone trigger a repack deliberately?
- **Evidence (10_packfiles):** Git will occasionally repack your database automatically, always trying to save more space, but you can also manually repack at any time by running git gc by hand.
- **First relevant rank:** >10
- **Top-1 retrieved (07_debugging):** Another cool thing about Git is that it doesn't track file renames explicitly. It records the snapshots and then tries to figure out what was renamed implicitly, after the fact. One of the interesting features of this is that you can ask i…

## recursive 200 - q208: wrong document

- **Question:** What does HEAD normally hold, and how does that differ from an ordinary ref?
- **Evidence (10_refs):** Usually the HEAD file is a symbolic reference to the branch you're currently on. By symbolic reference, we mean that unlike a normal reference, it contains a pointer to another reference.
- **First relevant rank:** 6
- **Top-1 retrieved (07_reset):** Here's a cheat-sheet for which commands affect which trees. The "HEAD" column reads "REF" if that command moves the reference (branch) that HEAD points to, and "HEAD" if it moves HEAD itself. Pay especial attention to the 'WD Safe?' column…

## recursive 200 - q210: wrong document

- **Question:** What does the leading plus sign in front of a mapping authorise Git to do?
- **Evidence (10_refspec):** The + tells Git to update the reference even if it isn't a fast-forward.
- **First relevant rank:** >10
- **Top-1 retrieved (02_aliases):** $ git last commit 66938dae3329c7aebe598c2246a8e6af90d04646 Author: Josh Goebel <dreamer3@example.com> Date: Tue Aug 26 19:48:51 2008 +0800 Test for current head Signed-off-by: Scott Chacon <schacon@example.com> As you can tell, Git simply …

## fixed_overlap 200+80 - q005: wrong document

- **Question:** Which kind of Git interface can I count on every user already having?
- **Evidence (01_command-line):** all users will have the command-line tools installed and available.
- **First relevant rank:** >10
- **Top-1 retrieved (04_git-on-a-server):** and that's how you're accessing the server. There are a few ways you can give access to everyone on your team. The first is to set up accounts for everybody, which is straightforward but can be cumbersome. You may not want to run adduser (…

## fixed_overlap 200+80 - q012: wrong document

- **Question:** Which flag prints a brief list of a command's options instead of the whole manual?
- **Evidence (01_help):** In addition, if you don't need the full-blown manpage help, but just need a quick refresher on the available options for a Git command, you can ask for the more concise "help" output with the -h option, as in:
- **First relevant rank:** >10
- **Top-1 retrieved (06_2-contributing):** this: - [X] Write the code - [ ] Write all the tests - [ ] Document the code If we include this in the description of our Pull Request or Issue, we'll see it rendered like _eg_task_lists. Task lists rendered in a Markdown comment This is o…

## fixed_overlap 200+80 - q019: wrong document

- **Question:** Do everyday Git commands have to reach another machine to do their work?
- **Evidence (01_what-is-git):** Most operations in Git need only local files and resources to operate -- generally no information is needed from another computer on your network.
- **First relevant rank:** 7
- **Top-1 retrieved (06_3-maintaining):** pretty easily. To demonstrate this, we're going to use a low-level command (often referred to as a "plumbing" command, which we'll read about more in ch10-git-internals#_plumbing_porcelain) called ls-remote. This command is generally not u…

## fixed_overlap 200+80 - q021: wrong document

- **Question:** Where does Git keep the record of what is queued up for the next commit?
- **Evidence (01_what-is-git):** The staging area is a file, generally contained in your Git directory, that stores information about what will go into your next commit.
- **First relevant rank:** >10
- **Top-1 retrieved (03_nutshell):** create that snapshot when needed. Your Git repository now contains five objects: three blobs (each representing the contents of one of the three files), one tree that lists the contents of the directory and specifies which file names are s…

## fixed_overlap 200+80 - q028: wrong document

- **Question:** I edited a file again after staging it; what do I have to do before committing?
- **Evidence (02_recording-changes):** If you modify a file after you run git add, you have to run git add again to stage the latest version of the file:
- **First relevant rank:** >10
- **Top-1 retrieved (02_undoing):** and commit again using the --amend option: $ git commit --amend This command takes your staging area and uses it for the commit. If you've made no changes since your last commit (for instance, you run this command immediately after your pr…

## fixed_overlap 200+80 - q030: right document, wrong passage

- **Question:** Which files in my working directory does Git consider untracked?
- **Evidence (02_recording-changes):** Untracked files are everything else -- any files in your working directory that were not in your last snapshot and are not in your staging area.
- **First relevant rank:** >10
- **Top-1 retrieved (02_recording-changes):** , you see your untracked file like so: $ echo 'My Project' > README $ git status On branch master Your branch is up-to-date with 'origin/master'. Untracked files: (use "git add <file>..." to include in what will be committed) README nothin…

## fixed_overlap 200+80 - q031: wrong document

- **Question:** Besides downloading new commits, what else does pulling do?
- **Evidence (02_remotes):** Running git pull generally fetches data from the server you originally cloned from and automatically tries to merge it into the code you're currently working on.
- **First relevant rank:** >10
- **Top-1 retrieved (05_contributing):** pulled. For instance, if Jessica wants to send John a pull request, and she's done two commits on the topic branch she just pushed, she can run this: $ git request-pull origin/master myfork The following changes since commit 1edee6b1d61823…

## fixed_overlap 200+80 - q038: wrong document

- **Question:** When is rewriting the most recent commit considered safe?
- **Evidence (02_undoing):** Only amend commits that are still local and have not been pushed somewhere.
- **First relevant rank:** >10
- **Top-1 retrieved (07_rewriting-history):** entirely, and you should consider pushed work as final unless you have good reason to change it. In short, you should avoid pushing your work until you're happy with it and ready to share it with the rest of the world. Changing the Last Co…

## fixed_overlap 200+80 - q040: right document, wrong passage

- **Question:** How do I track down commits where a particular piece of text appeared or vanished?
- **Evidence (02_viewing-history):** Another really helpful filter is the -S option (colloquially referred to as Git's "pickaxe" option), which takes a string and shows only those commits that changed the number of occurrences of that string.
- **First relevant rank:** >10
- **Top-1 retrieved (02_viewing-history):** Viewing the Commit History After you have created several commits, or if you have cloned a repository with an existing commit history, you'll probably want to look back to see what has happened. The most basic and powerful tool to do this …

## fixed_overlap 200+80 - q057: right document, wrong passage

- **Question:** What do local pointers such as origin/master actually stand for?
- **Evidence (03_remote-branches):** Remote-tracking branches are references to the state of remote branches.
- **First relevant rank:** >10
- **Top-1 retrieved (03_remote-branches):** place as origin's master branch, so you have something to work from. ."origin" is not special Just like the branch name "master" does not have any special meaning in Git, neither does "origin". While "master" is the default name for a star…

## fixed_overlap 200+80 - q058: right document, wrong passage

- **Question:** Is any network traffic involved while you create branches and combine them?
- **Evidence (03_workflows):** When you're branching and merging, everything is being done only in your Git repository -- there is no communication with the server.
- **First relevant rank:** >10
- **Top-1 retrieved (03_workflows):** Branching Workflows Now that you have the basics of branching and merging down, what can or should you do with them? In this section, we'll cover some common workflows that this lightweight branching makes possible, so you can decide if yo…

## fixed_overlap 200+80 - q067: wrong document

- **Question:** What gives a developer the ability to send commits up, once they can log in over SSH?
- **Evidence (04_git-on-a-server):** If a user SSHs into a server and has write access to the /srv/git/my_project.git directory, they will also automatically have push access.
- **First relevant rank:** >10
- **Top-1 retrieved (10_transfer-protocols):** the client and connects to a receive-pack process on the remote side. SSH For example, say you run git push origin master in your project, and origin is defined as a URL that uses the SSH protocol. Git fires up the send-pack process, which…

## fixed_overlap 200+80 - q068: right document, wrong passage

- **Question:** Which flag makes the initialization set group write permissions correctly?
- **Evidence (04_git-on-a-server):** Git will automatically add group write permissions to a repository properly if you run the git init command with the --shared option.
- **First relevant rank:** >10
- **Top-1 retrieved (04_git-on-a-server):** have to do almost no work (as we covered in the last section). If you want more complex access control type permissions on your repositories, you can handle them with the normal filesystem permissions of your server's operating system. If …

## fixed_overlap 200+80 - q083: wrong document

- **Question:** What has to be done on the machine itself each time a new project should be hosted?
- **Evidence (04_setting-up-server):** Note that someone must shell onto the machine and create a bare repository every time you want to add a project.
- **First relevant rank:** >10
- **Top-1 retrieved (06_3-maintaining):** Maintaining a Project Now that we're comfortable contributing to a project, let's look at the other side: creating, maintaining and administering your own project. Creating a New Repository Let's create a new repository to share our projec…

## fixed_overlap 200+80 - q084: wrong document

- **Question:** Which bundled tool keeps a shared account confined to version-control operations?
- **Evidence (04_setting-up-server):** You can easily restrict the git user account to only Git-related activities with a limited shell tool called git-shell that comes with Git.
- **First relevant rank:** >10
- **Top-1 retrieved (07_credentials):** edential-store and friends are separate programs from Git, it's not much of a leap to realize that any program can be a Git credential helper. The helpers provided by Git cover many common use cases, but not all. For example, let's say you…

## fixed_overlap 200+80 - q087: wrong document

- **Question:** Why does the group ownership of the repository directories need changing?
- **Evidence (04_smart-http):** You'll also need to set the Unix user group of the /srv/git directories to www-data so your web server can read- and write-access the repositories
- **First relevant rank:** >10
- **Top-1 retrieved (06_4-managing-organization):** fork a repository, you'll have the choice of forking it to your organization's namespace. When you create new repositories you can create them either under your personal account or under any of the organizations that you are an owner in. Y…

## fixed_overlap 200+80 - q091: right document, wrong passage

- **Question:** Why must a force flag be added when pushing a topic branch whose history you have just rewritten with a rebase?
- **Evidence (05_contributing):** Because you rebased the branch, you have to specify the -f to your push command in order to be able to replace the featureA branch on the server with a commit that isn't a descendant of it.
- **First relevant rank:** >10
- **Top-1 retrieved (05_contributing):** and to do your work in topic branches that you can easily discard if they're rejected. Having work themes isolated into topic branches also makes it easier for you to rebase your work if the tip of the main repository has moved in the mean…

## fixed_overlap 200+80 - q097: wrong document

- **Question:** When a mailed patch is applied, which parts of the email supply the commit's authorship and its message?
- **Evidence (05_maintaining):** The author information is taken from the email's From and Date headers, and the message of the commit is taken from the Subject and body (before the patch) of the email.
- **First relevant rank:** >10
- **Top-1 retrieved (05_contributing):** t commit Now you have two commits that you want to send to the mailing list. You use git format-patch to generate the mbox-formatted files that you can email to the list -- it turns each commit into an email message with the first line of …

## fixed_overlap 200+80 - q101: wrong document

- **Question:** What piece of information does GitHub use to attribute a commit to a particular member?
- **Evidence (06_1-setting-up-account):** The way that GitHub maps your Git commits to your user is by email address.
- **First relevant rank:** >10
- **Top-1 retrieved (10_objects):** and author data. Moreover, while in principle any commit object can be reproduced precisely given that data, historical details of this book's construction mean that the printed commit hashes might not correspond to the given commits. Repl…

## fixed_overlap 200+80 - q103: wrong document

- **Question:** Why is it worth giving each uploaded public key a label such as the machine it belongs to?
- **Evidence (06_1-setting-up-account):** You can name each of your keys (e.g. "My Laptop" or "Work Account") so that if you need to revoke a key later, you can easily tell which one you're looking for.
- **First relevant rank:** >10
- **Top-1 retrieved (05_maintaining):** con <schacon@gmail.com>" 1024-bit DSA key, ID F721C45A, created 2009-02-09 If you do sign your tags, you may have the problem of distributing the public PGP key used to sign your tags. The maintainer of the Git project has solved this issu…

## fixed_overlap 200+80 - q116: wrong document

- **Question:** How does the generic hooks mechanism hand event data over to your own system?
- **Evidence (06_5-scripting):** You specify a URL and GitHub will post an HTTP payload to that URL on any event you want.
- **First relevant rank:** 8
- **Top-1 retrieved (08_hooks):** is invoked just before the garbage collection takes place, and can be used to notify you that this is happening, or to abort the collection if now isn't a good time. Server-Side Hooks In addition to the client-side hooks, you can use a cou…

## fixed_overlap 200+80 - q124: wrong document

- **Question:** Does Git work out automatically which refs belong in a bundle, or must I enumerate them?
- **Evidence (07_bundling):** With the bundle command you need to list out every reference or specific range of commits that you want to be included.
- **First relevant rank:** 8
- **Top-1 retrieved (06_3-maintaining):** = +refs/pull//head:refs/remotes/origin/pr/ That last line tells Git, "All the refs that look like refs/pull/123/head should be stored locally like refs/remotes/origin/pr/123." Now, if you save that file, and do a git fetch: $ git fetch # ……

## fixed_overlap 200+80 - q129: right document, wrong passage

- **Question:** If more than one helper is configured, which one's answer does Git end up using for a given host?
- **Evidence (07_credentials):** When looking for credentials for a particular host, Git will query them in order, and stop after the first answer is provided.
- **First relevant rank:** 7
- **Top-1 retrieved (07_credentials):** , Git will send the username and password to all of the helpers in the list, and they can choose what to do with them. Here's what a .gitconfig would look like if you had a credentials file on a thumb drive, but wanted to use the in-memory…

## fixed_overlap 200+80 - q130: right document, wrong passage

- **Question:** Which credential helper ships with Git on Apple machines, and where does it keep the secrets?
- **Evidence (07_credentials):** If you're using macOS, Git comes with an "osxkeychain" mode, which caches credentials in the secure keychain that's attached to your system account.
- **First relevant rank:** >10
- **Top-1 retrieved (07_credentials):** -credential-store replies with the username and password we stored above. Here's what the ~/git.store file looks like: https://bob:s3cre7@mygithost It's just a series of lines, each of which contains a credential-decorated URL. The osxkeyc…

## fixed_overlap 200+80 - q132: wrong document

- **Question:** After tracking down the faulty revision, what command returns me to the checkout I had beforehand?
- **Evidence (07_debugging):** When you're finished, you should run git bisect reset to reset your HEAD to where you were before you started, or you'll end up in a weird state
- **First relevant rank:** >10
- **Top-1 retrieved (07_reset):** reset would let you run that) -- it's not working-directory safe, and it does not move HEAD. Also, like git reset and git add, checkout will accept a --patch option to allow you to selectively revert file contents on a hunk-by-hunk basis. …

## fixed_overlap 200+80 - q138: right document, wrong passage

- **Question:** Which menu choice displays the changes already added to the staging area?
- **Evidence (07_interactive-staging):** To see the diff of what you've staged, you can use the d or 6 (for diff) command.
- **First relevant rank:** >10
- **Top-1 retrieved (07_interactive-staging):** displaying something like this: $ git add -i staged unstaged path 1: unchanged +0/-1 TODO 2: unchanged +1/-1 index.html 3: unchanged +5/-1 lib/simplegit.rb - Commands *** 1: [s]tatus 2: [u]pdate 3: [r]evert 4: [a]dd untracked 5: [p]atch 6:…

## fixed_overlap 200+80 - q139: wrong document

- **Question:** Which two command-line switches make the add command open its menu-driven prompt?
- **Evidence (07_interactive-staging):** If you run git add with the -i or --interactive option, Git enters an interactive shell mode, displaying something like this
- **First relevant rank:** >10
- **Top-1 retrieved (01_command-line):** , while your choice of graphical client is a matter of personal taste, all users will have the command-line tools installed and available. So we will expect you to know how to open Terminal in macOS or Command Prompt or PowerShell in Windo…

## fixed_overlap 200+80 - q144: wrong document

- **Question:** Apart from the config flag, which directory can I create inside one repository to switch the feature on there?
- **Evidence (07_rerere):** You can also turn it on by creating the .git/rr-cache directory in a specific repository, but the config setting is clearer and enables that feature globally for you.
- **First relevant rank:** >10
- **Top-1 retrieved (04_git-on-a-server):** repository into a new bare repository -- a repository that doesn't contain a working directory. This is generally straightforward to do. In order to clone your repository to create a new bare repository, you run the clone command with the …

## fixed_overlap 200+80 - q146: wrong document

- **Question:** What three words is the odd-looking name of Git's conflict-memory feature short for?
- **Evidence (07_rerere):** The name stands for "reuse recorded resolution" and, as the name implies, it allows you to ask Git to remember how you've resolved a hunk conflict
- **First relevant rank:** >10
- **Top-1 retrieved (07_advanced-merging):** the merge conflict markers. This can be useful if you want to reset the markers and try to resolve them again. You can pass --conflict either diff3 or merge (which is the default). If you pass it diff3, Git will use a slightly different ve…

## fixed_overlap 200+80 - q152: right document, wrong passage

- **Question:** How far back does Git's background record of where HEAD and branch tips have pointed normally reach?
- **Evidence (07_revision-selection):** One of the things Git does in the background while you're working away is keep a "reflog" -- a log of where your HEAD and branch references have been for the last few months.
- **First relevant rank:** 8
- **Top-1 retrieved (07_revision-selection):** updating HEAD 7e05da5 HEAD@{6}: rebase -i (pick): updating HEAD Every time your branch tip is updated for any reason, Git stores that information for you in this temporary history. You can use your reflog data to refer to older commits as …

## fixed_overlap 200+80 - q158: right document, wrong passage

- **Question:** Which instruction word in the rebase script melds a commit into the one before it and asks you to join their log messages?
- **Evidence (07_rewriting-history):** If, instead of "pick" or "edit", you specify "squash", Git applies both that change and the change directly before it and makes you merge the commit messages together.
- **First relevant rank:** 6
- **Top-1 retrieved (07_rewriting-history):** into a single commit with the interactive rebasing tool. The script puts helpful instructions in the rebase message: # # Commands: # p, pick <commit> = use commit # r, reword <commit> = use commit, but edit the commit message # e, edit <co…

## fixed_overlap 200+80 - q160: wrong document

- **Question:** How can you ask the log command to replay the whole evolution of a single function as patches?
- **Evidence (07_searching):** Simply run git log with the -L option, and it will show you the history of a function or line of code in your codebase.
- **First relevant rank:** 10
- **Top-1 retrieved (05_contributing):** limit-to-log-function.patch 0002-increase-log-output-to-30-from-25.patch The format-patch command prints out the names of the patch files it creates. The -M switch tells Git to look for renames. The files end up looking like this: $ cat 00…

## fixed_overlap 200+80 - q174: right document, wrong passage

- **Question:** Which tracked configuration file records the pairing of a subproject's URL with the local folder it sits in?
- **Evidence (07_submodules):** First you should notice the new .gitmodules file. This is a configuration file that stores the mapping between the project's URL and the local subdirectory you've pulled it into:
- **First relevant rank:** 6
- **Top-1 retrieved (07_submodules):** ..c3f01dc --- /dev/null +++ b/DbConnector @@ -0,0 +1 @@ +Subproject commit c3f01dc8862123d317dd46284b05b6892c7b29bc Although DbConnector is a subdirectory in your working directory, Git sees it as a submodule and doesn't track its contents…

## fixed_overlap 200+80 - q175: right document, wrong passage

- **Question:** Why can work you commit inside a subproject vanish when the superproject later refreshes it?
- **Evidence (07_submodules):** With no working branch tracking changes, that means even if you commit changes to the submodule, those changes will quite possibly be lost the next time you run git submodule update.
- **First relevant rank:** 7
- **Top-1 retrieved (07_submodules):** the submodule project changes its hosting platform. In that case, it is possible for git pull --recurse-submodules, or git submodule update, to fail if the superproject references a submodule commit that is not found in the submodule remot…

## fixed_overlap 200+80 - q178: wrong document

- **Question:** Which plumbing command loads another branch's top-level tree into your index and working files?
- **Evidence (07_subtree-merges):** You'll learn more about read-tree and its friends in ch10-git-internals#ch10-git-internals, but for now know that it reads the root tree of one branch into your current staging area and working directory.
- **First relevant rank:** >10
- **Top-1 retrieved (07_reset):** 8f9404f2... Rakefile 040000 tree 99f1a6d12cb4b6f19... lib The Git cat-file and ls-tree commands are "plumbing" commands that are used for lower level things and not really used in day-to-day work, but they help us see what's going on here.…

## fixed_overlap 200+80 - q179: wrong document

- **Question:** Which two settings bring the vendored project's updates across with a ready-made commit message?
- **Evidence (07_subtree-merges):** To pull in the changes and prepopulate the commit message, use the --squash option, as well as the recursive merge strategy's -Xsubtree option.
- **First relevant rank:** >10
- **Top-1 retrieved (05_contributing):** "Fixed bug" or "Fixes bug." This convention matches up with commit messages generated by commands like git merge and git revert. Further paragraphs come after blank lines. - Bullet points are okay, too - Typically a hyphen or asterisk is u…

## fixed_overlap 200+80 - q183: wrong document

- **Question:** In what time unit is the numeric value of the mistyped-command correction delay expressed?
- **Evidence (08_config):** help.autocorrect is actually an integer which represents tenths of a second.
- **First relevant rank:** >10
- **Top-1 retrieved (07_searching):** struct tm *git_gmtime_r(const time_t *timep, struct tm *result) compat/gmtime.c:16: ret = gmtime_r(timep, result); compat/mingw.c:826:struct tm *gmtime_r(const time_t *timep, struct tm *result) compat/mingw.h:206:struct tm *gmtime_r(const …

## fixed_overlap 200+80 - q191: right document, wrong passage

- **Question:** Where does text printed by a server-side enforcement script end up?
- **Evidence (08_policy):** Anything your script echoes to stdout will be transferred to the client.
- **First relevant rank:** >10
- **Top-1 retrieved (08_policy):** An Example Git-Enforced Policy In this section, you'll use what you've learned to establish a Git workflow that checks for a custom commit message format, and allows only certain users to modify certain subdirectories in a project. You'll …

## fixed_overlap 200+80 - q201: wrong document

- **Question:** Besides the automatic repacking Git performs on its own, how can someone trigger a repack deliberately?
- **Evidence (10_packfiles):** Git will occasionally repack your database automatically, always trying to save more space, but you can also manually repack at any time by running git gc by hand.
- **First relevant rank:** >10
- **Top-1 retrieved (08_hooks):** working tree changes. The pre-push hook runs during git push, after the remote refs have been updated but before any objects have been transferred. It receives the name and location of the remote as parameters, and a list of to-be-updated …

## fixed_overlap 200+80 - q203: wrong document

- **Question:** What similarity does Git look for between objects when deciding which ones to store as differences?
- **Evidence (10_packfiles):** When Git packs objects, it looks for files that are named and sized similarly, and stores just the deltas from one version of the file to the next.
- **First relevant rank:** >10
- **Top-1 retrieved (01_what-is-git):** stores and thinks about information in a very different way, and understanding these differences will help you avoid becoming confused while using it. Snapshots, Not Differences The major difference between Git and any other VCS (Subversio…

## fixed_overlap 200+80 - q210: wrong document

- **Question:** What does the leading plus sign in front of a mapping authorise Git to do?
- **Evidence (10_refspec):** The + tells Git to update the reference even if it isn't a fast-forward.
- **First relevant rank:** >10
- **Top-1 retrieved (07_interactive-staging):** displaying something like this: $ git add -i staged unstaged path 1: unchanged +0/-1 TODO 2: unchanged +1/-1 index.html 3: unchanged +5/-1 lib/simplegit.rb - Commands *** 1: [s]tatus 2: [u]pdate 3: [r]evert 4: [a]dd untracked 5: [p]atch 6:…

## fixed_overlap 200+80 - q212: wrong document

- **Question:** Why does pushing with nothing before the colon wipe out a branch upstream?
- **Evidence (10_refspec):** Because the refspec is <src>:<dst>, by leaving off the <src> part, this basically says to make the topic branch on the remote nothing, which deletes it.
- **First relevant rank:** >10
- **Top-1 retrieved (02_remotes):** then you can run this to push any commits you've done back up to the server: $ git push origin master This command works only if you cloned from a server to which you have write access and if nobody has pushed in the meantime. If you and s…

## semantic p85 - q005: wrong document

- **Question:** Which kind of Git interface can I count on every user already having?
- **Evidence (01_command-line):** all users will have the command-line tools installed and available.
- **First relevant rank:** >10
- **Top-1 retrieved (05_contributing):** Contributing to a Project The main difficulty with describing how to contribute to a project are the numerous variations on how to do that. Because Git is very flexible, people can and do work together in many ways, and it's problematic to…

## semantic p85 - q012: wrong document

- **Question:** Which flag prints a brief list of a command's options instead of the whole manual?
- **Evidence (01_help):** In addition, if you don't need the full-blown manpage help, but just need a quick refresher on the available options for a Git command, you can ask for the more concise "help" output with the -h option, as in:
- **First relevant rank:** 9
- **Top-1 retrieved (02_viewing-history):** Another really useful option is --pretty. This option changes the log output to formats other than the default. A few prebuilt option values are available for you to use. The oneline value for this option prints each commit on a single lin…

## semantic p85 - q021: wrong document

- **Question:** Where does Git keep the record of what is queued up for the next commit?
- **Evidence (01_what-is-git):** The staging area is a file, generally contained in your Git directory, that stores information about what will go into your next commit.
- **First relevant rank:** >10
- **Top-1 retrieved (02_recording-changes):** Recording Changes to the Repository At this point, you should have a bona fide Git repository on your local machine, and a checkout or working copy of all of its files in front of you. Typically, you'll want to start making changes and com…

## semantic p85 - q025: wrong document

- **Question:** After turning an existing folder into a repository, how do I record its current files?
- **Evidence (02_getting-a-repository):** You can accomplish that with a few git add commands that specify the files you want to track, followed by a git commit:
- **First relevant rank:** >10
- **Top-1 retrieved (02_recording-changes):** Recording Changes to the Repository At this point, you should have a bona fide Git repository on your local machine, and a checkout or working copy of all of its files in front of you. Typically, you'll want to start making changes and com…

## semantic p85 - q026: wrong document

- **Question:** Can I choose a target folder name that differs from the project's own?
- **Evidence (02_getting-a-repository):** If you want to clone the repository into a directory named something other than libgit2, you can specify the new directory name as an additional argument:
- **First relevant rank:** >10
- **Top-1 retrieved (07_rewriting-history):** The command is filter-branch, and it can rewrite huge swaths of your history, so you probably shouldn't use it unless your project isn't yet public and other people haven't based work off the commits you're about to rewrite.

## semantic p85 - q028: wrong document

- **Question:** I edited a file again after staging it; what do I have to do before committing?
- **Evidence (02_recording-changes):** If you modify a file after you run git add, you have to run git add again to stage the latest version of the file:
- **First relevant rank:** >10
- **Top-1 retrieved (02_undoing):** For more on what happens when you do this and how to recover if you're on the receiving end read _rebase_peril. Unstaging a Staged File The next two sections demonstrate how to work with your staging area and working directory changes. The…

## semantic p85 - q030: right document, wrong passage

- **Question:** Which files in my working directory does Git consider untracked?
- **Evidence (02_recording-changes):** Untracked files are everything else -- any files in your working directory that were not in your last snapshot and are not in your staging area.
- **First relevant rank:** >10
- **Top-1 retrieved (02_recording-changes):** Ignoring Files Often, you'll have a class of files that you don't want Git to automatically add or even show you as being untracked. These are generally automatically generated files such as log files or files produced by your build system…

## semantic p85 - q031: wrong document

- **Question:** Besides downloading new commits, what else does pulling do?
- **Evidence (02_remotes):** Running git pull generally fetches data from the server you originally cloned from and automatically tries to merge it into the code you're currently working on.
- **First relevant rank:** 9
- **Top-1 retrieved (10_transfer-protocols):** You have your tree object, so you continue walking your commits. They're all also within the packfile you just downloaded, so you don't have to do any more requests to your server. Git checks out a working copy of the master branch that wa…

## semantic p85 - q038: wrong document

- **Question:** When is rewriting the most recent commit considered safe?
- **Evidence (02_undoing):** Only amend commits that are still local and have not been pushed somewhere.
- **First relevant rank:** >10
- **Top-1 retrieved (07_rewriting-history):** Use -c <commit> to reword the commit message. # # These lines can be re-ordered; they are executed from top to bottom. # # If you remove a line here THAT COMMIT WILL BE LOST. # # However, if you remove everything, the rebase will be aborte…

## semantic p85 - q040: right document, wrong passage

- **Question:** How do I track down commits where a particular piece of text appeared or vanished?
- **Evidence (02_viewing-history):** Another really helpful filter is the -S option (colloquially referred to as Git's "pickaxe" option), which takes a string and shows only those commits that changed the number of occurrences of that string.
- **First relevant rank:** >10
- **Top-1 retrieved (02_viewing-history):** Viewing the Commit History After you have created several commits, or if you have cloned a repository with an existing commit history, you'll probably want to look back to see what has happened. The most basic and powerful tool to do this …

## semantic p85 - q044: wrong document

- **Question:** Which snapshots are combined when the current commit is not a direct ancestor of the branch being brought in?
- **Evidence (03_basic-branching-and-merging):** Git does a simple three-way merge, using the two snapshots pointed to by the branch tips and the common ancestor of the two.
- **First relevant rank:** >10
- **Top-1 retrieved (03_rebasing):** That way, the maintainer doesn't have to do any integration work -- just a fast-forward or a clean apply. Note that the snapshot pointed to by the final commit you end up with, whether it's the last of the rebased commits for a rebase or t…

## semantic p85 - q045: right document, wrong passage

- **Question:** Why was no new snapshot needed when the hotfix work was integrated back into master?
- **Evidence (03_basic-branching-and-merging):** Because the commit C4 pointed to by the branch hotfix you merged in was directly ahead of the commit C2 you're on, Git simply moves the pointer forward.
- **First relevant rank:** >10
- **Top-1 retrieved (03_basic-branching-and-merging):** At this stage, you'll receive a call that another issue is critical and you need a hotfix. You'll do the following: - Switch to your production branch. - Create a branch to add the hotfix. - After it's tested, merge the hotfix branch, and …

## semantic p85 - q050: wrong document

- **Question:** Whose history does the log command display if you give it no extra arguments?
- **Evidence (03_nutshell):** by default, git log will only show commit history below the branch you've checked out.
- **First relevant rank:** >10
- **Top-1 retrieved (02_viewing-history):** Remove unnecessary test commit a11bef06a3f659402fe7563abf99ad00de2209e6 Author: Scott Chacon <schacon@gee-mail.com> Date: Sat Mar 15 10:31:28 2008 -0700 Initial commit By default, with no arguments, git log lists the commits made in that r…

## semantic p85 - q051: wrong document

- **Question:** Why are branches so inexpensive to make and throw away in Git?
- **Evidence (03_nutshell):** Because a branch in Git is actually a simple file that contains the 40 character SHA-1 checksum of the commit it points to, branches are cheap to create and destroy.
- **First relevant rank:** >10
- **Top-1 retrieved (03_workflows):** Some larger projects also have a proposed or pu (proposed updates) branch that has integrated branches that may not be ready to go into the next or master branch. The idea is that your branches are at various levels of stability; when they…

## semantic p85 - q053: right document, wrong passage

- **Question:** What does the rebase command do with work recorded on one branch?
- **Evidence (03_rebasing):** With the rebase command, you can take all the changes that were committed on one branch and replay them on a different branch.
- **First relevant rank:** >10
- **Top-1 retrieved (03_rebasing):** That way, the maintainer doesn't have to do any integration work -- just a fast-forward or a clean apply. Note that the snapshot pointed to by the final commit you end up with, whether it's the last of the rebased commits for a rebase or t…

## semantic p85 - q054: right document, wrong passage

- **Question:** Which commits must never be rebased?
- **Evidence (03_rebasing):** Do not rebase commits that exist outside your repository and that people may have based work on.
- **First relevant rank:** >10
- **Top-1 retrieved (03_rebasing):** This only works if C4 and C4' that your partner made are almost exactly the same patch. Otherwise the rebase won't be able to tell that it's a duplicate and will add another C4-like patch (which will probably fail to apply cleanly, since t…

## semantic p85 - q055: wrong document

- **Question:** Do branches you create on your own machine reach the server by themselves?
- **Evidence (03_remote-branches):** Your local branches aren't automatically synchronized to the remotes you write to -- you have to explicitly push the branches you want to share.
- **First relevant rank:** 8
- **Top-1 retrieved (03_workflows):** It's important to remember when you're doing all this that these branches are completely local. When you're branching and merging, everything is being done only in your Git repository -- there is no communication with the server.

## semantic p85 - q057: right document, wrong passage

- **Question:** What do local pointers such as origin/master actually stand for?
- **Evidence (03_remote-branches):** Remote-tracking branches are references to the state of remote branches.
- **First relevant rank:** >10
- **Top-1 retrieved (03_remote-branches):** Let's say you have a Git server on your network at git.ourcompany.com. If you clone from this, Git's clone command automatically names it origin for you, pulls down all its data, creates a pointer to where its master branch is, and names i…

## semantic p85 - q065: wrong document

- **Question:** Which command registers the service so it comes up when the machine boots?
- **Evidence (04_git-daemon):** you'll run systemctl enable git-daemon to automatically start the service on boot
- **First relevant rank:** >10
- **Top-1 retrieved (06_5-scripting):** We'll walk through setting up a very simple one, the Email hook. If you choose "email" from the "Add Service" dropdown, you'll get a configuration screen like _service_config. Email service configuration In this case, if we hit the "Add se…

## semantic p85 - q067: right document, wrong passage

- **Question:** What gives a developer the ability to send commits up, once they can log in over SSH?
- **Evidence (04_git-on-a-server):** If a user SSHs into a server and has write access to the /srv/git/my_project.git directory, they will also automatically have push access.
- **First relevant rank:** >10
- **Top-1 retrieved (04_git-on-a-server):** This doesn't affect the commit data in any way -- the SSH user you connect as doesn't affect the commits you've recorded. Another way to do it is to have your SSH server authenticate from an LDAP server or some other centralized authentica…

## semantic p85 - q068: wrong document

- **Question:** Which flag makes the initialization set group write permissions correctly?
- **Evidence (04_git-on-a-server):** Git will automatically add group write permissions to a repository properly if you run the git init command with the --shared option.
- **First relevant rank:** >10
- **Top-1 retrieved (05_contributing):** Are you involved in that process? Is a lieutenant system in place, and do you have to submit your work to them first? The next variable is your commit access. The workflow required in order to contribute to a project is much different if y…

## semantic p85 - q072: wrong document

- **Question:** Who is able to read a project whose visibility has been set to Internal?
- **Evidence (04_gitlab):** An Internal project is visible to any logged-in user, and a Public project is visible to anyone.
- **First relevant rank:** >10
- **Top-1 retrieved (08_policy):** README lib/test.rb If you use the ACL structure returned from the get_acl_access_data method and check it against the listed files in each of the commits, you can determine whether the user has access to push all of their commits: # only a…

## semantic p85 - q084: wrong document

- **Question:** Which bundled tool keeps a shared account confined to version-control operations?
- **Evidence (04_setting-up-server):** You can easily restrict the git user account to only Git-related activities with a limited shell tool called git-shell that comes with Git.
- **First relevant rank:** >10
- **Top-1 retrieved (07_bundling):** So, git bundle can be really useful for sharing or doing network-type operations when you don't have the proper network or shared repository to do so.

## semantic p85 - q087: wrong document

- **Question:** Why does the group ownership of the repository directories need changing?
- **Evidence (04_smart-http):** You'll also need to set the Unix user group of the /srv/git directories to www-data so your web server can read- and write-access the repositories
- **First relevant rank:** >10
- **Top-1 retrieved (05_distributed-workflows):** The maintainer adds the contributor's repository as a remote and merges locally. 6. The maintainer pushes merged changes to the main repository. Integration-manager workflow This is a very common workflow with hub-based tools like GitHub o…

## semantic p85 - q098: wrong document

- **Question:** Which long-running branches does the Git project itself keep, and what is each one for?
- **Evidence (05_maintaining):** The Git project has four long-running branches: master, next, and seen (formerly 'pu' -- proposed updates) for new work, and maint for maintenance backports.
- **First relevant rank:** >10
- **Top-1 retrieved (03_nutshell):** Branches in a Nutshell To really understand the way Git does branching, we need to take a step back and examine how Git stores its data. As you may remember from ch01-getting-started#what_is_git_section, Git doesn't store data as a series …

## semantic p85 - q101: wrong document

- **Question:** What piece of information does GitHub use to attribute a commit to a particular member?
- **Evidence (06_1-setting-up-account):** The way that GitHub maps your Git commits to your user is by email address.
- **First relevant rank:** >10
- **Top-1 retrieved (10_environment):** Committing The final creation of a Git commit object is usually done by git-commit-tree, which uses these environment variables as its primary source of information, falling back to configuration values only if these aren't present. GIT_AU…

## semantic p85 - q103: wrong document

- **Question:** Why is it worth giving each uploaded public key a label such as the machine it belongs to?
- **Evidence (06_1-setting-up-account):** You can name each of your keys (e.g. "My Laptop" or "Work Account") so that if you need to revoke a key later, you can easily tell which one you're looking for.
- **First relevant rank:** >10
- **Top-1 retrieved (04_generating-ssh-key):** authorized_keys2 id_dsa known_hosts config id_dsa.pub You're looking for a pair of files named something like id_dsa or id_rsa and a matching file with a .pub extension. The .pub file is your public key, and the other file is the correspon…

## semantic p85 - q122: wrong document

- **Question:** Which numbered index slot holds the common ancestor of a conflicted file, and which one holds the incoming branch's copy?
- **Evidence (07_advanced-merging):** Stage 1 is the common ancestor, stage 2 is your version and stage 3 is from the MERGE_HEAD, the version you're merging in ("theirs").
- **First relevant rank:** >10
- **Top-1 retrieved (08_attributes):** index 88839c4..4afcb7c 100644 Binary files a/chapter1.docx and b/chapter1.docx differ You can't directly compare two versions unless you check them out and scan them manually, right?

## semantic p85 - q124: right document, wrong passage

- **Question:** Does Git work out automatically which refs belong in a bundle, or must I enumerate them?
- **Evidence (07_bundling):** With the bundle command you need to list out every reference or specific range of commits that you want to be included.
- **First relevant rank:** >10
- **Top-1 retrieved (07_bundling):** Now we have a commits.bundle file in our directory. If we take that and send it to our partner, she can then import it into the original repository, even if more work has been done there in the meantime. When she gets the bundle, she can i…

## semantic p85 - q125: wrong document

- **Question:** What artifact does Git produce from the data a push would normally send across the network?
- **Evidence (07_bundling):** The bundle command will package up everything that would normally be pushed over the wire with a git push command into a binary file
- **First relevant rank:** >10
- **Top-1 retrieved (02_remotes):** Pushing to Your Remotes When you have your project at a point that you want to share, you have to push it upstream. The command for this is simple: git push <remote> <branch>. If you want to push your master branch to your origin server (a…

## semantic p85 - q126: wrong document

- **Question:** What goes wrong if someone packages only their newest couple of commits and the receiving repository lacks the earlier ones?
- **Evidence (07_bundling):** If the bundler had created a bundle of just the last two commits they had done, rather than all three, the original repository would not be able to import it, since it is missing requisite history.
- **First relevant rank:** >10
- **Top-1 retrieved (03_rebasing):** This only works if C4 and C4' that your partner made are almost exactly the same patch. Otherwise the rebase won't be able to tell that it's a duplicate and will add another C4-like patch (which will probably fail to apply cleanly, since t…

## semantic p85 - q130: right document, wrong passage

- **Question:** Which credential helper ships with Git on Apple machines, and where does it keep the secrets?
- **Evidence (07_credentials):** If you're using macOS, Git comes with an "osxkeychain" mode, which caches credentials in the secure keychain that's attached to your system account.
- **First relevant rank:** 9
- **Top-1 retrieved (07_credentials):** It's just a series of lines, each of which contains a credential-decorated URL. The osxkeychain and wincred helpers use the native format of their backing stores, while cache uses its own in-memory format (which no other process can read).…

## semantic p85 - q132: wrong document

- **Question:** After tracking down the faulty revision, what command returns me to the checkout I had beforehand?
- **Evidence (07_debugging):** When you're finished, you should run git bisect reset to reset your HEAD to where you were before you started, or you'll end up in a weird state
- **First relevant rank:** >10
- **Top-1 retrieved (07_reset):** Summary Hopefully now you understand and feel more comfortable with the reset command, but are probably still a little confused about how exactly it differs from checkout and could not possibly remember all the rules of the different invoc…

## semantic p85 - q137: right document, wrong passage

- **Question:** Inside the menu-driven prompt, which letter or number takes a file back out of the staging area?
- **Evidence (07_interactive-staging):** If you want to unstage the TODO file at this point, you use the r or 3 (for revert) option
- **First relevant rank:** >10
- **Top-1 retrieved (07_interactive-staging):** The * next to each file means the file is selected to be staged. If you press Enter after typing nothing at the Update>> prompt, Git takes anything selected and stages it for you: Update>> updated 2 paths - Commands *** 1: [s]tatus 2: [u]p…

## semantic p85 - q138: right document, wrong passage

- **Question:** Which menu choice displays the changes already added to the staging area?
- **Evidence (07_interactive-staging):** To see the diff of what you've staged, you can use the d or 6 (for diff) command.
- **First relevant rank:** >10
- **Top-1 retrieved (07_interactive-staging):** You can see that this command shows you a much different view of your staging area than you're probably used to -- basically, the same information you get with git status but a bit more succinct and informative. It lists the changes you've…

## semantic p85 - q142: right document, wrong passage

- **Question:** When joining a short recent history to a long archived one, which two commits do you pair up?
- **Evidence (07_replace):** You can graft one history onto the other by "replacing" the earliest commit in the new line with the latest commit on the older one.
- **First relevant rank:** >10
- **Top-1 retrieved (07_replace):** First, rewinding head to replay your work on top of it... Applying: fourth commit Applying: fifth commit Rebasing the history on top of the base commit OK, so now we've re-written our recent history on top of a throw away base commit that …

## semantic p85 - q143: right document, wrong passage

- **Question:** Which low-level command turns a tree into a fresh commit object that has no parent?
- **Evidence (07_replace):** We can create our base commit using the commit-tree command, which just takes a tree and will give us a brand new, parentless commit object SHA-1 back.
- **First relevant rank:** >10
- **Top-1 retrieved (07_replace):** The commit-tree command is one of a set of commands that are commonly referred to as 'plumbing' commands. These are commands that are not generally meant to be used directly, but instead are used by other Git commands to do smaller jobs. O…

## semantic p85 - q144: wrong document

- **Question:** Apart from the config flag, which directory can I create inside one repository to switch the feature on there?
- **Evidence (07_rerere):** You can also turn it on by creating the .git/rr-cache directory in a specific repository, but the config setting is clearer and enables that feature globally for you.
- **First relevant rank:** >10
- **Top-1 retrieved (04_git-on-a-server):** This is generally straightforward to do. In order to clone your repository to create a new bare repository, you run the clone command with the --bare option. By convention, bare repository directory names end with the suffix .git, like so:…

## semantic p85 - q148: wrong document

- **Question:** Between resetting and checking out a branch, which one relocates the branch pointer and which relocates HEAD?
- **Evidence (07_reset):** Whereas reset will move the branch that HEAD points to, checkout will move HEAD itself to point to another branch.
- **First relevant rank:** 8
- **Top-1 retrieved (03_nutshell):** HEAD moves when you checkout That command did two things. It moved the HEAD pointer back to point to the master branch, and it reverted the files in your working directory back to the snapshot that master points to. This also means the cha…

## semantic p85 - q160: wrong document

- **Question:** How can you ask the log command to replay the whole evolution of a single function as patches?
- **Evidence (07_searching):** Simply run git log with the -L option, and it will show you the history of a function or line of code in your codebase.
- **First relevant rank:** 6
- **Top-1 retrieved (05_maintaining):** It looks something like this: From 330090432754092d704da8e76ca5c05c198e71a8 Mon Sep 17 00:00:00 2001 From: Jessica Smith <jessica@example.com> Date: Sun, 6 Apr 2008 10:17:23 -0700 Subject: [PATCH 1/2] Add limit to log function Limit log fu…

## semantic p85 - q162: wrong document

- **Question:** Which pickaxe-style log flag takes a regular expression rather than a fixed string?
- **Evidence (07_searching):** If you need to be more specific, you can provide a regular expression to search for with the -G option.
- **First relevant rank:** >10
- **Top-1 retrieved (02_recording-changes):** $ git rm log/\*.log Note the backslash (\) in front of the *. This is necessary because Git does its own filename expansion in addition to your shell's filename expansion. This command removes all files that have the .log extension in the …

## semantic p85 - q164: wrong document

- **Question:** From which release can merging and pulling be made to reject unsigned incoming commits, and with what argument?
- **Evidence (07_signing):** In Git 1.8.3 and later, git merge and git pull can be told to inspect and reject when merging a commit that does not carry a trusted GPG signature with the --verify-signatures command.
- **First relevant rank:** >10
- **Top-1 retrieved (06_3-maintaining):** So if someone opens a Pull Request in our repository and their branch is named bug-fix and it points to commit a5a775, then in our repository we will not have a bug-fix branch (since that's in their fork), but we will have pull/<pr#>/head …

## semantic p85 - q167: right document, wrong passage

- **Question:** Which tag flag replaces -a when you want the tag cryptographically signed?
- **Evidence (07_signing):** If you have a GPG private key set up, you can now use it to sign new tags. All you have to do is use -s instead of -a:
- **First relevant rank:** >10
- **Top-1 retrieved (07_signing):** Author: Scott Chacon <schacon@gee-mail.com> Date: Mon Mar 17 21:52:11 2008 -0700 Change version number Verifying Tags To verify a signed tag, you use git tag -v <tag-name>. This command uses GPG to verify the signature. You need the signer…

## semantic p85 - q168: wrong document

- **Question:** Since -u still skips files matched by ignore rules, what flag sweeps those in as well?
- **Evidence (07_stashing-cleaning):** including untracked files in the stash will still not include explicitly ignored files; to additionally include ignored files, use --all (or just -a).
- **First relevant rank:** 10
- **Top-1 retrieved (02_recording-changes):** That's because the -a flag includes all changed files. This is convenient, but be careful; sometimes this flag will cause you to include unwanted changes. Removing Files To remove a file from Git, you have to remove it from your tracked fi…

## semantic p85 - q170: right document, wrong passage

- **Question:** Which popular stash flag puts staged content into the saved entry yet still leaves that content ready for commit?
- **Evidence (07_stashing-cleaning):** The first option that is quite popular is the --keep-index option to the git stash command. This tells Git to not only include all staged content in the stash being created, but simultaneously leave it in the index.
- **First relevant rank:** 6
- **Top-1 retrieved (07_stashing-cleaning):** Stashing and Cleaning Often, when you've been working on part of your project, things are in a messy state and you want to switch branches for a bit to work on something else. The problem is, you don't want to do a commit of half-done work…

## semantic p85 - q176: wrong document

- **Question:** Since ordinary diff will not compare the vendored folder against the branch it came from, what must you use instead?
- **Evidence (07_subtree-merges):** you must run git diff-tree with the branch you want to compare to:
- **First relevant rank:** >10
- **Top-1 retrieved (07_advanced-merging):** Let's go through them all. To compare your result to what you had in your branch before the merge, in other words, to see what the merge introduced, you can run git diff --ours: $ git diff --ours - Unmerged path hello.rb diff --git a/hello…

## semantic p85 - q178: wrong document

- **Question:** Which plumbing command loads another branch's top-level tree into your index and working files?
- **Evidence (07_subtree-merges):** You'll learn more about read-tree and its friends in ch10-git-internals#ch10-git-internals, but for now know that it reads the root tree of one branch into your current staging area and working directory.
- **First relevant rank:** 8
- **Top-1 retrieved (07_replace):** The commit-tree command is one of a set of commands that are commonly referred to as 'plumbing' commands. These are commands that are not generally meant to be used directly, but instead are used by other Git commands to do smaller jobs. O…

## semantic p85 - q179: wrong document

- **Question:** Which two settings bring the vendored project's updates across with a ready-made commit message?
- **Evidence (07_subtree-merges):** To pull in the changes and prepopulate the commit message, use the --squash option, as well as the recursive merge strategy's -Xsubtree option.
- **First relevant rank:** >10
- **Top-1 retrieved (02_recording-changes):** ".git/COMMIT_EDITMSG" 9L, 283C You can see that the default commit message contains the latest output of the git status command commented out and one empty line on top. You can remove these comments and type your commit message, or you can…

## semantic p85 - q180: wrong document

- **Question:** Where do you declare that particular paths should be run through scripts on checkout and on staging, and what are those two processing steps named?
- **Evidence (08_attributes):** In the .gitattributes file, you can set a filter for particular paths and then set up scripts that will process files just before they're checked out ("smudge", see filters_a) and just before they're staged ("clean", see filters_b).
- **First relevant rank:** >10
- **Top-1 retrieved (07_reset):** With Paths The other way to run checkout is with a file path, which, like reset, does not move HEAD. It is just like git reset [branch] file in that it updates the index with that file at that commit, but it also overwrites the file in the…

## semantic p85 - q182: wrong document

- **Question:** Why might a content filter that works for you break for a colleague who clones the same project?
- **Evidence (08_attributes):** You have to be careful, though, because the .gitattributes file is committed and passed around with the project, but the driver (in this case, dater) isn't, so it won't work everywhere.
- **First relevant rank:** >10
- **Top-1 retrieved (07_rewriting-history):** The command is filter-branch, and it can rewrite huge swaths of your history, so you probably shouldn't use it unless your project isn't yet public and other people haven't based work off the commits you're about to rewrite.

## semantic p85 - q183: wrong document

- **Question:** In what time unit is the numeric value of the mistyped-command correction delay expressed?
- **Evidence (08_config):** help.autocorrect is actually an integer which represents tenths of a second.
- **First relevant rank:** 7
- **Top-1 retrieved (07_debugging):** 066b7ed955808 (Michal Marek 2014-07-04 14:29:30 +0200 78) Q = 066b7ed955808 (Michal Marek 2014-07-04 14:29:30 +0200 79) else 066b7ed955808 (Michal Marek 2014-07-04 14:29:30 +0200 80) quiet=quiet_ 066b7ed955808 (Michal Marek 2014-07-04 14:2…

## semantic p85 - q184: wrong document

- **Question:** Which configuration file is consulted first, and whose repositories does it affect?
- **Evidence (08_config):** The first place Git looks for these values is in the system-wide [path]/etc/gitconfig file, which contains settings that are applied to every user on the system and all of their repositories.
- **First relevant rank:** 7
- **Top-1 retrieved (07_debugging):** Notice that the first field is the partial SHA-1 of the commit that last modified that line. The next two fields are values extracted from that commit -- the author name and the authored date of that commit -- so you can easily see who mod…

## semantic p85 - q191: right document, wrong passage

- **Question:** Where does text printed by a server-side enforcement script end up?
- **Evidence (08_policy):** Anything your script echoes to stdout will be transferred to the client.
- **First relevant rank:** >10
- **Top-1 retrieved (08_policy):** The scripts we'll show are written in Ruby; partly because of our intellectual inertia, but also because Ruby is easy to read, even if you can't necessarily write it. However, any language will work – all the sample hook scripts distribute…

## semantic p85 - q194: wrong document

- **Question:** Which variable supplies fallback locations to search when an object is missing from the main object store?
- **Evidence (10_environment):** GIT_ALTERNATE_OBJECT_DIRECTORIES is a colon-separated list (formatted like /dir/one:/dir/two:…) which tells Git where to check for objects if they aren't in GIT_OBJECT_DIRECTORY.
- **First relevant rank:** >10
- **Top-1 retrieved (10_packfiles):** If you look in your objects directory, you'll find that most of your objects are gone, and a new pair of files has appeared: $ find .git/objects -type f git/objects/bd/9dbf5aae1a3862dd1526723246b20206e5fc37 git/objects/d6/70460b4b4aece5915…

## semantic p85 - q195: wrong document

- **Question:** How many unpacked objects or how many pack files does it take before the automatic cleanup actually does work?
- **Evidence (10_maintenance):** You must have around 7,000 loose objects or more than 50 packfiles for Git to fire up a real gc command.
- **First relevant rank:** >10
- **Top-1 retrieved (10_packfiles):** If you look in your objects directory, you'll find that most of your objects are gone, and a new pair of files has appeared: $ find .git/objects -type f git/objects/bd/9dbf5aae1a3862dd1526723246b20206e5fc37 git/objects/d6/70460b4b4aece5915…

## semantic p85 - q198: wrong document

- **Question:** How is the on-disk path of a stored object split up between folder name and file name?
- **Evidence (10_objects):** The subdirectory is named with the first 2 characters of the SHA-1, and the filename is the remaining 38 characters.
- **First relevant rank:** >10
- **Top-1 retrieved (10_packfiles):** It turns out that it can. The initial format in which Git saves objects on disk is called a "loose" object format. However, occasionally Git packs up several of these objects into a single binary file called a "packfile" in order to save s…

## semantic p85 - q199: wrong document

- **Question:** Is an object's checksum computed over its payload alone, or over something more?
- **Evidence (10_objects):** Git concatenates the header and the original content and then calculates the SHA-1 checksum of that new content.
- **First relevant rank:** 7
- **Top-1 retrieved (08_config):** `receive.fsckObjects` Git is capable of making sure every object received during a push still matches its SHA-1 checksum and points to valid objects. However, it doesn't do this by default; it's a fairly expensive operation, and might slow…

## semantic p85 - q201: wrong document

- **Question:** Besides the automatic repacking Git performs on its own, how can someone trigger a repack deliberately?
- **Evidence (10_packfiles):** Git will occasionally repack your database automatically, always trying to save more space, but you can also manually repack at any time by running git gc by hand.
- **First relevant rank:** >10
- **Top-1 retrieved (08_hooks):** This may mean moving in large binary files that you don't want source controlled, auto-generating documentation, or something along those lines. The post-merge hook runs after a successful merge command. You can use it to restore data in t…

## semantic p85 - q208: wrong document

- **Question:** What does HEAD normally hold, and how does that differ from an ordinary ref?
- **Evidence (10_refs):** Usually the HEAD file is a symbolic reference to the branch you're currently on. By symbolic reference, we mean that unlike a normal reference, it contains a pointer to another reference.
- **First relevant rank:** 10
- **Top-1 retrieved (07_reset):** Summary Hopefully now you understand and feel more comfortable with the reset command, but are probably still a little confused about how exactly it differs from checkout and could not possibly remember all the rules of the different invoc…

## semantic p85 - q210: wrong document

- **Question:** What does the leading plus sign in front of a mapping authorise Git to do?
- **Evidence (10_refspec):** The + tells Git to update the reference even if it isn't a fast-forward.
- **First relevant rank:** >10
- **Top-1 retrieved (02_aliases):** Date: Tue Aug 26 19:48:51 2008 +0800 Test for current head Signed-off-by: Scott Chacon <schacon@example.com> As you can tell, Git simply replaces the new command with whatever you alias it for. However, maybe you want to run an external co…

## semantic p85 - q212: wrong document

- **Question:** Why does pushing with nothing before the colon wipe out a branch upstream?
- **Evidence (10_refspec):** Because the refspec is <src>:<dst>, by leaving off the <src> part, this basically says to make the topic branch on the remote nothing, which deletes it.
- **First relevant rank:** >10
- **Top-1 retrieved (05_contributing):** This is called a refspec. See ch10-git-internals#_refspec for a more detailed discussion of Git refspecs and different things you can do with them. Also notice the -u flag; this is short for --set-upstream, which configures the branches fo…
