
===========================
Git, as far as I understand
===========================

-------
Summary
-------

+ Main differences with SVN

+ Hands on
    + creating a repository
    + controlling the staging area
    + remotes
    + branching and merging
    + using the stash

-------------------------
Main differences with SVN
-------------------------

+ You have the local history: fast
+ Staging area: control your commits
+ No central repository: everybody is a repo


---------------------
Creating a repository
---------------------

Simple.

::

    git init       # create in local dir
    git clone url  # copy existing repo

------------
Staging area
------------

Intermediate place where you put changes before committing.

::

    git add file # staged
    git commit   # commit the changes

-------------
Communication
-------------

How to share stuff.

::

    git push     # send commits to another repository
    git pull     # receive commits from another repository

-------------------------
Staging area, like a boss
-------------------------

You can control every single line of changes staged.

::

    git add -p # edit your patches...
    git commit

-------
Remotes
-------

A remote is an alias.

::

    git remote -v           # list remotes
    git remote add name url # add remote
    git remote rm name      # rm remote

---------
Branching
---------

Branches are cheap.

::

    git branch name   # create branch
    git checkout name # switch branch
    git merge name    # merge branch


---------
The stash
---------

The stash is a place were your stash changes.
Useful to save without committing.

::

    git stash # in firstbranch
    git checkout otherbranch

    # do stuff
    git checkout firstbranch
    git stash apply

-------------
gitattributes
-------------

You knew .gitignore, but do you know .gitattributes?
How to view diffs inside zip files:

::

    # Your .gitattributes
    *.zip diff=zip

    # Your .gitconfig
    [diff "zip"]
        textconv = unzip -c -a


----------
Submodules
----------

To have foreign repository in your repository.

::

    git submodule add ...
    git submodule init
    git submodule update

