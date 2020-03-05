# -*- coding: utf-8 -*-
# Copyright (C) Cardiff University (2020)
#
# This file is part of ciecplib.
#
# ciecplib is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ciecplib is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ciecplib.  If not, see <http://www.gnu.org/licenses/>.

"""Tests for :mod:`ciecplib.tool.ecp_get_cert`
"""

try:
    from unittest import mock
except ImportError:  # python < 3
    import mock
    FileNotFoundError = OSError

import pytest

from .. import ecp_get_cert


@mock.patch("os.unlink", mock.Mock(side_effect=(None, FileNotFoundError)))
@pytest.mark.parametrize("dummy", (True, False))
def test_destroy(dummy):
    """Check that the --destory option works whether the file exists or not
    """
    ecp_get_cert.main(["user", "--destroy"])