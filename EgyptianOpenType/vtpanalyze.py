#!/usr/bin/python
# egyptian opentype generator data

import re
import sys
from os import path
from eotHelper import EotHelper
d = True

if len(sys.argv) > 1:
    fontconfig = 'config_'+str(sys.argv[1])
    if path.exists(fontconfig+'.py'):
        print('Using config: '+fontconfig)
        exec('from '+fontconfig+' import pvar')
        d = False
if (d): 
    print ('Using default config')
    from config import pvar

eothelper = EotHelper(pvar)
eothelper.vtpanalyze()
