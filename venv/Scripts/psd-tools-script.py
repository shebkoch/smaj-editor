#!D:\Projects\smaj-editor\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'psd-tools3==1.8.2','console_scripts','psd-tools'
__requires__ = 'psd-tools3==1.8.2'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('psd-tools3==1.8.2', 'console_scripts', 'psd-tools')()
    )
