#!/usr/bin/python
# egyptian opentype generator

import os
import sys
from eotHelper import EotHelper
from config import pvar

if len(sys.argv) > 1:
    testscope = sys.argv[1]
else:
    testscope = 'A'

print ('Font: '+ pvar['fontfilename'])
eothelper = EotHelper(pvar)
eothelper.initializeTestHTML(testscope)