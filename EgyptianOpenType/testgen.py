#!/usr/bin/python
# egyptian opentype generator

import os
from os import path
import sys
from eotHelper import EotHelper

if len(sys.argv) > 1:
    fontconfig = 'config_'+str(sys.argv[1])
    if path.exists(fontconfig+'.py'):
        print('Using config: '+fontconfig)
        exec('from '+fontconfig+' import pvar')
        d = False
if (d): 
    print ('Using default config')
    from config import pvar

if len(sys.argv) > 2:
    testscope = sys.argv[2]
else:
    testscope = 'A' # A[ll], F[ailing], P[assing]

print ('Font: '+ pvar['fontfilename'])
eothelper = EotHelper(pvar)
eothelper.initializeTestHTML(testscope)