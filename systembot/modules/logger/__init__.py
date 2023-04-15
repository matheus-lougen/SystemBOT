"""A logging library wrapper to make logging easy and simple.

MIT License

Copyright (c) 2023 Matheus Lougen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import logging

from typing import List, Union, Optional

from .handlers import FileHandler, StreamHandler

DEBUG = 10
INFO = 20
WARNING = 30
ERROR = 40
CRITICAL = 50


def create(
    name: str, level: int = DEBUG, handlers: List[Union[FileHandler, StreamHandler]] = None
) -> Optional[logging.Logger]:
    """Create a logger instance
    Returns a logger instance ready to use, defaults the handlers formatter to default values
    """
    log = logging.getLogger(name)
    log.setLevel(logging.DEBUG)

    for handler in handlers:
        log.addHandler(handler)
        handler.setLevel(level)

    return log


def get(name: str) -> logging.Logger:
    """Get a logger instance
    Returns the logger instance
    """
    return logging.getLogger(name)
