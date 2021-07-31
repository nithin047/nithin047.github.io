"""
script to compile all jemdoc files found in root directory and all subdirectories
the script will also look for a jemdoc CSS file, and if found, will copy it to all subdirectories before compiling the respective jemdoc files
"""

import glob
import sys
import os
from subprocess import Popen, PIPE
from shutil import copyfile

current_dir_path = os.path.dirname(os.path.realpath(__file__))

jemdoc_compile_cmd_list = ['python3', 'jemdoc.py', '-c', 'mysite.conf']



if glob.glob("*.jemdoc"):

    #check if essential files are present
    if glob.glob("jemdoc.css"):
        pass
    else:
        raise FileNotFoundError("jemdoc CSS file not found!")

    if glob.glob("jemdoc.py"):
        pass
    else:
        raise FileNotFoundError("jemdoc .py file not found!")

    if glob.glob("mysite.conf"):
        pass
    else:
        raise FileNotFoundError("JS conf file for latex compilation not found!")


    #compile all jemdoc files
    for jemdoc_file in glob.glob("*.jemdoc"):

        Popen(jemdoc_compile_cmd_list + [jemdoc_file], cwd = current_dir_path).wait()

    for directory, _, _ in os.walk(current_dir_path):

        jemdoc_file_list = glob.glob(os.path.join(directory, "*.jemdoc"))

        if jemdoc_file_list:
            if glob.glob(os.path.join(directory, "jemdoc.css")):
                pass
            else:
                copyfile(os.path.join(current_dir_path, "jemdoc.css"), os.path.join(directory, "jemdoc.css"))

        for jemdoc_file in jemdoc_file_list:
            Popen(jemdoc_compile_cmd_list + [jemdoc_file], cwd = current_dir_path).wait()
        

