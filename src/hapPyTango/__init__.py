from gevent import monkey
monkey.patch_all()

import os
import sys
sys.path.insert(0, os.path.dirname(__file__))

from .client import *
