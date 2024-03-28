# -*- coding: utf-8 -*-
#
#  Copyright (c) 2024 Ayakura Yuki
#  Released under the terms of the MIT License. See LICENSE for details.

import argparse
import platform
import sys

from colorama import init as color_init, Style

from gitupdater import __version__
from gitupdater.update import update_directories


def _decode(path):
    """decode the given string using the system filesystem encoding"""
    if sys.version_info.major > 2:
        return path
    return path.decode(sys.getfilesystemencoding())


def _build_parser():
    """build and return the argument parser"""
    parser = argparse.ArgumentParser(
            description="easily update multiple git repositories at once",
            epilog="Both relative and absolute paths are accepted by all arguments.",
            add_help=False)

    group_u = parser.add_argument_group("updating repositories")
    group_m = parser.add_argument_group("miscellaneous")

    # directories_to_update
    group_u.add_argument("directories_to_update", nargs="*", metavar="path", type=_decode,
                         help="""update this repository, or all repositories in contains 
                         if not a repo directly""")
    # max_depth: -t --depth
    group_u.add_argument("-t", "--depth", dest="max_depth", metavar="n", type=int, default=3,
                         help="""max recursion depth when searching for repositories in 
                         subdirectories, default is 3, use 0 fo no recursion, 
                         or -1 for unlimited""")
    # -c --current-only
    group_u.add_argument("-c", "--current-only", action="store_true",
                         help="""only fetch the remote tracked by the current branch 
                         instead of all remotes""")
    # -f --fetch-only
    group_u.add_argument("-f", "--fetch-only", action="store_true",
                         help="""only fetch remotes, don't try to fast-forward any branches""")
    # -p --prune
    group_u.add_argument("-p", "--prune", action="store_true",
                         help="""after fetching, delete remote-tracking branches that 
                         no longer exist on their remote""")

    # -h --help
    group_m.add_argument("-h", "--help", action="help", help="show this help message and exit")
    # -v --version
    group_m.add_argument("-v", "--version", action="version",
                         version="git-updater {0} (Python {1})".format(__version__, platform.python_version()))
    # --self-test
    group_m.add_argument("--self-test", action="store_true",
                         help="run integrated test suite and exit (required pytest)")

    return parser


def _self_test():
    """run the integrated test suite with pytest"""
    from .test import run_tests
    run_tests()


def main():
    """Parse arguments and then call the appropriate function(s)."""
    parser = _build_parser()
    color_init(autoreset=True)
    args = parser.parse_args()

    print(Style.BRIGHT + "[git-updater]" + Style.RESET_ALL + ": the git-repo-updater without bookmark")
    print()

    if args.self_test:
        _self_test()
        return

    _acted = False
    if args.directories_to_update:
        update_directories(args.directories_to_update, args)
        _acted = True


def run():
    """Thin wrapper for main()"""
    try:
        main()
    except KeyboardInterrupt:
        print("stopped by user")
