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

## about this project

it is for knowing how `gitup` works, and make it pure to just update given base dir

## Installation

### From source

First

```shell
git clone --depth=1 https://github.com/AyakuraYuki/gitup-no-bookmark.git
cd gitup-no-bookmark
```

Then to install for everyone:

```shell
sudo python setup.py install
```

or for just yourself (make sure you have `~/.local/bin` in your `PATH`):

```shell
python setup.py install --user
```

Finally, simply delete the `gitup-no-bookmark` directory and you're done!

Note: If you are using Windows, you may wish to add a macro, so you can invoke
`git-updater` in any directory. Note that `C:\Python27` refers to the
directory where Python is installed:

```shell
DOSKEY git-updater=c:\python27\python.exe c:\python27\Scripts\git-updater $*
```
