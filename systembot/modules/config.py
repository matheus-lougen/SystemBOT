import os
import yaml
import logging
from typing import Optional

from systembot.modules import logger


class Config():
    def __init__(self, path: str,
                 formatter_style: str = '%(asctime)s %(name)s %(levelname)-4s [%(filename)s:%(lineno)d] %(message)s',
                 colored_formatter_style: str ='%(light_green)s%(asctime)s %(red)s%(name)s %(log_color)s%(levelname)s %(yellow)s[%(filename)s:%(lineno)d]%(reset)s %(message)s'
                ) -> None:

        self.log = self.setup_logging(formatter_style, colored_formatter_style)
        self.path = self.check_path(path)
        if self.path:
            self.load_file(self.path)

    def setup_logging(self, formatter_style: str, colored_formatter_style: str) -> logging.Logger:
        formatter = logger.Formatter(formatter_style)
        colored_formatter = logger.ColoredFormatter(colored_formatter_style)
        logger.create('config',
                      level=logger.DEBUG,
                      handlers=[logger.StreamHandler(formatter=colored_formatter),
                                logger.FileHandler('./data/logs/config.log', formatter=formatter)])
        return logger.get('config')

    def check_path(self, path: str) -> Optional[str]:
        if os.path.exists(path):
            self.log.debug(f'Found valid config file at [{path}]')
            return path
        else:
            self.log.critical(f'Could NOT find a valid configuration file at [{path}]')

    def load_file(self, path):
        try:
            with open(path, 'r') as file:
                content = yaml.safe_load(file)
        except Exception as e:
            self.log.exception('An exception ocurred while reading the configuration file')
        else:
            for key in content:
                setattr(self, key, content[key])
