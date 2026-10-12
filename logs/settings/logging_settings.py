from datetime import time

from logs.settings.filters import ErrorLogFilter, InfoLogFilter

logging_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '#%(levelname)-8s %(name)s:%(funcName)s - %(message)s'
        },
        'custom_formatter': {
            'format': ('[%(asctime)s.%(msecs)03d] %(filename)-22s'
                       ':%(lineno)-4d #%(levelname)s - %(message)s'),
            'datefmt': '%d-%m-%Y %H:%M:%S'
        },
        'lite_formatter': {
            'format': ('[%(asctime)s.%(msecs)03d] #%(levelname)s - '
                       '%(message)s'),
            'datefmt': '%d-%m-%Y %H:%M:%S'
        },
    },
    'filters': {
        'info_filter': {
            '()': InfoLogFilter,
        },
        'error_filter': {
            '()': ErrorLogFilter,
        },
    },
    'handlers': {
        'default': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        },
        'error_file': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': 'logs/errors.log',
            'when': 'midnight',
            'atTime': time(9, 0),
            'backupCount': 7,
            'level': 'DEBUG',
            'formatter': 'custom_formatter',
            'filters': ['error_filter'],
            'encoding': 'utf-8'
        },
        'info_file': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': 'logs/info.log',
            'when': 'midnight',
            'atTime': time(9, 0),
            'backupCount': 7,
            'formatter': 'custom_formatter',
            'filters': ['info_filter'],
            'encoding': 'utf-8'
        },
        'custom_apscheduler': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': 'logs/apscheduler.log',
            'when': 'midnight',
            'atTime': time(9, 0),
            'backupCount': 7,
            'formatter': 'lite_formatter',
            'encoding': 'utf-8'
        },
    },
    'loggers': {
        '__main__': {
            'level': 'INFO',
            'handlers': ['error_file', 'info_file'],
            'propagate': False
        },
        'uvicorn': {
            'handlers': ['default', 'info_file'],
            'level': 'INFO',
            'propagate': False
        },
        'uvicorn.error': {
            'handlers': ['default', 'error_file'],
            'level': 'INFO',
            'propagate': False
        },
        'uvicorn.access': {
            'handlers': ['default', 'info_file'],
            'level': 'INFO',
            'propagate': False
        },
        'api.fastapi.routers.ping': {
            'level': 'INFO',
            'handlers': ['default', 'info_file', 'error_file'],
            'propagate': False
        },
        'apscheduler': {
            'level': 'DEBUG',
            'handlers': ['custom_apscheduler'],
            'propagate': False
        },
    },
    'root': {
        'formatter': 'default',
        'handlers': ['default']
    },
}
