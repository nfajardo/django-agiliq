LOGGING = {
	'version':1,
	'disable_existing_loggers': False,
	'formatters':{
		'large':{
			'format':'%(asctime)s  %(levelname)s  %(process)d  %(pathname)s  %(funcName)s  %(lineno)d  %(message)s  '
		},
		'tiny':{
			'format':'%(asctime)s  %(message)s'
		}
	},
	'handlers':{
		'db_log': {
            'level': 'DEBUG',
            'class': 'django_db_logger.db_log_handler.DatabaseLogHandler',
			'formatter':'large',
        },
	},
	'loggers':{
		'db': {
            'handlers': ['db_log'],
            'level': 'DEBUG'
        },
	},
}