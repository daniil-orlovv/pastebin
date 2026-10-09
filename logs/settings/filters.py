import logging


class ErrorLogFilter(logging.Filter):

    def filter(self, record):
        return record.levelname == 'ERROR'


class InfoLogFilter(logging.Filter):

    def filter(self, record):
        return record.levelname == 'INFO'
