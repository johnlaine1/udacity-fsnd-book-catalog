#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/catalog_app/")

import config
from main import app as application

application.secret_key = config.secret_key

