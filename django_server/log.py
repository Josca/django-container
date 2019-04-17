import logging
from logstash_formatter import LogstashFormatterV1


class LogstashLowerLevelFormatterV1(LogstashFormatterV1):

    def __init__(self, *args, **kwargs):
        super(LogstashLowerLevelFormatterV1, self).__init__(*args, **kwargs)
        logging.addLevelName(logging.INFO, "info")
        logging.addLevelName(logging.DEBUG, "debug")
        logging.addLevelName(logging.WARNING, "warning")
        logging.addLevelName(logging.ERROR, "error")
        logging.addLevelName(logging.FATAL, "fatal")
