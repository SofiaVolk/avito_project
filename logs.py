import logging.config

LOGGING = {
    'version': 1,
    'formatters': {  # Форматирование сообщения
        'simple': {
            'format': '127.0.0.1 - - [%(asctime)s] %(levelname)-8s %(module)-s  %(message)-s',
            'datefmt': '%d/%m/%Y %H:%M:%S'
        },
    },

    'handlers': {  # Обработчики сообщений
        'api_log_handler': {
            'class': 'logging.FileHandler',
            'filename': '/tmp/api_logs',
            'formatter': 'simple',
        },
        'streamlogger': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },

    'loggers': {   # Логгеры
        'api_logger': {
            'handlers': ['api_log_handler', 'streamlogger'],
            'level': 'INFO',
        },
    },
}


logging.config.dictConfig(LOGGING)
api_logger = logging.getLogger('api_logger')