# -*- coding: utf-8 -*-
#
# Copyright (c) 2024 Ayakura Yuki
# Released under the terms of the MIT License. See LICENSE for details.


def run_tests(args=None):
    import pytest

    if args is None:
        args = ["-v", "-rxw"]
    return pytest.main(args)
