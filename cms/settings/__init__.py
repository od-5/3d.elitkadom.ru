__author__ = 'alexy'

from .base import *
from .apps import *
from .middleware import *
from .other import *
from .suit import *
try:
    from local_settings import *
except ImportError:
    pass