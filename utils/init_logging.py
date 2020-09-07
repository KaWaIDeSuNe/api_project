
#
# Author: ldq <15611213733@163.com>
# Date:   2017-6-26

import logging
import logging.handlers

from project_config import project_config


def init_log(log_name, file_name):
    log_path = project_config.LOG_PATH_BASE + file_name
    LOGGER = logging.getLogger(log_name)
    formatter = logging.Formatter('%(name)-12s %(asctime)s %(levelname)-8s '
                                  '%(filename)s (%(lineno)d)\t####\t'
                                  '%(message)s', '%a, %d %b %Y %H:%M:%S',)
    file_handler = logging.handlers.TimedRotatingFileHandler(
        log_path, "midnight", project_config.LOG_INTERVAL)
    file_handler.suffix = "%Y%m%d"
    file_handler.setFormatter(formatter)
    LOGGER.addHandler(file_handler)
    LOGGER.setLevel(logging.INFO)
    return LOGGER
