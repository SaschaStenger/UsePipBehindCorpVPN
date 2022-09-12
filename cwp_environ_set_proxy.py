# -*- coding: utf-8 -*-
# this script is used on windows to wrap shortcuts so that they are executed within an environment
#   It only sets the appropriate prefix PATH entries - it does not actually activate environments

import os
import sys
import subprocess
from os.path import join, pathsep
import urllib.parse

from menuinst.knownfolders import FOLDERID, get_folder_path, PathNotFoundException

# call as: python cwp.py PREFIX ARGs...


if (sys.version_info > (3, 0)):
    # Python 3 code in this block
    from tkinter import Tk
    from tkinter.simpledialog import askstring
    from os import getlogin
else:
    from Tkinter import Tk
    from tkSimpleDialog import askstring
    from getpass import getuser as getlogin
    

root = Tk() # dialog needs a root window, or will create an "ugly" one for you
root.withdraw() # hide the root window
pwd = askstring("Password", "Enter password:", show='*', parent=root)
root.destroy() # clean up after yourself!
username = getlogin()


os.environ["HTTP_PROXY"] = "http://%s:%s@proxy.yourproxy.local:8080" % (username, urllib.parse.quote(pwd))
os.environ["HTTPS_PROXY"] = "http://%s:%s@proxy.yourproxy.local:8080" % (username, urllib.parse.quote(pwd))
os.environ['REQUESTS_CA_BUNDLE'] = os.path.dirname(os.path.realpath(__file__)) + '/ROOT-CA.crt'
del username
del pwd
del root

try:
    import requests
    
    r = requests.get("http://httpbin.org/get", verify=False,)
    if r.status_code != 200:
        os.environ["HTTPS_PROXY"] = ""
        os.environ["HTTP_PROXY"] = ""

        raise Exception("Proxy Auth not successfull")
except ModuleNotFoundError as e:
    pass        
except Exception as e:
    os.environ["HTTPS_PROXY"] = ""
    os.environ["HTTP_PROXY"] = ""

    raise
    sys.exit("stop")



prefix = sys.argv[1]
args = sys.argv[2:]

new_paths = pathsep.join([prefix,
                         join(prefix, "Library", "mingw-w64", "bin"),
                         join(prefix, "Library", "usr", "bin"),
                         join(prefix, "Library", "bin"),
                         join(prefix, "Scripts")])
env = os.environ.copy()
env['PATH'] = new_paths + pathsep + env['PATH']
env['CONDA_PREFIX'] = prefix

documents_folder, exception = get_folder_path(FOLDERID.Documents)
if exception:
    documents_folder, exception = get_folder_path(FOLDERID.PublicDocuments)
if not exception:
    os.chdir(documents_folder)
sys.exit(subprocess.call(args, env=env))


