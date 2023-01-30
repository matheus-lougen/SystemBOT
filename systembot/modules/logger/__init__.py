import logging
import functools
from typing import Optional, List

from .handlers import StreamHandler, FileHandler
from .formatters import Formatter, ColoredFormatter

DEBUG = 10
INFO = 20
WARNING = 30
ERROR = 40
CRITICAL = 50


def create(name: str, level=DEBUG, handlers: list = None) -> None:
    log = logging.getLogger(name)
    log.setLevel(logging.DEBUG)

    if isinstance(handlers, list):
        for handler in handlers:
            log.addHandler(handler)
            handler.setLevel(level)
        log.debug(f'New logger sucessfully created [{name}]')
    else:
        raise TypeError(f'Handlers has to be of type List not {type(handlers)}')

def get(name: str) -> logging.Logger:
    return logging.getLogger(name)
