# logging
import logging

from pathlib import Path


log_dir = Path.cwd()
logging.basicConfig(level=logging.INFO,
					format='%(levelname)s, %(asctime)s, %(filename)s, %(funcName)s, %(message)s',
					filename='{dir_name}/logfile.log'.format(dir_name=log_dir),
					filemode='a')
logger = logging.getLogger('')