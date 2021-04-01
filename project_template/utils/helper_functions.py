# coding=utf-8
# Copyright 2018 George Mihaila.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Helper functions.
"""

import numpy as np
import logging
from time import time

import yaml

logger = logging.getLogger(__name__)

def power_up(use_number, use_power):
    """
    Return power of a number in numpy array format.
    """

    return np.power(use_number, use_power)

def get_yaml_content(use_path):
    """
    Read file in YAML format.
    """
    with open(use_path, "r") as file_stream:
        yaml_content = yaml.safe_load(file_stream)

    return yaml_content

def print_execution_time(function):
    """
    Measuring running time.
    """

    def timed(*args, **kw):
        time_start = time()
        return_value = function(*args, **kw)
        time_end = time()
        execution_time = time_end - time_start
        logger.info("`%s` ran in %.2f seconds.", function.__name__, execution_time)
        return return_value

    return timed
