# gitup-no-bookmark

> gitup is a tool for updating multiple git repositories at once.
> It is smart enough to handle several remotes, dirty working directories,
> diverged local branches, detached HEADs, and more. It was originally
> created to manage a large collection of projects and deal with sporadic
> internet access.
>
> gitup should work on macOS, Linux, and Windows. You should have the
> latest version of git and either Python 2.7 or Python 3 installed.

`gitup-no-bookmark` is `gitup` without bookmark, rewrite from [earwig/git-repo-updater](https://github.com/earwig/git-repo-updater)

this tool is just an updater, and I removed all features that I **don't** need

**I highly recommend you use the [original version](https://github.com/earwig/git-repo-updater) to support [earwig](https://github.com/earwig).**

> ## Installation
>
> With [pip](https://github.com/pypa/pip/):
>
>     pip install gitup
>
> With [Homebrew](http://brew.sh/):
>
>     brew install gitup

see more details in [earwig/git-repo-updater](https://github.com/earwig/git-repo-updater), **please**

## About this project

it is for knowing how `gitup` works, and make it pure to just update given base dir

## Usage

```text
usage: git-updater [-t n] [-c] [-f] [-p] [-h] [-v] [--self-test] [path ...]

easily update multiple git repositories at once

updating repositories:
  path                update this repository, or all repositories in contains if not a repo directly
  -t n, --depth n     max recursion depth when searching for repositories in subdirectories, default is 3, use 0 fo no recursion, or -1 for unlimited
  -c, --current-only  only fetch the remote tracked by the current branch instead of all remotes
  -f, --fetch-only    only fetch remotes, don't try to fast-forward any branches
  -p, --prune         after fetching, delete remote-tracking branches that no longer exist on their remote

miscellaneous:
  -h, --help          show this help message and exit
  -v, --version       show program's version number and exit
  --self-test         run integrated test suite and exit (required pytest)

Both relative and absolute paths are accepted by all arguments.

```

## Installation

### From source

First, get ready with Python 3.12 and pipenv installed, then clone this repository:

```shell
git clone --depth=1 https://github.com/AyakuraYuki/gitup-no-bookmark.git
cd gitup-no-bookmark
```

I use PyInstaller to package the standalone executable program, use the following command to package:

```shell
pipenv shell
pipenv sync
pipenv run package
```
