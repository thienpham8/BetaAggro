#!/usr/bin/env python
# Created by: Zac Smith
# 2017-1-31                     
#


# Use these commands to set the PATH to the virtual environment on run
import os
virtualenv = os.path.dirname(os.path.abspath(__file__))
activate = os.path.join(virtualenv, "venv/Scripts/activate_this.py")
execfile(activate, dict(__file__=activate))
# ---------------------------------------------------------------------------------------- #

# THIS SCRIPT ACTIVATES ON IMPORT INTO ANOTHER SCRIPT