# coding: utf-8
from __future__ import print_function

import os
import sys
import logging


LOG_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'log')
if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)

LOGGER = logging.getLogger('ProfileInspector')
LOGGER.propagate = False
LOGGER.setLevel(logging.DEBUG)

BASE_FORMAT = logging.Formatter(
    '[%(asctime)s]  %(levelname)-10s %(filename)-20s %(funcName)-25s :: %(message)s',
    "%m-%d %I:%M%p")


def set_critical():
    critical = logging.FileHandler(os.path.join(LOG_PATH, 'errors.log'), 'w')
    critical.setLevel(logging.ERROR)
    critical.setFormatter(BASE_FORMAT)
    critical.set_name('Critical')
    return critical


def set_debug():
    debug = logging.FileHandler(os.path.join(LOG_PATH, 'debug.log'), 'w')
    debug.setLevel(logging.DEBUG)
    debug.setFormatter(BASE_FORMAT)
    return debug


def set_console():
    console_format = logging.Formatter(
        '%(name)s %(levelname)-8s %(module)-10s%(funcName)-15sL:%(lineno)-5d :: %(message)s')
    console = logging.StreamHandler(stream=sys.stdout)
    console.set_name('Console')
    console.setLevel(logging.WARNING)
    console.setFormatter(console_format)
    return console


LOGGER.addHandler(set_console())
LOGGER.addHandler(set_critical())
LOGGER.addHandler(set_debug())
