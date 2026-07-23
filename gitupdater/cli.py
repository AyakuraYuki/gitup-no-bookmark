# -*- coding: utf-8 -*-
#
# Copyright (c) 2024 Ayakura Yuki
# Released under the terms of the MIT License. See LICENSE for details.

import argparse
import platform

from colorama import init as color_init, Style

from gitupdater import __version__
from gitupdater.update import update_directories


def _build_parser():
    """Build and return the argument parser."""
    parser = argparse.ArgumentParser(
        description="Easily update multiple git repositories at once.",
        epilog="Both relative and absolute paths are accepted by all arguments.",
        add_help=False,
    )

    group_u = parser.add_argument_group("updating repositories")
    group_m = parser.add_argument_group("miscellaneous")

    group_u.add_argument(
        "directories_to_update",
        nargs="*",
        metavar="path",
        help="""update this repository, or all repositories it contains
                (if not a repo directly)""",
    )
    group_u.add_argument(
        "-t",
        "--depth",
        dest="max_depth",
        metavar="n",
        type=int,
        default=3,
        help="""max recursion depth when searching for repos in subdirectories
                (default: 3; use 0 for no recursion, or -1 for unlimited)""",
    )
    group_u.add_argument(
        "-c",
        "--current-only",
        action="store_true",
        help="""only fetch the
                remote tracked by the current branch instead of all remotes""",
    )
    group_u.add_argument(
        "-f",
        "--fetch-only",
        action="store_true",
        help="only fetch remotes, don't try to fast-forward any branches",
    )
    group_u.add_argument(
        "-p",
        "--prune",
        action="store_true",
        help="""after fetching, delete
            remote-tracking branches that no longer exist on their remote""",
    )

    group_m.add_argument(
        "-h", "--help", action="help", help="show this help message and exit"
    )
    group_m.add_argument(
        "-v",
        "--version",
        action="version",
        version="git-updater {0} (Python {1})".format(__version__, platform.python_version()),
    )
    group_m.add_argument(
        "--selftest",
        action="store_true",
        help="run integrated test suite and exit (pytest must be available)",
    )

    return parser


def _selftest():
    """Run the integrated test suite with pytest."""
    from .test import run_tests

    run_tests()


def main():
    """Parse arguments and then call the appropriate function(s)."""
    parser = _build_parser()
    color_init(autoreset=True)
    args = parser.parse_args()

    print(Style.BRIGHT + "[git-updater]" + Style.RESET_ALL + ": the git-repo-updater")
    print()

    if args.selftest:
        _selftest()
        return

    _acted = False
    if args.directories_to_update:
        update_directories(args.directories_to_update, args)
        _acted = True


def run():
    """Thin wrapper for main() that catches KeyboardInterrupts."""
    try:
        main()
    except KeyboardInterrupt:
        print("Stopped by user.")


if __name__ == "__main__":
    """Thin wrapper for main()"""
    try:
        main()
    except KeyboardInterrupt:
        print("Stopped by user.")
