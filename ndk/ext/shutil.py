#
# Copyright (C) 2017 The Android Open Source Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""Extensions for shutil APIs."""
from __future__ import absolute_import

import errno
import os
import sys


def create_directory(path):
    """Creates a directory, ignoring errors if the directory exists."""
    try:
        os.makedirs(path)  # pylint: disable=no-member
    except OSError as ex:
        if ex.errno != errno.EEXIST:
            raise


if sys.version_info >= (3, 3):
    import shutil

    def which(cmd, path=None):
        return shutil.which(cmd, path=path)  # pylint: disable=no-member
else:
    # virtualenv does tricks for distutils, so this fails pylint in virtualenv.
    import distutils.spawn  # pylint: disable=no-name-in-module,import-error

    def which(cmd, path=None):
        # pylint: disable=no-member
        return distutils.spawn.find_executable(cmd, path=path)
        # pylint: enable=no-member
