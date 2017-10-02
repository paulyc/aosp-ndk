#!/usr/bin/env python
#
# Copyright (C) 2015 The Android Open Source Project
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
"""Builds ndk-depends."""
from __future__ import print_function

import os
import site

site.addsitedir(os.path.join(os.path.dirname(__file__), '../../../build/lib'))

import build_support  # pylint: disable=import-error


def main(args):
    src_dir_arg = '--src-dir={}'.format(build_support.toolchain_path())

    build_cmd = [
        'bash', 'build-ndk-depends.sh', src_dir_arg,
    ]

    if args.host in ('windows', 'windows64'):
        build_cmd.append('--mingw')

    if args.host != 'windows':
        build_cmd.append('--try-64')

    build_cmd.append(
        '--build-dir=' + os.path.join(args.out_dir, 'ndk-depends'))

    build_support.build(build_cmd, args)

if __name__ == '__main__':
    build_support.run(main)
