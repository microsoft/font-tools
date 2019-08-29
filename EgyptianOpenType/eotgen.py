#!/usr/bin/python
# egyptian opentype generator data

import os
import sys
from config import pvar
from eotHelper import EotHelper

eothelper = EotHelper(pvar)
eothelper.initializeVTP()
eothelper.createVTPFile()
eothelper.createErrorFile()
eothelper.gdef()
eothelper.groups()
eothelper.haln()
eothelper.pres()
eothelper.rlig()
eothelper.blws()
eothelper.abvs()
eothelper.psts()
eothelper.rtlm()
eothelper.vrt2()
eothelper.mark()
eothelper.mkmk()
eothelper.scriptandlang()
eothelper.anchors()
eothelper.coda()
eothelper.writeerrors()