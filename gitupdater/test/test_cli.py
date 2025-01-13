# -*- coding: utf-8 -*-
#
# Copyright (c) 2024 Ayakura Yuki
# Released under the terms of the MIT License. See LICENSE for details.

from __future__ import print_function, unicode_literals

import platform
import subprocess
import sys

from gitupdater import __version__


def run_cli(*args):
    cmd = [sys.executable, "-m", "git-updater"] + list(args)
    output = subprocess.check_output(cmd)
    return output.strip().decode("utf8")


def test_cli_version():
    output = run_cli("--version")
    expected = "git-updater {0} (Python {1})".format(__version__, platform.python_version())
    assert output == expected
