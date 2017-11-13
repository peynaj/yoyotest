import os

FILE_PATH = os.path.abspath(__file__)
PROJECT_DIR = '/'.join(FILE_PATH.split('/')[:-1])

# --- postgres connection ---
USERNAME = 'DBUSERNAME'
DBNAME = 'DBNAME'
PASSWORD = 'PASSWORD'

from local_setting import *

