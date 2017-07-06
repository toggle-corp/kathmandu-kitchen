#!/usr/bin/python

import sys
import os

addr = "localhost:8000"

if len(sys.argv) > 1:
    addr = sys.argv[1]

os.system("php -S " + addr +" -t public_html/")
