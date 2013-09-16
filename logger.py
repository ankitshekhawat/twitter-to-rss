# logger.py
#
# Basuc custom logger with local timestamping feature. Writes to a file
#
# Requires: 
# pytz              | easy_install --upgrade pytz   | http://pytz.sourceforge.net/
# datetime
#
#
# Created by: Ankit Shekhawat
# Website: http://www.ankit.ws
#
# # USAGE: 
# from logger import Logger
# log = Logger('log_file.txt', 'UTC')
# 
# log.debug('Message')
# log.info('Message')
# log.warn('Message')
# log.error('Message')
# log.critical('Message')
# 
# log.separator = ' : '
# log.fmt = '%Y-%m-%d %H:%M:%S %p  %Z' - strftime time format
# log.set_level_to('WARNING') - show only messages warning or more
# 


import pytz
from datetime import datetime


class Logger:
	"""Custom logger  to log and print to file with localized timestamp feature 
		requrires: PYTZ
	"""

	def __init__(self, filename, locale='UTC'):
		self.file = filename
		self.locale = pytz.timezone(locale)
		self.separator = ' | ' 
		self.fmt = '%Y-%m-%d %H:%M:%S %p  %Z'
		self.level = 4
		self.key ={'DEBUG': 4, 'INFO': 3, 'WARNING': 2, 'ERROR': 1, 'CRITICAL' : 0 }

	def set_level_to(self, key):
		self.level= self.key[key]

	def print_log(self, message, level='DEBUG'):
		utctime = pytz.timezone('utc').localize(datetime.utcnow())
		localtime = utctime.astimezone(self.locale).strftime(self.fmt)
		string = localtime + self.separator + level + self.separator + message
		print string
		with open(self.file, 'a') as the_file:
			the_file.write(string + '\n')
 
	def debug(self, message, name=''):
		if self.level >= self.key['DEBUG']:
			self.print_log(message, 'DEBUG')

	def info(self, message):
		if self.level >= self.key['INFO']:
			self.print_log(message, 'INFO')

	def warn(self, message):
		if self.level >= self.key['WARNING']:
			self.print_log(message, 'WARNING')

	def error(self, message):
		if self.level >= self.key['ERROR']:
			self.print_log(message, 'ERROR')

	def critical(self, message):
		if self.level >= self.key['CRITICAL']:
			self.print_log(message, 'CRITICAL')	