"""Handlers with default formatters.

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
from typing import Optional, Any

import colorlog


class StreamHandler(logging.StreamHandler):
    """Represents a StreamHandler.
    Subclasses logging.StreamHandler
    Logs directly to the console output, defaults to a predefined colorlog colored formatter
    """

    def __init__(self, formatter: Optional[Any] = None) -> None:
        super().__init__()
        if formatter is None:
            colors = {
                'DEBUG': 'cyan',
                'INFO': 'green',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'red',
            }
            formatter = colorlog.ColoredFormatter(
                '%(light_green)s%(asctime)s %(red)s%(name)s %(log_color)s%(levelname)s %(yellow)s[%(filename)s:%(lineno)d]%(reset)s %(message)s',
                datefmt='%d-%m-%Y %H:%M:%S',
                log_colors=colors,
            )
        self.setFormatter(formatter)


class FileHandler(logging.FileHandler):
    """Represents a FileHandler.
    Subclasses logging.StreamHandler
    Logs to a file, defaults to a predefined formatter
    """

    def __init__(self, path, formatter: Optional[Any] = None) -> None:
        super().__init__(filename=path, encoding='utf-8')
        if formatter is None:
            formatter = logging.Formatter(
                '%(asctime)s %(name)s %(levelname)-4s [%(filename)s:%(lineno)d] %(message)s', datefmt='%d-%m-%Y %H:%M:%S'
            )
        self.setFormatter(formatter)
