#!C:\Users\skruvi\PycharmProjects\WorldOfGames\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'aws==0.2.5','console_scripts','aws'
__requires__ = 'aws==0.2.5'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('aws==0.2.5', 'console_scripts', 'aws')()
    )
