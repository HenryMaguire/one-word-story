
import sys
from .config import PACKAGE_ROOT
from ows_language_model.config import config
config.temperature = 1.1
config.N_MAX_WORDS_GENERATED = 40

with open(PACKAGE_ROOT / 'VERSION') as version_file:
    __version__ = version_file.read().strip()