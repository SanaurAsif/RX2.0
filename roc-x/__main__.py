__version__ = '1.0.0'
__author__ = 'SanaurAsif'
__date__ = '14.06.2022'
__license__ = 'MIT'
__copyright__ = 'Copyright (c) 2022 roc-x'
__email__ = 'rootofcyber@gmail.com'
__status__ = 'Development'

from main import Services
import os

# COLOR_VALUE

BLUE = '\33[94m'
LIGHT_BLUE = '\033[94m'
RED = '\033[91m'
WHITE = '\33[97m'
YELLOW = '\33[93m'
GREEN = "\033[0;92m"
CYAN = "\033[96m"
END = '\033[0m'
BLACK = "\033[0;30m"

# HEADER

LINE = YELLOW + "===================================================" \
                "===================================================================" + END
SPACE = " "
LOGO = RED + str("""
   8888888b.  Y88b   d88P  .d8888b.       .d8888b.  
   888   Y88b  Y88b d88P  d88P  Y88b     d88P  Y88b 
   888    888   Y88o88P          888     888    888 
   888   d88P    Y888P         .d88P     888    888 
   8888888P"     d888b     .od888P"      888    888 
   888 T88b     d88888b   d88P"          888    888 
   888  T88b   d88P Y88b  888"       d8b Y88b  d88P 
   888   T88b d88P   Y88b 888888888  Y8P  "Y8888P"               
""") + END

notice = ""


def header():
    print(LOGO + CYAN + "\n\n\t\t   Developed By : Sanaur Asif\n\n" + GREEN + "\t\t       Version : " + str(
        __version__) + " \n\n" + END + LINE + "\n" + END)


def clear():
    os.system("clear || cls")


rocx = Services()

packages = ["requests"]
to_install = rocx.check_requirements(packages)

if to_install:
    rocx.install_requirements(to_install)

rocx.must_require(packages)

header()
