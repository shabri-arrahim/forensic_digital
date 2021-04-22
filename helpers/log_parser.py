import os
import sys

import logbook


class Logger:
    _logger = None

    def __init__(self, verbose=True):
        """init all helpers and services"""
        self.verbose = verbose
        self.filename, file_extension = os.path.splitext(os.path.basename(__file__))
        self._logger = logbook.Logger(name=self.filename)

    def get_logger(self):
        # Determine config directory
        log_file = os.path.join(
            os.path.abspath(os.path.dirname(__file__)),
            "../logs",
            "%s.log" % self.filename,
        )
        # init logger
        logbook.set_datetime_format("local")
        format_string = "%s %s" % (
            "[{record.time:%Y-%m-%d %H:%M:%S.%f%z}] {record.level_name}",
            "{record.module}:{record.lineno}: {record.message}",
        )
        if not self.verbose:
            log_handler = logbook.TimedRotatingFileHandler(
                log_file,
                level="INFO",
                date_format="%Y%m%d",
                backup_count=5,
                bubble=True,
                format_string=format_string,
            )
            self._logger.handlers.append(log_handler)

        log_handler = logbook.StreamHandler(
            sys.stdout, level="DEBUG", bubble=True, format_string=format_string
        )
        self._logger.handlers.append(log_handler)
        log_handler = logbook.TimedRotatingFileHandler(
            log_file,
            level="DEBUG",
            date_format="%Y%m%d",
            backup_count=5,
            bubble=True,
            format_string=format_string,
        )
        self._logger.handlers.append(log_handler)

        return self._logger
