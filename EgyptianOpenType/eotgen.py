#!/usr/bin/python
# egyptian opentype generator data

import os
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
eothelper.initializeVTP()
eothelper.createVTPFile()
eothelper.createErrorFile()
eothelper.loadVariationDatabase()
eothelper.gdef()
eothelper.groups()
eothelper.haln()
eothelper.pres()
eothelper.rlig()
eothelper.blws()
eothelper.abvs()
eothelper.psts()
eothelper.ss01()
eothelper.rtlm()
eothelper.vrt2()
eothelper.mark()
eothelper.mkmk()
eothelper.scriptandlang()
eothelper.anchors()
eothelper.coda()
eothelper.compileTTX()
eothelper.writeerrors()
eothelper.vtpanalyze()
