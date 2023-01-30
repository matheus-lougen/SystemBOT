"""Logging formatters"""

import logging

import colorlog


class Formatter(logging.Formatter):
    """A simple formatter to be used on files"""
    def __init__(self,
                 format_style: str,
                 date_style: str = '%d-%m-%Y %H:%M:%S',) -> None:

        super().__init__(format_style, datefmt=date_style, style='%')


class ColoredFormatter(colorlog.ColoredFormatter):
    """A colored formatter to be used on terminal for a more pleasant view"""
    def __init__(self,
                 format_style,
                 colors: dict = None,
                 date_style: str = '%d-%m-%Y %H:%M:%S') -> None:

        if isinstance(colors, type(None)):
            colors={
                'DEBUG': 'cyan',
                'INFO': 'green',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'red',
            }
        super().__init__(format_style, datefmt=date_style, style='%', log_colors=colors)

