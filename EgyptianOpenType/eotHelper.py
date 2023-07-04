# egyptian opentype helper

import os
from os import listdir
from os.path import isfile, join
import sys
import re
import codecs
import math
from pprint import pprint
from featuredata import featurename
from featuredata import groupdata
from featuredata import basetypes
from featuredata import qcontrols
from featuredata import punctuation
from featuredata import internalligatures
from featuredata import internalmirrors
from featuredata import mirroring
from featuredata import mirroredvariants
from featuredata import verticalmetrics
from insertions import insertions
from pres import pres
from mark import mark
from mkmk import mkmk
from fontTools import ttx
from fontTools.ttLib import TTFont
from fontTools.ttLib.tables._g_l_y_f import Glyph

ver = 200

# Unicode 15 requirements
    # VS to control expansion of all atomic shades – done
    # Rotations
        # glyph recipes for size variants — done
        # baseline alignment
        # ensure rotational variant bases don't merge with tshashes
    # Mirrored forms
        # write glyph recipes for mirror variants incl. rotational variants
    # RTL structures
    # Vertical
    # insertions inside sign area not total sign area?
    #   TCMs all [font, OT]
    #   expanded enclosing glyph - when to expand? pres016 - expansion
    #   block illegal sequences (vertical group before OM; atomic shades in OM; sign shade after blank)
    # validate self.pvar for minimal info and guard missing attributes.

class EotHelper:
    def __init__(self, pvar):
        """Initialize the Egyptian OpenType helper class with config variable."""
        # print(sys.version)

        self.pvar = pvar
        self.fontsrc = TTFont(pvar['fontsrc'])
        self.startingGlyphNames = []
        self.loadInsertionContextsAndGroups()
        self.compactfontfilename = re.sub(' ','',self.pvar['fontfilename'])+'_'+str(ver)
        self.abvslines = []
        self.blwslines = []
        self.halnlines = []
        self.defaultLookupObj = {'feature':'','name':'','marks':'','contexts':[],'details':[]}
        self.errors = []
        self.filenames = []
        self.gdeflines = []
        self.glyphdata = {}
        self.glyphHexToName = {}
        self.lookupcount = 0
        self.marklines = []
        self.mkmklines = []
        self.preslines = []
        self.pstslines = []
        self.ss01lines = []
        self.rliglines = []
        self.rotated090 = []
        self.rotated180 = []
        self.rotated270 = []
        self.vrt2lines = []
        self.sizekeys = []
        self.targetsizes = {}
        self.tshashes = []
        self.uniqueglyphnames = []
        self.ligatures = []
        self.ligatures_all = []
        self.maxhvsizes = {}
        print(pvar['fontsrc'])
    
    def initializeVTP(self):
        """Initialize the Volt OpenType project for the currently instantiated class."""
        def setdefaultfeatures():
            defaultObj = {}
            defaultObj['haln'] = []
            defaultObj['pres'] = []
            defaultObj['abvs'] = []
            defaultObj['blws'] = []
            defaultObj['rlig'] = []
            defaultObj['psts'] = []
            defaultObj['ss01'] = []
            defaultObj['rtlm'] = []
            defaultObj['vrt2'] = []
            defaultObj['mark'] = []
            defaultObj['mkmk'] = []
            return defaultObj
        def setdefaultfeatureindexes():
            defaultObj = {}
            defaultObj['haln'] = 1
            defaultObj['pres'] = 1
            defaultObj['abvs'] = 1
            defaultObj['blws'] = 1
            defaultObj['rlig'] = 1
            defaultObj['psts'] = 1
            defaultObj['ss01'] = 1
            defaultObj['rtlm'] = 1
            defaultObj['vrt2'] = 1
            defaultObj['mark'] = 1
            defaultObj['mkmk'] = 1
            return defaultObj

        self.features = setdefaultfeatures()
        self.featureindexes = setdefaultfeatureindexes()
        #Main
        print ('preload groups...')
        self.preloadgroups()
        print ('loading glyph data...')
        self.loadglyphdata()
        # print(self.maxhvsizes['66'])
        # for key in sorted(self.maxhvsizes):
        #     print (key + "\t" + str(self.maxhvsizes[key]))
        print ('loading groups...')
        self.loadgroups()

        return

    def initializeTestHTML(self,testscope):
        """Initialize and write the HTML test file for the currently instantiated class."""
        def tl(line):
            self.testfile.extend(line)
            return
        def htmlHeader():
            tl("<!DOCTYPE html>\n"+"<html>\n"+"\t<head>\n")
            tl("\t\t<title>Test Page - "+self.pvar['fontfilename']+"</title>\n")
            tl("\t\t<meta http-equiv='Content-Type' content='text/html; charset=UTF-8'/>")
            tl("\t\t<style type='text/css'>\n")
            tl("\t\t\t@font-face {font-family: '"+self.pvar['fontfilename']+"';\n")
            tl("\t\t\tsrc: url("+self.pvar['fontout']+") format(\"truetype\");}\n")
            tl("\t\t\t@font-face {font-family: 'EgyptianTextPrior';\n")
            tl("\t\t\tsrc: url("+self.pvar['fontprior']+") format(\"truetype\");}\n")
            tl("\t\t\tbody {background-color:#AAA; color: #555; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }\n")
            tl("\t\t\t.page {margin: 0px auto; text-align: center}\n")
            tl("\t\t\th2 {clear: left; margin: 0px auto; text-align: center; display: block;padding-top: 30px;padding-bottom: 12px;}\n")
            tl("\t\t\t.row {clear: left}\n")
            tl("\t\t\t.cellN {margin: 1px; float: left; height:100px; width: 75px; background-color: #DDD; text-align: left;}\n")
            tl("\t\t\t.cellL {margin: 1px; float: left; height:100px; width: 150px; background-color: #DDD; text-align: left;}\n")
            tl("\t\t\t.rowLabel {font-size: 11pt;margin-top:30px;}\n")
            tl("\t\t\t.cellWide {margin: 1px; float: left; height:100px; width: 300px; background-color: #FFF; text-align: left;}\n")
            tl("\t\t\t.cell {margin: 1px; float: left; height:100px; width: 75px; background-color: #EEE;}\n")
            tl("\t\t\t.image {height:100px;}\n")
            tl("\t\t\t.pass {background-color: #c9f0b4;}\n")
            tl("\t\t\t.stable {background-color: lightseagreen;}\n")
            tl("\t\t\t.pointer {cursor: pointer;}\n")
            tl("\t\t\t.letter-inner {font-family: '"+self.pvar['fontfilename']+"'; font-size: 60px; line-height:75px;  background-color: #FFF; width:32px; }\n")
            tl("\t\t\t.letter-inner span {margin:0px; border:none; padding:0px; }\n")
            tl("\t\t\t.letter-stable {font-family: 'EgyptianTextPrior'; font-size: 60px; line-height:75px;  background-color: #FFF; width:32px; }\n")
            tl("\t\t\t.label {font-size: 10pt;}\n")
            tl("\t\t</style>\n")
            tl("\t</head>\n")
            tl("\t<body>\n")
            return
        def htmlBody():
            def startPage():
                tl("\t\t<div class='page'>\n")
                tl("\t\t\t<h1>"+self.pvar['fontfilename']+"</h1>\n")
                if testscope == 'A':
                    subtitle = 'All'
                elif testscope == 'P':
                    subtitle = 'Passing'
                elif testscope == 'F':
                    subtitle = 'Failing'
                tl("\t\t\t<h3>["+subtitle+" test cases]</h3>\n")
                return                
            def genTable():
                testfile = open('testsequences.txt',"r")
                widetests = ['Enclosures','Phrases','Invalid Phrases','Internal ligatures','Max cluster size','Invalid']
                self.wide = False
                lineno = 1
                for line in testfile:
                    key = line[0:1]
                    ps = ''

                    if (key == '#'):
                        h2 = line[1:].strip()
                        genHeading(h2)
                        if h2 in widetests:
                            self.wide = True
                        else:
                            self.wide = False
                    elif (key != '/'):
                        line.strip()
                        if key == '%':
                            ps = ' pass'
                            line = line[1:]
                        else:
                            ps = ' fail'
                        if len(line)>1:
                            if testscope == 'A': # Write all test cases
                                genRow(lineno,line,ps)
                            if testscope == 'F': # Write failing test cases
                                if key != '%':
                                    genRow(lineno,line,ps)
                            if testscope == 'P': # Write passing test cases
                                if key == '%':
                                    genRow(lineno,line,ps)
                    lineno += 1
                return
            def genRow(lineno,line,ps):
                tl("\t\t\t<div class='row'>\n")
                genLabel(str(lineno)+'.','cellN')
                glyphseq = re.sub(r'\s+\(.*','',line)    
                seq = glyphseq.split()
                if len(seq) >= 1:
                    genLabel(glyphseq,'cellL')
                    if self.wide:
                        block = ''
                        for el in seq:
                            if el in self.glyphdata:
                                glyph = self.glyphdata[el]
                                cp = re.sub('0x','',glyph['hex'])
                                block += '&#x'+cp+';'
                        genCell(block,'','Wide')
                    else:
                        i = len(seq)
                        j = 0
                        while i >= 1:
                            block = ''
                            if j >= 1:
                                ps = ''
                            for el in seq:
                                if el in self.glyphdata:
                                    glyph = self.glyphdata[el]
                                    cp = re.sub('0x','',glyph['hex'])
                                    block += '&#x'+cp+';'
                            genCell(block,str(i),ps,glyphseq)
                            seq.pop()
                            i = i - 1
                            j += 1
                tl("\t\t\t</div>\n")
                return
            def genLabel(label, cellclass):
                label = label.replace('\r', '').replace('\n', '')
                tl("\t\t\t\t<div class='"+cellclass+"'>\n")
                tl("\t\t\t\t\t<div class='Letter'>\n")
                tl("\t\t\t\t\t\t<span class='rowLabel'>"+label+"</span>\n")
                tl("\t\t\t\t\t</div>\n")
                tl("\t\t\t\t</div>\n")
                return
            def genCell(block,label,test='',glyphseq='',):
                def writeCell(block,label,test,css):
                    label = label.replace('\r', '').replace('\n', '')
                    tl("\t\t\t\t<div class='cell"+test+"'>\n")
                    tl("\t\t\t\t\t<div class='letter'>\n")
                    tl("\t\t\t\t\t\t<span class='"+css+"'>"+block+"</span>\n")
                    tl("\t\t\t\t\t</div>\n")
                    tl("\t\t\t\t\t<div class='label'>\n")
                    tl("\t\t\t\t\t\t"+label+"\n")
                    tl("\t\t\t\t\t</div>\n")
                    tl("\t\t\t\t</div>\n")
                    return

                # Comment next two lines to suppress stable version.
                if len(test) > 0:
                    writeCell(block,'R',' stable','letter-stable')
                writeCell(block,label,test,'letter-inner')
                return
            def genHeading(label):
                tl("\t\t\t<h2>"+label+"</h2>\n")
                return
            def endPage():
                tl("\t\t</div>\n")
                return

            startPage()
            genTable()                
            endPage()

            return
        def htmlFooter():
            tl("\t</body>\n")
            tl("</html>\n")
            return
        def echoTestScope(testscope):
            if testscope == 'A':
                print("\t"+"Writing all test cases")
            if testscope == 'F':
                print("\t"+"Writing failing test cases")
            if testscope == 'P':
                print("\t"+"Writing passing test cases")

        self.testfile = []
        testscope = testscope.upper()
        if testscope not in ['A','F','P']:
            print ("Defaulting scope to A")
            testscope = 'A'
        echoTestScope(testscope)
        self.loadglyphdata()
        htmlHeader()
        htmlBody()
        htmlFooter()

        self.writeTestFile(self.testfile)
        pass

    def loadInsertionContextsAndGroups(self):
        def getinsertionObj(ins):
            retobj = []
            retobj.append(loadbases(ins))
            retobj.append(loadMappings(ins))

            return retobj
        def loadbases(ins):
            def testbase(map,ins):
                if ins in nonadjs:
                    array = [ins]
                else:
                    array = adjs

                test = False
                for key in array:
                    if key in map:
                        test = True
                return test

            truekeys = []
            for key in insertions:
                perglyphmap = insertions[key]
                if testbase(perglyphmap,ins):
                    if key not in truekeys:
                        truekeys.append(key)
                    if key not in self.insertionsall:
                        # this checks whether a glyph for Unicode defined
                        # variation sequences exists in the font
                        if key in self.startingGlyphNames:
                            self.insertionsall.append(key)
            return truekeys
        def loadMappings(ins):
            def stripoffsets(obj):
                def xyoffsets(it,bxy,ixy,ov,sign):
                    offset = {
                        'it':it,  #insertion type {bs, be, ti etc.}
                        'tt':'', #transform type {x, y}
                        'bd':0,   #base dimension for type {6,5,4,3}
                        'id':0,   #ins dimension for type {3,2,1}
                        'om':0,   #offset multiplier where 5 is 50% offset {5,4,3,2,1}
                        'os':0,   #offset value for type (multiplier * font units per block) {float}
                        'sign':sign, #signs at this offset {G25, G25_65} # TODO MAKE THIS AN ARRAY?
                        'hash':'' #hash value
                        }
                    # print(str(it)+','+str(bxy)+','+str(ixy)+','+str(ov)+','+str(sign))
                    if ov[0:1] == 'x':
                        offset['tt'] = 'x'
                        offset['bd'] = bxy
                        offset['id'] = ixy 
                        offset['om'] = int(ov[1:])/20
                        offset['os'] = int(offset['om'] * (self.pvar['hfu'] * self.pvar['chu']))
                    elif ov[0:1] == 'y':
                        offset['tt'] = 'y'
                        offset['bd'] = bxy
                        offset['id'] = ixy
                        offset['om'] = int(ov[1:])/20
                        offset['os'] = int(offset['om'] * (self.pvar['vfu'] * self.pvar['vhu']))
                    offset['hash'] = str(offset['tt'])+str(offset['os'])
                    # print(offset)
                    return offset
                def storeoffsets(o):
                    h = o['hash']

                    if h not in self.offsets:
                        self.offsets[h] = [o]
                    else:
                        self.offsets[h].append(o)
                    pass
                for k in obj:
                    v = obj[k]
                    if len(v) > 2:
                        obj[k] = ds = str(v)[0:2] #default size for offset
                        storeoffsets(xyoffsets(ins,str(k),str(ds),str(v)[2:],key))
                return obj
            def customhash(obj):
                string = ''
                for key in obj:
                    val = obj[key]
                    string += str(key)+str(val)
                return hash(string)
            if ins in nonadjs:
                array = [ins]
            else:
                array = adjs

            mappings = {}
            for key in sorted(insertions):
                values = insertions[key]

                for k in array:
                    if k in values:
                        valset = stripoffsets(values[k])
                        valkey = customhash(valset)
                        if valkey not in mappings:
                            mappings[valkey] = [values]
                            mappings[valkey].append(key)
                        else:
                            mappings[valkey].append(key)

            return mappings

        for name in self.fontsrc.getGlyphOrder():
            self.startingGlyphNames.append(name)

        self.insertionsall = []
        self.insertionmappings = {'ad':[],'bs':[],'te':[],'be':[],'mi':[],'bi':[]}
        adjs = ['ts','ti']
        nonadjs = ['bs','te','be','mi','bi']

        self.offsets = {}
        for ins in self.insertionmappings:
            self.insertionmappings[ins] = getinsertionObj(ins)
        groupdata['insertions_all'] = self.insertionsall
        pass

    def loadVariationDatabase(self):
        def parseVariationLine(line):
            def lookupVSType(vs,description):
                vsType = 'x' # no rotation
                if vs in ['FE00','FE01','FE02']:
                    if vs == 'FE00':
                        vsType = 'n' #  90 degree rotation
                    if vs == 'FE01':
                        vsType = 'o' # 180 degree rotation
                    if vs == 'FE02':
                        vsType = 't' # 270 degree rotation
                    if re.match(r'^.*expanded.*$',description,flags=re.IGNORECASE):
                        vsType = 'x'
                else:
                    print ('Unsupported variation selector in StandardizedVariants.txt')
                
                return vsType
            varObj = {'base':'','vs':'','type':''}
            parts = line.split(';')
            if len(parts)>0:
                vs = parts[0]
                chrs = vs.split()
                if len(chrs) > 0:
                    decval = int('0x'+chrs[0],16)
                    if decval >= 77824 and decval <= 79199:
                        varObj['base'] = chrs[0]
                        varObj['vs']   = chrs[1]
                        varObj['type'] = lookupVSType(chrs[1],parts[1])
                if chrs[0] == '13000':
                    self.defaultA1 = True
            return varObj

        self.variations = []
        self.defaultA1 = False
        if self.pvar['variations']>0:
            # https://www.unicode.org/Public/UCD/latest/ucd/StandardizedVariants.txt
            unicodehvdfile = open('src/StandardizedVariants.txt',"r")
            i = 0
            for line in unicodehvdfile:
                key = line[0:1]
                if (key == '#'):
                    hv = line[1:].strip()
                else:
                    if (len(line)>1):
                        varObj = parseVariationLine(line.strip())
                        if varObj['base']:
                            self.variations.append(varObj)
                            i += 1
            if self.defaultA1 == False:
                self.variations.insert(0,{'base': '13000', 'vs': 'FE02', 'type': 't'})
                self.variations.insert(0,{'base': '13000', 'vs': 'FE01', 'type': 'o'})
                self.variations.insert(0,{'base': '13000', 'vs': 'FE00', 'type': 'n'})

            print('Loaded '+str(i)+' variations from StandardizedVariants.txt')

            if i > 0:
                self.genCMAPFormat14_TTX()
        else:
            print('Variations skipped per config')

        pass

    def genCMAPFormat14_FC(self):
        def loadHead():
            lines = []
            lines.append('cmap subtable 1\n')
            lines.append('platformID	0\n')
            lines.append('encodingID	5\n')
            lines.append('format	14\n')
            lines.append('language	0\n')
            return lines
        def loadBody():
            lines = []
            for varObj in self.variations:
                base = '0x'+varObj['base']
                lcbase = base.lower()
                vs   = '0x'+varObj['vs']
                vstype = varObj['type']
                target = ''

                if lcbase in self.glyphHexToName:
                    target = self.glyphHexToName[lcbase]+vstype
                try:
                    targetID = self.fontsrc.getGlyphID(target)
                    line = base + "\t" + vs  + "\t\\#" + str(targetID) + "\n"
                    lines.append(line)
                except:
                    line = ''

            return lines
        def loadFoot():
            lines = []
            lines.append('end subtable\n')
            return lines

        cmap14 = []
        cmap14.extend(loadHead())
        cmap14.extend(loadBody())
        cmap14.extend(loadFoot())

        self.writeCMAP14File(cmap14,'.fc')
        pass

    def genCMAPFormat14_TTX(self):
        def loadHead():
            lines = []
            lines.append('    <cmap_format_14 platformID="0" platEncID="5">\n')
            return lines
        def loadBody():
            lines = []
            for varObj in self.variations:
                base = '0x'+varObj['base']
                lcbase = base.lower()
                vs   = '0x'+varObj['vs']
                vstype = varObj['type']
                target = ''

                if lcbase in self.glyphHexToName:
                    # Defined in StandardizedVariants (270 == mirrored 90)
                    basename = self.glyphHexToName[lcbase]
                    if basename not in mirroring:
                        if vstype == 't':
                            vstype == 'nR'
                    try:
                        if vstype == 'x':
                            target = basename[0:2]+'2'
                        else:
                            target = basename+vstype
                        if target in self.glyphdata:
                            line = '      <map uv="'+base.lower()+'" uvs="'+vs.lower()+'" name="'+target+'"/>'
                            lines.append(line+"\n")
                    except:
                        print(basename + ' : ' + vstype)
                        line = ''
                else:
                    print('Failed to find base for StandardizedVariants row '+base)

            return lines
        def loadFoot():
            lines = []
            lines.append('    </cmap_format_14>\n')
            return lines

        cmap14 = []
        cmap14.extend(loadHead())
        cmap14.extend(loadBody())
        cmap14.extend(loadFoot())

        self.writeCMAP14File(cmap14,'.ttx')
        pass

    def vmtx_FC(self):
        def loadHead():
            lines = []
            lines.append('Font Chef Table vmtx\n')
            lines.append('\n')
            lines.append('unitsPerEm	2048\n')
            lines.append('\n')
            return lines
        def loadBody():
            lines = []
            for key in self.glyphdata:
                if (key == '.notdef'):
                    key = '\#0'
                if (key == '.null'):
                    key = 'null'
                if (key in verticalmetrics):
                    pair = verticalmetrics[key]
                    vert =   pair[0]
                    offset = pair[1]
                else:
                    vert   = 0
                    offset = 0
                line = key + "\t" + str(vert) + "\t" + str(offset) + "\n"
                lines.append(line)
            return lines

        if self.pvar['vertical']:
            vmtx = []
            vmtx.extend(loadHead())
            vmtx.extend(loadBody())
            self.writeVmtxFile(vmtx)

        pass

    def writeRotationRecipes(self,incSizeVariants):
        """"Output FL glyph recipes to generate rotation variants"""
        def transformlookup(string):
            tlookup = {
                'n':'@0, -1, 1, 0, 100, 100',
                'o':'@-1, 0, 0, -1, 100, 100',
                't':'@0, 1, -1, 0, 100, 100',
            }
            if string in tlookup:
                return tlookup[string]
            pass
        def sizeLookup(type,size):
            if type in ['n','t']:
                size = size[1] + size[0]
            return size
        recipes = []
        i = 0
        for varObj in self.variations:
            base = '0x'+varObj['base']
            vstype = varObj['type']
            transform = transformlookup(vstype)

            lcbase = base.lower()
            if lcbase in self.glyphHexToName:
                basename = self.glyphHexToName[lcbase]
                if basename not in ['AS1','AQ1','AT1','AW1']:
                    if basename in self.glyphdata:
                        obj = self.glyphdata[basename]

                        # recipes.append(basename + vstype + ' = ' + base)
                        recipes.append(basename + vstype + ' = ' + basename + transform)
                        i += 1

                        if incSizeVariants:
                            tsh = obj['tshash']
                            sizes = [tsh[i:i+2] for i in range(0, len(tsh), 2)]
                            if len(sizes) > 1:
                                sizes.pop(0)
                                for size in sizes:
                                    nsize = sizeLookup(vstype,size)
                                    recipes.append(basename + vstype + '_' + nsize + ' = ' + basename + '_' + size + transform)
                                    i += 1
        filename = 'eot_rotationRecipes.txt'
        recipefile = open('out/'+filename,"w")
        for line in recipes:
            recipefile.write(line+"\n")
        print(str(i) + ' rotation recipes written')
        pass

    def writeMirrorRecipes(self,incSizeVariants):
        recipes = []
        transform = '@~,'
        i = 0

        # list mirrorable base glyphs
        for basename in self.sort_alphanumeric(mirroring):
            if basename in self.glyphdata:
                obj = self.glyphdata[basename]
                recipes.append(basename + 'R' + ' = ' + basename + transform)
                i += 1

                if incSizeVariants:
                    tsh = obj['tshash']
                    sizes = [tsh[i:i+2] for i in range(0, len(tsh), 2)]
                    if len(sizes) > 1:
                        sizes.pop(0)
                        for size in sizes:
                            sizename = basename + '_' + size
                            if sizename in self.glyphdata:
                                recipes.append(sizename + 'R' + ' = ' + sizename + transform)
                                i += 1

        filename = 'eot_mirroringRecipes.txt'
        recipefile = open('out/'+filename,"w")
        for line in recipes:
            recipefile.write(line+"\n")
        print(str(i) + ' mirroring recipes written')
        pass

    def writeMirroredRotations(self,incSizeVariants):
        recipes = []
        transform = '@~,'
        i = 0

        # list mirrorable base glyphs
        for basename in self.sort_alphanumeric(mirroredvariants):            
            if basename in self.glyphdata:
                obj = self.glyphdata[basename]
                recipes.append(basename + 'R' + ' = ' + basename + transform)
                i += 1

                if incSizeVariants:
                    tsh = obj['tshash']
                    sizes = [tsh[i:i+2] for i in range(0, len(tsh), 2)]
                    if len(sizes) > 1:
                        sizes.pop(0)
                        for size in sizes:
                            sizename = basename + '_' + size
                            if sizename in self.glyphdata:
                                recipes.append(sizename + 'R' + ' = ' + sizename + transform)
                                i += 1

        filename = 'eot_mirroredRotations.txt'
        recipefile = open('out/'+filename,"w")
        for line in recipes:
            recipefile.write(line+"\n")
        print(str(i) + ' mirrored rotation recipes written')


        pass

    def sort_alphanumeric(self,l):
        convert = lambda text: int(text) if text.isdigit() else text
        alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
        return sorted(l, key=alphanum_key)
    
### GDEF
    def gdef(self):
        def formatgdefline(glyph):
            if (glyph['id']):
                gid = str(glyph['id'])
            else :
                gid = str(0)
            if (glyph['dec']):
                gunic = ' UNICODE ' + str(glyph['dec'])
            else :
                gunic = ''
            if (glyph['type']=='M'):
                gtype = 'MARK'
            else :
                gtype = 'BASE'
            gdefline = 'DEF_GLYPH "'+glyph['name']+'" ID '+gid+gunic+' TYPE '+gtype+' END_GLYPH'+"\n"

            return gdefline

        # Main
        font = TTFont('out/fontout_temp.ttf')
        for name in font.getGlyphOrder():
            if name in self.glyphdata:
                glyph = self.glyphdata[name]
                if not glyph['name'] in self.uniqueglyphnames:
                    self.uniqueglyphnames.append(glyph['name'])
                else:
                    self.errors.append('Duplicate name [eh316]: '+str(glyph['id'])+'. '+glyph['name'])
                gdefline = formatgdefline(glyph)
                self.gdeflines.append(gdefline)

        if self.pvar['test']['gdef'] == 1:
            print ('GDEF in test mode')
        else:
            print ('GDEF written')
            self.writelines(self.gdeflines)

### GROUPS
    def groups(self):
        if self.pvar['test']['groups'] == 1:
            print ('GROUPS in test mode')
        else:
            self.writelines(self.grouplines)
            print ('GROUPS written')

### GSUB
    #Ligatures
    def haln(self):
        featuretag = 'haln'
        if self.pvar['test']['haln'] == 1:
            print ('HALN in test mode')
        else:
            self.halnlines = self.GSUBligatures()
            n = self.featureindexes[featuretag] - 1
            self.lookupcount += n
            print (featuretag.upper() + ' written: ' + str(n) + ' (7 expected)')
            self.writelines(self.halnlines)

    #Structure
    def pres(self):
        def loadtsgsubpairs():
            keys = groupdata['characters_all']
            subpairs = []
            for key in keys:
                if key not in ['GB1','dottedcircle','O33a']:
                    hval = self.glyphdata[key]['ehuh']
                    if hval > self.pvar['hhu']:
                        hval = self.pvar['hhu']
                    vval = self.glyphdata[key]['ehuv']
                    if vval > self.pvar['vhu']:
                        vval = self.pvar['vhu']
                    et = 'et'+str(hval)+str(vval)
                    tsh = 'tsh'+str(self.glyphdata[key]['tshash'])
                    subpair = {'sub':[key],'target':[et,tsh,key,'Qf'] }
                    subpairs.append(subpair)
            return subpairs
        def loadtbbgb1subpairs():
            keys = ['tcbb0']
            subpairs = []
            tsh = 'tsh'+str(self.glyphdata['GB1']['tshash'])
            for key in keys:
                subpair = {'sub':[key],'target':[key,'et66',tsh,'GB1','Qf'] }
                subpairs.append(subpair)
            return subpairs
        def loadgb1subpairs():
            keys = [
                'vj0A','hj0A','its0A','ibs0A','ite0A','ibe0A','om0A',
                'vj1A','hj1A','its1A','ibs1A','ite1A','ibe1A','om1A',
                'vj2A','hj2A','ti0A','mi0A','bi0A','ti1A','mi1A','bi1A','ss'
            ]
            subpairs = []
            tsh = 'tsh'+str(self.glyphdata['GB1']['tshash'])
            for key in keys:
                control = key
                subpair = {'sub':[control],'target':[control,'Qi','et66',tsh,'GB1','Qf'] }
                subpairs.append(subpair)
            return subpairs
        def loadsubpairs():
            keys = sorted(self.sizekeys)
            subpairs = []
            for key in keys:
                et = 'et'+str(key[-2:5])
                subpair = {'sub':[key],'target':[et,key,'Qf'] }
                subpairs.append(subpair)
            return subpairs

        featuretag = 'pres'
        for featuredef in pres:
            lookupObj = featuredef
            lookupObj['feature'] = featuretag
            # if (lookupObj['name'] == 'rninety'):#DYNAMIC FEATURE
            #     subpairs = loadr090subpairs()
            #     lookupObj['details'] = subpairs
            # if (lookupObj['name'] == 'roneeighty'):#DYNAMIC FEATURE
            #     subpairs = loadr180subpairs()
            #     lookupObj['details'] = subpairs
            # if (lookupObj['name'] == 'rtwoseventy'):#DYNAMIC FEATURE
            #     subpairs = loadr270subpairs()
            #     lookupObj['details'] = subpairs
            if (lookupObj['name'] == 'tsg'):#DYNAMIC FEATURE TSG
                subpairs = loadtsgsubpairs()
                lookupObj['details'] = subpairs
            if (lookupObj['name'] == 'tbb_gb1'):#DYNAMIC FEATURE TBB GB1
                subpairs = loadtbbgb1subpairs()
                lookupObj['details'] = subpairs
            if (lookupObj['name'] == 'gb1'):#DYNAMIC FEATURE GB1
                subpairs = loadgb1subpairs()
                lookupObj['details'] = subpairs
            if (lookupObj['name'] == 'ehv'):#DYNAMIC FEATURE EHV
                subpairs = loadsubpairs()
                lookupObj['details'] = subpairs
            # if (lookupObj['name'] == 'expansion'):
            #     print('No expansions'+str(self.pvar['expansions']))
            #     if (self.pvar['expansions'] == 0 ):
            #         lookupObj = 0
            if (lookupObj):
                self.preslines.append(self.writefeature(lookupObj))

        if self.pvar['test']['pres'] == 1:
            print ('PRES in test mode')
        else:
            n = self.featureindexes[featuretag] - 1
            self.lookupcount += n
            print (featuretag.upper() + ' written: ' + str(n) + ' (76 expected)')
            self.writelines(self.preslines)

    #Level 0
    def rlig(self):
        level = 0
        featuretag = self.setfeaturetag(level)

        if self.pvar['test'][featuretag] == 1:
            print ('RLIG in test mode')
        else:
            # H O R I Z O N T A L
            self.rliglines = self.GSUBhorizontal(featuretag,level)

            # V E R T I C A L
            lines = self.GSUBvertical(featuretag,level)

            self.rliglines.extend(lines)
            n = self.featureindexes[featuretag] - 1
            self.lookupcount += n
            print (featuretag.upper() + ' written: ' + str(n) + ' (208 expected)')
            self.writelines(self.rliglines)

    #Level 1
    def blws(self):
        level = 1
        featuretag = self.setfeaturetag(level)

        if self.pvar['test'][featuretag] == 1:
            print ('BLWS in test mode')
        else:
            # H O R I Z O N T A L
            self.blwslines = self.GSUBhorizontal(featuretag,level)

            # V E R T I C A L
            lines = self.GSUBvertical(featuretag,level)

            self.blwslines.extend(lines)
            n = self.featureindexes[featuretag] - 1
            self.lookupcount += n
            print (featuretag.upper() + ' written: ' + str(n) + ' (430 expected)')
            self.writelines(self.blwslines)

    #Level 2
    def abvs(self):
        featuretag = 'abvs'
        level = 2

        if self.pvar['test']['abvs'] == 1:
            print ('ABVS in test mode')
        else:
            # H O R I Z O N T A L
            self.abvslines = self.GSUBhorizontal(featuretag,level)

            # V E R T I C A L
            lines = self.GSUBvertical(featuretag,level)

            self.abvslines.extend(lines)
            n = self.featureindexes[featuretag] - 1
            self.lookupcount += n
            print (featuretag.upper() + ' written: ' + str(n) + ' (399 expected)')
            self.writelines(self.abvslines)

    #Resizing & post processing
    def psts(self):
        featuretag = 'psts'
        if self.pvar['test'][featuretag] == 1:
            print ('PSTS in test mode')
        else:
            self.pstslines = self.GSUBresizing()
            n = self.featureindexes[featuretag] - 1
            self.lookupcount += n
            print (featuretag.upper() + ' written: ' + str(n) + ' (73 expected)')
            self.writelines(self.pstslines)

    #Stylistic variants
    def ss01(self):
        featuretag = 'ss01'
        if self.pvar['test'][featuretag] == 1:
            print ('SS01 in test mode')
        else:
            self.ss01lines = self.GSUBbaseline()
            n = self.featureindexes[featuretag] - 1
            self.lookupcount += n
            print (featuretag.upper() + ' written: ' + str(n) + ' (1 expected)')
            self.writelines(self.ss01lines)

    #Mirroring
    def rtlm(self):
        featuretag = 'rtlm'
        if self.pvar['test'][featuretag] == 1:
            print ('RTLM in test mode')
        else:
            self.rtlalines = self.GSUBmirror()
            n = self.featureindexes[featuretag] - 1
            self.lookupcount += n
            print (featuretag.upper() + ' written: ' + str(n) + ' (4 expected)')
            self.writelines(self.rtlalines)

    #Vertical layout
    def vrt2(self):
        featuretag = 'vrt2'
        if self.pvar['test'][featuretag] == 1:
            print ('VRT2 in test mode')
        else:
            self.vrt2lines = self.GSUBvert()
            n = self.featureindexes[featuretag] - 1
            self.lookupcount += n
            print (featuretag.upper() + ' written: ' + str(n) + ' (1 expected)')
            self.writelines(self.vrt2lines)

### GPOS
    def mark(self):
        featuretag = 'mark'
        if self.pvar['test']['gpos'] == 1:
            print ('MARK in test mode')
        else:
            for featuredef in mark:
                lookupObj = featuredef
                lookupObj['feature'] = featuretag
                self.marklines.append(self.writefeature(lookupObj))
            n = self.featureindexes[featuretag] - 1
            self.lookupcount += n
            print (featuretag.upper() + ' written: ' + str(n) + ' (2 expected)')
            self.writelines(self.marklines)

    def mkmk(self):
        def distanceoffset(key,offset):
            def gencontexts(offset):
                contexts = []
                sign = offset['sign']
                ins = offset['it'] + str(offset['id'])
                contexts.append({'left':[sign,ins],'right':[]})
                return contexts
            def gendetails(offset):
                details = []
                ins = 'it'+str(offset['id'])
                if ins not in usedoffsets:
                    if offset['tt'] == 'x':
                        dx = int(offset['os'])
                        dy = 0
                        if offset['it'] in ('te','be'):
                            dx = dx * -1
                    if offset['tt'] == 'y':
                        dx = 0
                        dy = int(offset['os'])
                        if offset['it'] in ('ts','ti','te'):
                            dy = dy * -1
                    details.append({'adjust':[ins],'dx':dx,'dy':dy})
                    usedoffsets.append(ins)

                return details
            # process self.offsets when name = 'offsets1'
            # foreach hash make a lookup that does the xy offset to itXY proportionate to hv in context of each sign
            # and each insertion size descending from the max attested size of that insertion
                # QB6 r0v6 c0h6 o66 m0 ***G25 bs22 it22*** r1v2 c1h2 s22 m0 X1_21 c1eA r1eB c0eA r0eB 
            # process self.offsets in here when name = 'offsets2'
            # do the same for offsets2 for bs2, be2 etc.

            # {'it': 'bs', 'tt': 'y', 'bd': '6', 'id': '3', 'om': 0.1, 'os': 186, 'signs': ['A28'], 'hash': 'y186'}
            # {'it': 'bs', 'tt': 'y', 'bd': '6', 'id': '2', 'om': 0.1, 'os': 186, 'signs': ['F29'], 'hash': 'y186'}
            # {'it': 'bs', 'tt': 'y', 'bd': '6', 'id': '2', 'om': 0.1, 'os': 186, 'signs': ['G1'], 'hash': 'y186'}
            # {'it': 'bs', 'tt': 'y', 'bd': '6', 'id': '2', 'om': 0.1, 'os': 186, 'signs': ['G14'], 'hash': 'y186'}
            # {'it': 'bs', 'tt': 'y', 'bd': '6', 'id': '2', 'om': 0.1, 'os': 186, 'signs': ['G15'], 'hash': 'y186'}
            # {'it': 'bs', 'tt': 'y', 'bd': '6', 'id': '2', 'om': 0.1, 'os': 186, 'signs': ['G17'], 'hash': 'y186'}
            # {'it': 'bs', 'tt': 'y', 'bd': '6', 'id': '2', 'om': 0.1, 'os': 186, 'signs': ['G18'], 'hash': 'y186'}
            # {'it': 'bs', 'tt': 'y', 'bd': '6', 'id': '2', 'om': 0.1, 'os': 186, 'signs': ['G2'], 'hash': 'y186'}

            lookupObj = {'name':'dist_offset_'+key,'marks':'','contexts':[],'details':[]}
            usedoffsets = []
            for o in offset:
                lookupObj['contexts'].extend(gencontexts(o))
                lookupObj['details'].extend(gendetails(o))
            return lookupObj
        def distanceoffsets(level):
            lookupObjs = []
            if level == 1:
                for key in sorted(self.offsets):
                    lookupObjs.append(distanceoffset(key,self.offsets[key]))

            return lookupObjs

        featuretag = 'mkmk'
        if self.pvar['test']['gpos'] == 1:
            print ('MKMK in test mode')
        else:
            for featuredef in mkmk:
                if featuredef['name'] in ['offsets1','offsets2']:
                    if self.pvar['offsets']:
                        lookupObjs = distanceoffsets(int(featuredef['name'][-1:]))
                        for lookupObj in lookupObjs:
                            lookupObj['feature'] = featuretag
                            if 'name' in lookupObj:
                                # print(lookupObj)
                                self.mkmklines.append(self.writefeature(lookupObj))
                        pass
                else:
                    lookupObj = featuredef
                    lookupObj['feature'] = featuretag
                    self.mkmklines.append(self.writefeature(lookupObj))
            n = self.featureindexes[featuretag] - 1
            self.lookupcount += n
            print (featuretag.upper() + ' written: ' + str(n) + ' (67 expected)')
            self.writelines(self.mkmklines)

### LANGSYS
    def scriptandlang(self):
        self.langlines = []
        def al(line):
            self.langlines.append(line)
        def enumfeatures():
            for key in featurename:
                if (key == 'mark' or key == 'mkmk'):
                    testkey = 'gpos'
                else:
                    testkey = key
                if not self.pvar['test'][testkey] == 1:
                    if len(self.features[key]) > 0:
                        al('DEF_FEATURE NAME "'+featurename[key]['name']+'" TAG "'+key+'"\n')
                        for feature in self.features[key]:
                            al(' LOOKUP "'+feature+'"')
                        al('\n')
                        al('END_FEATURE\n')
            return

        al('\n')
        al('DEF_SCRIPT NAME "'+self.pvar['scriptname']+'" TAG "'+self.pvar['scripttag']+'"\n')
        al('DEF_LANGSYS NAME "'+self.pvar['langsysname']+'" TAG "'+self.pvar['langsystag']+'"\n')
        enumfeatures()
        al('END_LANGSYS\n')
        al('END_SCRIPT\n')

        if self.pvar['test']['langsys'] == 1:
            print ('LANGSYS in test mode')
        else:
            print ('LANGSYS written')
            self.writelines(self.langlines)

### ANCHORS
    def anchors(self):
        self.anchorlines = []
        def anchorgroup(groupname,anchorgroups,details):
            grplist = sorted(groupdata[groupname])
            for listitem in grplist :
                if listitem in self.groupnames:
                    if details['recursive'] :
                        if not listitem in anchorgroups:
                            anchorgroups.append(listitem)
                            anchorgroup(listitem,anchorgroups,details)
                if listitem in self.glyphnames:
                    preformatanchor(details['aname'], listitem,details['xtype'],details['ytype'])
        def preformatanchor(anchor, glyphname,xtype,ytype):
            def formatdxy(type, max):
                if (type == 'YFULL'):
                    retvalue = int(round(self.pvar['vfu'] * self.pvar['vhu']))
                elif (type == 'MAX'):
                    retvalue = int(max)
                elif (type == 'MID'):
                    retvalue = int(max/2)
                elif (type == 'NYMID'):
                    searchObj = re.search('^.*([0-9])$',glyphname)
                    if (searchObj):
                        mtp = int(searchObj.group(1))
                        retvalue = int(mtp * self.pvar['vfu'] / 2) * -1
                    else:
                        retvalue = -1
                elif (type == 'NYSPC'): # Negative Y spacer
                    searchObj = re.search('^r[012]s([0-9])p([0-9]+)R?',glyphname)
                    if (searchObj):
                        mtp = float(searchObj.group(1)+'.'+searchObj.group(2))
                        retvalue = int(mtp * self.pvar['vfu'] * -1)
                    else:
                        retvalue = 0
                elif (type == 'NXUNIT'):
                    searchObj = re.search('^.*([0-9])R?$',glyphname)
                    if (searchObj):
                        mtp = int(searchObj.group(1))
                        retvalue = int(mtp * self.pvar['hfu'] * -1)
                    else:
                        retvalue = 0
                elif (type == 'NYUNIT'):
                    searchObj = re.search('^.*([0-9])R?$',glyphname)
                    if (searchObj):
                        mtp = int(searchObj.group(1))
                        retvalue = int(mtp * self.pvar['vfu'] * -1)
                    else:
                        retvalue = 0
                elif (type == 'PADDING'):
                    retvalue = self.pvar['sb']
                elif (type == 'PADDINGR'):
                    searchObj = re.search('^.*([0-9])V?$',glyphname)
                    if (searchObj):
                        mtp = int(searchObj.group(1))
                        retvalue = int(mtp * self.pvar['hfu']) + self.pvar['sb']
                    else:
                        retvalue = 0
                elif (type == 'XSUNIT'):
                    searchObj = re.search('^.*([0-9])[0-9]R?$',glyphname)
                    if (searchObj):
                        mtp = int(searchObj.group(1))
                        retvalue = int(mtp * self.pvar['hfu'])
                    else:
                        retvalue = 0
                elif (type == 'XUNIT'):
                    searchObj = re.search('^.*([0-9])$',glyphname)
                    if (searchObj):
                        mtp = int(searchObj.group(1))
                        retvalue = int(mtp * self.pvar['hfu'])
                    else:
                        retvalue = 0
                elif (type == 'YUNIT'):
                    searchObj = re.search('^.*([0-9])$',glyphname)
                    if (searchObj):
                        mtp = int(searchObj.group(1))
                        retvalue = int(mtp * self.pvar['vfu'])
                    else:
                        retvalue = 0
                elif (type == 'XMID'):
                    searchObj = re.search('^.*([0-9])[0-9]$',glyphname)
                    if (searchObj):
                        mtp = int(searchObj.group(1))
                        retvalue = int(mtp * self.pvar['hfu'] / 2)
                    else:
                        retvalue = -1
                elif (type == 'YMID'):
                    searchObj = re.search('^.*([0-9])$',glyphname)
                    if (searchObj):
                        mtp = int(searchObj.group(1))
                        retvalue = int(mtp * self.pvar['vfu'] / 2)
                    else:
                        retvalue = -1
                elif (type == 'XSPC'):
                    searchObj = re.search('^c[012]s([0-9])p([0-9]+)R?',glyphname)
                    if (searchObj):
                        mtp = float(searchObj.group(1)+'.'+searchObj.group(2))
                        retvalue = int(mtp * self.pvar['hfu'])
                    else:
                        retvalue = 0
                elif (type == 'NXSPC'):
                    searchObj = re.search('^c[012]s([0-9])p([0-9]+)R?',glyphname)
                    if (searchObj):
                        mtp = float(searchObj.group(1)+'.'+searchObj.group(2))
                        retvalue = int(mtp * self.pvar['hfu']) * -1
                    else:
                        retvalue = 0
                elif (type == 'ZERO'):
                    retvalue = int(0)
                else:
                    retvalue = -1
                return retvalue
            if not glyphname in self.glyphdata:
                self.errors.append('Missing glyph [eh647]: '+glyphname)
                return 0
            anchorObj = {'anchor':"",'gid':"",'gname':"",'dx':"",'dy':""}
            anchorObj['anchor'] = anchor
            anchorObj['gid'] = str(self.glyphdata[glyphname]['id'])
            anchorObj['gname'] = glyphname
            maxx = self.glyphdata[glyphname]['maxh']
            maxy = self.glyphdata[glyphname]['maxv']
            anchorObj['dx'] = str(formatdxy(xtype,maxx))
            anchorObj['dy'] = str(formatdxy(ytype,maxy))
            if (not anchorObj['dx'] == '-1' and not anchorObj['dy'] == '-1'):
                line = formatanchor(anchorObj)
                al(line)
            #else:
                #self.errors.append('Dropped anchor [eh661]:'+glyphname)
            return 0
        def formatanchor(anchorObj):
            anchor = anchorObj['anchor']
            gid = anchorObj['gid']
            gname = anchorObj['gname']
            if int(anchorObj['dx']):
                dx = ' DX '+str(anchorObj['dx'])
            else :
                dx = ''
            if int(anchorObj['dy']):
                dy = ' DY '+str(anchorObj['dy'])
            else :
                dy = ''
            line = 'DEF_ANCHOR "'+anchor+'" ON '+gid+\
                ' GLYPH '+gname+' COMPONENT 1 AT  POS'+\
                dx+dy+' END_POS END_ANCHOR\n'
            return line
        def al(line):
            self.anchorlines.append(line)
        self.groupnames = sorted(groupdata)
        self.glyphnames = sorted(self.glyphdata)

        # a1
        group = 'stems0-v'
        details = {'aname':'MARK_a1','xtype':'ZERO','ytype':'ZERO','recursive':1}
        anchorgroup(group,[group],details)
        group = 'bases_all'
        details = {'aname':'a1','xtype':'PADDING','ytype':'YFULL','recursive':1}
        anchorgroup(group,[group],details)
        group = 'extensionendsL'
        details = {'aname':'a1','xtype':'PADDING','ytype':'YFULL','recursive':1}
        anchorgroup(group,[group],details)

        # r1
        group = 'stems0-vR'
        details = {'aname':'MARK_r1','xtype':'ZERO','ytype':'ZERO','recursive':1}
        anchorgroup(group,[group],details)
        group = 'bases_all'
        details = {'aname':'r1','xtype':'PADDINGR','ytype':'YFULL','recursive':1}
        anchorgroup(group,[group],details)

        # bottom
        group = 'stems0-v'
        details = {'aname':'MARK_bottom','xtype':'ZERO','ytype':'ZERO','recursive':1}
        anchorgroup(group,[group],details)
        group = 'stems0-vR'
        details = {'aname':'MARK_bottom','xtype':'ZERO','ytype':'ZERO','recursive':1}
        anchorgroup(group,[group],details)
        group = 'stems1-v'
        details = {'aname':'MARK_bottom','xtype':'ZERO','ytype':'ZERO','recursive':1}
        anchorgroup(group,[group],details)
        group = 'stems1-vR'
        details = {'aname':'MARK_bottom','xtype':'ZERO','ytype':'ZERO','recursive':1}
        anchorgroup(group,[group],details)
        group = 'stems2-v'
        details = {'aname':'MARK_bottom','xtype':'ZERO','ytype':'ZERO','recursive':1}
        anchorgroup(group,[group],details)
        group = 'stems2-vR'
        details = {'aname':'MARK_bottom','xtype':'ZERO','ytype':'ZERO','recursive':1}
        anchorgroup(group,[group],details)
        group = 'stems0-v'
        details = {'aname':'bottom','xtype':'ZERO','ytype':'NYUNIT','recursive':0}
        anchorgroup(group,[group],details)
        group = 'stems0-vR'
        details = {'aname':'bottom','xtype':'ZERO','ytype':'NYUNIT','recursive':0}
        anchorgroup(group,[group],details)
        group = 'stems1-v'
        details = {'aname':'bottom','xtype':'ZERO','ytype':'NYUNIT','recursive':0}
        anchorgroup(group,[group],details)
        group = 'stems1-vR'
        details = {'aname':'bottom','xtype':'ZERO','ytype':'NYUNIT','recursive':0}
        anchorgroup(group,[group],details)
        group = 'stems2-v'
        details = {'aname':'bottom','xtype':'ZERO','ytype':'NYUNIT','recursive':0}
        anchorgroup(group,[group],details)
        group = 'stems2-vR'
        details = {'aname':'bottom','xtype':'ZERO','ytype':'NYUNIT','recursive':0}
        anchorgroup(group,[group],details)
        group = 'rowspacers0'
        details = {'aname':'bottom','xtype':'ZERO','ytype':'NYSPC','recursive':0}
        anchorgroup(group,[group],details)
        group = 'rowspacers0R'
        details = {'aname':'bottom','xtype':'ZERO','ytype':'NYSPC','recursive':0}
        anchorgroup(group,[group],details)
        group = 'rowspacers1'
        details = {'aname':'bottom','xtype':'ZERO','ytype':'NYSPC','recursive':0}
        anchorgroup(group,[group],details)
        group = 'rowspacers1R'
        details = {'aname':'bottom','xtype':'ZERO','ytype':'NYSPC','recursive':0}
        anchorgroup(group,[group],details)
        group = 'rowspacers2'
        details = {'aname':'bottom','xtype':'ZERO','ytype':'NYSPC','recursive':0}
        anchorgroup(group,[group],details)
        group = 'rowspacers2R'
        details = {'aname':'bottom','xtype':'ZERO','ytype':'NYSPC','recursive':0}
        anchorgroup(group,[group],details)

        # top
        group = 'stems0-h'
        details = {'aname':'MARK_top','xtype':'ZERO','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)
        group = 'stems0-hR'
        details = {'aname':'MARK_top','xtype':'ZERO','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)
        group = 'stems1-h'
        details = {'aname':'MARK_top','xtype':'ZERO','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)
        group = 'stems1-hR'
        details = {'aname':'MARK_top','xtype':'ZERO','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)
        group = 'stems2-h'
        details = {'aname':'MARK_top','xtype':'ZERO','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)
        group = 'stems2-hR'
        details = {'aname':'MARK_top','xtype':'ZERO','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)
        group = 'tcbb_mks'
        details = {'aname':'MARK_top','xtype':'ZERO','ytype':'YUNIT','recursive':0}
        anchorgroup(group,[group],details)
        group = 'stems0-h'
        details = {'aname':'top','xtype':'ZERO','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)
        group = 'stems0-v'
        details = {'aname':'top','xtype':'ZERO','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)
        group = 'stems0-vR'
        details = {'aname':'top','xtype':'ZERO','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)
        group = 'stems1-v'
        details = {'aname':'top','xtype':'ZERO','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)
        group = 'stems1-vR'
        details = {'aname':'top','xtype':'ZERO','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)
        group = 'stems2-v'
        details = {'aname':'top','xtype':'ZERO','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)
        group = 'stems2-vR'
        details = {'aname':'top','xtype':'ZERO','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)

        # right
        group = 'stems0-h'
        details = {'aname':'MARK_right','xtype':'ZERO','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)
        group = 'stems1-h'
        details = {'aname':'MARK_right','xtype':'ZERO','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)
        group = 'stems2-h'
        details = {'aname':'MARK_right','xtype':'ZERO','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)
        group = 'shapes_u'
        details = {'aname':'MARK_right','xtype':'XSUNIT','ytype':'YUNIT','recursive':0}
        anchorgroup(group,[group],details)
        group = 'tcbe0_mks'
        details = {'aname':'MARK_right','xtype':'ZERO','ytype':'YUNIT','recursive':0}
        anchorgroup(group,[group],details)
        group = 'tcbe1_mks'
        details = {'aname':'MARK_right','xtype':'ZERO','ytype':'YUNIT','recursive':0}
        anchorgroup(group,[group],details)
        group = 'tcbe2_mks'
        details = {'aname':'MARK_right','xtype':'ZERO','ytype':'YUNIT','recursive':0}
        anchorgroup(group,[group],details)
        group = 'stems0-h'
        details = {'aname':'right','xtype':'XUNIT','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)
        group = 'stems1-h'
        details = {'aname':'right','xtype':'XUNIT','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)
        group = 'stems2-h'
        details = {'aname':'right','xtype':'XUNIT','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)
        group = 'colspacers0'
        details = {'aname':'right','xtype':'XSPC','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)
        group = 'colspacers1'
        details = {'aname':'right','xtype':'XSPC','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)
        group = 'colspacers2'
        details = {'aname':'right','xtype':'XSPC','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)
        group = 'shapes_0'
        details = {'aname':'right','xtype':'XSUNIT','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)
        group = 'shapes_1'
        details = {'aname':'right','xtype':'XSUNIT','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)
        group = 'shapes_2'
        details = {'aname':'right','xtype':'XSUNIT','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)
        group = 'shapes_u'
        details = {'aname':'right','xtype':'XSUNIT','ytype':'YUNIT','recursive':0}
        anchorgroup(group,[group],details)
        group = 'shapes_om'
        details = {'aname':'right','xtype':'XSUNIT','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)
        group = 'shapes_om2'
        details = {'aname':'right','xtype':'XSUNIT','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)
        # group = 'insertionsizes1R'
        # details = {'aname':'right','xtype':'XSUNIT','ytype':'ZERO','recursive':0}
        # anchorgroup(group,[group],details)

        # left
        group = 'stems0-hR'
        details = {'aname':'MARK_left','xtype':'ZERO','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)
        group = 'stems1-hR'
        details = {'aname':'MARK_left','xtype':'ZERO','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)
        group = 'stems2-hR'
        details = {'aname':'MARK_left','xtype':'ZERO','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)
        group = 'stems0-hR'
        details = {'aname':'left','xtype':'NXUNIT','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)
        group = 'stems1-hR'
        details = {'aname':'left','xtype':'NXUNIT','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)
        group = 'stems2-hR'
        details = {'aname':'left','xtype':'NXUNIT','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)
        group = 'colspacers0R'
        details = {'aname':'left','xtype':'NXSPC','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)
        group = 'colspacers1R'
        details = {'aname':'left','xtype':'NXSPC','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)
        group = 'colspacers2R'
        details = {'aname':'left','xtype':'NXSPC','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)
        group = 'shapes_0'
        details = {'aname':'MARK_left','xtype':'ZERO','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)
        group = 'shapes_1'
        details = {'aname':'MARK_left','xtype':'ZERO','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)
        group = 'shapes_2'
        details = {'aname':'MARK_left','xtype':'ZERO','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)
        group = 'shapes_u'
        details = {'aname':'MARK_left','xtype':'ZERO','ytype':'YUNIT','recursive':0}
        anchorgroup(group,[group],details)
        group = 'corners1b'
        details = {'aname':'MARK_left','xtype':'ZERO','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)
        group = 'stems0-v'
        details = {'aname':'MARK_left','xtype':'ZERO','ytype':'ZERO','recursive':1}
        anchorgroup(group,[group],details)
        group = 'stems0-vR'
        details = {'aname':'MARK_left','xtype':'ZERO','ytype':'ZERO','recursive':1}
        anchorgroup(group,[group],details)
        group = 'stems1-v'
        details = {'aname':'MARK_left','xtype':'ZERO','ytype':'ZERO','recursive':1}
        anchorgroup(group,[group],details)
        group = 'stems1-vR'
        details = {'aname':'MARK_left','xtype':'ZERO','ytype':'ZERO','recursive':1}
        anchorgroup(group,[group],details)
        group = 'stems2-v'
        details = {'aname':'MARK_left','xtype':'ZERO','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)
        group = 'stems2-vR'
        details = {'aname':'MARK_left','xtype':'ZERO','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)
        group = 'shapes_mi'
        details = {'aname':'MARK_left','xtype':'ZERO','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)
        group = 'shapes_mi2'
        details = {'aname':'MARK_left','xtype':'ZERO','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)
        group = 'shapes_0'
        details = {'aname':'left','xtype':'ZERO','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)
        group = 'shapes_1'
        details = {'aname':'left','xtype':'ZERO','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)
        group = 'shapes_u'
        details = {'aname':'left','xtype':'ZERO','ytype':'YUNIT','recursive':0}
        anchorgroup(group,[group],details)

        # its
        group = 'shapes_u'
        details = {'aname':'MARK_ts','xtype':'ZERO','ytype':'YUNIT','recursive':0}
        anchorgroup(group,[group],details)

        # ibs
        for glyph in groupdata['shapes_0']:
            preformatanchor('bs',glyph,'ZERO','NYUNIT')
            preformatanchor('te',glyph,'XSUNIT','ZERO')
            preformatanchor('be',glyph,'XSUNIT','NYUNIT')
        for glyph in groupdata['shapes_1']:
            preformatanchor('bs',glyph,'ZERO','NYUNIT')
            preformatanchor('te',glyph,'XSUNIT','ZERO')
            preformatanchor('be',glyph,'XSUNIT','NYUNIT')

        for glyph in groupdata['shapes_bs']:
            preformatanchor('MARK_bs',glyph,'ZERO','NYUNIT')
            preformatanchor('MARK_be',glyph,'XSUNIT','NYUNIT') # RTL
        for glyph in groupdata['shapes_bs2']:
            preformatanchor('MARK_bs',glyph,'ZERO','NYUNIT')
            preformatanchor('MARK_be',glyph,'XSUNIT','NYUNIT') # RTL

        for glyph in groupdata['shapes_te']:
            preformatanchor('MARK_te',glyph,'XSUNIT','ZERO')
            preformatanchor('MARK_ts',glyph,'ZERO','ZERO') # RTL
        for glyph in groupdata['shapes_te2']:
            preformatanchor('MARK_te',glyph,'XSUNIT','ZERO')
            preformatanchor('MARK_ts',glyph,'ZERO','ZERO') # RTL
        for glyph in groupdata['shapes_be']:
            preformatanchor('MARK_be',glyph,'XSUNIT','NYUNIT')
            preformatanchor('MARK_bs',glyph,'ZERO','NYUNIT') # RTL
        for glyph in groupdata['shapes_be2']:
            preformatanchor('MARK_be',glyph,'XSUNIT','NYUNIT')
            preformatanchor('MARK_bs',glyph,'ZERO','NYUNIT') # RTL

        # itm
        group = 'shapes_ti'
        details = {'aname':'MARK_ti','xtype':'XMID','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)
        group = 'shapes_ti2'
        details = {'aname':'MARK_ti','xtype':'XMID','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)
        group = 'insertionsizes1'
        details = {'aname':'MARK_ti','xtype':'XMID','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)
        group = 'insertionsizes2'
        details = {'aname':'MARK_ti','xtype':'XMID','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)
        group = 'shapes_u'
        details = {'aname':'MARK_ti','xtype':'XMID','ytype':'YUNIT','recursive':0}
        anchorgroup(group,[group],details)
        group = 'shapes_0'
        details = {'aname':'ti','xtype':'XMID','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)
        group = 'shapes_1'
        details = {'aname':'ti','xtype':'XMID','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)
        group = 'shapes_ti'
        details = {'aname':'ti','xtype':'XMID','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)
        group = 'shapes_ti2'
        details = {'aname':'ti','xtype':'XMID','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)

        # ibm
        preformatanchor('MARK_bi','b0','ZERO','ZERO')
        group = 'shapes_bi'
        details = {'aname':'MARK_bi','xtype':'XMID','ytype':'NYUNIT','recursive':0}
        anchorgroup(group,[group],details)
        group = 'shapes_bi2'
        details = {'aname':'MARK_bi','xtype':'XMID','ytype':'NYUNIT','recursive':0}
        anchorgroup(group,[group],details)
        group = 'insertionsizes1'
        details = {'aname':'MARK_bi','xtype':'XMID','ytype':'NYUNIT','recursive':0}
        anchorgroup(group,[group],details)
        group = 'insertionsizes2'
        details = {'aname':'MARK_bi','xtype':'XMID','ytype':'NYUNIT','recursive':0}
        anchorgroup(group,[group],details)
        group = 'shapes_u'
        details = {'aname':'MARK_bi','xtype':'XMID','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)
        preformatanchor('bi','b0','ZERO','ZERO')
        group = 'shapes_0'
        details = {'aname':'bi','xtype':'XMID','ytype':'NYUNIT','recursive':0}
        anchorgroup(group,[group],details)
        group = 'shapes_1'
        details = {'aname':'bi','xtype':'XMID','ytype':'NYUNIT','recursive':0}
        anchorgroup(group,[group],details)
        group = 'shapes_bi'
        details = {'aname':'bi','xtype':'XMID','ytype':'NYUNIT','recursive':0}
        anchorgroup(group,[group],details)
        group = 'shapes_bi2'
        details = {'aname':'bi','xtype':'XMID','ytype':'NYUNIT','recursive':0}
        anchorgroup(group,[group],details)
        group = 'shapes_df'
        details = {'aname':'MARK_bi','xtype':'XMID','ytype':'NYUNIT','recursive':0}
        anchorgroup(group,[group],details)
        group = 'shapes_dq'
        details = {'aname':'MARK_bi','xtype':'XMID','ytype':'NYUNIT','recursive':0}
        anchorgroup(group,[group],details)
        group = 'glyphs_all'
        details = {'aname':'MARK_bi','xtype':'MID','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)
        group = 'mirror_all'
        details = {'aname':'MARK_bi','xtype':'MID','ytype':'ZERO','recursive':0}
        anchorgroup(group,[group],details)

        # center        
        preformatanchor('MARK_center','m0','ZERO','ZERO')

        group = 'insertionsizes1'
        details = {'aname':'MARK_center','xtype':'XMID','ytype':'NYMID','recursive':0}
        anchorgroup(group,[group],details)
        # group = 'insertionsizes1R'
        # details = {'aname':'MARK_center','xtype':'XMID','ytype':'NYMID','recursive':0}
        # anchorgroup(group,[group],details)
        group = 'insertionsizes2'
        details = {'aname':'MARK_center','xtype':'XMID','ytype':'NYMID','recursive':0}
        anchorgroup(group,[group],details)
        # group = 'insertionsizes2R'
        # details = {'aname':'MARK_center','xtype':'XMID','ytype':'NYMID','recursive':0}
        # anchorgroup(group,[group],details)
        group = 'shapes_om'
        details = {'aname':'MARK_center','xtype':'XMID','ytype':'NYMID','recursive':0}
        anchorgroup(group,[group],details)
        group = 'shapes_om2'
        details = {'aname':'MARK_center','xtype':'XMID','ytype':'NYMID','recursive':0}
        anchorgroup(group,[group],details)
        group = 'shapes_ti'
        details = {'aname':'MARK_center','xtype':'XMID','ytype':'NYMID','recursive':0}
        anchorgroup(group,[group],details)
        group = 'shapes_ti2'
        details = {'aname':'MARK_center','xtype':'XMID','ytype':'NYMID','recursive':0}
        anchorgroup(group,[group],details)
        group = 'shapes_mi'
        details = {'aname':'MARK_center','xtype':'XMID','ytype':'NYMID','recursive':0}
        anchorgroup(group,[group],details)
        group = 'shapes_mi2'
        details = {'aname':'MARK_center','xtype':'XMID','ytype':'NYMID','recursive':0}
        anchorgroup(group,[group],details)
        group = 'shapes_bi'
        details = {'aname':'MARK_center','xtype':'XMID','ytype':'NYMID','recursive':0}
        anchorgroup(group,[group],details)
        group = 'shapes_bi2'
        details = {'aname':'MARK_center','xtype':'XMID','ytype':'NYMID','recursive':0}
        anchorgroup(group,[group],details)
        group = 'shapes_u'
        details = {'aname':'MARK_center','xtype':'XMID','ytype':'YMID','recursive':0}
        anchorgroup(group,[group],details)
        group = 'shapes_df'
        details = {'aname':'MARK_center','xtype':'XMID','ytype':'YMID','recursive':0}
        anchorgroup(group,[group],details)
        group = 'shapes_dq'
        details = {'aname':'MARK_center','xtype':'XMID','ytype':'YMID','recursive':0}
        anchorgroup(group,[group],details)
        group = 'glyphs_all'
        details = {'aname':'MARK_center','xtype':'MID','ytype':'MID','recursive':0}
        anchorgroup(group,[group],details)
        group = 'mirror_all'
        details = {'aname':'MARK_center','xtype':'MID','ytype':'MID','recursive':0}
        anchorgroup(group,[group],details)
        group = 'controls_joiners'
        details = {'aname':'MARK_center','xtype':'MID','ytype':'MID','recursive':0}
        anchorgroup(group,[group],details)
        preformatanchor('center','m0','ZERO','ZERO')
        group = 'shapes_0'
        details = {'aname':'center','xtype':'XMID','ytype':'NYMID','recursive':0}
        anchorgroup(group,[group],details)
        group = 'shapes_1'
        details = {'aname':'center','xtype':'XMID','ytype':'NYMID','recursive':0}
        anchorgroup(group,[group],details)
        group = 'shapes_2'
        details = {'aname':'center','xtype':'XMID','ytype':'NYMID','recursive':0}
        anchorgroup(group,[group],details)
        group = 'shapes_u'
        details = {'aname':'center','xtype':'XMID','ytype':'YMID','recursive':0}
        anchorgroup(group,[group],details)
        group = 'shapes_ts'
        details = {'aname':'center','xtype':'XMID','ytype':'NYMID','recursive':0}
        anchorgroup(group,[group],details)
        group = 'shapes_bs'
        details = {'aname':'center','xtype':'XMID','ytype':'NYMID','recursive':0}
        anchorgroup(group,[group],details)
        group = 'shapes_te'
        details = {'aname':'center','xtype':'XMID','ytype':'NYMID','recursive':0}
        anchorgroup(group,[group],details)
        group = 'shapes_be'
        details = {'aname':'center','xtype':'XMID','ytype':'NYMID','recursive':0}
        anchorgroup(group,[group],details)
        group = 'shapes_om'
        details = {'aname':'center','xtype':'XMID','ytype':'NYMID','recursive':0}
        anchorgroup(group,[group],details)
        group = 'shapes_mi'
        details = {'aname':'center','xtype':'XMID','ytype':'NYMID','recursive':0}
        anchorgroup(group,[group],details)
        group = 'shapes_ts2'
        details = {'aname':'center','xtype':'XMID','ytype':'NYMID','recursive':0}
        anchorgroup(group,[group],details)
        group = 'shapes_bs2'
        details = {'aname':'center','xtype':'XMID','ytype':'NYMID','recursive':0}
        anchorgroup(group,[group],details)
        group = 'shapes_te2'
        details = {'aname':'center','xtype':'XMID','ytype':'NYMID','recursive':0}
        anchorgroup(group,[group],details)
        group = 'shapes_be2'
        details = {'aname':'center','xtype':'XMID','ytype':'NYMID','recursive':0}
        anchorgroup(group,[group],details)
        group = 'shapes_om2'
        details = {'aname':'center','xtype':'XMID','ytype':'NYMID','recursive':0}
        anchorgroup(group,[group],details)
        group = 'shapes_mi2'
        details = {'aname':'center','xtype':'XMID','ytype':'NYMID','recursive':0}
        anchorgroup(group,[group],details)
        group = 'genericbases'
        details = {'aname':'center','xtype':'MID','ytype':'MID','recursive':0}
        anchorgroup(group,[group],details)

        # write lines
        if self.pvar['test']['anchors'] == 1:
            print ('ANCHORS in test mode')
        else:
            self.writelines(self.anchorlines)
            print ('ANCHORS written')

### CODA 
    def coda(self):
        self.codalines = []
        def al(line):
            self.codalines.append(line)

        al('GRID_PPEM 36\n')
        al('PRESENTATION_PPEM 120\n')
        al('PPOSITIONING_PPEM 144\n')
        al('COMPILER_USEEXTENSIONLOOKUPS\n')
        al('DO_NOT_TOUCH_CMAP\n')
        al('CMAP_FORMAT 0 3 4\n')
        al('CMAP_FORMAT 1 0 6\n')
        al('CMAP_FORMAT 3 1 4\n')
        al('CMAP_FORMAT 3 10 12 END\n')

        if self.pvar['test']['coda'] == 1:
            print ('CODA in test mode')
        else:
            self.writelines(self.codalines)
            print ('CODA written')
        print (self.fontsave)
        print ('Total lookups written: ' + str(self.lookupcount))

### AUX
    def preloadgroups(self):
        self.injectedglyphcount = 0

        # output groups
        self.fontsrc = TTFont(self.pvar['fontsrc'])
        glyphnames = self.fontsrc.getGlyphOrder()
        groupnames = sorted(groupdata)
        for key in groupnames:
            grplist = sorted(groupdata[key],\
                key=lambda item: (int(item.partition(' ')[0])\
                            if item[0].isdigit() else float('inf'), item))
            groupenum = ''            
            for listitem in grplist:
                grouptype = 'GLYPH'
                if listitem in groupnames:
                    grouptype = 'GROUP'
                elif listitem in glyphnames:
                    grouptype = 'GLYPH'
                else:
                    grouptype = 'GLYPH'
                    self.insertglyphs(listitem)
                    self.injectedglyphcount += 1
                groupenum += grouptype+' "'+listitem+'" '
    def loadglyphdata(self):
        def calculateGroup(dec, name):
            variation  = re.search(r'^VS[0-9]$',name)
            hieroglyph = re.search(r'^[A-Z]+[0-9]+[a-z]?v?$',name)
            sizevar    = re.search(r'^[A-Z]+[0-9]+[a-z]?_([0-9][0-9])$',name)
            mirror     = re.search(r'^[A-Z]+[0-9]+[a-z]?(_[0-9][0-9])?R$',name)
            ninetyC    = re.search(r'^[A-Z]+[0-9]+[a-z]?n$',name)
            ninetyS    = re.search(r'^[A-Z]+[0-9]+[a-z]?n_[0-9][0-9]$',name)
            oneeightyC = re.search(r'^[A-Z]+[0-9]+[a-z]?o$',name)
            oneeightyS = re.search(r'^[A-Z]+[0-9]+[a-z]?o_[0-9][0-9]$',name)
            twoseventyC= re.search(r'^[A-Z]+[0-9]+[a-z]?t$',name)
            twoseventyS= re.search(r'^[A-Z]+[0-9]+[a-z]?t_[0-9][0-9]$',name)
            shade      = re.search(r'^LS_[1-8][1-6]$',name)
            qshade     = re.search(r'DQ[0-9]\_[0-9]+',name)
            ligature   = re.search(r'^lig.*[^R]$',name)
            ligmirror  = re.search(r'^lig.*R$',name)
            tcm        = re.search(r'^tc[abchpr][be]$',name)
            tcmvar     = re.search(r'^tc[abchpr][be]_[0-9][0-9]$',name)

            if dec > 65535: #mapped SMP characters
                if name in qcontrols:
                    group = 'Joiner'
                elif (hieroglyph): #name matches the pattern for a hieroglyph
                    group = 'Chr'
                elif name in punctuation:
                    group = 'Cmn'
                else:    
                    group = 'Chr' #pick up glyphs outside Gardiner set
            elif dec > 0 and dec <= 65535: #mapped BMP characters
                if name in punctuation:
                    group = 'Punctuation'
                elif (variation): #name matches the pattern for a variation selector
                    group = 'VS'
                elif dec == 9676: #dotted circle as generic base
                    group = 'Chr'
                else:
                    group = 'Cmn'
            elif (ligature): #is a ligature
                if (re.search(r'^.*_([0-9][0-9])$',name)):
                    group = 'LigV' #ligature size variant
                    if name not in self.ligatures_all:
                        self.ligatures_all.append(name)
                else:
                    group = 'LigR' #ligature root size
                    if name not in self.ligatures:
                        self.ligatures.append(name)
                        self.ligatures_all.append(name)
            elif (shade): #sign shade
                group = 'Shade'
            elif (qshade): #quarter shade
                group = 'Shade'
            elif (ninetyC): #name is a rotated glyph and includes n flag
                group = 'Chr'
                if name not in self.rotated090:
                    self.rotated090.append(name)
            elif (ninetyS): #name is a size variant and includes n flag
                group = 'SVar'
            elif (oneeightyC): #name is a rotated glyph and includes n flag
                group = 'Chr'
                if name not in self.rotated180:
                    self.rotated180.append(name)
            elif (oneeightyS): #name is a rotated glyph and includes o flag
                group = 'SVar'
            elif (twoseventyC): #name is a rotated glyph and includes t flag
                group = 'Chr'
                if name not in self.rotated270:
                    self.rotated270.append(name)
            elif (twoseventyS): #name is a rotated size variant and includes t flag
                group = 'SVar'
            elif (sizevar): #name includes glyph size in ehu
                group = 'SVar'
            elif (mirror): #name includes R flag
                group = 'Mirror'
            elif (ligmirror): #name is a ligature and includes R flag
                group = 'Mirror'
            elif (tcm): #composing text critical mark
                group = 'Chr'
            elif (tcmvar): #text critical mark size variant
                group = 'SVar'
            elif (name in ['GB1','BF1','BQ1','dottedcircle','AS2','AQ2','AT2','AW2']): # treat these as hieroglyphs
                group = 'Chr'
            else: #unmapped control characters for OTL
                group = 'Ctrl'
            return group

        glyphTable = self.fontsrc['glyf']
        cmap = self.fontsrc.getBestCmap()
        for name in self.fontsrc.getGlyphOrder():
            glyph = {'id':'','name':'','root':'','dec':0,'hex':0x0,'group':'','type':'M','maxh':0,'maxv':0,'ehuh':0,'ehuv':0,'tshash':''}
            glyph['id'] = self.fontsrc.getGlyphID(name)
            glyph['name'] = name
            if name in cmap.values():
                gdec = list(cmap.keys())[list(cmap.values()).index(name)]
                glyph['dec'] = gdec
                glyph['hex'] = hex(gdec)                
                if self.pvar['useproxycontrols']:
                    # suppress original proxy values for non controls
                    if gdec in self.pvar['proxycontrols']:
                        glyph['dec'] = 0
                        glyph['hex'] = 0x0
            if self.pvar['useproxycontrols']:
                # apply proxy values to controls
                if name in self.pvar['controls2']:
                    index = self.pvar['controls2'].index(name)
                    pdec = self.pvar['proxycontrols'][index]
                    glyph['dec'] = pdec
                    glyph['hex'] = hex(pdec)
                    cmap[pdec] = name
            if glyph['dec'] > 0:
                self.glyphHexToName[glyph['hex']] = name
            group = calculateGroup(glyph['dec'],name)
            glyph['group'] = group
            glyph['type'] = 'M'
            if name in basetypes:
                glyph['type'] = 'B'
            if group == 'Cmn':
                glyph['type'] = 'B'
            if group in ['Chr','LigR']:
                glyph['root'] = name
            if group in ['Chr','Joiner','Mirror','SVar','LigR','LigV']:
                glyphObj = glyphTable[name]
                if name[0:2] in ['BF','BQ']:
                    if name == 'BF1':
                        glyph['maxh'] = self.pvar['hfu'] * 6
                        glyph['maxv'] = self.pvar['vfu'] * 6
                    elif name == 'BQ1':
                        glyph['maxh'] = self.pvar['hfu'] * 3
                        glyph['maxv'] = self.pvar['vfu'] * 3
                    else:
                        hval = re.sub(r'B[FQ]1_(\d)\d',r'\1',name)
                        vval = re.sub(r'B[FQ]1_\d(\d)',r'\1',name)
                        glyph['maxh'] = self.pvar['hfu'] * int(hval)
                        glyph['maxv'] = self.pvar['vfu'] * int(vval)
                elif name[0:3] == 'AS2':
                    if name == 'AS2':
                        glyph['maxh'] = self.pvar['hfu'] * 6
                        glyph['maxv'] = self.pvar['vfu'] * 6
                    else:
                        hval = re.sub(r'AS2_(\d)\d',r'\1',name)
                        vval = re.sub(r'AS2_\d(\d)',r'\1',name)
                        glyph['maxh'] = self.pvar['hfu'] * int(hval)
                        glyph['maxv'] = self.pvar['vfu'] * int(vval)
                elif name[0:3] == 'AQ2':
                    if name == 'AQ2':
                        glyph['maxh'] = self.pvar['hfu'] * 3
                        glyph['maxv'] = self.pvar['vfu'] * 3
                    else:
                        hval = re.sub(r'AQ2_(\d)\d',r'\1',name)
                        vval = re.sub(r'AQ2_\d(\d)',r'\1',name)
                        glyph['maxh'] = self.pvar['hfu'] * int(hval)
                        glyph['maxv'] = self.pvar['vfu'] * int(vval)
                elif name[0:3] == 'AT2':
                    if name == 'AT2':
                        glyph['maxh'] = self.pvar['hfu'] * 3
                        glyph['maxv'] = self.pvar['vfu'] * 6
                    else:
                        hval = re.sub(r'AT2_(\d)\d',r'\1',name)
                        vval = re.sub(r'AT2_\d(\d)',r'\1',name)
                        glyph['maxh'] = self.pvar['hfu'] * int(hval)
                        glyph['maxv'] = self.pvar['vfu'] * int(vval)
                elif name[0:3] == 'AW2':
                    if name == 'AW2':
                        glyph['maxh'] = self.pvar['hfu'] * 6
                        glyph['maxv'] = self.pvar['vfu'] * 3
                    else:
                        hval = re.sub(r'AW2_(\d)\d',r'\1',name)
                        vval = re.sub(r'AW2_\d(\d)',r'\1',name)
                        glyph['maxh'] = self.pvar['hfu'] * int(hval)
                        glyph['maxv'] = self.pvar['vfu'] * int(vval)
                elif name[0:2] in ['dq']:
                    glyph['maxh'] = self.pvar['hfu'] * 6
                    glyph['maxv'] = self.pvar['vfu'] * 6
                else:
                    if hasattr(glyphObj, 'xMax'):
                        glyph['maxh'] = glyphObj.xMax
                    else:
                        print("Error: xMax missing for "+str(glyph['name']+" "+glyph['group']))
                    if hasattr(glyphObj, 'yMax'):
                        glyph['maxv'] = glyphObj.yMax - self.pvar['vbase']
                    else:
                        print("Error: yMax missing for "+str(glyph['name']))
            else :
                glyph['maxh'] = 0
                glyph['maxv'] = 0
            glyph['ehuh'] = int(math.ceil((float(glyph['maxh'])-self.pvar['issp'])/(float(self.pvar['hfu']))))
            if glyph['ehuh'] > self.pvar['hhu']:
                self.errors.append('Too wide [eh104]: '+str(glyph['id'])+' '+glyph['name']+', >>> '+str(glyph['ehuh'])+'.')           
            glyph['ehuv'] = int(math.ceil((float(glyph['maxv'])-self.pvar['issp'])/(float(self.pvar['vfu']))))
            if glyph['ehuv'] > self.pvar['vhu']:
                if glyph['name'] not in qcontrols:
                    self.errors.append('Too tall [eh105]: '+str(glyph['id'])+' '+glyph['name']+', >>> '+str(glyph['ehuv'])+'.')
            if group in ['SVar','LigV']:
                searchObj = re.search(r'^(.*)_([0-9]*)$',name)
                namedsize= '00'
                if (searchObj):
                    root = searchObj.group(1)
                    namedsize = searchObj.group(2)
                    glyph['root'] = root
                ehv = str(glyph['ehuh']) + str(glyph['ehuv'])
                if namedsize != ehv:
                    self.errors.append('Wrong size [eh1450]: '+str(glyph['id'])+' '+glyph['name']+', >>> '+ehv+'.')
            hvsize = str(glyph['ehuh'])+str(glyph['ehuv'])
            if hvsize in self.maxhvsizes:
                self.maxhvsizes[hvsize] += 1
                pass
            else:
                self.maxhvsizes[hvsize] = 1

            self.glyphdata[name] = glyph
    def insertglyphs(self,newglyph):
        self.fontsrc['glyf'][newglyph] = Glyph()
        self.fontsrc['hmtx'][newglyph] = (0,0)
        # print(self.fontsrc.getGlyphID(newglyph))
        return self.fontsrc.getGlyphID(newglyph)
    def loadgroups(self):
        def formatgroup(groupObj):
            groupline = 'DEF_GROUP "'+groupObj['name']+'"\n'\
                ' ENUM '+groupObj['enum']+'END_ENUM\n'\
                'END_GROUP\n'
            return groupline
        def al(line):
            self.grouplines.append(line)
        def loadtargetsizes(key):
            root = self.glyphdata[key]['root']
            hval = self.glyphdata[key]['ehuh']
            if hval > 9:
                hval = 9
            vval = self.glyphdata[key]['ehuv']
            if vval > 9:
                vval = 9
            ehv = str(hval) + str(vval)
            if root in self.targetsizes:
                sizes = self.targetsizes[root]
                sizes.append(ehv)
            else:
                sizes = [ehv]
            self.targetsizes[root] = sizes
        def hashtargetsizes():
            groupdata['tsh'] = []
            for key in self.targetsizes:
                if key in self.glyphdata:
                    tshash = ''
                    for size in sorted(self.targetsizes[key], reverse = True):
                        tshash += size
                    self.glyphdata[key]['tshash'] = str(tshash)
                    if not tshash in self.tshashes:
                        self.tshashes.append(tshash)
                        tsg = 'tsh'+(tshash)
                        groupdata['tsh'].append(tsg)
                        gid = self.insertglyphs(tsg)
                        glyph = {'id':gid,'name':tsg,'root':'','dec':0,'hex':0x0,'group':'','type':'M','maxh':0,'maxv':0,'ehuh':0,'ehuv':0,'tshash':''}
                        self.glyphdata[tsg] = glyph
                        self.injectedglyphcount += 1
                else:
                    self.errors.append('Missing base glyph '+str(key)+' for variant sizes')
        def savefont():
            print ('Saving font...')
            if self.pvar['test']['font'] == 1:
                self.fontsave = 'Font save suppressed'
            else: 
                if self.injectedglyphcount > 0:
                    self.fontsrc.save('out/fontout_temp.ttf')
                    self.fontsrc.getBestCmap
                    self.fontsave = 'Glyphs added: '+str(self.injectedglyphcount)
                else:
                    self.fontsave = 'No glyphs added'

        self.ehv_ligatures = []
        self.glyphs_all = []
        self.glyphs_ligatures = []
        self.grouplines = []
        glyphnames = sorted(self.glyphdata)
        ehvs = {}

        # dynamic groups
        for key in self.glyphdata:
            ggroup = self.glyphdata[key]['group']

            # sizevariants groups
            if ggroup in ['SVar','LigV']:
                groupdata['glyphs_all'].append(key)
                loadtargetsizes(key)

            # character groups
            if ggroup in ['Chr','LigR']:
                if not key in qcontrols:
                    groupdata['characters_all'].append(key)
                    groupdata['glyphs_all'].append(key)
                    loadtargetsizes(key)

            # mirror group
            if (ggroup == 'Mirror'):
                if not key in qcontrols:
                    groupdata['mirror_all'].append(key)

        hashtargetsizes()
        savefont()
        ehvkeys = sorted(ehvs)
        for ehvkey in ehvkeys:
            sizekey = 'ehv'+ehvs[ehvkey]
            ehvgroup = []
            if sizekey in groupdata:
                ehvgroup = groupdata[sizekey]
                ehvgroup.append(ehvkey)
            else:
                ehvgroup.append(ehvkey)
                self.sizekeys.append(sizekey)

        # output groups
        groupnames = sorted(groupdata)
        for key in groupnames:
            grplist = sorted(groupdata[key],\
                key=lambda item: (int(item.partition(' ')[0])\
                            if item[0].isdigit() else float('inf'), item))

            groupenum = ''            
            groupObj = {}
            for listitem in grplist:
                grouptype = 'GLYPH'
                if listitem in groupnames:
                    grouptype = 'GROUP'
                elif listitem in glyphnames:
                    grouptype = 'GLYPH'
                else:
                    grouptype = 'GLYPH'
                groupenum += grouptype+' "'+listitem+'" '
            groupObj['name'] = key
            groupObj['enum'] = groupenum
            grpline = formatgroup(groupObj)
            al(grpline)
    def glyphOrGroup(self, item):
        glyphnames = sorted(self.glyphdata)
        groupnames = sorted(groupdata)
        if item in glyphnames:
            retval = 'GLYPH'
        elif item in groupnames:
            retval = 'GROUP'
            #self.errors.append('GROUPCHECK: lookup group - '+item)
        else:
            print('Error: Glyph name missing, '+str(item))
            retval = -1
        return retval
    def setfeaturetag(self,level):
        tags = ['rlig','blws','abvs']
        featuretag = tags[level]
        return featuretag
    def createVTPFile(self):
        self.writefile = 'out/'+self.compactfontfilename+'.vtp'
        writefile = open(self.writefile,"w")
        writefile.write('')

        return
    def createErrorFile(self):
        self.errorfile = 'out/'+self.compactfontfilename+'_errors.txt'
        errorfile = open(self.errorfile,"w")
        errorfile.write('')

        return
    def writeTestFile(self,lines):
        self.testfile = 'out/'+self.compactfontfilename+'.html'
        writefile = open(self.testfile,"w")

        for line in lines:
            writefile.write(line)        
        return
    def writeCMAP14File(self,lines,type):
        self.cmap14file = self.compactfontfilename+'.cmap'+type
        writefile = open('out/'+self.cmap14file,"w")

        i = 0
        for line in lines:
            writefile.write(line)
            if line.find('0xfe') > 0:
                i += 1
        print('Wrote '+str(i)+' variations to '+self.cmap14file)
        return
    def writeVmtxFile(self,lines):
        self.vmtxfile = 'out/'+self.compactfontfilename+'.vmtx'
        writefile = open(self.vmtxfile,"w")

        i = 0
        for line in lines:
            writefile.write(line)
            if line.find('0xFE') > 0:
                i += 1
        print('Wrote vmtx table to '+self.vmtxfile)
        return
    def writeKbdFile(self,lines):
        fontfilename = re.sub(' ','',self.pvar['fontfilename'])
        self.kbdfile = 'out/'+fontfilename.lower()+'.kmn'
        wf = codecs.open(self.kbdfile, 'w','utf-8')

        for line in lines:
            wf.write(line+"\n")
        wf.close()

        return
    def writeFntFile(self,lines):
        fontfilename = re.sub(' ','',self.pvar['fontfilename'])
        self.freqsfile = 'out/FontReqs_'+fontfilename.lower()+'.txt'
        wf = codecs.open(self.freqsfile, 'w','utf-8')

        for line in lines:
            wf.write(line+"\n")
        wf.close()

        return
    def writeClassesFile(self,lines):
        fontfilename = re.sub(' ','',self.pvar['fontfilename'])
        self.freqsfile = 'out/FLClasses_'+fontfilename.lower()+'.flc'
        wf = codecs.open(self.freqsfile, 'w','utf-8')

        for line in lines:
            wf.write(line+"\n")
        wf.close()

        return
    def writeerrors(self):
        errorfile = open(self.errorfile,"a")

        i = 0
        for error in self.errors:
            errorfile.write(error+"\n")        
            i += 1

        if i > 0:
            print ('Errors written: '+str(i))
        return
    def writefeature(self, lookupObj):
        def formatcontext(side,array):
            string = ''
            for item in array:
                gg = self.glyphOrGroup(item)
                if (gg != -1):
                    string += ' '+side+' '+gg+' "'+item+'"\n'
                else:
                    string = '-1'
            return string.strip()
        def formatelement(array):
            string = ''
            for item in array:
                gg = self.glyphOrGroup(item)
                if (gg != -1):
                    string += ' '+gg+' "'+item+'"'
                else:
                    string = '-1'
            return string.strip()
        def formatname(feature,name,marktag):
            prefix = featurename[feature]['prefix']
            index = self.featureindexes[feature]
            self.featureindexes[feature] = index + 1
            index = str(index).zfill(3)
            lookupname = prefix + index + '_' + name + marktag
            self.features[feature].append(lookupname)
            return lookupname        
        
        #lookup
        name = lookupObj['name']
        feature = lookupObj['feature']
        lookuptype = featurename[feature]['type']
        #reversal
        reversal = ''
        if 'reversal' in lookupObj:
            if lookupObj['reversal'] == 1:
                reversal = ' REVERSAL'
        #bases
        bases = 'PROCESS_BASE'
        if 'bases' in lookupObj:
            if lookupObj['bases'] == 'SKIP':
                bases = 'SKIP_BASE'
        #marks
        marks = False
        if 'marks' in lookupObj:
            marks = lookupObj['marks']
        if marks:
            if marks == 'SKIP':
                marks = 'SKIP_MARKS'
                marktag = '_S'
            else: 
                if marks[0:1] == '*':
                    marks = ' PROCESS_MARKS MARK_GLYPH_SET "'+marks.replace('*','')+'"'
                else:
                    marks = ' PROCESS_MARKS "'+marks+'"'
                marktag = '_M'
        else :
            marks = ' PROCESS_MARKS ALL'
            marktag = '_A'
        lookupname = formatname(feature,name,marktag)
        #contexts
        contexts = ''
        if 'exceptcontexts' in lookupObj:
            contextsObj = lookupObj['exceptcontexts']
        else:
            contextsObj = []
        if len(contextsObj) > 0:
            for contextpair in contextsObj:
                left = 0
                right = 0
                if 'left' in contextpair:
                    left = formatcontext('LEFT', contextpair['left'])
                    if left == '-1':
                        print("\t"+'Left except context missing: '+name)
                if 'right' in contextpair:
                    right = formatcontext('RIGHT', contextpair['right'])
                    if right == '-1':
                        print("\t"+'Right except context missing: '+name)
                contexts += 'EXCEPT_CONTEXT'+"\n"
                if (left) or (right):
                    contexts += ' '+str(left)+str(right)+"\n"
                contexts += 'END_CONTEXT'+"\n"
        if 'contexts' in lookupObj:
            contextsObj = lookupObj['contexts']
            for contextpair in contextsObj:
                left = 0
                right = 0
                if 'left' in contextpair:
                    left = formatcontext('LEFT', contextpair['left'])
                    if left == '-1':
                        print("\t"+'Left context missing: '+name)
                if 'right' in contextpair:
                    right = formatcontext('RIGHT', contextpair['right'])
                    if right == '-1':
                        print("\t"+'Right context missing: '+name+str(contextpair['right']))
                contexts += 'IN_CONTEXT'+"\n"
                if (left) or (right):
                    contexts += ' '+str(left)+str(right)+"\n"
                contexts += 'END_CONTEXT'+"\n"

        #append to list of subpairs
        line = 'DEF_LOOKUP "'+lookupname+'" '+bases+' '+marks+' DIRECTION LTR'+reversal+"\n"
        line += contexts

        #substitutions        
        if lookuptype == 'GSUB':
            subpairs = lookupObj['details']
            substitutions = ''
            for subpair in subpairs:
                subsource = formatelement(subpair['sub'])
                if subsource == '-1':
                    print("\t"+'Subsource missing: '+name+' : '+str(subpair['sub']))
                subtarget = formatelement(subpair['target'])
                #if subtarget == '-1':
                    #print("\t"+'Subtarget missing: '+name)
                    #Generates too many tsg values as errors, but these are OK.
                substitutions += ' SUB'+" "+str(subsource)+"\n"+' WITH'+" "+str(subtarget)+"\n"+'END_SUB'+"\n"

            line += 'AS_SUBSTITUTION'+"\n"
            line += substitutions
            line += 'END_SUBSTITUTION'+"\n"

        #positionings        
        elif lookuptype == 'GPOS':
            posdetails = lookupObj['details']
            positionings = ''
            prvattach = ''
            if name[0:4] == 'dist':
                for posdetail in posdetails:
                    adjust = formatelement(posdetail['adjust'])                    
                    dx = posdetail['dx']
                    if not dx == 0:
                        dx = ' DX '+str(dx)
                    else:
                        dx = ''
                    dy = posdetail['dy']
                    if not dy == 0:
                        dy = ' DY '+str(dy)
                    else:
                        dy = ''
                    positionings += ' '+adjust+' BY POS'+dx+dy+' END_POS'
            else:
                for posdetail in posdetails:
                    if 'attach' in posdetail:
                        attach = posdetail['attach']
                    else:
                        attach = ''
                    to = formatelement(posdetail['to'])
                    atanchor = posdetail['anchor']
                    if attach:
                        if not attach == prvattach:
                            prvattach = attach
                            attach = formatelement(attach)
                            positionings += ' ATTACH'+" "+str(attach)+"\n"+' TO'
                    positionings += " "+str(to)+' AT ANCHOR "'+str(atanchor)+'"'+"\n"
                positionings += 'END_ATTACH'+"\n"

            if name[0:4] == 'dist':
                positionings = " ADJUST_SINGLE"+positionings+"\n"+'END_ADJUST'+"\n"
            line += 'AS_POSITION'+"\n"
            line += positionings
            line += 'END_POSITION'+"\n"

        return line
    def writeMarkPOS(self,lookupObj):
        line = ''
        return line
    def writelines(self,lines):
        writefile = open(self.writefile,"a")

        
        for line in lines:
            writefile.write(line)        
        return
    def writeGlyphProperties(self):
        if 'glyphproperties' in self.pvar:
            if self.pvar['glyphproperties'] == 1:
                writefile = open('out/glyph_properties.txt',"w")
                insertions = [
                    'A14','A16','A17','A17a','A18','A26','A28','A30','A40','A41','A43','A45',
                    'A50','A55','B1','C1','C2a','C2b','C9','C10','C22','C23','D3','D17','D28',
                    'D29','D32','D36','D37','D38','D39','D40','D41','D42','D43','D44','D45',
                    'D46a','D52','D53','D54','D54a','D55','D56','D58','D60','D66','E1','E3',
                    'E6','E7','E8','E8a','E9','E100','E10','E11','E13','E14','E15','E16','E17',
                    'E141','E18','E19','E20','E20a','E21','E22','E23','E27','E28','E29','E30',
                    'E31','E32','E34','E38','F4','F5','F6','F13','F16','F18','F20','F26','F29',
                    'F30','F39','F40','G1','G2','G3','G4','G5','G6','G139','G7','G7a','G7b','G8',
                    'G9','G11','G11a','G13','G14','G15','G17','G18','G20','G90','G21','G22','G23',
                    'G25','G26','G26a','G27','G28','G29','G30','G31','G32','G33','G34','G35',
                    'G36','G36a','G37','G37a','G38','G39','G41','G42','G43','G43a','G44','G45',
                    'G45a','G47','G50','G53','I1','I3','I5','I7','I8','I9','I10','I31','I11',
                    'I11a','L1','M9','M10','M72','M11','M22','M22a','M23','M26','M27','M140b',
                    'N2','N3','N11','N12','N36','N37','O1','O54','O2','O6','O13','O14','O16',
                    'O17','O18','O26','O32','O36','O38','Q1','Q2','R8','R12','R13','S1','S2',
                    'S19','S22','S28','S29','T2','T5','T6','T7a','T14','T30','T31','T32','T32a',
                    'U1','U2','U6','U13','U14','U15','U19','U21','U35','V4','V6','V7','V10','V12',
                    'V12a','V12b','V15','V22','V23','V23a','V71','V81','W4','W15','W16','X4b',
                    'Z6','Z8','Z10','Z11','Z13','J5','J7','J13','J14','J15','J16','J19'
                ]
                print('Writing glyph properties')
                i = 0
                for name in self.glyphdata:
                    if name in insertions:
                        glyphdata = self.glyphdata[name]
                        # line = str(glyphdata['hex'])+"\n"+\
                        #     "\t'"+glyphdata['name']+"' : {\n"+\
                        #     "\t\t'': {"+str(glyphdata['ehuh'])+str(glyphdata['ehuv'])+":''}\n"+\
                        #     "},\n"
                        line = glyphdata['name']+"\t"+str(glyphdata['hex'])+"\t"+str(glyphdata['ehuh'])+str(glyphdata['ehuv'])+"\n"
                        i += 1
                        writefile.write(line)
                print('Wrote '+str(i)+' glyph properties to glyph_properties.txt')    
        
        return

# L I G A T U R E S
    def GSUBligatures(self):  
        def genligatures():
            def genligatureLookups(groupedligatures):
                def genligature(srtcontrol,targets):
                    def genExceptContexts(control):
                        # Except contexts are needed to prevent ligatures distorting control precedence
                        contexts = []
                        if   control == 'vj':
                            # 1.	L = E v E
                            # 	E v E -> L ^ ([hj,corners,om]|)
                            # 	E v E -> L ^ (|[hj,corners,om])
                            contexts.append({'left':['hj'],     'right':[]})
                            contexts.append({'left':['corners'],'right':[]})
                            contexts.append({'left':['om'],     'right':[]})
                            contexts.append({'left':[],         'right':['hj']})
                            contexts.append({'left':[],         'right':['corners']})
                            contexts.append({'left':[],         'right':['om']})
                        elif control == 'hj':
                            # 2.	L = E h E
                            # 	E h E -> L ^ ([corners,om]|)	
                            # 	E h E -> L ^ (|[corners,om])
                            contexts.append({'left':['corners'],'right':[]})
                            contexts.append({'left':['om'],     'right':[]})
                            contexts.append({'left':[],         'right':['corners']})
                            contexts.append({'left':[],         'right':['om']})
                        elif control == 'ts':
                            # 3.	L = E ts E
                            # 	E te E -> L ^ ([corners,om]|) 
                            # 	E te E -> L ^ (|ts,om) 
                            contexts.append({'left':['corners'],'right':[]})
                            contexts.append({'left':['om'],     'right':[]})
                            contexts.append({'left':[],         'right':['ts']})
                            contexts.append({'left':[],         'right':['om']})
                        elif control == 'bs':
                            # 4.	L = E bs E
                            # 	E te E -> L ^ ([corners,om]|) 
                            # 	E te E -> L ^ (|ts,bs,om) 
                            contexts.append({'left':['corners'],'right':[]})
                            contexts.append({'left':['om'],     'right':[]})
                            contexts.append({'left':[],         'right':['ts']})
                            contexts.append({'left':[],         'right':['bs']})
                            contexts.append({'left':[],         'right':['om']})
                        elif control == 'te':
                            # 5.	L = E te E
                            # 	E te E -> L ^ ([corners,om]|) 
                            # 	E te E -> L ^ (|ts,bs,te,om) 
                            contexts.append({'left':['corners'],'right':[]})
                            contexts.append({'left':['om'],     'right':[]})
                            contexts.append({'left':[],         'right':['ts']})
                            contexts.append({'left':[],         'right':['bs']})
                            contexts.append({'left':[],         'right':['te']})
                            contexts.append({'left':[],         'right':['om']})
                        elif control == 'be':
                            # 6.	L = E be E
                            # 	E te E -> L ^ ([corners,om]|) 
                            # 	E te E -> L ^ (|ts,bs,te,be,om) 
                            contexts.append({'left':['corners'],'right':[]})
                            contexts.append({'left':['om'],     'right':[]})
                            contexts.append({'left':[],         'right':['corners']})
                            contexts.append({'left':[],         'right':['om']})
                        elif control == 'om':
                            # 7.	L = E om E                   
                            # 	E om E -> L ^ (om|)
                            # 	E om E -> L ^ (|om)
                            contexts.append({'left':['om'],     'right':[]})
                            contexts.append({'left':[],         'right':['om']})
                        else:
                            # control is 'multi', so rule is separate per ligature length:
                            # 7.	L = E om E                   
                            # 	E om E -> L ^ (om|)
                            # 	E om E -> L ^ (|om)
                            contexts.append({'left':['hj'],     'right':[]})
                            contexts.append({'left':['corners'],'right':[]})
                            contexts.append({'left':['om'],     'right':[]})
                            contexts.append({'left':[],         'right':['hj']})
                            contexts.append({'left':[],         'right':['corners']})
                            contexts.append({'left':[],         'right':['om']})

                        return contexts                        
                    def genSub(target):
                        subname = target[4:]
                        return subname.split('.')
                    control = srtcontrol[1:]
                    lookupObj = {'feature':'haln','name':'','marks':'ALL','contexts':[],'details':[]}
                    lookupObj['name'] = 'ligatures_'+control
                    contexts = genExceptContexts(control)
                    if len(contexts) > 0:
                        lookupObj['exceptcontexts'] = contexts
                    for target in targets:
                        sub = genSub(target)
                        details = {'sub':sub,'target':[target]}
                        lookupObj['details'].append(details)

                    return lookupObj

                lookupObjs = []
                for key in sorted(groupedligatures):
                    targets = groupedligatures[key]
                    if len(targets)>0:
                        lookupObj = genligature(key,targets)
                        lookupObjs.append(lookupObj)

                return lookupObjs

            groupedligatures = {}
            for name in self.ligatures:
                subname = name[4:] # ignore the first 4 chars which is already determined to be 'lig.'
                components = subname.split('.')
                nomissingcomponent = True

                for component in components:
                    if component not in self.glyphdata:
                        nomissingcomponent = False
                        print("\t"+component+' occurs in ligature name, but is not found as an atomic sign.')

                if nomissingcomponent:
                    if len(components) == 3:
                        # collect all ligatures with same control and group in one lookup with exceptions
                        control = components[1]
                        if control in qcontrols:
                            idx = qcontrols.index(control)
                            srtcontrol = str(idx)+control
                            if srtcontrol not in groupedligatures:
                                groupedligatures[srtcontrol] = []    

                            groupedligatures[srtcontrol].append(name)

                    if len(components) > 3:
                        # collect all and group in one lookup with all controls (^ss,se) as exceptions
                        # We have to make a new lookup for each ligature length because the ligature
                        # lookups includes an except clause.
                        srtkey = 'a'
                        if len(components)-5 <26:
                            z2a = ('z','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a')
                            srtkey = z2a[len(components)-5]
                        liglen = '0a'+srtkey
                        if liglen not in groupedligatures:
                            groupedligatures[liglen] = []    
                        groupedligatures[liglen].append(name)

            return genligatureLookups(groupedligatures)
        def genInternalLigatures():
            def genLookup(cycle):
                lookupObj = {'feature':'haln','name':'','marks':'ALL','contexts':[],'details':[]}
                lookupObj['name'] = 'ligatures_internal_'+str(cycle)
                lookupObj['exceptcontexts'] = genExceptContexts()
                for key in internalligatures:
                    sub = genSub(internalligatures[key])
                    if len(sub) == cycle:
                        target = key
                        details = {'sub':sub,'target':[target]}
                        lookupObj['details'].append(details)

                return lookupObj
            def genExceptContexts():
                contexts = []
                contexts.append({'left':['vj'],     'right':[]})
                contexts.append({'left':['hj'],     'right':[]})
                contexts.append({'left':['corners'],'right':[]})
                contexts.append({'left':['om'],     'right':[]})
                contexts.append({'left':[],         'right':['vj']})
                contexts.append({'left':[],         'right':['hj']})
                contexts.append({'left':[],         'right':['corners']})
                contexts.append({'left':[],         'right':['om']})
                return contexts 
            def genSub(sub):
                return sub.split('.')
            def loadLigatureLenghts():
                lengths = []
                for key in internalligatures:
                    val = internalligatures[key]
                    vals = val.split('.')
                    l = len(vals)
                    if l not in lengths:
                        lengths.append(l)

                return lengths
            print('Internal Ligatures')
            liglengths = loadLigatureLenghts()
            lookupObjs = []
            for l in liglengths:
                lookupObj = genLookup(l)
                lookupObjs.append(lookupObj)

            return lookupObjs

        lines = []
        if len(self.ligatures) > 0:
            lookupObjs = genligatures()
            for lookupObj in lookupObjs:
                lines.append(self.writefeature(lookupObj))

        if 'internalligatures' in self.pvar:
            if self.pvar['internalligatures'] > 0:
                lookupObjs = genInternalLigatures()
                for lookupObj in lookupObjs:
                    lines.append(self.writefeature(lookupObj))

        return lines

# H O R I Z O N T A L
    def GSUBhorizontal(self,featuretag,level):
        lines = []

        #Count columns
        lookupObjs = self.GSUBcountcols(level)
        for lookupObj in lookupObjs:
            lines.append(self.writefeature(lookupObj))

        #Sum width per group
        lookupObjs = self.GSUBsumWidth(level)
        for lookupObj in lookupObjs:
            lines.append(self.writefeature(lookupObj))

        #Inserted width per group
        if level > 0:
            lookupObjs = self.GSUBinsertedwidth(level)
            for lookupObj in lookupObjs:
                lines.append(self.writefeature(lookupObj))

        #Max width among groups
        lookupObjs = self.GSUBmaxWidth(lookupObj,level)
        for lookupObj in lookupObjs:
            lines.append(self.writefeature(lookupObj))

        #Reduce to target
        lookupObjs = self.GSUBreduceWidth(lookupObj,level)
        for lookupObj in lookupObjs:
            lines.append(self.writefeature(lookupObj))

        #Normalize groups and distribute space
        lookupObjs = self.GSUBnormalizeWidth(lookupObj,level)
        for lookupObj in lookupObjs:
            lines.append(self.writefeature(lookupObj))

        return lines
    def GSUBcountcols(self,level): #hvm-
        #split et tokens to eh and ev values 
        #insert target width maker at the start of each level column
        def converthvmarkers(level):
            #Convert et token to width and height markers
            lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'hvm-H-convert-'+str(level)
            lookupObj['contexts'] = [
                {'left':['c'+str(level)+'bA'],'right':[]},
                {'left':['c'+str(level)+'bA','tcbb'+str(level)],'right':[]},
                ]
            if level < 2:
                context = {'left':['corners'+str(level)+'b'],'right':[]}
                lookupObj['contexts'].append(context)
                context = {'left':['corners'+str(level)+'b','tcbb'+str(level+1)],'right':[]}
                lookupObj['contexts'].append(context)

            i = 0
            while i < self.pvar['hhu']:
                h = i + 1
                j = 0
                while j < self.pvar['vhu']:
                    v = j + 1
                    et = 'et'+str(h)+str(v)
                    eh = 'eh'+str(h)
                    ev = 'ev'+str(v)
                    details = {'sub':[et],'target':[eh,ev]}
                    lookupObj['details'].append(details)
                    j += 1
                i += 1
            if (level < 2):
                # Add min size block to insertion
                minh = self.pvar['insertionwidthmin'][level] # Nested insertion
                minv = self.pvar['insertionheightmin'][level]
                details = {'sub':['mt'+str(minh)+str(minv)],'target':['eh'+str(minh),'mn'+str(minh),'ev'+str(minv)]}
                lookupObj['details'].append(details)
                
            return lookupObj
        def cornerminsize(level):
            def insertionmarkers(level):
	            # A sign that contains a corner insertion should not shrink beyond the point it can
                # contain the insertion. So use mn token to block reduction past a min size.
                # This group of rules insert the mn token. Blocking takes place later.
                # Insert im0 after eh4,5,6; Insert imb after eh1,2,3
                lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
                lookupObj['name'] = 'hvm-H-insertionmarkers-'+str(level)
                i = self.pvar['chu']
                if level < 2:
                    min = self.pvar['cornerwidthmin'][level] # Corner insertion
                while i >= min:
                    details = {'sub':['eh'+str(i)],'target':['eh'+str(i),'im0']}
                    lookupObj['details'].append(details)
                    i = i - 1
                i = min - 1
                while i > 0:
                    details = {'sub':['eh'+str(i)],'target':['eh'+str(i),'imb']}
                    lookupObj['details'].append(details)
                    i = i - 1
                return lookupObj
            def insertioncontext(level):
	            # Convert im0 to mn3 (|it33) [it33 level 0, it22 level 1]
                lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
                lookupObj['name'] = 'hvm-H-nminmarker-'+str(level)
                lookupObj['marks'] = 'insertions'
                minh = self.pvar['cornerwidthmin'][level]  # Corner insertion
                minv = self.pvar['cornerheightmin'][level]
                context = 'it'+str(minh)+str(minv)
                lookupObj['contexts'].append({'left':[],'right':[context]})
                details = {'sub':['im0'],'target':['mn'+str(minh)]}
                lookupObj['details'].append(details)
                return lookupObj
            def insertioncleanup(level):
	            # Cleanup im0,imb
                lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
                lookupObj['name'] = 'hvm-H-insertioncleanup-'+str(level)
                i = self.pvar['chu']
                min = self.pvar['cornerwidthmin'][level]  # Corner insertion
                while i >= min:
                    details = {'sub':['eh'+str(i),'im0'],'target':['eh'+str(i)]}
                    lookupObj['details'].append(details)
                    i = i - 1
                i = min - 1
                while i > 0:
                    details = {'sub':['eh'+str(i),'imb'],'target':['eh'+str(i)]}
                    lookupObj['details'].append(details)
                    i = i - 1
                return lookupObj

            lookupObjs = []
            if level < 2:
                lookupObjs.append(insertionmarkers(level))
                lookupObjs.append(insertioncontext(level))
                lookupObjs.append(insertioncleanup(level))

            return lookupObjs
        def insertcountmarker(level):
            lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'hvm-H-insert-'+str(level)
            details = {'sub':['c'+str(level)+'bA'],'target':['c'+str(level)+'bA','h0']}
            lookupObj['details'].append(details)
            return lookupObj
        def swapjoinerset(level):
            #insert count markers
            lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'hvm-swap-'+str(level)
            details = {'sub':['hj'+str(level)+'A'],'target':['hj'+str(level)+'B']}
            lookupObj['details'].append(details)
            return lookupObj
        def countcolumns(level):
            def counter(level,cycle):
                lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
                lookupObj['name'] = 'hvm-H-count_'+str(cycle)
                lookupObj['marks'] = 'colCounter'
                context = []
                unitA = 'hj'+str(level)+'B'
                unitB = ['h0',unitA]
                c = 1
                while c < int(cycle):
                    detail = []
                    a = c
                    b = int(cycle) - a - 1
                    i = 0
                    while i < a:
                        detail.append(unitA)
                        i += 1
                    j = 0
                    while j < b:
                        detail.extend(unitB)
                        j += 1
                    c += 1
                    details = {'left':[],'right':detail}
                    context.append(details)
                lookupObj['contexts'] = context
                details = {'sub':['h0'],'target':['h'+str(cycle)]}
                lookupObj['details'].append(details)
                return lookupObj

            cycle = self.pvar['targetwidthmax'][level]
            lookupObjs = []
            while cycle > 0:
                lookupObjs.append(counter(level,cycle))
                cycle = cycle - 1
            return lookupObjs

        featuretag = self.setfeaturetag(level)

        lookupObjs = []
        lookupObjs.append(converthvmarkers(level))
        lookupObjs.extend(cornerminsize(level))
        lookupObjs.append(insertcountmarker(level))
        lookupObjs.append(swapjoinerset(level))
        lookupObjs.extend(countcolumns(level))
        return lookupObjs
    def GSUBsumWidth(self,level): #sum-
        # insert token glyphs at start of each row
        # insert width counting glyph to match current eh value
        # sum width glyphs between token glyphs
        # move sum total into token
        def inserttokens(level):
            rowmarker = 'r'+str(level)+'bA'
            lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'sum-H-insertCh-'+str(level)
            lookupObj['details'] = [{'sub':[rowmarker],'target':['ch0',rowmarker]}]
            i = 1
            while i <= self.pvar['hhu']:
                details = {'sub':['eh'+str(i)],'target':['ch'+str(i),'eh'+str(i)]}
                lookupObj['details'].append(details)
                i += 1
            return lookupObj
        def calculate(level):
            def counter(level,cycle):
                # This group of rules can add up to 6 items each with a max of 6
                # in three paired adding passes and one final total pass
                # 1-6, 1-6 = 2-12   [first pass] 1,2, or 3 substitutions made [1-6 values]
                # 2-12, 1-12 = 3-24 [second pass] 1 or 2 substitutions made [1-3 values]
                # 4-24, 1-12 = 5-36 [third pass]  1 substitution made [1-2 values]
                # by design, don't include glyphs > 6h in clusters, but allow ch7 and ch8 to cluster as singleton
                lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
                lookupObj['name'] = 'sum-H-counter-'+str(level)+'_'+str(cycle)
                lookupObj['marks'] = 'counters_h'
                maxh = self.pvar['chu']
                secondmax = self.pvar['scndmax']
                c = cycle
                m = maxh * cycle
                n = secondmax[cycle-1][level]
                while c <= m:
                    d = 1
                    while d <= n:
                        details = {'sub':['ch'+str(c),'ch'+str(d)],'target':['ch'+str(c + d)]}
                        lookupObj['details'].append(details)
                        d += 1
                    c += 1
                return lookupObj
            def lastcounter():
                lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
                lookupObj['name'] = 'sum-H-lastcounter-'+str(level)+'_E'
                lookupObj['marks'] = 'counters_h'
                c = 1
                max = self.pvar['maxperlevel'][level]
                while c <= max:
                    details = {'sub':['ch0','ch'+str(c)],'target':['ch'+str(c)]}
                    lookupObj['details'].append(details)
                    c += 1
                return lookupObj

            cycle = 1
            cpl = self.pvar['cyclesperlevel'][level]
            lookupObjs = []
            while cycle <= cpl:
                lookupObj = counter(level,cycle)
                lookupObjs.append(lookupObj)
                cycle += 1
            lookupObj = lastcounter()
            lookupObjs.append(lookupObj)            
            return lookupObjs

        featuretag = self.setfeaturetag(level)

        lookupObjs = []
        lookupObjs.append(inserttokens(level))
        lookupObjs.extend(calculate(level))

        return lookupObjs
    def GSUBinsertedwidth(self, level): #ins-
        # Inserted groups need to have their block width calculated without impacting
        # the width of the enclosing sign's row. For example: N35 vj G9 te X1 hj ss D2 vj D21 se
        # Inserted groups must be level 1 or level 2. So process these levels before GSUBmaxWidth
        # The resulting form is invisible to GSUBmaxWidth processing above the level of the insertion

        def insertiontokens(level):
            # Inject insertion marker after all per-row summed width tokens (ch#)
            # Ch# -> ch# im0 (insertion token)
            lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'ins-H-instokens'
            j = self.pvar['maxperlevel'][level]
            while j >= 1:
                details = {'sub':['ch'+str(j)],'target':['ch'+str(j),'im0']}
                lookupObj['details'].append(details)
                j = j - 1

            #containing cell start
            # Inject insertion blocking token after outer level cell begin
            #c0bA -> c0bA imb (insertion marker block)
            outer = level - 1
            details = {'sub':['c'+str(outer)+'bA'],'target':['c'+str(outer)+'bA','imb']}
            lookupObj['details'].append(details)

            return lookupObj
        def cornerinsertiontokens(level):
            #inserted block marker alpha
            # Inject insertion begin token insertion sizer marker
            # it33 -> it33 ima (insertion marker alpha)

            lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'ins-H-cornerinstokens'
            src = 'corners'+str(level - 1)+'b'
            details = {'sub':[src],'target':[src,'ima']}
            lookupObj['details'].append(details)

            return lookupObj
        def insertionsize(level):
            # Copy the size of the containing cell to each insertion.
            # Lookup the target size of the insertion for the current character.
            def inserttargetH():
                # ibs0B -> ibs0B sh0
                lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
                lookupObj['name'] = 'inserttarget-H'
                lookupObj['contexts'] = [{'left':[],'right':['ima']}]
                for glyph in groupdata['corners'+str(level - 1)+'b']:
                    details = {'sub':[glyph],'target':[glyph,'sh0']}
                    lookupObj['details'].append(details)
                return lookupObj
            def copytargetsizeH():
                # (sh5|) sh0 -> sh5
                def copyshapesizeH(cycle):
                    lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
                    lookupObj['name'] = 'copyshapesizeH-'+str(cycle)
                    lookupObj['marks'] = 'shapewidths'
                    context = {'left':['sh'+str(cycle)],'right':[]}
                    lookupObj['contexts'].append(context)
                    details = {'sub':['sh0'],'target':['sh'+str(cycle)]}
                    lookupObj['details'].append(details)
                    return lookupObj
                cycle = 6
                objs = []
                while cycle >= 1:
                    objs.append(copyshapesizeH(cycle))
                    cycle = cycle - 1
                return objs
            def inserttargetV():
                # ih1-5 -> ih1-5 iv0
                lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
                lookupObj['name'] = 'inserttarget-V'
                context = {'left':['corners'+str(level - 1)+'b'],'right':[]}
                lookupObj['contexts'].append(context)
                i = 6
                while i > 1:
                    details = {'sub':['sh'+str(i)],'target':['sh'+str(i),'sv0']}
                    lookupObj['details'].append(details)
                    i = i - 1
                return lookupObj
            def copytargetsizeV():
                # (o*6|) iv0 -> iv6
                def copyshapesizeV(cycle):
                    lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
                    lookupObj['name'] = 'copyshapesizeV-'+str(cycle)
                    lookupObj['marks'] = 'shapeheights'
                    context = {'left':['sv'+str(cycle)],'right':[]}
                    lookupObj['contexts'].append(context)
                    details = {'sub':['sv0'],'target':['sv'+str(cycle)]}
                    lookupObj['details'].append(details)
                    return lookupObj
                cycle = 6
                objs = []
                while cycle >= 1:
                    objs.append(copyshapesizeV(cycle))
                    cycle = cycle - 1
                return objs
            def cornersizes():
                # ibs0B sh5 sv6 -> bs56
                lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
                lookupObj['name'] = 'insertsize'
                prefix = ['ts','bs','te','be','ti','mi','bi','om']
                pad = ''
                if level == 2:
                    pad = '2'
                i = 0
                for glyph in groupdata['corners'+str(level-1)+'b']:
                    h = 6
                    while h > 1:
                        v = 6
                        while v > 1:
                            details = {'sub':[glyph,'sh'+str(h),'sv'+str(v)],'target':[prefix[i]+pad+str(h)+str(v)]}
                            lookupObj['details'].append(details)
                            v = v - 1
                        h = h - 1
                    i += 1
                return lookupObj
            def perglyphsizes():
                # rules to specify the available insertion size per glyph
                # cycle through corners and pad context for multi-corners
                # specify mark filtering set *multicorners{LEVEL} for bs,te,be
                # bs56 -> bs42 (G9|)
                def loadContexts(obj):
                    contexts = []
                    if len(obj) > 0:
                        for g in obj:
                            if g in self.glyphdata:
                                context = {'left':[g],'right':[]}
                                contexts.append(context)
                    return contexts
                def loadDetails(ic, obj):
                    def extendsizes(obj):
                        basesize = list(obj.keys())[0]
                        bh = int(str(basesize)[0:1])
                        bv = int(str(basesize)[1:2])
                        
                        defsize = obj[basesize]
                        dh = int(str(defsize)[0:1])
                        dv = int(str(defsize)[1:2])
                        hr = dh/bh
                        vr = dv/bv

                        ih = self.pvar['chu']
                        while ih > 1:
                            iv = self.pvar['vhu']
                            if bh <= ih:
                                th = dh
                            else:
                                th = math.floor(hr*ih)
                            if th == 0:
                                th = 1

                            while iv > 1:
                                if bv <= iv:
                                    tv = dv
                                else:
                                    tv = math.floor(vr*iv)
                                if tv == 0:
                                    tv = 1

                                sizekey = int(str(ih)+str(iv))
                                if sizekey not in obj:
                                    obj[sizekey] = str(th)+str(tv)

                                iv -= 1
                            ih -= 1                                
                        return obj
                    if ic == 'ad':
                        ics = ['ts','ti']
                    else:
                        ics = [ic]                    
                    details = []
                    if len(obj) > 0:
                        for key in obj:
                            if key in ics:
                                sizes = extendsizes(obj[key])
                                lv = ''
                                if level == 2:
                                    lv = '2'
                                for size in sizes:
                                    sub = key + lv + str(size)
                                    target = key + lv + str(sizes[size])
                                    block = 'block'
                                    detail = {'sub':[sub],'target':[block,target]}
                                    details.append(detail)
                    return details

                objs = []
                # per-glyph sizes
                for ic in ['ad','bs','te','be','mi','bi']:
                    inssizes = self.insertionmappings[ic]
                    pginsmap = inssizes[1]
                    lv = ''
                    if level == 2:
                        lv = '2'

                    if (len(pginsmap) > 0):
                        markset = ''
                        if ic != 'ad':
                            markset = '*insmarkset'+ic+lv
                        cycle = 1

                        for key in pginsmap:
                            mapclass = pginsmap[key]
                            details  = loadDetails(ic,mapclass[0])
                            contexts = loadContexts(mapclass[1:])
                            if len(contexts) > 0:
                                lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
                                lookupObj['name'] = 'perglyphsize_'+ic+'_'+str(cycle)
                                lookupObj['marks']    = markset
                                lookupObj['contexts'] = contexts
                                lookupObj['details']  = details
                                if len(details) > 0: 
                                    objs.append(lookupObj)
                            cycle += 1

                # default sizes
                for ic in ['ad','bs','te','be','mi','bi']:
                    def loaddefaultdetails(it):
                        details = []
                        if it == 'ad':
                            ics = ['ts','ti']
                        else:
                            ics = [it]
                        lv = ''
                        if level == 2:
                            lv = '2'

                        for it in ics:
                            h = self.pvar['chu']
                            while h >= 2:
                                v = self.pvar['vhu']
                                while v >= 2:
                                    sub = it + lv + str(h) + str(v)
                                    ht = 2
                                    vt = 2
                                    if h <= 3:
                                        ht = 1
                                    if v <= 3:
                                        vt = 1
                                    trg =  it + lv + str(ht) + str(vt)
                                    detail = {'sub':[sub],'target':[trg]}
                                    details.append(detail)
                                    v -= 1
                                h -= 1
                        return details
                    markset = ''
                    if ic != 'ad':
                        markset = '*insmarkset'+ic

                    # print(str(level) + ' : ' + str(self.pgmapdetails))
                    lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
                    lookupObj['name'] = 'definssize_'+ic
                    lookupObj['exceptcontexts'] = [{'left':['block'],'right':[]}]
                    lookupObj['details']  = loaddefaultdetails(ic)
                    objs.append(lookupObj)

                return objs
            # def defaultomsize():
                # # it00 -> it66
                # lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
                # lookupObj['name'] = 'defaultomsize'
                # shapesom = 'shapes_om'
                # if level > 1:
                #     shapesom += str(level)
                # context = {'left':[shapesom],'right':[]}
                # lookupObj['contexts'].append(context)
                # details = {'sub':['it00'],'target':['it66']}
                # lookupObj['details'].append(details)
                # return lookupObj
            def defaultinsertionsizes():
                # rules to specify the default available insertion size per insertion size
                def loaddetails():
                    details = []
                    ics = ['ts','bs','te','be','ti','mi','bi','om']
                    infix = ''
                    if level == 2:
                        infix = '2'

                    for ic in ics:
                        h = self.pvar['chu']
                        while h >= 1:
                            v = self.pvar['vhu']
                            while v >= 1:
                                src = ic + infix + str(h) + str(v)
                                copy =  'it' + infix + str(h) + str(v)
                                detail = {'sub':[src],'target':[src,copy]}
                                details.append(detail)
                                v -= 1
                            h -= 1
                    # detail = {'sub':['it00','ima'],'target':['ima']}
                    # details.append(detail)
                    return details

                # print(str(level) + ' : ' + str(self.pgmapdetails))
                lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
                lookupObj['name'] = 'copyinssize'
                lookupObj['details']  = loaddetails()
                return lookupObj
            def insertiondeepclean():
                lookupObj = {'feature':featuretag,'name':'','marks':'*insdeepclean','contexts':[],'details':[]}
                lookupObj['name'] = 'ins-deepclean-'+str(level)
                details = {'sub':['c0bA','block'],'target':['c0bA']}
                lookupObj['details'].append(details)

                return lookupObj

            lookupObjs = []
            lookupObjs.append(inserttargetH())
            lookupObjs.extend(copytargetsizeH())
            lookupObjs.append(inserttargetV())
            lookupObjs.extend(copytargetsizeV())
            lookupObjs.append(cornersizes())
            lookupObjs.extend(perglyphsizes())
            # lookupObjs.extend(insertionsize())
            # lookupObjs.append(defaultomsize())
            lookupObjs.append(defaultinsertionsizes())
            lookupObjs.append(insertiondeepclean())

            return lookupObjs
        def insertiondeltamarker(level):
            # Convert insertion marker within the cell to a delta marker
            lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'ins-H-insdeltamarker-'+str(level)
            lookupObj['marks'] = 'insertions'
            lookupObj['contexts'] = [{'left':['ima'],'right':[]}]
            details = {'sub':['im0'],'target':['dv0']}
            lookupObj['details'].append(details)

            return lookupObj
        def insertionmaxperrow(level): 
            # Calculate max width per row and inject after current total width before a delta marker
            # (it33 ima|dv0) ch# -> ch# rm

            lookupObjs = []
            max = self.pvar['maxperlevel'][level]
            lvlpfx = ''
            if level == 2:
                lvlpfx = '2'
            ith = self.pvar['chu']
            while ith >= 1:
                lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
                lookupObj['name'] = 'ins-H-rowmax-'+str(ith)+'-'+str(level)
                contexts = []
                itv = self.pvar['vhu']
                while itv >= 1:
                    ithv = 'it'+lvlpfx+str(ith)+str(itv)
                    contexts.append({'left':[ithv,'ima'],'right':['dv0']}) # regular
                    contexts.append({'left':[ithv,'ima','ub'],'right':['dv0']}) #unbalanced
                    itv -= 1
                lookupObj['contexts'] = contexts

                j = max
                while j >= 1:
                    if j > ith:
                        val = str(ith)
                    else:
                        val = str(j)
                    rm = 'rm'+val
                    details = {'sub':['ch'+str(j)],'target':['ch'+str(j),rm]}
                    lookupObj['details'].append(details)
                    j = j - 1
                lookupObjs.append(lookupObj)
                ith -= 1

            return lookupObjs
        def insertmaxcalcmarker(level):
            #insertion block start max calc marker
            lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'ins-H-insmaxcalcmarker-'+str(level)
            details = {'sub':['ima'],'target':['rc0']}
            lookupObj['details'].append(details)

            return lookupObj
        # def targetmax(level):
        #     # For levels 1 and 2, copy target width from insertion size
        #     # 
        #     lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
        #     lookupObj['name'] = 'ins-H-target-'+str(level)

        #     maxh = self.pvar['insertionwidthmax'][level]
        #     maxv = self.pvar['insertionheightmax'][level]
        #     left = 'it'+str(maxh)+str(maxv)
        #     context = {'left':[left],'right':[]}
        #     lookupObj['contexts'].append(context)
                
        #     i = self.pvar['chu']
        #     while i > maxh:
        #         details = {'sub':['rm'+str(i)],'target':['rm'+str(maxh)]}
        #         lookupObj['details'].append(details)
        #         i = i - 1

        #     return lookupObj
        def storerowmax(level):
            #copy the max block size to om value so the overstrike can be centered on the host layer
            # om66 -> om26 (| it66 rm2)
            lookupObjs = []
            i = self.pvar['targetwidthmax'][level]
            if i == 6:
                # substitution of om66 -> om66 is redundant
                i = 5
            while i >= 1:
                lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
                lookupObj['name'] = 'ins-H-storerowmax-'+str(i)+'-'+str(level)
                right = 'rm'+str(i)
                shapes = 'om'
                if level > 1:
                    shapes += str(level)
                lookupObj['contexts'] = [{'left':[],'right':['insertionsizes'+str(level),right]}]
                details = {'sub':['om66'],'target':['om'+str(i)+'6']}
                lookupObj['details'].append(details)
                i = i - 1
                lookupObjs.append(lookupObj)
            return lookupObjs
        def insshrinkclean(level):
            # insertion width reduces to block width
            # it([1-6])([1-6]) rm([1-6]) -> it(lesser of $1 | $3)$2
            lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'ins-H-insshrinkclean-'+str(level)
            prefix = 'it'
            if level == 2:
                prefix = 'it2'

            # cycle rm
            r = self.pvar['chu']
            while r >= 1:
                # cycle h
                h = self.pvar['chu']
                while h >= 1:
                    # cycle v
                    t = min(h,r)
                    v = self.pvar['vhu']
                    while v >= 1:
                        details = {'sub':[prefix+str(h)+str(v),'rm'+str(r)],'target':[prefix+str(t)+str(v)]}
                        lookupObj['details'].append(details)
                        v -= 1
                    h -= 1                
                r -= 1                

            details = {'sub':['im0'],'target':['dv0']}
            lookupObj['details'].append(details)
            details = {'sub':['imb'],'target':['rc0']}
            lookupObj['details'].append(details)

            return lookupObj

        featuretag = self.setfeaturetag(level)

        lookupObjs = []
        lookupObjs.append(insertiontokens(level))
        lookupObjs.append(cornerinsertiontokens(level))

        if level > 0:
            lookupObjs.extend(insertionsize(level))
        lookupObjs.append(insertiondeltamarker(level))
        lookupObjs.extend(insertionmaxperrow(level))
        lookupObjs.append(insertmaxcalcmarker(level))
        lookupObjs.extend(self.calculatemax(level,'ins'))
        # lookupObjs.append(targetmax(level))
        lookupObjs.extend(storerowmax(level))
        lookupObjs.append(self.insertrowmaxmarker(level,'ins'))
        lookupObjs.extend(self.copyblockmaxtorow(level,'ins'))
        lookupObjs.extend(self.swaprowwidth(level,'ins'))
        lookupObjs.append(self.deltaperrow(level,'ins'))
        lookupObjs.append(self.calculateexcess(level,'ins'))
        lookupObjs.append(insshrinkclean(level))

        return lookupObjs
    def GSUBmaxWidth(self,lookupObj,level): #max-
        # For each row in the same embedding group, get the max of the current widths
        # this should be the target width or sum if delta is positive
        # [1] Cleanup rm at start of block, Qi rm{1-6} -> Q1

        #level 0
        def overwidemax(level):
            #Signs > 6h don't cluster by design. Block width needs to be reset to 7 or 8 for these.
            lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'max-H-overwide'
            contexts = {'left':[],'right':['r0bA','c0bA','h1']}
            lookupObj['contexts'].append(contexts)

            i = self.pvar['hhu'] #Max oversize width
            c = self.pvar['chu'] #Max clustering width

            if i > c : 
                while i > c: 
                    ch = 'ch'+str(i)
                    rm = 'rm'+str(i)
                    details = {'sub':[ch],'target':[ch,rm,'dv0']}
                    lookupObj['details'].append(details)
                    i = i - 1
            else:
                return
            
            return lookupObj

        def maxperrow(level): #14 
            # Calculate max width per row and inject after current total width.
            # Also inject dv0 as placeholder per row.
            max = self.pvar['maxperlevel'][level]
            lookupObjs = []
            t = self.pvar['targetwidthmax'][level]
            tmin = t 
            while t >= tmin:
                lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
                lookupObj['name'] = 'max-H-row-'+str(t)+'-'+str(level)
                lookupObj['contexts'] = [{'left':[],'right':['r0bA']}]
                j = max
                while j >= 1:
                    if j > t:
                        val = str(t)
                    else:
                        val = str(j)
                    rm = 'rm'+val
                    details = {'sub':['ch'+str(j)],'target':['ch'+str(j),rm,'dv0']}
                    lookupObj['details'].append(details)
                    j = j - 1
                lookupObjs.append(lookupObj)
                t = t - 1

            return lookupObjs
        def blockstart(level): #15
            # Insert rc0 at start of current block Qi for L0;
            lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'max-H-blockstart-'+str(level)
            if (level > 0):
                lookupObj['contexts'] = [{'left':[],'right':['shapewidths']}]                
            if level == 0:
                blockstart = 'Qi'
                details = {'sub':[blockstart],'target':[blockstart,'rc0']}
                lookupObj['details'].append(details)

            return lookupObj
        #levels 1,2
        def deltamarkers(level):
            # Convert insertion markers to delta markers
            # Im0 -> dv0
            lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'max-H-embdeltamarker-'+str(level)
            details = {'sub':['im0'],'target':['dv0']}
            lookupObj['details'].append(details)

            #embedded cell start max calc marker
            details = {'sub':['imb'],'target':['rc0']}
            lookupObj['details'].append(details)

            return lookupObj
        def embeddedmaxperrow(level): 
            # Calculate max width per row and inject after current total width before a delta marker
            # (|dv0) ch# -> ch# rm
            max = self.pvar['maxperlevel'][level]
            lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'max-H-rowmax-'+str(level)
            lookupObj['contexts'] = [{'left':[],'right':['dv0']}]
            j = max
            t = self.pvar['insertionwidthmax'][level]
            while j >= 1:
                if j > t:
                    val = str(t)
                else:
                    val = str(j)
                rm = 'rm'+val
                details = {'sub':['ch'+str(j)],'target':['ch'+str(j),rm]}
                lookupObj['details'].append(details)
                j = j - 1

            return lookupObj
        #all levels
        #calculatemax 16-20
        def targetmax(level): #20-23
            # For level 0, let the calculated row max through
            # rm{1-6} (|sh{6}) -> no changes
            # For levels 1 and 2, force the target max size
            # 1: rm{1-6} sh{(2-5)} -> rm$1 sh$1             
            # 2: rm{1-6} sh{(2-3)} -> rm$1 sh$1 
            lookupObjs = []
            if (level > 0):
                ol = level - 1
                t = self.pvar['targetwidthmax'][level]
                tmin = self.pvar['targetwidthmin'][level]
                while t >= tmin:
                    lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
                    lookupObj['name'] = 'max-H-target-'+str(t)+'-'+str(level)
                    lookupObj['contexts'] = [{'left':['c'+str(ol)+'bA'],'right':['sh'+str(t)]}]

                    j = self.pvar['targetwidthmax'][level]
                    while j >= 1:
                        details = {'sub':['rm'+str(j)],'target':['rm'+str(t)]}
                        if (t != j):
                            lookupObj['details'].append(details)
                        j = j - 1
                    lookupObjs.append(lookupObj)
                    t = t - 1

            return lookupObjs

        # MAX only
        def blockstartcleanup(level): #31
            # Clean up the row max token (rm#) at the beginning of the containing cell (c{0-1}bA|)
            lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'max-H-blockstartcleanup-'+str(level)
            if level == 0:
                lookupObj['contexts'] = [{'left':['Qi'],'right':[]}]
                i = 1
                while i <= self.pvar['hhu']:
                    details = {'sub':['rm'+str(i)],'target':['sh'+str(i)]}
                    lookupObj['details'].append(details)
                    i += 1                
            else:
                ol = level - 1
                blockstart = 'c'+str(ol)+'bA'

                i = 1
                while i <= self.pvar['targetwidthmax'][level]:
                    details = {'sub':[blockstart,'rm'+str(i)],'target':[blockstart]}
                    lookupObj['details'].append(details)
                    i += 1                
                details = {'sub':[blockstart,'rc0'],'target':[blockstart]}
                lookupObj['details'].append(details)
                for insertion in groupdata['insertionsizes'+str(level)]:
                    details = {'sub':[insertion,'rc0'],'target':[insertion]}
                    lookupObj['details'].append(details)
            
            return lookupObj
        def unbalancedblockstartcleanup(level): 
            # Clean up the row count token (rm#) after the unbalanced token
            # Not needed at level 1
            lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'max-H-rcunbalancedcleanup-'+str(level)
            contexts = {'left':['insertionsizes'+str(level)],'right':[]}
            lookupObj['contexts'].append(contexts)
            details = {'sub':['ub','rc0'],'target':['ub']}
            lookupObj['details'].append(details)

            return lookupObj
        # Common to INS and MAX
        def swapembedded(level): #33
            # 20190125 - RULE SEEMS BLOCKED, IMMEDIATE RIGHT CONTEXT BLOCKED BY EH4
            #eh{1-4}, r(level+1)bA -> r(level+1)bA
            lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'max-H-swapembedded-'+str(level)
            innerlevel = level + 1
            right = 'r'+str(innerlevel)+'bA'
            contexts = {'left':[],'right':[right]}
            lookupObj['contexts'].append(contexts)
            i = 1
            while i <= self.pvar['targetwidthmax'][innerlevel]:
                details = {'sub':['eh'+str(i)],'target':['sh'+str(i)]}
                lookupObj['details'].append(details)
                i += 1                
            return lookupObj
        featuretag = self.setfeaturetag(level)

        lookupObjs = []
        if level == 0:
            if self.pvar['hhu'] > self.pvar['chu']:
                lookupObjs.append(overwidemax(level))
            lookupObjs.extend(maxperrow(level))
            lookupObjs.append(blockstart(level))
        else:
            lookupObjs.append(deltamarkers(level))
            lookupObjs.append(embeddedmaxperrow(level))
        lookupObjs.extend(self.calculatemax(level,'max'))
        lookupObjs.extend(targetmax(level))
        lookupObjs.append(self.insertrowmaxmarker(level,'max'))
        lookupObjs.extend(self.copyblockmaxtorow(level,'max'))
        lookupObjs.extend(self.swaprowwidth(level,'max'))
        lookupObjs.append(blockstartcleanup(level))
        if level > 0:
            lookupObjs.append(unbalancedblockstartcleanup(level))
        lookupObjs.append(self.deltaperrow(level,'max'))
        if level < 2:
            lookupObjs.append(swapembedded(level))

        return lookupObjs
    def GSUBreduceWidth(self,lookupObj,level): #red-       
        def decrementloop(level):
            # This is a three stage sequence. 1. swap current target to a separate class to ensure visibility between
            # delta and target size. 2. substitute the target token to the lower sized value and add a token. 3. Use
            # the token to signal downsizing the target size.
            #     1. SWAP
            #     Eh6 -> th6
            #     2. SHRINK
            #     [Dn{7-1}] th6 -> dd1 eh5
            #     3. DECREMENT DELTA
            #     Dn{7-1} dd1 -> dn{6-0}
            def swap(level,cycle):
                #     Eh6 -> th6
                lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
                lookupObj['name'] = 'red-H-swap'+str(cycle)+'-'+str(level)
                # Nested and corner insertions
                insertionmins = [self.pvar['cornerwidthmin'][level],self.pvar['insertionwidthmin'][level]]
                lookupObj['exceptcontexts'] = []
                if cycle in insertionmins:
                    lookupObj['exceptcontexts'].append({'left':[],'right':['mn'+str(cycle)]})
                sub = 'eh'+str(cycle)
                target = 'th'+str(cycle)
                lookupObj['details'] = [{'sub':[sub],'target':[target]}]
                return lookupObj
            def shrink(level,cycle):
                #   [Dn{36-1}] th6 -> dd1 eh5
                #   repeat enough times to shrink each column
                lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
                lookupObj['name'] = 'red-H-shrink'+str(cycle)+'-'+str(level)
                lookupObj['marks'] = '*deltas_allH'+str(level)
                sub = 'th'+str(cycle)
                target = 'eh'+str(cycle-1)
                contexts = []
                c = 0
                tmax = self.pvar['targetwidthmax'][level]
                while c < tmax:
                    detail = ['deltas']
                    d = 0
                    while d < c:                         
                        detail.append(sub)
                        d += 1
                    details = {'left':detail,'right':[]}
                    contexts.append(details)
                    c += 1
                lookupObj['contexts'] = contexts
                lookupObj['details'] = [{'sub':[sub],'target':['dda',target]}]
                return lookupObj
            def swapDD(level,cycle):
                #     dda -> dd1
                lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
                lookupObj['name'] = 'red-H-swapdd'+str(cycle)+'-'+str(level)
                sub = 'dda'
                target = 'dd1'
                lookupObj['details'] = [{'sub':[sub],'target':[target]}]
                return lookupObj
            def decrement(level,cycle):
                # Need to be able to decrement parallel cells
                # Parallel columns are applicable to decremental values with 
                # a max of 6h and min of 2h
                deltamax = self.pvar['deltamax']
                lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
                lookupObj['name'] = 'red-H-decrement'+str(cycle)+'-'+str(level)
                lookupObj['marks'] = '*deltas_allH'+str(level)
                details = []
                i = deltamax[level] # the max delta for the given level 
                while i >= 1: # iterate down the delta levels
                    # j = colspersum[level][i] # the number of possible columns
                    j = self.pvar['targetwidthmax'][level] # the number of possible columns
                    while j >= 1: # iterate down for each possible column depth 
                        subs = ['dv'+str(i)] # initial sub is the current delta value
                        k = j # append dd1 value for each column
                        while k >= 1:
                            subs.append('dd1')
                            k = k - 1
                        l = i - j
                        if l >= 0: # delta still positive or zero
                            target = 'dv'+str(i-j)
                        else: # delta becomes negative
                            target = 'dn'+str(j-i)                        
                        detail = {'sub':subs,'target':[target]}
                        details.append(detail)
                        j = j - 1
                    i = i - 1
                lookupObj['details'] = details
                return lookupObj
            
            lookupObjs = []
            series = self.pvar['redh'][level]

            for cycle in series:
                lookupObjs.append(swap(level,cycle))
                lookupObjs.append(shrink(level,cycle))
                lookupObjs.append(swapDD(level,cycle))
                lookupObjs.append(decrement(level,cycle))

            return lookupObjs
        def unswap(level):
            #     th{6-2} -> eh{6-2}
            lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'red-H-unswap-'+str(level)
            i = 6
            details = []
            while i > 1:                
                sub = 'th'+str(i)
                target = 'eh'+str(i)
                details.append({'sub':[sub],'target':[target]})
                i = i - 1
            lookupObj['details'] = details
            return lookupObj
        def cleanup(level):
            lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'red-H-cleanup-'+str(level)
            a = 'dv0'
            t = self.pvar['targetwidthmax'][level]
            details = []
            while t >= 1:
                sub = [a,'rm'+str(t)]
                target = ['rm'+str(t)]
                details.append({'sub':sub,'target':target})
                t = t - 1
            if (level < 2):
                # Get the lower of the corner and nested insertion values
                minh = min([self.pvar['insertionwidthmin'][level],self.pvar['cornerwidthmin'][level]])
                i = self.pvar['chu']
                while i >= minh:
                    details.append({'sub':['eh'+str(i),'mn'+str(self.pvar['insertionwidthmin'][level])],'target':['eh'+str(i)]})
                    if self.pvar['insertionwidthmin'][level] != self.pvar['cornerwidthmin'][level]:
                        details.append({'sub':['eh'+str(i),'mn'+str(self.pvar['cornerwidthmin'][level])],'target':['eh'+str(i)]})
                    i = i - 1
            lookupObj['details'] = details
            return lookupObj

        featuretag = self.setfeaturetag(level)

        lookupObjs = []
        lookupObjs.append(self.calculateexcess(level,'red'))
        lookupObjs.extend(decrementloop(level))
        lookupObjs.append(unswap(level))
        lookupObjs.append(cleanup(level))

        return lookupObjs
    def GSUBnormalizeWidth(self,lookupObj,level): #nrm-
        # increase the width of cells less than the max width
        #       delta  distribution
        # cols          h1  h2      h3              h4                         h5
        # trg6	dv5   	5				
        # trg5	dv4   	4	2<0>2			
        # trg4	dv3   	3	1<1>1   1<0>1<0>1		
        # trg3	dv2   	2	1<0>1	0<1>0<1>0	    0<0.67>0<0.67>0	
        # trg2	dv1   	1	0<1>0	0<0.5>0<0.5>0	0<0.33>0<0.33>0<0.33>0     0<0.25>0<0.25>0

        # [dv{1-5}] h1 eh{1-5} -> eh$1+$2 (per col), csp0 -> csp{h-1/dv}

        def swaps(level):
            #Swap dv, h, and eh for dn, hn, and en respectively
            def swaphj(level):
                lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
                lookupObj['name'] = 'nrm-H-swaphj-'+str(level)
                lookupObj['contexts'] = [{'left':['c'+str(level)+'eA'],'right':[]}]
                details = {'sub':['hj'+str(level)+'B'],'target':['cs0']}
                lookupObj['details'].append(details)
                return lookupObj
            def swap(level):
                lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
                lookupObj['name'] = 'nrm-H-swaphj-'+str(level)
                i = 1
                while i < self.pvar['targetwidthmax'][level]:
                    details = {'sub':['dv'+str(i)],'target':['dn'+str(i)]}
                    lookupObj['details'].append(details)
                    details = {'sub':['h'+str(i)],'target':['hn'+str(i)]}
                    lookupObj['details'].append(details)
                    i += 1
                j = 1
                while j <= self.pvar['targetwidthmax'][level]:
                    details = {'sub':['eh'+str(j)],'target':['en'+str(j)]}
                    lookupObj['details'].append(details)
                    j += 1
                return lookupObj

            lookupObjs = []
            lookupObjs.append(swaphj(level))
            lookupObjs.append(swap(level))
            return lookupObjs
        def insertrowboundary(level):
            #Insert a boundary marker in the deltas_cells class to prevent incrementing across rows
            # r{0-2}eB > r$1eB 
            lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'nrm-H-insertrowboundary-'+str(level)
            rowend = 'r'+str(level)+'eA'
            details = {'sub':[rowend],'target':[rowend,'enb']}
            lookupObj['details'].append(details)
            
            return lookupObj
        def insertdeltatokens(level):
            def distribute(level,columns,col,spc):
                details = {'sub':['hn'+str(columns)],'target':['hn'+str(columns),'dc'+str(col),'ds'+str(spc)]}
                lookupObj['details'].append(details)

                return lookupObj
            def distribution(delta,columns):
                obj = {'col':0,'spc':0}
                if columns >= 1:
                    obj['col'] = int(delta/columns)
                if delta%columns > 0:
                    a = delta%columns
                    b = columns - 1
                    c = a*100/b
                    if c >= 100:
                        obj['spc'] = '1p0'
                    elif c in [10,20,30,40,50,60,70,80,90]:
                        c = int(c/10)
                        obj['spc'] = '0p'+str(c)
                    elif c < 100:
                        c = int(c)
                        obj['spc'] = '0p'+str(c)
                return obj

            objs = []
            delta = 1
            while delta < self.pvar['targetwidthmax'][level]:
                columns = 1
                while columns < self.pvar['targetwidthmax'][level]:                    
                    h = delta + columns
                    if h <= self.pvar['targetwidthmax'][level]: #sum of delta + columns
                        lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
                        lookupObj['name'] = 'nrm-H-insert'+str(delta)+'-'+str(columns)+'-'+str(level)
                        lookupObj['marks'] = 'normalize'
                        contexts = {'left':['dn'+str(delta)],'right':[]}
                        lookupObj['contexts'].append(contexts)

                        obj = distribution(delta,columns)
                        col = obj['col']         
                        spc = obj['spc']
                        distribute(level,columns,col,spc)

                        objs.append(lookupObj)
                    columns += 1
                delta += 1

            return objs
        def incrementcells(level):
            #TODO: repeat this per column to ensure all columns get incremented
            # not applicable at level 2
            dc = 1
            objs = []
            while dc < self.pvar['targetwidthmax'][level]:
                lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
                lookupObj['name'] = 'nrm-H-increment-'+str(dc)+'-'+str(level)
                lookupObj['marks'] = 'deltas_cells'
                contexts = {'left':['dc'+str(dc)],'right':[]}
                lookupObj['contexts'].append(contexts)

                i = 1
                while i + dc <= self.pvar['targetwidthmax'][level]:
                    j = i + dc
                    details = {'sub':['en'+str(i)],'target':['eh'+str(j)]}
                    lookupObj['details'].append(details)
                    i += 1

                dc += 1
                if len(lookupObj['details']) > 0:
                    objs.append(lookupObj)
            return objs
        def incrementspacers(level):
            #TODO: repeat this per spacer to ensure all spacers get incremented
            # not applicable at level 2
            objs = []
            cspacers = groupdata['spacers_cols'+str(level)]
            dspacers = groupdata['spacers_deltas']
            i = 1
            while i < len(dspacers):
                csp = cspacers[i]
                dsp = dspacers[i]

                lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
                lookupObj['name'] = 'nrm-H-distribute-'+str(i)+'-'+str(level)
                lookupObj['marks'] = 'deltas_spacers'
                contexts = {'left':[dsp],'right':[]}
                lookupObj['contexts'].append(contexts)
                details = {'sub':[cspacers[0]],'target':[csp]}
                lookupObj['details'].append(details)
                i += 1
                if len(lookupObj['details']) > 0:
                    objs.append(lookupObj)
            return objs
        def unswap(level):
            lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'nrm-H-unswap-'+str(level)
            # TODO: consider how to narrow the full glyph when all rows have negative delta
            # E.g., X1 hj X1 hj X1 hj X1 resolves narrower than max width so has dn2
            i = 1
            while i < self.pvar['targetwidthmax'][level]:
                details = {'sub':['dn'+str(i)],'target':['dv'+str(i)]}
                lookupObj['details'].append(details)
                details = {'sub':['hn'+str(i)],'target':['h'+str(i)]}
                lookupObj['details'].append(details)
                i += 1
            j = 1
            while j <= self.pvar['chu']:
                details = {'sub':['en'+str(j)],'target':['eh'+str(j)]}
                lookupObj['details'].append(details)
                j += 1

            return lookupObj
        # def overwidewidth(level):
        #     #Signs > 6h don't cluster by design. Block width needs to be reset to 7 or 8 for these.
        #     lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
        #     lookupObj['name'] = 'nrm-H-overwide-'+str(level)
        #     contexts = {'left':[],'right':['r0bA']} # Include additional context if needed: 'c0bA','sh8' || 'c0bA','sh7'
        #     lookupObj['contexts'].append(contexts)

        #     i = self.pvar['hhu'] #Max oversize width
        #     while i > self.pvar['chu']: # Max clustering width
        #         sh = 'sh'+str(self.pvar['chu'])
        #         dv = 'dv'+str(i - self.pvar['chu'])
        #         th = 'sh'+str(i)
        #         details = {'sub':[sh,dv],'target':[th]}
        #         lookupObj['details'].append(details)
        #         i = i - 1
            
        #     return lookupObj
        def cleanupDNDV(level):
            lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'nrm-H-cleanupDV-'+str(level)

            i = 1
            while i <= self.pvar['targetwidthmax'][level]: # Remove leftover dv from start of block
                details = {'sub':['Qi','dv'+str(i)],'target':['Qi']}
                lookupObj['details'].append(details)
                i += 1
            
            return lookupObj
        def swapsizehforshape(level):
            # SWAP TO SH TO AVOID CONTACT IN SUBSEQUENT LAYER PROCESSING
            lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'nrm-H-swapS-'+str(level)

            #Use full width for level 0 for wide signs.
            if level == 0:
                maxeh = self.pvar['hhu']
            else:
                maxeh = self.pvar['chu']

            i = 1
            while i <= maxeh:
                details = {'sub':['eh'+str(i)],'target':['sh'+str(i)]}
                lookupObj['details'].append(details)
                i += 1

            return lookupObj
        def embeddedwidth(level):
            lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'nrm-H-embedded-'+str(level)
            if level > 0:
                outerlevel = level - 1
                left = 'c'+str(outerlevel)+'bA'
            elif level == 0:
                #TODO: Embedded width may not be correct because spacing isn't done for level 0
                left = 'Qi'
            contexts = {'left':[left],'right':[]}
            lookupObj['contexts'].append(contexts)
            if level != 0:
                context = {'left':['shapes_cornersom_'+str(level)],'right':[]}
                lookupObj['contexts'].append(context)
            i = 1
            while i <= self.pvar['chu']:
                details = {'sub':['rm'+str(i)],'target':['eh'+str(i)]}
                lookupObj['details'].append(details)
                i += 1

            return lookupObj
        def cleanupC(level):
            lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'nrm-H-cleanupC-'+str(level)

            #unused column spacers
            details = {'sub':['cs0','c'+str(level)+'bA'],'target':['c'+str(level)+'bA']}
            lookupObj['details'].append(details)

            return lookupObj
        def cleanupH(level):
            lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'nrm-H-cleanupH-'+str(level)

            i = 1
            #h values now obsolete
            while i <= self.pvar['targetwidthmax'][level]:
                details = {'sub':['c'+str(level)+'bA','h'+str(i)],'target':['c'+str(level)+'bA']}
                lookupObj['details'].append(details)
                i += 1

            return lookupObj
        def cleanupDC(level):
            lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'nrm-H-cleanupDC-'+str(level)

            i = 0
            while i < self.pvar['targetwidthmax'][level]:
                #dc values now obsolete
                details = {'sub':['c'+str(level)+'bA','dc'+str(i)],'target':['c'+str(level)+'bA']}
                lookupObj['details'].append(details)
                i += 1

            return lookupObj
        def cleanupDS(level):
            lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'nrm-H-cleanupDS-'+str(level)

            #ds values now obsolete
            dspacers = groupdata['spacers_deltas']
            i = 0
            while i < len(dspacers):
                dsp = dspacers[i]
                details = {'sub':['c'+str(level)+'bA',dsp],'target':['c'+str(level)+'bA']}
                lookupObj['details'].append(details)
                i += 1

            rowend = 'r'+str(level)+'eA'
            details = {'sub':[rowend,'enb'],'target':[rowend]}
            lookupObj['details'].append(details)

            return lookupObj
        def cleanupE(level):
            lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'sum-H-cleanupE-'+str(level)
            right = 'r'+str(level)+'bA'
            contexts = {'left':[],'right':[right]}
            lookupObj['contexts'].append(contexts)
            i = 1
            while i <= self.pvar['targetwidthmax'][level]:
                details = {'sub':['eh'+str(i)],'target':['sh'+str(i)]}
                lookupObj['details'].append(details)
                i += 1                

            return lookupObj
        def cleanupDV(level):
            lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'nrm-H-cleanupDV-'+str(level)

            i = 0
            while i < self.pvar['targetwidthmax'][level]:
                #dv values now obsolete
                details = {'sub':['dv'+str(i),'r'+str(level)+'bA'],'target':['r'+str(level)+'bA']}
                lookupObj['details'].append(details)
                i += 1

            return lookupObj
        def cleanupRM(level):
            lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'sum-H-cleanupRM-'+str(level)
            i = 1
            while i <= self.pvar['targetwidthmax'][level]:
                details = {'sub':['rm'+str(i),'r'+str(level)+'bA'],'target':['r'+str(level)+'bA']}
                lookupObj['details'].append(details)
                i += 1                
            return lookupObj

        featuretag = self.setfeaturetag(level)

        lookupObjs = []
        lookupObjs.extend(swaps(level))
        lookupObjs.append(insertrowboundary(level))
        lookupObjs.extend(insertdeltatokens(level))
        lookupObjs.extend(incrementcells(level))
        lookupObjs.extend(incrementspacers(level))
        lookupObjs.append(unswap(level))
        # if level == 0:
        #     lookupObjs.append(overwidewidth(level))
        lookupObjs.append(cleanupDNDV(level))
        lookupObjs.append(swapsizehforshape(level))
        obj = embeddedwidth(level)
        if (obj):
            lookupObjs.append(obj)
        lookupObjs.append(cleanupC(level))
        lookupObjs.append(cleanupH(level))
        lookupObjs.append(cleanupDC(level))
        lookupObjs.append(cleanupDS(level))
        lookupObjs.append(cleanupDV(level))
        if level == 0:
            lookupObjs.append(cleanupE(level))
        lookupObjs.append(cleanupRM(level))

        return lookupObjs
    def calculatemax(self,level,name): #16-19
        # Merge rm values over up to three cycles (two for level 2) to get max per block
        # Copy merged rm value to rc0: rc0 rm{1-6} -> rm$1
        def counter(level,cycle):
            # This group of rules finds the widest row from up to 6 rows each with a max of 6
            # in three paired comparison passes and one final pass to copy to row beginning
            # [first pass] 1,2, or 3 substitutions made [1-6 values]
            # [second pass] 1 or 2 substitutions made [1-3 values]
            # [third pass] 1 substitution made [1-2 values]
            lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = name+'-H-maxcalc-'+str(level)+'_'+str(cycle)
            markgroup = 'rowmaxes'
            if level == 0:
                markgroup = '*rowmaxes0'
            lookupObj['marks'] = markgroup
            c = 1
            m = self.pvar['chu']
            n = self.pvar['chu']
            while c <= m:
                d = 1
                while d <= n:
                    if c > d:
                        e = c
                    else:
                        e = d
                    details = {'sub':['rm'+str(c),'rm'+str(d)],'target':['rm'+str(e)]}
                    lookupObj['details'].append(details)
                    d += 1
                c += 1
            return lookupObj
        def lastcounter():
            lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = name+'-H-blockmax-'+str(level)+'_E'
            markgroup = 'rowmaxes'
            if level == 0:
                markgroup = '*rowmaxes0'
            lookupObj['marks'] = markgroup
            c = 1
            max = self.pvar['hhu'] # The widest row in a block
            while c <= max:
                details = {'sub':['rc0','rm'+str(c)],'target':['rm'+str(c)]}
                lookupObj['details'].append(details)
                c += 1
            return lookupObj

        featuretag = self.setfeaturetag(level)
        cycle = 1
        cpl = self.pvar['cyclesperlevel'][level] #TODO: cycle can be 2 for level 1 insertions not 3
        lookupObjs = []
        while cycle <= cpl:
            lookupObjs.append(counter(level,cycle))
            cycle += 1
        lookupObjs.append(lastcounter())            

        return lookupObjs
    def insertrowmaxmarker(self,level,name): #24
        # Insert rc0 before dv0 to receive block max width per row
        featuretag = self.setfeaturetag(level)
        lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
        lookupObj['name'] = name+'-H-rowmaxmarker-'+str(level)
        if level == 0:
            h = self.pvar['hhu']
            contexts = []
            while h > self.pvar['chu']:
                context = {'left':['rm'+str(h),'ch'+str(h)],'right':[]}
                contexts.append(context)
                h = h - 1
            if len(contexts) > 0:
                lookupObj['exceptcontexts'] = contexts
        details = {'sub':['dv0'],'target':['rc0','dv0']}
        lookupObj['details'].append(details)

        return lookupObj
    def copyblockmaxtorow(self,level,name): #25-29
        # Copy max width per block rm to each rc0
        objs = []
        i = 1
        featuretag = self.setfeaturetag(level)
        while i <= self.pvar['chu']:
            lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = name+'-H-blocktomaxrow-'+str(i)+'-'+str(level)
            markgroup = 'rowmaxes'
            if level == 0:
                markgroup = '*rowmaxes0'
            lookupObj['marks'] = markgroup
            context = {'left':['rm'+str(i)],'right':[]}
            lookupObj['contexts'].append(context)
            details = {'sub':['rc0'],'target':['dv'+str(i)]}
            lookupObj['details'].append(details)
            objs.append(lookupObj)
            i += 1

        return objs
    def swaprowwidth(self,level,name): #30
        # dv values was being used to be invisible to inserted rm values. Now we need them back as rm values
        # TODO using mark filter sets would make this unnecessary
        objs = []
        featuretag = self.setfeaturetag(level)
        lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
        lookupObj['name'] = name+'-H-swaprowwidth-'+str(level)
        if name == 'max':
            contexts = [{'left':['vj'+str(level)+'A'],'right':[]}]
            if level > 0:
                contexts.append({'left':['insertionsizes'+str(level)],'right':[]})
                contexts.append({'left':['insertionsizes'+str(level),'ub'],'right':[]})
            lookupObj['exceptcontexts'] = contexts
        i = 1
        while i <= self.pvar['chu']:
            details = {'sub':['dv'+str(i)],'target':['rm'+str(i)]}
            lookupObj['details'].append(details)
            i += 1
        objs.append(lookupObj)

        # Row width sizing needs to be skipped for overstrikes, so we have another rule to revert to rm for
        # overstrikes when the level is 1 or 2 and the rule is max.
        if level > 0:
            if name == 'max':
                lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
                lookupObj['name'] = name+'-H-swapomrowwidth-'+str(level)
                shapes = 'shapes_om'
                if level > 1:
                    shapes += str(level)
                lookupObj['contexts'].append({'left':[shapes,'insertionsizes'+str(level)],'right':[]})
                lookupObj['contexts'].append({'left':[shapes,'insertionsizes'+str(level), 'ub'],'right':[]})
                i = 1
                while i <= self.pvar['chu']:
                    details = {'sub':['dv'+str(i)],'target':['rm'+str(i)]}
                    lookupObj['details'].append(details)
                    i += 1
                objs.append(lookupObj)

        return objs
    def deltaperrow(self,level,name): #32
        # The total width of the row is less than the target width
        # 0: Target min/max (6); Min width (1); Max delta (5)
        # 1: Target min/max (2-5); Min width (1); Max delta (4)
        # 2: Target min/max (2-3); Min width (1); Max delta (2)
        # [5] Calculate dv per row: (ch{1-5[^>$2]} rm{2-6}|) dv0 -> dv$2-$1

        featuretag = self.setfeaturetag(level)
        lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
        lookupObj['name'] = name+'-H-rowdelta-'+str(level)

        #The rm value is between or within tmin/tmax
        i = 1 # target size
        while i <= self.pvar['chu']:
            target = 'rm'+str(i)
            j = 1
            while j <= self.pvar['chu']: #max width of row having delta
                width = 'ch'+str(j)
                if (j < i):
                    d = i - j
                    delta = 'dn'+str(d)
                    details = {'sub':[width,target,'dv0'],'target':[delta]}
                    lookupObj['details'].append(details)
                if (j == i): #cleans up ch and rm values
                    details = {'sub':[width,target,'dv0'],'target':['dv0']}
                    lookupObj['details'].append(details)
                j += 1
            i += 1
        if level == 0:
            hhu = self.pvar['hhu']
            chu = self.pvar['chu']
            while hhu > chu: #cleans up overwide ch values
                details = {'sub':['ch'+str(hhu),'dv0'],'target':['dv0']}
                lookupObj['details'].append(details)
                hhu = hhu - 1
        return lookupObj
    def calculateexcess(self,level,name):
        # The total width of the row is greater than the target width
        # 0: Target min/max (6); Max width (36); Max excess (30)
        # 1: Target min/max (2-5); Max width (30); Max excess (28)
        # 2: Target min/max (2-3); Max width (18); Max excess (16)
        # [5] Calculate dv per row: (ch{1-5[^>$2]} rm{2-6}|) dv0 -> dv$2-$1

        featuretag = self.setfeaturetag(level)
        lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
        lookupObj['name'] = name+'-H-rowexcess-'+str(level)

        #The rm value is between or within tmin/tmax
        tmin = self.pvar['targetwidthmin'][level] 
        tmax = self.pvar['chu']

        i = tmin # target size
        while i <= tmax:
            target = 'rm'+str(i)
            j = 1
            while j <= self.pvar['maxperlevel'][level]: #max width of row
                width = 'ch'+str(j)
                if (j > i):
                    d = j - i
                    delta = 'dv'+str(d)
                    details = {'sub':[width,target,'dv0'],'target':[delta]}
                    lookupObj['details'].append(details)
                j += 1
            i += 1
        return lookupObj

# V E R T I C A L
    def GSUBvertical(self, featuretag, level):
        lines = []

        #Count rows
        lookupObjs = self.GSUBcountrows(level)
        for lookupObj in lookupObjs:
            lines.append(self.writefeature(lookupObj))

        #Target size
        lookupObjs = self.GSUBinsertTargetHeight(level)
        for lookupObj in lookupObjs:
            lines.append(self.writefeature(lookupObj))

        #Max height per row
        lookupObjs = self.GSUBmaxHeight(level)
        for lookupObj in lookupObjs:
            lines.append(self.writefeature(lookupObj))

        #Sum height per group
        lookupObjs = self.GSUBsumHeight(level)
        for lookupObj in lookupObjs:
            lines.append(self.writefeature(lookupObj))

        #Reduce to target
        lookupObjs = self.GSUBreduceHeight(level)
        for lookupObj in lookupObjs:
            lines.append(self.writefeature(lookupObj))

        #Normalize groups and distribute space
        lookupObjs = self.GSUBnormalizeHeight(level)
        for lookupObj in lookupObjs:
            lines.append(self.writefeature(lookupObj))

        return lines
    def GSUBcountrows(self,level):
        #insert target height maker at the start of each level row
        def insertcountmarker(level):
            lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'row-V-insert-'+str(level)
            details = {'sub':['r'+str(level)+'bA'],'target':['r'+str(level)+'bA','v0']}
            lookupObj['details'].append(details)
            return lookupObj
        def swapjoinerset(level):
            #insert count markers
            lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'row-V-swap-'+str(level)
            details = {'sub':['vj'+str(level)+'A'],'target':['vj'+str(level)+'B']}
            lookupObj['details'].append(details)
            return lookupObj
        def countrows(level):
            #count rows using row joiners
            def counter(level,cycle):
                lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
                lookupObj['name'] = 'row-V-count_'+str(cycle)
                lookupObj['marks'] = 'rowCounter'
                context = []
                unitA = 'vj'+str(level)+'B'
                unitB = ['v0',unitA]
                c = 1
                while c < int(cycle):
                    detail = []
                    a = c
                    b = int(cycle) - a - 1
                    i = 0
                    while i < a:
                        detail.append(unitA)
                        i += 1
                    j = 0
                    while j < b:
                        detail.extend(unitB)
                        j += 1
                    c += 1
                    details = {'left':[],'right':detail}
                    context.append(details)
                lookupObj['contexts'] = context
                details = {'sub':['v0'],'target':['v'+str(cycle)]}
                lookupObj['details'].append(details)
                return lookupObj

            cycle = self.pvar['targetheightmax'][level]
            lookupObjs = []
            while cycle > 0:
                lookupObj = counter(level,cycle)
                lookupObjs.append(lookupObj)
                cycle = cycle - 1
            return lookupObjs

        featuretag = self.setfeaturetag(level)

        lookupObjs = []
        obj = insertcountmarker(level)
        lookupObjs.append(obj)
        obj = swapjoinerset(level)
        lookupObjs.append(obj)
        objs = countrows(level)
        lookupObjs.extend(objs)
        return lookupObjs
    def GSUBinsertTargetHeight(self,level):
        #insert a target height value glyph at start of row
        #embedded levels adjust based on col count of outer levels
        #so process in level order with col count as prerequisite

        def inserttoken(level):
            # TODO:LSEP
            if level == 0:
                ctxt = 0
            else:
                ctxt = 1
            
            objs = []
            i = self.pvar['targetheightmin'][level]
            while i <= self.pvar['vhu']:
                lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
                lookupObj['name'] = 'ith-V-insert_'+str(i)+'_'+str(level)
                if ctxt == 0:
                    lookupObj['exceptcontexts'] = [{'left':['vj0B'],'right':[]}]
                if ctxt == 1:
                    lookupObj['contexts'] = [
                        {'left':['sv'+str(i)],'right':[]},
                        {'left':['sv'+str(i),'ub'],'right':[]},
                    ]
                    # it = 'it'+str(i)+str(i) # START HERE need to include it43
                    for it in groupdata['insertionsizes'+str(level)]:
                        itv = it[-1:]
                        if int(itv) == i:
                            lookupObj['contexts'].append({'left':[it],'right':[]})
                            lookupObj['contexts'].append({'left':[it,'ub'],'right':[]})
                lookupObj['details'] = [{'sub':['r'+str(level)+'bA'],'target':['trg'+str(i),'r'+str(level)+'bA']}]
                objs.append(lookupObj)
                i += 1
            return objs

        featuretag = self.setfeaturetag(level)

        lookupObjs = []
        objs = inserttoken(level)
        lookupObjs.extend(objs)
        return lookupObjs
    def GSUBmaxHeight(self,level):
        # for each cell in the same row, get the max of the current heights
        def inserttokens(level):
            rowmarker = 'r'+str(level)+'bA'
            lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'max-V-insertC-'+str(level)
            lookupObj['details'] = [{'sub':[rowmarker],'target':['cv0',rowmarker]}]
            i = 1
            while i <= self.pvar['vhu']:
                details = {'sub':['ev'+str(i)],'target':['cv'+str(i),'ev'+str(i)]}
                lookupObj['details'].append(details)
                i += 1
            if level > 0:
                outer = level - 1 
                details = {'sub':['c'+str(outer)+'bA'],'target':['cvb','c'+str(outer)+'bA']}
                lookupObj['details'].append(details)
                if level >= 1:
                    cornerlist = groupdata['shapes_cornersom_'+str(level)]
                for corner in cornerlist:
                    details = {'sub':[corner],'target':['cvb',corner]}
                    lookupObj['details'].append(details)
            return lookupObj
        def calculate(level):
            def counter(level,cycle):
                # This group of rules finds the tallest item from up to 6 items each with a max of 6
                # in three paired comparison passes and one final copy to row beginning pass
                # [first pass] 1,2, or 3 substitutions made [1-6 values]
                # [second pass] 1 or 2 substitutions made [1-3 values]
                # [third pass] 1 substitution made [1-2 values]
                lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
                lookupObj['name'] = 'max-V-maxcalc-'+str(level)+'_'+str(cycle)
                lookupObj['marks'] = 'counters_v'
                c = 1
                m = self.pvar['vhu']
                n = self.pvar['vhu']
                while c <= m:
                    d = 1
                    while d <= n:
                        if c > d:
                            e = c
                        else:
                            e = d
                        details = {'sub':['cv'+str(c),'cv'+str(d)],'target':['cv'+str(e)]}
                        lookupObj['details'].append(details)
                        d += 1
                    c += 1
                return lookupObj
            def lastcounter():
                lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
                lookupObj['name'] = 'max-V-lastmax-'+str(level)+'_E'
                lookupObj['marks'] = 'counters_v'
                c = 1
                max = self.pvar['vhu'] # The tallest item in a row
                while c <= max:
                    details = {'sub':['cv0','cv'+str(c)],'target':['cv'+str(c)]}
                    lookupObj['details'].append(details)
                    c += 1
                return lookupObj

            cycle = 1
            cpl = self.pvar['cyclesperlevel'][level]
            lookupObjs = []
            while cycle <= cpl:
                lookupObj = counter(level,cycle)
                lookupObjs.append(lookupObj)
                cycle += 1
            lookupObj = lastcounter()
            lookupObjs.append(lookupObj)            

            return lookupObjs
        def maxperrow(level):
            #Insert row max marker for later use based on calculated row max
            lookupObjs = []
            lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'max-V-insertRM-'+str(level)
            lookupObj['contexts'] = [{'left':[],'right':[]}]
            j = self.pvar['vhu']
            while j >= 1:
                details = {'sub':['cv'+str(j)],'target':['cv'+str(j),'rm'+str(j)]}
                lookupObj['details'].append(details)
                j = j - 1
            lookupObjs.append(lookupObj)

            return lookupObjs

        featuretag = self.setfeaturetag(level)

        lookupObjs = []
        obj = inserttokens(level)
        lookupObjs.append(obj)
        objs = calculate(level)
        lookupObjs.extend(objs)
        objs = maxperrow(level)
        lookupObjs.extend(objs)

        return lookupObjs
    def GSUBsumHeight(self,level):
        # insert token glyphs at start of each row
        # sum width glyphs between token glyphs
        # move sum total into token
        def calculate(level):
            def counter(level,cycle):
                # This group of rules can add up to 6 items each with a max of 6
                # in three paired adding passes and one final total pass
                # 1-6, 1-6 = 2-12   [first pass] 1,2, or 3 substitutions made [1-6 values]
                # 2-12, 1-12 = 3-24 [second pass] 1 or 2 substitutions made [1-3 values]
                # 4-24, 1-12 = 5-36 [third pass]  1 substitution made [1-2 values]
                # by design, don't include glyphs > 6h in clusters, but allow ch7 and ch8 to cluster as singleton
                lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
                lookupObj['name'] = 'sum-V-counter-'+str(level)+'_'+str(cycle)
                lookupObj['marks'] = 'counters_v'
                maxv = self.pvar['vhu']
                secondmax = self.pvar['scndmax']
                c = cycle
                m = maxv * cycle
                n = secondmax[cycle-1][level]
                while c <= m:
                    d = 1
                    while d <= n:
                        details = {'sub':['cv'+str(c),'cv'+str(d)],'target':['cv'+str(c + d)]}
                        #print ("\t"+str(c)+' + '+str(d)+' = '+str(c+d))
                        lookupObj['details'].append(details)
                        d += 1
                    c += 1
                return lookupObj
            def lastcounter():
                lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
                lookupObj['name'] = 'sum-V-lastcounter-'+str(level)+'_E'
                lookupObj['marks'] = 'counters_v'
                c = 1
                max = self.pvar['maxperlevel'][level]
                while c <= max:
                    details = {'sub':['cv0','cv'+str(c)],'target':['cv'+str(c)]}
                    lookupObj['details'].append(details)
                    c += 1
                return lookupObj
            def countercleanup():
                lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
                lookupObj['name'] = 'sum-V-countercleanup-'+str(level)
                outer = level - 1
                details = {'sub':['cvb','c'+str(outer)+'bA'],'target':['c'+str(outer)+'bA']}
                lookupObj['details'].append(details)
                if level >= 1:
                    cornerlist = groupdata['shapes_cornersom_'+str(level)]
                    for corner in cornerlist:
                        details = {'sub':['cvb',corner],'target':[corner]}
                        lookupObj['details'].append(details)
                return lookupObj

            cycle = 1
            cpl = self.pvar['cyclesperlevel'][level]
            lookupObjs = []
            while cycle <= cpl:
                lookupObj = counter(level,cycle)
                lookupObjs.append(lookupObj)
                cycle += 1
            lookupObj = lastcounter()
            lookupObjs.append(lookupObj)            
            if level > 0:
                lookupObj = countercleanup()
                lookupObjs.append(lookupObj)            
            return lookupObjs

        featuretag = self.setfeaturetag(level)

        lookupObjs = []
        objs = calculate(level)
        lookupObjs.extend(objs)

        return lookupObjs
    def GSUBreduceHeight(self,level):       
        def insertminheighttoken(level):
            lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'red-V-mintoken-'+str(level)
            if level < 2:
                if level == 0:
                    lookupObj['marks'] = '*rowmaxes0'
                    lookupObj['contexts'] = [{'left':[],'right':['mt22']}]
                i = self.pvar['vhu']
                minv = self.pvar['insertionheightmin'][level]
                while i >= minv:
                    lookupObj['details'].append({'sub':['rm'+str(i)],'target':['rm'+str(i),'mn'+str(minv)]})
                    i = i - 1
            return lookupObj
        def calculatedelta(level):
            #Determine the delta between the sum of the max row heights and the target height.
            lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'red-V-delta-'+str(level)

            tmin = self.pvar['targetheightmin'][level]
            tmax = self.pvar['vhu']
            i = tmin
            while i <= tmax:
                target = 'trg'+str(i)
                j = 1
                vmax = i * self.pvar['vhu']
                while j <= vmax:
                    height = 'cv'+str(j)
                    d = i - j
                    if d <= 0:
                        delta = 'dv' + str(d * -1)
                    else:
                        delta = 'ds' + str(d)
                    # print (target+' - '+height+' -> '+delta)
                    details = {'sub':[target,height],'target':[delta]}
                    lookupObj['details'].append(details)
                    j += 1
                i += 1
            return lookupObj
        def decrementloop(level):
            # This is a three stage sequence.
            #   1. SWAP current target to a separate class to ensure visibility between
            #      delta and target size.
            #      Rm6 -> th6
            #   2. SHRINK the target token to the lower sized value and add a token.
            #      [Dn{7-1}] th6 -> dd1 Rm5
            #   3. Use the token to signal downsizing the target size.
            #      Dn{7-1} dd1 -> dn{6-0}
            # Reduce in the sequence 6>5,5>4,2>1,4>3,3>2,2>1
            def swap(level,cycle):
                #     rm6 -> th6
                lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
                lookupObj['name'] = 'red-V-swap-'+str(cycle)+'-'+str(level)
                minsv = [self.pvar['insertionheightmin'][level],self.pvar['cornerheightmin'][level]]
                lookupObj['exceptcontexts'] = []
                if cycle in minsv:
                    lookupObj['exceptcontexts'].append([{'left':[],'right':['mn'+str(cycle)]}])
                sub = 'rm'+str(cycle)
                target = 'th'+str(cycle)
                lookupObj['details'] = [{'sub':[sub],'target':[target]}]
                return lookupObj
            def shrink(level,cycle):
                #   [Dn{36-1}] th6 -> dd1 ev5
                #   repeat enough times to shrink each column
                lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
                lookupObj['name'] = 'red-V-shrink-'+str(cycle)+'-'+str(level)
                lookupObj['marks'] = 'deltas_all'
                sub = 'th'+str(cycle)
                target = 'rm'+str(cycle-1)
                contexts = []
                c = 0
                while c < self.pvar['vhu']:
                    detail = ['deltas']
                    d = 0
                    while d < c:                         
                        detail.append(sub)
                        d += 1
                    details = {'left':detail,'right':[]}
                    contexts.append(details)
                    c += 1
                lookupObj['contexts'] = contexts
                lookupObj['details'] = [{'sub':[sub],'target':['dda',target]}]
                return lookupObj
            def swapDD(level,cycle):
                #     dda -> dd1
                lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
                lookupObj['name'] = 'red-V-swapdd-'+str(cycle)+'-'+str(level)
                sub = 'dda'
                target = 'dd1'
                lookupObj['details'] = [{'sub':[sub],'target':[target]}]
                return lookupObj
            def decrement(level,cycle):
                # Need to be able to decrement parallel cells
                # Parallel columns are applicable to decremental values with 
                # a max of 6v and min of 2v
                deltamax = self.pvar['deltamax']
                lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
                lookupObj['name'] = 'red-V-decrement'+str(cycle)+'-'+str(level)
                lookupObj['marks'] = 'deltas_all'
                details = []
                i = deltamax[level]
                while i >= 1:
                    j = self.pvar['targetheightmax'][level] # the number of possible columns
                    while j >= 1: # iterate down for each possible row depth 
                        subs = ['dv'+str(i)] # initial sub is the current delta value
                        k = j # append dd1 value for each column
                        while k >= 1:
                            subs.append('dd1')
                            k = k - 1
                        l = i - j
                        if l >= 0: # delta still positive or zero
                            target = 'dv'+str(i-j)
                        else: # delta becomes negative
                            target = 'ds'+str(j-i)                        
                        detail = {'sub':subs,'target':[target]}
                        details.append(detail)
                        j = j - 1
                    i = i - 1
                lookupObj['details'] = details
                return lookupObj
            
            lookupObjs = []
            series = self.pvar['redv'][level]

            for cycle in series:
                obj = swap(level,cycle)
                lookupObjs.append(obj)  
                obj = shrink(level,cycle)
                lookupObjs.append(obj)
                obj = swapDD(level,cycle)
                lookupObjs.append(obj)
                obj = decrement(level,cycle)
                lookupObjs.append(obj)

            return lookupObjs
        def unswap(level):
            #     th{6-2} -> rm{6-2}
            lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'red-V-unswap-'+str(level)
            i = 6
            details = []
            while i > 1:                
                sub = 'th'+str(i)
                target = 'rm'+str(i)
                details.append({'sub':[sub],'target':[target]})
                i = i - 1
            lookupObj['details'] = details
            return lookupObj
        def cleanup(level):
            lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'red-V-cleanup-'+str(level)
            a = 'dv0'
            t = self.pvar['vhu']
            details = []
            while t >= 1:
                minv = self.pvar['insertionheightmin'][level]
                if level < 2:
                    if t >= minv:
                        sub = [a,'rm'+str(t),'mn'+str(minv)]
                        target = ['rm'+str(t)]
                        details.append({'sub':sub,'target':target})
                        sub = ['rm'+str(t),'mn'+str(minv)]
                        details.append({'sub':sub,'target':target})

                sub = [a,'rm'+str(t)]
                target = ['rm'+str(t)]
                details.append({'sub':sub,'target':target})
                t = t - 1
            lookupObj['details'] = details
            return lookupObj
        def resolvecellheights(level):
            # Swap current ev values for a common token
            # Resolve all tokens to max for current row
            def swap(level):
                lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
                lookupObj['name'] = 'red-V-rcswap-'+str(level)
                i = 1
                details = []
                while i <= self.pvar['vhu']:                
                    sub = 'ev'+str(i)
                    target = 'rc0'
                    details.append({'sub':[sub],'target':[target]})
                    i += 1
                lookupObj['details'] = details
                return lookupObj
            def resolve(level,cycle):
                lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
                lookupObj['name'] = 'red-V-resolve-'+str(cycle)+'-'+str(level)
                markgroup = 'rowmaxes'
                if level == 0:
                    markgroup = '*rowmaxes0'
                lookupObj['marks'] = markgroup
                lookupObj['contexts'] = [{'left':['rm'+str(cycle)],'right':[]}]

                sub = ['rc0']
                target = ['ev'+str(cycle)]
                details = [{'sub':sub,'target':target}]
                lookupObj['details'] = details

                return lookupObj

            lookupObjs = []
            obj = swap(level)
            lookupObjs.append(obj)
            cycle = self.pvar['vhu']
            while cycle >= 1:
                obj = resolve(level,cycle)
                lookupObjs.append(obj)
                cycle = cycle - 1

            return lookupObjs

        featuretag = self.setfeaturetag(level)

        lookupObjs = []
        if level == 0:
            obj = insertminheighttoken(level)
            lookupObjs.append(obj)
        obj = calculatedelta(level)
        lookupObjs.append(obj)
        objs = decrementloop(level)
        lookupObjs.extend(objs)
        obj = unswap(level)
        lookupObjs.append(obj)
        obj = cleanup(level)
        lookupObjs.append(obj)
        objs = resolvecellheights(level)
        lookupObjs.extend(objs)

        return lookupObjs
    def GSUBnormalizeHeight(self,level):
        # Ds({1-5}) v1 -> vp$1
        # Ds({1-4}) v2 -> vi$1
        # Ds({1-3}) v3 -> vi$1/2
        # Ds({1-2}) v4 -> vi$1/3
        # Ds({1})   v5 -> vi$1/4

        # [dv{1-5}] h1 eh{1-5} -> eh$1+$2 (per col), csp0 -> csp{h-1/dv}

        def swap(level):
            lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'nrm-V-swap-'+str(level)
            lookupObj['contexts'] = [{'left':['r'+str(level)+'eA'],'right':[]}]

            details = {'sub':['vj'+str(level)+'B'],'target':['rs0']}
            lookupObj['details'].append(details)

            return lookupObj
        def insertdeltatokens(level):
            def distribute(level,delta,rows,target):
                details = {'sub':['ds'+str(delta),'v'+str(rows)],'target':[target]}
                lookupObj['details'].append(details)

                return lookupObj
            def distribution(delta,rows):
                obj = {'target':0}
                if rows == 1:
                    obj['target'] = 'rp'+str(delta)
                else:
                    a = delta
                    b = rows - 1
                    c = a/b
                    d = str(c)[0:1]
                    e = int(str(c)[2:3])
                    if e > 0: 
                        e = int(str(c)[2:4])
                    obj['target'] = 'ds' + d + 'p' + str(e)
                return obj

            objs = []
            delta = 1
            while delta < self.pvar['targetheightmax'][level]: #6,5,3
                rows = 1
                while rows < self.pvar['targetheightmax'][level]: #6,5,3                
                    h = delta + rows
                    if h <= self.pvar['targetheightmax'][level]: #sum of delta + rows
                        lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
                        lookupObj['name'] = 'nrm-V-insert-'+str(delta)+'-'+str(rows)+'-'+str(level)
                        lookupObj['marks'] = 'verticals2'

                        obj = distribution(delta,rows)
                        target = obj['target']         
                        distribute(level,delta,rows,target)

                        objs.append(lookupObj)
                    rows += 1
                delta += 1

            return objs
        def incrementcells(level):
            def docycle(level):
                def swap(cycle,level):
                    # Swap ev{1-5} -> xv$1
                    lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
                    lookupObj['name'] = 'nrm-V-exp-swap-'+str(cycle)+'-'+str(level)
                    lookupObj['details'] = [{'sub':['ev'+str(cycle)],'target':['xv'+str(cycle)]}]

                    return lookupObj
                def cycle(swapcycle,level):
                    def contextcycle(contextcycle,cyclesum, level):
                        # Increment (rp{1-5}|) xv{1-5} -> sv$1+$2
                        lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
                        lookupObj['name'] = 'nrm-V-expand-'+str(contextcycle)+'-'+str(swapcycle)+'-'+str(level)
                        lookupObj['marks'] = '*expansion_lvl'+str(level)
                        lookupObj['contexts'] = [{'left':['rp'+str(contextcycle)],'right':[]}]
                        lookupObj['details'] = [{'sub':['xv'+str(swapcycle)],'target':['sv'+str(cyclesum)]}]

                        return lookupObj

                    objs = []
                    j = 1
                    k = j + swapcycle
                    while k <= self.pvar['vhu']: 
                        obj = contextcycle(j, k, level)
                        objs.append(obj)
                        j += 1
                        k += 1
                    
                    return objs

                docycleobjs = []
                i = 1
                while i < self.pvar['vhu']:
                    obj = swap(i,level)                    
                    docycleobjs.append(obj)
                    objs = cycle(i,level)                    
                    docycleobjs.extend(objs)
                    i += 1

                return docycleobjs
            def unswap(level):
                lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
                lookupObj['name'] = 'nrm-V-unswap-'+str(level)
                i = 1
                details = []
                while i < self.pvar['vhu']:                
                    sub = 'xv'+str(i)
                    target = 'sv'+str(i)
                    details.append({'sub':[sub],'target':[target]})
                    i += 1
                lookupObj['details'] = details
                return lookupObj

            objs = docycle(level)
            obj = unswap(level)
            objs.append(obj)

            return objs
        def incrementspacers(level):
            #Spacer expands based on spacing marker
            objs = []
            rspacers = groupdata['spacers_rows'+str(level)]
            dspacers = groupdata['spacers_deltarows']
            i = 1 #TODO: determine start value based on current level, e.g., level 2 not applicable
            while i < len(dspacers):
                rsp = rspacers[i]
                dsp = dspacers[i]

                lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
                lookupObj['name'] = 'nrm-V-distribute-'+str(i)+'-'+str(level)
                lookupObj['marks'] = 'deltas_spacers'
                contexts = {'left':[dsp],'right':[]}
                lookupObj['contexts'].append(contexts)
                details = {'sub':[rspacers[0]],'target':[rsp]}
                lookupObj['details'].append(details)
                i += 1
                if len(lookupObj['details']) > 0:
                    objs.append(lookupObj)
            return objs
        def unswap(level):
            lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'nrm-V-unswap-'+str(level)

            i = 1
            while i < self.pvar['targetheightmax'][level]:
                details = {'sub':['dn'+str(i)],'target':['dv'+str(i)]}
                lookupObj['details'].append(details)
                details = {'sub':['hn'+str(i)],'target':['v'+str(i)]}
                lookupObj['details'].append(details)
                i += 1
            j = 1
            while j <= self.pvar['vhu']:
                details = {'sub':['en'+str(j)],'target':['ev'+str(j)]}
                lookupObj['details'].append(details)
                j += 1

            return lookupObj
        def swapsizehforshape(level):
            lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'nrm-V-swapVforS-'+str(level)

            i = 1
            while i <= self.pvar['vhu']: # SWAP TO SV TO AVOID CONTACT IN SUBSEQUENT LAYER PROCESSING
                details = {'sub':['ev'+str(i)],'target':['sv'+str(i)]}
                lookupObj['details'].append(details)
                i += 1

            return lookupObj
        def embeddedwidth(level):
            lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'nrm-V-embedded-'+str(level)
            if level > 0:
                left = 'eh_all'
            elif level == 0:
                #TODO: Embedded height may not be correct because spacing isn't done for level 0
                #For horizontal text level 0 height is always 6 (targetheightmax)[0].
                left = 'Qi'
            contexts = {'left':[left],'right':[]}
            lookupObj['contexts'].append(contexts)
            i = 1
            while i <= self.pvar['vhu']:
                details = {'sub':['rm'+str(i)],'target':['ev'+str(i)]}
                lookupObj['details'].append(details)
                i += 1

            return lookupObj
        def cleanupV(level):
            lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'nrm-V-cleanupV-'+str(level)

            i = 1
            #obsolete v values
            while i <= self.pvar['targetheightmax'][level]:
                details = {'sub':['r'+str(level)+'bA','v'+str(i)],'target':['r'+str(level)+'bA']}
                lookupObj['details'].append(details)
                i += 1

            return lookupObj
        def expandHeight(level):
            # expand the row max height by remaining rp value 
            # rp{1-5} rm{1-5} -> rm$1+$2
            lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'nrm-V-expandHeight-'+str(level)

            i = 1
            while i <= self.pvar['targetheightmax'][level]:
                j = 1
                k = i + j
                while k <= self.pvar['targetheightmax'][level]:  
                    details = {'sub':['rp'+str(i),'rm'+str(j)],'target':['rm'+str(k)]}
                    lookupObj['details'].append(details)
                    j += 1
                    k = i + j
                i += 1

            return lookupObj
        def rowHeight(level):
            lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'nrm-V-rowheight-'+str(level)

            i = 1
            while i <= self.pvar['vhu']:
                details = {'sub':['rm'+str(i),'r'+str(level)+'bA'],'target':['r'+str(level)+'v'+str(i)]}
                lookupObj['details'].append(details)
                i += 1

            return lookupObj
        def cleanupRP(level):
            lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'nrm-V-cleanupRP-'+str(level)

            i = 1
            while i < self.pvar['vhu']:
                rp = 'rp'+str(i)
                details = {'sub':[rp],'target':['cleanup']}
                lookupObj['details'].append(details)
                i += 1

            return lookupObj
        def cleanupDS(level):
            lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'nrm-V-cleanupDS-'+str(level)

            #ds values now obsolete
            dspacers = groupdata['spacers_deltarows']
            i = 0
            while i < len(dspacers):
                dsp = dspacers[i]
                details = {'sub':[dsp],'target':['cleanup']}
                lookupObj['details'].append(details)
                i += 1

            return lookupObj
        def cleanupC(level):
            lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'nrm-V-cleanupC-'+str(level)

            #unused column spacers
            details = {'sub':['rs0'],'target':['cleanup']}
            lookupObj['details'].append(details)
            #leftover delta value (was delta negative)
            details = {'sub':['dv1'],'target':['cleanup']}
            lookupObj['details'].append(details)

            return lookupObj
        def removeCleanup(level):
            lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'nrm-V-remove_cleanup-'+str(level)

            i = 1
            while i <= self.pvar['vhu']:
                details = {'sub':['cleanup','r'+str(level)+'v'+str(i)],'target':['r'+str(level)+'v'+str(i)]}
                lookupObj['details'].append(details)
                i += 1

            return lookupObj
        def swapRowEnds(level):
            lookupObj = {'feature':featuretag,'name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'nrm-swaprowends-'+str(level)
            details = {'sub':['r'+str(level)+'eA'],'target':['r'+str(level)+'eB']}
            lookupObj['details'].append(details)

            return lookupObj

        featuretag = self.setfeaturetag(level)

        lookupObjs = []
        lookupObjs.append(swap(level))
        lookupObjs.extend(insertdeltatokens(level))
        lookupObjs.extend(incrementcells(level))
        lookupObjs.extend(incrementspacers(level))
        lookupObjs.append(unswap(level))
        lookupObjs.append(swapsizehforshape(level))
        obj = embeddedwidth(level)
        if (obj):
            lookupObjs.append(obj)
        lookupObjs.append(cleanupV(level))
        lookupObjs.append(expandHeight(level))
        lookupObjs.append(rowHeight(level))
        lookupObjs.append(cleanupRP(level))
        lookupObjs.append(cleanupDS(level))
        lookupObjs.append(cleanupC(level))
        lookupObjs.append(removeCleanup(level))
        lookupObjs.append(swapRowEnds(level))

        return lookupObjs

# P S T S
    def GSUBresizing(self):
        def cleanup():
            lookupObj = {'feature':'psts','name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'cleanup'
            details = {'sub':['r0eB','Qf'],'target':['r0eB']}
            lookupObj['details'].append(details)
            details = {'sub':['c0bA','rc0'],'target':['c0bA']}
            lookupObj['details'].append(details)
            details = {'sub':['c1bA','rc0'],'target':['c1bA']}
            lookupObj['details'].append(details)
            details = {'sub':['c2bA','rc0'],'target':['c2bA']}
            lookupObj['details'].append(details)

            return lookupObj
        def extensionbeginout():
            #Outer extension begin - o
            lookupObj = {'feature':'psts','name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'extensionbeginouter'
            context = {'left':[],'right':['eob']}
            lookupObj['contexts'].append(context)
            cartA = ['cb','crb','hwtb','hwttb','hwtbb']
            cartB = ['cobL','corbL','hwtosL','hwtotsL','hwtobsL']
            i = 0
            for source in cartA:
                target = cartB[i]
                details = {'sub':[source],'target':[target]}
                lookupObj['details'].append(details)
                i += 1

            return lookupObj
        def extensionbegindbl():
            #Double extension begin - d
            lookupObj = {'feature':'psts','name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'extensionbegindbl'
            context = {'left':[],'right':['edb']}
            lookupObj['contexts'].append(context)
            cartA = ['cb','crb','hwtb','hwttb','hwtbb']
            cartB = ['cdbL','cdrbL','hwtdsL','hwtdtsL','hwtdbsL']
            i = 0
            for source in cartA:
                target = cartB[i]
                details = {'sub':[source],'target':[target]}
                lookupObj['details'].append(details)
                i += 1

            return lookupObj
        def extensionbeginfortified():
            #Double extension begin - f
            lookupObj = {'feature':'psts','name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'extensionbeginfortified'
            context = {'left':[],'right':['efb']}
            lookupObj['contexts'].append(context)
            details = {'sub':['cwb'],'target':['cfbL']}
            lookupObj['details'].append(details)
            details = {'sub':['hwtwb'],'target':['hwbL']}
            lookupObj['details'].append(details)

            return lookupObj
        def extensionbegin():
            #extension begin
            lookupObj = {'feature':'psts','name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'extensionbegin'
            cartA = ['cb','crb','cwb','hwtb','hwttb','hwtbb','hwtwb']
            cartB = ['cbL','crbL','cwbL','hwtbL','hwttbL','hwtbbL','hwbL']
            i = 0
            for source in cartA:
                target = cartB[i]
                details = {'sub':[source],'target':[target]}
                lookupObj['details'].append(details)
                i += 1

            return lookupObj
        def extensionendout():
            #Outer extension end
            lookupObj = {'feature':'psts','name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'extensionendouter'
            context = {'left':['eoe'],'right':[]}
            lookupObj['contexts'].append(context)
            cartA = ['ce','cre','hwte','hwtte','hwtbe','O33a']
            cartB = ['coeL','coreL','hwtoeL','hwtoteL','hwtobeL','O33aoeL']
            i = 0
            for source in cartA:
                target = cartB[i]
                details = {'sub':[source],'target':[target]}
                lookupObj['details'].append(details)
                i += 1

            return lookupObj
        def extensionenddbl():
            #Double extension end
            lookupObj = {'feature':'psts','name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'extensionenddbl'
            context = {'left':['ede'],'right':[]}
            lookupObj['contexts'].append(context)
            cartA = ['ce','cre','hwte','hwtte','hwtbe','O33a']
            cartB = ['cdeL','cdreL','hwtdeL','hwtdteL','hwtdbeL','O33adeL']
            i = 0
            for source in cartA:
                target = cartB[i]
                details = {'sub':[source],'target':[target]}
                lookupObj['details'].append(details)
                i += 1

            return lookupObj
        def extensionendfortified():
            #Double extension end
            lookupObj = {'feature':'psts','name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'extensionendfortified'
            context = {'left':['efe'],'right':[]}
            lookupObj['contexts'].append(context)
            details = {'sub':['cwe'],'target':['cfeL']}
            lookupObj['details'].append(details)
            details = {'sub':['hwtwe'],'target':['hfeL']}
            lookupObj['details'].append(details)

            return lookupObj
        def extensionend():
            #Swap extension ends
            lookupObj = {'feature':'psts','name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'extensionend'
            cartA = ['ce','cre','cwe','hwte','hwtte','hwtbe','hwtwe','O33a']
            cartB = ['ceL', 'creL','cweL','hwteL','hwtteL','hwtbeL','hweL','O33aeL']
            i = 0
            for source in cartA:
                target = cartB[i]
                details = {'sub':[source],'target':[target]}
                lookupObj['details'].append(details)
                i += 1

            return lookupObj
        def quadratWidth():
            #Qi ch{1-8} -> QB$1
            lookupObj = {'feature':'psts','name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'quadratwidth'
            i = self.pvar['hhu']
            while i >= 1:
                details = {'sub':['Qi','sh'+str(i)],'target':['QB'+str(i)]}
                lookupObj['details'].append(details)
                i = i - 1

            return lookupObj
        def columnWidth():
            def split():
                # sh{1-8}} -> h$1 sh$8
                lookupObj = {'feature':'psts','name':'','marks':'','contexts':[],'details':[]}
                lookupObj['name'] = 'columnsplitwidth'
                i = self.pvar['hhu']
                while i >= 1:
                    details = {'sub':['sh'+str(i)],'target':['h'+str(i),'sh'+str(i)]}
                    lookupObj['details'].append(details)
                    i = i - 1
                return lookupObj
            def column():
                # c0bA h{1-8}} -> c0h$1
                lookupObj = {'feature':'psts','name':'','marks':'*horizontals','contexts':[],'details':[]}
                lookupObj['name'] = 'columnwidth'
                lmax = self.pvar['el']
                level = 0
                while level < lmax:
                    if level == 0:
                        i = self.pvar['hhu']
                    else:
                        i = self.pvar['chu']
                    while i >= 1:
                        details = {'sub':['c'+str(level)+'bA','h'+str(i)],'target':['c'+str(level)+'h'+str(i)]}
                        lookupObj['details'].append(details)
                        i = i - 1
                    level += 1
                return lookupObj

            lookupObjs = []
            lookupObjs.append(split())
            lookupObjs.append(column())

            return lookupObjs
        def mirrorquartershades():
            lookupObj = {'feature':'rtlm','name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'mirrorquartershades'
            lookupObj['details'].append({'sub':['dq12'],'target':['dq34']})
            lookupObj['details'].append({'sub':['dq14'],'target':['dq23']})
            lookupObj['details'].append({'sub':['dq23'],'target':['dq14']})
            lookupObj['details'].append({'sub':['dq34'],'target':['dq12']})
            lookupObj['details'].append({'sub':['dq123'],'target':['dq134']})
            lookupObj['details'].append({'sub':['dq124'],'target':['dq234']})
            lookupObj['details'].append({'sub':['dq134'],'target':['dq123']})
            lookupObj['details'].append({'sub':['dq234'],'target':['dq124']})

            return lookupObj
        def shadeSizes():
            #df -> df$1 (sh{1-8}|)
            #df{1-6} -> df{1-6}$1 (sv{1-6}|)
            def shadeSizeHs(cycle):
                lookupObj = {'feature':'psts','name':'','marks':'*shadegroupH','contexts':[],'details':[]}
                lookupObj['name'] = 'shadesize_H'+str(cycle)
                context = {'left':['sh'+str(cycle)],'right':[]}
                lookupObj['contexts'].append(context)
                if cycle <= self.pvar['chu']: # full shades
                    details = {'sub':['df'],'target':['df'+str(cycle)]}
                    lookupObj['details'].append(details)
                else: # full wide shades (no height variation)
                    details = {'sub':['df'],'target':['df'+str(cycle)+'6']}
                    lookupObj['details'].append(details)
                for dq in groupdata['dq_core']: # quarter shades
                    details = {'sub':[dq],'target':[dq + '_'+str(cycle)]}
                    lookupObj['details'].append(details)
                return lookupObj
            def shadeSizeVs(cycle):
                lookupObj = {'feature':'psts','name':'','marks':'*shadegroupV','contexts':[],'details':[]}
                lookupObj['name'] = 'shadesize_V'+str(cycle)
                context = {'left':['sv'+str(cycle)],'right':[]}
                lookupObj['contexts'].append(context)
                h = self.pvar['chu']
                while h >= 1:
                    details = {'sub':['df'+str(h)],'target':['df'+str(h)+str(cycle)]}
                    lookupObj['details'].append(details)
                    for dq in groupdata['dq_core']: # quarter shades
                        details = {'sub':[dq + '_'+str(h)],'target':[dq + '_'+str(h)+str(cycle)]}
                        lookupObj['details'].append(details)
                    h = h - 1
                return lookupObj

            lookupObjs = []
            h = self.pvar['hhu']
            while h >= 1:
                lookupObjs.append(shadeSizeHs(h))
                h = h - 1
            v = self.pvar['vhu']
            while v >= 1:
                lookupObjs.append(shadeSizeVs(v))
                v = v - 1

            return lookupObjs
        def shapeSize():
            #sh{1-8} sv{1-6} -> t$1$2
            lookupObj = {'feature':'psts','name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'shapesize'
            i = self.pvar['hhu']
            while i >= 1:
                j = self.pvar['vhu']
                while j >= 1:
                    details = {'sub':['sh'+str(i),'sv'+str(j)],'target':['o'+str(i)+str(j)]}
                    lookupObj['details'].append(details)
                    j = j - 1
                i = i - 1

            return lookupObj
        def unbalancedinsertions():
            def lvl2insertionsizes():
                #it{1-6}{1-6} -> it2$1$2
                lookupObj = {'feature':'psts','name':'','marks':'','contexts':[],'details':[]}
                lookupObj['name'] = 'lvl2insertionsizes'
                contexts = ['shapes_ts2','shapes_bs2','shapes_te2','shapes_be2','shapes_mi2','shapes_om2']
                for value in contexts:
                    context = {'left':[value],'right':[]}
                    lookupObj['contexts'].append(context)
                for it in groupdata['insertionsizes1']:
                    es = 'it2'+it[-2:]
                    details = {'sub':[it],'target':[es]}
                    lookupObj['details'].append(details)

                return lookupObj
            def unbalancedOm():
                #sh{1-8} sv{1-6} -> t$1$2
                lookupObj = {'feature':'psts','name':'','marks':'','contexts':[],'details':[]}
                lookupObj['name'] = 'unbalancedOm'
                for it in groupdata['insertionsizes1']:
                    es = 'es'+it[-2:]
                    details = {'sub':[it,'ub'],'target':[es]}
                    lookupObj['details'].append(details)

                return lookupObj
            def insertr1sepOm():
                #sh{1-8} sv{1-6} -> t$1$2
                lookupObj = {'feature':'psts','name':'','marks':'','contexts':[],'details':[]}
                lookupObj['name'] = 'insertgroupsep1'
                context = {'left':[],'right':['insertionsizes1']}
                lookupObj['contexts'].append(context)
                context = {'left':[],'right':['shapes_u']}
                lookupObj['contexts'].append(context)
                details = {'sub':['shapes_om'],'target':['r1sep','shapes_om']}
                lookupObj['details'].append(details)

                return lookupObj
            def insertr2sepOm():
                #sh{1-8} sv{1-6} -> t$1$2
                lookupObj = {'feature':'psts','name':'','marks':'','contexts':[],'details':[]}
                lookupObj['name'] = 'insertgroupsep2'
                context = {'left':[],'right':['insertionsizes2']}
                lookupObj['contexts'].append(context)
                context = {'left':[],'right':['shapes_u']}
                lookupObj['contexts'].append(context)
                details = {'sub':['shapes_om2'],'target':['r2sep','shapes_om2']}
                lookupObj['details'].append(details)

                return lookupObj
            def specialcaseinitialunbalanced():
                objs = []
                # o66 -> es66 (ub r0v6 c0h6|) - only horizontals needed
                cycle = self.pvar['chu']
                while cycle >= 1:
                    lookupObj = {'feature':'psts','name':'','marks':'','contexts':[],'details':[]}
                    lookupObj['name'] = 'specialcaseinitialss_'+str(cycle)
                    #TODO: r0v6 should be 6 in 'ss D2' but reduces to r0v4.
                    # lookupObj['contexts'].append({'left':['ub','r0v'+str(self.pvar['vhu']),'c0h'+str(self.pvar['chu'])],'right':[]})
                    lookupObj['contexts'].append({'left':['ub','r0v'+str(cycle),'c0h'+str(cycle)],'right':[]})
                    hv = str(cycle)+str(self.pvar['vhu'])
                    details = {'sub':['o'+hv],'target':['es'+hv]}
                    lookupObj['details'].append(details)
                    objs.append(lookupObj)
                    cycle = cycle - 1
                # ub r0v6 -> r0v6
                lookupObj = {'feature':'psts','name':'','marks':'','contexts':[],'details':[]}
                lookupObj['name'] = 'cleanupub'
                i = self.pvar['vhu']
                while i >= 1:
                    details = {'sub':['ub','r0v'+str(i)],'target':['r0v'+str(i)]}
                    lookupObj['details'].append(details)
                    i = i - 1
                objs.append(lookupObj)
                return objs

            lookupObjs = []
            lookupObjs.append(lvl2insertionsizes())
            lookupObjs.append(unbalancedOm())
            lookupObjs.append(insertr1sepOm())
            lookupObjs.append(insertr2sepOm())
            lookupObjs.extend(specialcaseinitialunbalanced())

            return lookupObjs
        def mapTargetSize():
            #sh{1-8} sv{1-6} -> t$1$2
            #exclude stems12 since o shapes are reused for insertion plates
            lookupObj = {'feature':'psts','name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'maptargetsize'
            lookupObj['exceptcontexts'] = [{'left':[],'right':['stems_12']}]
            i = self.pvar['hhu']
            while i >= 1:
                j = self.pvar['vhu']
                while j >= 1:
                    details = {'sub':['o'+str(i)+str(j)],'target':['o'+str(i)+str(j),'m0','t'+str(i)+str(j)]}
                    lookupObj['details'].append(details)
                    j = j - 1
                i = i - 1

            return lookupObj
        def unbalancedShape():
            #sh{1-6} sv{1-6} -> t$1$2
            lookupObj = {'feature':'psts','name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'unbalancedShape'
            i = self.pvar['chu']
            while i > 1: # Currently no glyph series with 'es1[6-1]'
                j = self.pvar['vhu']
                while j > 1: # If this is > 1, then we don't need glyphs for 'es[6-2]1' etc.
                    details = {'sub':['o'+str(i)+str(j),'ub'],'target':['es'+str(i)+str(j)]}
                    lookupObj['details'].append(details)
                    j = j - 1
                i = i - 1

            return lookupObj
        def swapLevelShapeKeys():
            def swapkeys(level):
                lookupObj = {'feature':'psts','name':'','marks':'*stems'+str(level)+'_shapes0','contexts':[],'details':[]}
                lookupObj['name'] = 'swapLevelShapes-'+str(level)
                i = 1
                while i <= self.pvar['chu']:
                    context = {'left':['c'+str(level)+'h'+str(i)],'right':[]}
                    lookupObj['contexts'].append(context)
                    i += 1
                levelkey = self.pvar['shapekey'][level]
                i = self.pvar['chu']
                while i >= 1:
                    j = self.pvar['vhu']
                    while j >= 1:
                        details = {'sub':['o'+str(i)+str(j)],'target':[levelkey+str(i)+str(j)]}
                        lookupObj['details'].append(details)
                        j = j - 1
                    i = i - 1

                return lookupObj
            lookupObjs = []
            level = 2
            while level > 0:
                lookupObj = swapkeys(level)
                lookupObjs.append(lookupObj)
                level = level - 1
            return lookupObjs
        def tartgetSizes():
            # Calculate best match target size
            def loadtargetsizes():
                def resolvetarget(target, tshash):
                    tshash = tshash+'00'
                    n = len(tshash)
                    h = target[1:2]
                    v = target[2:]
                    i = 0
                    while (i < n): # Loop assumes tshash is single digit pairs
                        x = int(str(tshash)[i:i+1])
                        if x > self.pvar['hhu']:
                            x = self.pvar['hhu']
                        y = int(str(tshash)[i+1:i+2])
                        if y > self.pvar['vhu']:
                            y = self.pvar['vhu']
                        if (int(h) >= x) and (int(v) >= y):
                            break
                        i = i + 2
                    et = 'et'+str(x)+str(y)
                    return et

                subpairs = []
                for t in groupdata['targets']:
                    for tshash in self.tshashes:
                        tsh = 'tsh'+tshash
                        et = resolvetarget(t,tshash)
                        subpair = {'sub':[t,tsh],'target':[et] }
                        subpairs.append(subpair)
                return subpairs
            lookupObj = {'feature':'psts','name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'targetsizes'
            lookupObj['details'] = loadtargetsizes()

            return lookupObj
        def targetglyphs():
            # Map resolved target size to sized glyph
            def loadtargetglyphs():
                subpairs = []
                for glyph in groupdata['glyphs_all']:
                    if glyph not in ['placeholder','dottedcircle']:
                        hval = self.glyphdata[glyph]['ehuh']
                        if hval > self.pvar['hhu']:
                            hval = self.pvar['hhu']
                        vval = self.glyphdata[glyph]['ehuv']
                        if vval > self.pvar['vhu']:
                            vval = self.pvar['vhu']
                        et = 'et'+str(hval)+str(vval)
                        root = self.glyphdata[glyph]['root']
                        subpair = {'sub':[et,root],'target':[glyph] }
                        subpairs.append(subpair)
                return subpairs
            lookupObj = {'feature':'psts','name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'targetglyphs'
            lookupObj['details'] = loadtargetglyphs()

            return lookupObj
        def placeholderglyphs():
            def mergeplaceholderglyphs():
                subpairs = []
                for et in groupdata['et_all']:
                    subpair = {'sub':[et],'target':['et00'] }
                    subpairs.append(subpair)
                return subpairs
            def loadplaceholderglyphs():
                subpairs = []
                for key in self.glyphdata:
                    glyph = self.glyphdata[key]
                    if glyph['group'] in ['Chr','LigR']:
                        if glyph['hex'] != '0x25cc':
                            name = glyph['name']                        
                            subpair = {'sub':['et00',name],'target':['placeholder'] }
                            subpairs.append(subpair)
                return subpairs

            lookupObjs = []
            lookupObj = {'feature':'psts','name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'mergeplaceholders'
            lookupObj['details'] = mergeplaceholderglyphs()
            lookupObjs.append(lookupObj)

            lookupObj = {'feature':'psts','name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'loadplaceholder'
            lookupObj['details'] = loadplaceholderglyphs()
            lookupObjs.append(lookupObj)

            return lookupObjs
        def tcbSizes():
            #tcbb0 -> tcbb_$1 (r0v{1-6}|)
            def tcbVs(level,cycle):
                lookupObj = {'feature':'psts','name':'','marks':'*tcms_'+str(level),'contexts':[],'details':[]}
                lookupObj['name'] = 'tcbSizes_'+str(level)+str(cycle)
                context = {'left':['r'+str(level)+'v'+str(cycle)],'right':[]}
                lookupObj['contexts'].append(context)
                details = {'sub':['tcbb'+str(level)],'target':['tcbb_'+str(cycle)]}
                lookupObj['details'].append(details)
                details = {'sub':['tcbe'+str(level)],'target':['tcbe'+str(level)+'_'+str(cycle)]}
                lookupObj['details'].append(details)
                return lookupObj

            lookupObjs = []
            l = 0
            while l < self.pvar['el']:
                v = self.pvar['vhu']
                while v >= 1:
                    lookupObjs.append(tcbVs(l,v))
                    v = v - 1
                l += 1
            return lookupObjs
        def extensionswap():
            #Swap extension ends to visible
            lookupObj = {'feature':'psts','name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'extensionendswap'
            for source in groupdata['extensioncontrolsb']:
                target = source+'V'
                details = {'sub':[source],'target':[target]}
                lookupObj['details'].append(details)
            for source in groupdata['extensioncontrolse']:
                target = source+'V'
                details = {'sub':[source],'target':[target]}
                lookupObj['details'].append(details)

            return lookupObj
        def extensionsout():
            lookupObj = {'feature':'psts','name':'','marks':'SKIP','contexts':[],'details':[]}
            lookupObj['name'] = 'extensionsouter'
            lefts = ['eobV','edeV','cdeL','cdreL','hwtdeL','hwtdteL','hwtdbeL','O33adeL','cfeL','hfeL','quadratOuters']
            for left in lefts:
                context = {'left': [left], 'right':[]}
                lookupObj['contexts'].append(context)
            i = self.pvar['hhu']
            while i >= 1:
                details = {'sub':['QB'+str(i)],'target':['QO'+str(i)]}
                lookupObj['details'].append(details)
                i = i - 1

            return lookupObj
        def extensionsdbl():
            lookupObj = {'feature':'psts','name':'','marks':'SKIP','contexts':[],'details':[]}
            lookupObj['name'] = 'extensionsdbl'
            lefts = ['edbV','quadratDoubles']
            for left in lefts:
                context = {'left': [left], 'right':[]}
                lookupObj['contexts'].append(context)
            i = self.pvar['hhu']
            while i >= 1:
                details = {'sub':['QB'+str(i)],'target':['QD'+str(i)]}
                lookupObj['details'].append(details)
                i = i - 1

            return lookupObj
        def extensionsfortified():
            lookupObj = {'feature':'psts','name':'','marks':'SKIP','contexts':[],'details':[]}
            lookupObj['name'] = 'extensionsfortified'
            lefts = ['efbV','quadratFortifieds']
            for left in lefts:
                context = {'left': [left], 'right':[]}
                lookupObj['contexts'].append(context)
            i = self.pvar['hhu']
            while i >= 1:
                details = {'sub':['QB'+str(i)],'target':['QF'+str(i)]}
                lookupObj['details'].append(details)
                i = i - 1

            return lookupObj
        def extensionssingle():
            lookupObj = {'feature':'psts','name':'','marks':'SKIP','contexts':[],'details':[]}
            lookupObj['name'] = 'extensionsingles'
            lookupObj['exceptcontexts'] = [{'left': ['eseV'], 'right':[]}]
            lefts = ['esbV','quadratSingles']
            for left in lefts:
                context = {'left': [left], 'right':[]}
                lookupObj['contexts'].append(context)
            i = self.pvar['hhu']
            while i >= 1:
                details = {'sub':['QB'+str(i)],'target':['QC'+str(i)]}
                lookupObj['details'].append(details)
                i = i - 1

            return lookupObj
        def extensionswalls():
            lookupObj = {'feature':'psts','name':'','marks':'SKIP','contexts':[],'details':[]}
            lookupObj['name'] = 'walls'
            lookupObj['exceptcontexts'] = [{'left': ['eweV'], 'right':[]}]
            lefts = ['ewbV','quadratWalls']
            for left in lefts:
                context = {'left': [left], 'right':[]}
                lookupObj['contexts'].append(context)
            i = self.pvar['hhu']
            while i >= 1:
                details = {'sub':['QB'+str(i)],'target':['QW'+str(i)]}
                lookupObj['details'].append(details)
                i = i - 1

            return lookupObj
        def extensionbgncleanup():
            #Remove extension begin controls by context
            lookupObj = {'feature':'psts','name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'extensionbgncleanup'
            details = {'sub':['eobV','edbV','quadratDoubles'],'target':['quadratDoubles']}
            lookupObj['details'].append(details)
            details = {'sub':['eobV','efbV','quadratFortifieds'],'target':['quadratFortifieds']}
            lookupObj['details'].append(details)
            details = {'sub':['esbV','quadratSingles'],'target':['quadratSingles']}
            lookupObj['details'].append(details)
            details = {'sub':['eobV','quadratOuters'],'target':['quadratOuters']}
            lookupObj['details'].append(details)
            details = {'sub':['edbV','quadratDoubles'],'target':['quadratDoubles']}
            lookupObj['details'].append(details)
            details = {'sub':['ewbV','quadratWalls'],'target':['quadratWalls']}
            lookupObj['details'].append(details)
            details = {'sub':['efbV','quadratFortifieds'],'target':['quadratFortifieds']}
            lookupObj['details'].append(details)
            details = {'sub':['eobV','cdbL'],'target':['cdbL']}
            lookupObj['details'].append(details)
            details = {'sub':['eobV','cfbL'],'target':['cfbL']}
            lookupObj['details'].append(details)

            #Normalize unused extension controls
            details = {'sub':['eobV'],'target':['esbV']}
            lookupObj['details'].append(details)
            details = {'sub':['edbV'],'target':['esbV']}
            lookupObj['details'].append(details)
            details = {'sub':['efbV'],'target':['esbV']}
            lookupObj['details'].append(details)
            return lookupObj
        def extensionendcleanup():
            #Remove extension end controls by context
            #Filtered so shaded extensions don't block the cleanup
            lookupObj = {'feature':'psts','name':'','marks':'*extensionscleanup','contexts':[],'details':[]}
            lookupObj['name'] = 'extensionendcleanup'
            details = {'sub':['r0eB','extensioncontrolse'],'target':['r0eB']}
            lookupObj['details'].append(details)

            return lookupObj
        def unusedcontrols():
            lookupObj = {'feature':'psts','name':'','marks':'','contexts':[],'details':[]}
            lookupObj['name'] = 'unusedcontrols'
            lookupObj['details'].append({'sub':['vj0B'],'target':['vj']})
            lookupObj['details'].append({'sub':['hj0B'],'target':['hj']})
            lookupObj['details'].append({'sub':['ti0A'],'target':['tiV']})
            lookupObj['details'].append({'sub':['mi0A'],'target':['miV']})
            lookupObj['details'].append({'sub':['bi0A'],'target':['biV']})
            # lookupObj['details'].append({'sub':['ss','ss'],'target':['ss.ssV']})
            lookupObj['details'].append({'sub':['ss'],'target':['ssV']})
            # lookupObj['details'].append({'sub':['ibs0B','sh0','it00','rc0'],'target':['bs']})
            # lookupObj['details'].append({'sub':['ite0B','sh0','it00','rc0'],'target':['te']})
            # lookupObj['details'].append({'sub':['ibe0B','sh0','it00','rc0'],'target':['be']})
            # lookupObj['details'].append({'sub':['om0B' ,'sh0','it00','rc0'],'target':['om']})

            return lookupObj

        lines = []
        lines.extend(self.writefeature(cleanup()))

        if self.pvar['extensions']:
            lines.extend(self.writefeature(extensionbeginout()))
            lines.extend(self.writefeature(extensionbegindbl()))
            lines.extend(self.writefeature(extensionbeginfortified()))
            lines.extend(self.writefeature(extensionbegin()))
            lines.extend(self.writefeature(extensionendout()))
            lines.extend(self.writefeature(extensionenddbl()))
            lines.extend(self.writefeature(extensionendfortified()))
            lines.extend(self.writefeature(extensionend()))
        lines.extend(self.writefeature(quadratWidth()))
        lookupObjs = columnWidth()
        for lookupObj in lookupObjs:
            lines.extend(self.writefeature(lookupObj))
        lines.extend(self.writefeature(mirrorquartershades()))
        lookupObjs = shadeSizes()
        for lookupObj in lookupObjs:
            lines.extend(self.writefeature(lookupObj))
        lines.extend(self.writefeature(shapeSize()))
        lines.extend(self.writefeature(mapTargetSize()))
        lines.extend(self.writefeature(unbalancedShape()))
        lookupObjs = swapLevelShapeKeys()
        for lookupObj in lookupObjs:
            lines.extend(self.writefeature(lookupObj))
        lookupObjs = unbalancedinsertions()
        for lookupObj in lookupObjs:
            lines.extend(self.writefeature(lookupObj))
        lines.extend(self.writefeature(tartgetSizes()))
        lines.extend(self.writefeature(targetglyphs()))
        lookupObjs = placeholderglyphs()
        for lookupObj in lookupObjs:
            lines.append(self.writefeature(lookupObj))
        if self.pvar['tcbs']:
            lookupObjs = tcbSizes()
            for lookupObj in lookupObjs:
                lines.append(self.writefeature(lookupObj))
        if self.pvar['extensions']:
            lines.extend(self.writefeature(extensionendcleanup()))
            lines.extend(self.writefeature(extensionswap()))
            lines.extend(self.writefeature(extensionsout()))
            lines.extend(self.writefeature(extensionsdbl()))
            lines.extend(self.writefeature(extensionsfortified()))
            lines.extend(self.writefeature(extensionssingle()))
            lines.extend(self.writefeature(extensionswalls()))
            lines.extend(self.writefeature(extensionbgncleanup()))
        lines.extend(self.writefeature(unusedcontrols()))

        return lines

# S S 0 1
    def GSUBbaseline(self):
        def swapglyphanchor():
            lookupObj = {'feature':'ss01','name':'','marks':'*ss01baselines','contexts':[],'details':[]}
            lookupObj['name'] = 'swapglyphanchor'
            lookupObj['exceptcontexts'] = [
                {'left':['m0'],'right':[]},
                {'left':[],'right':['m0']},
            ]
            details = {'sub':['m0'],'target':['b0']}
            lookupObj['details'].append(details)

            return lookupObj

        lines = []
        if self.pvar['baseline']:
            lookupObj = swapglyphanchor()
            lines.extend(self.writefeature(lookupObj))            
        return lines

# R T L M
    def GSUBmirror(self):
        def swaprtlstems():
            lookupObj = {'feature':'rtlm','name':'','marks':'ALL','contexts':[],'details':[]}
            lookupObj['name'] = 'swaprtlstems'
            details = {'sub':['stems0-v'],'target':['stems0-vR']}
            lookupObj['details'].append(details)
            details = {'sub':['stems0-h'],'target':['stems0-hR']}
            lookupObj['details'].append(details)
            details = {'sub':['stems1-v'],'target':['stems1-vR']}
            lookupObj['details'].append(details)
            details = {'sub':['stems1-h'],'target':['stems1-hR']}
            lookupObj['details'].append(details)
            details = {'sub':['stems2-v'],'target':['stems2-vR']}
            lookupObj['details'].append(details)
            details = {'sub':['stems2-h'],'target':['stems2-hR']}
            lookupObj['details'].append(details)

            return lookupObj
        def swaprtlextensions():
            lookupObj = {'feature':'rtlm','name':'','marks':'ALL','contexts':[],'details':[]}
            lookupObj['name'] = 'swaprtlextensions'

            for ceL in groupdata['extensionendsL']:
                index = groupdata['extensionendsL'].index(ceL)
                ceR = groupdata['extensionendsR'][index]
                details = {'sub':[ceL],'target':[ceR]}
                lookupObj['details'].append(details)

            return lookupObj
        def swaprtlglyphs():
            def loadmirrorpairs():
                subpairs = []
                # internal pairs
                for key in internalmirrors:
                    sub = key
                    target = internalmirrors[key]
                    if sub in groupdata['glyphs_all'] and target in groupdata['glyphs_all']:
                        subpair = {'sub':[sub],'target':[target] }
                        subpairs.append(subpair)
                    else:
                        self.errors.append('Missing mirror glyph '+target+' for base '+sub)
                # dynamic pairs
                for mirrorglyph in groupdata['mirror_all']:
                    baseglyph = mirrorglyph[0:-1] 
                    if baseglyph in groupdata['glyphs_all']:
                        subpair = {'sub':[baseglyph],'target':[mirrorglyph] }
                        subpairs.append(subpair)
                    elif baseglyph in self.ligatures_all:
                        subpair = {'sub':[baseglyph],'target':[mirrorglyph] }
                        subpairs.append(subpair)
                return subpairs

            lookupObj = {'feature':'rtlm','name':'','marks':'ALL','contexts':[],'details':[]}
            lookupObj['name'] = 'swaprtlsigns'
            lookupObj['details'] = loadmirrorpairs()

            return lookupObj
        def controlledMirrorL(): # P S T S
            def loadmirrorpairs():
                subpairs = []
                # internal pairs
                for key in internalmirrors:
                    sub = key
                    target = internalmirrors[key]
                    if sub in groupdata['glyphs_all']:
                        if target in groupdata['glyphs_all']:
                            subpair = {'sub':[sub,'mr'],'target':[target] }
                            subpairs.append(subpair)
                # dynamic mirror pairs
                for mirrorglyph in groupdata['mirror_all']:
                    baseglyph = mirrorglyph[0:-1] 
                    if baseglyph in groupdata['glyphs_all']:
                        subpair = {'sub':[baseglyph,'mr'],'target':[mirrorglyph] }
                        subpairs.append(subpair)
                    elif baseglyph in self.ligatures_all:
                        subpair = {'sub':[baseglyph,'mr'],'target':[mirrorglyph] }
                        subpairs.append(subpair)
                return subpairs

            lookupObj = {'feature':'psts','name':'','marks':'ALL','contexts':[],'details':[]}
            lookupObj['name'] = 'cntrlmirrorglyphsL'
            lookupObj['details'] = loadmirrorpairs()

            return lookupObj
        def controlledMirrorR(): # P S T S
            def loadmirrorpairs():
                subpairs = []
                # dynamic mirror pairs
                for mirrorglyph in groupdata['mirror_all']:
                    baseglyph = mirrorglyph[0:-1] 
                    if baseglyph in groupdata['glyphs_all']:
                        subpair = {'sub':[mirrorglyph,'mr'],'target':[baseglyph] }
                        subpairs.append(subpair)
                    # elif baseglyph in self.ligatures_all:
                    #     subpair = {'sub':[mirrorglyph,'mr'],'target':[baseglyph] }
                    #     subpairs.append(subpair)
                return subpairs

            lookupObj = {'feature':'psts','name':'','marks':'ALL','contexts':[],'details':[]}
            lookupObj['name'] = 'cntrlmirrorglyphsR'
            subpairs = loadmirrorpairs()
            if len(subpairs) > 0:
                lookupObj['details'] = loadmirrorpairs()
                return lookupObj
            else:
                print('Skipped cntrlmirrorglyphsR, no pairs')
            pass

        lines = []
        if self.pvar['mirror']:
            lookupObj = swaprtlstems()
            lines.extend(self.writefeature(lookupObj))            
            lookupObj = swaprtlextensions()
            lines.extend(self.writefeature(lookupObj))
            lookupObj = swaprtlglyphs()
            lines.extend(self.writefeature(lookupObj))
            lookupObj = controlledMirrorL()
            lines.extend(self.writefeature(lookupObj))
            lookupObj = controlledMirrorR()
            lines.extend(self.writefeature(lookupObj))

        return lines

# V R T 2
    def GSUBvert(self):
        def swaprtlextensions():
            lookupObj = {'feature':'vrt2','name':'','marks':'ALL','contexts':[],'details':[]}
            lookupObj['name'] = 'swapvertextensions'

            for ceL in groupdata['extensionendsL']:
                index = groupdata['extensionendsL'].index(ceL)
                ceV = groupdata['extensionendsV'][index]
                details = {'sub':[ceL],'target':[ceV]}
                lookupObj['details'].append(details)

            for ceR in groupdata['extensionendsR']:
                index = groupdata['extensionendsR'].index(ceR)
                ceV = groupdata['extensionendsV'][index]
                details = {'sub':[ceR],'target':[ceV]}
                lookupObj['details'].append(details)

            for qcH in groupdata['quadratSingles']:
                index = groupdata['quadratSingles'].index(qcH)
                qcV = groupdata['quadratSinglesV'][index]
                details = {'sub':[qcH],'target':[qcV]}
                lookupObj['details'].append(details)

            for qcH in groupdata['quadratWalls']:
                index = groupdata['quadratWalls'].index(qcH)
                qcV = groupdata['quadratWallsV'][index]
                details = {'sub':[qcH],'target':[qcV]}
                lookupObj['details'].append(details)
    
            for qcH in groupdata['quadratOuters']:
                index = groupdata['quadratOuters'].index(qcH)
                qcV = groupdata['quadratOutersV'][index]
                details = {'sub':[qcH],'target':[qcV]}
                lookupObj['details'].append(details)
    
            for qcH in groupdata['quadratDoubles']:
                index = groupdata['quadratDoubles'].index(qcH)
                qcV = groupdata['quadratDoublesV'][index]
                details = {'sub':[qcH],'target':[qcV]}
                lookupObj['details'].append(details)
    
            for qcH in groupdata['quadratFortifieds']:
                index = groupdata['quadratFortifieds'].index(qcH)
                qcV = groupdata['quadratFortifiedsV'][index]
                details = {'sub':[qcH],'target':[qcV]}
                lookupObj['details'].append(details)
    
            return lookupObj

        lines = []
        lines.extend(self.writefeature(swaprtlextensions()))

        return lines

# COMPILE TTX
    def compileTTX(self):
        def dumpTTX(fontout):
            ttxfont = ttx.TTFont('out/'+fontout)
            ttxfont.saveXML('out/eot.ttx',splitTables=True)
            pass
        def cleanupWorkingFiles():
            def checkAndRemove(name):
                if os.path.exists('out/'+name):
                    os.remove('out/'+name)
                pass

            names = ['_h_e_a_d','_h_h_e_a','_h_m_t_x','_m_a_x_p','GlyphOrder','O_S_2f_2','_l_o_c_a',
                    '_c_m_a_p','_g_l_y_f','_n_a_m_e','_p_o_s_t','_v_h_e_a','_v_m_t_x',
                    'C_O_L_R_','C_P_A_L_','D_S_I_G_','t_s_i_v_']
            
            checkAndRemove('fontout_temp.ttf')
            for name in names:
                name = 'eot.'+name+'.ttx'
                checkAndRemove(name)
            checkAndRemove(self.compactfontfilename+'.cmap.ttx')
            checkAndRemove(self.compactfontfilename+'.vmtx')
            checkAndRemove('eot.ttx')
            pass
        # def dircompileTTX(fontout):
        #     ttxfont = ttx.TTFont('out/eot.ttx')
        #     ttxfont.save('out/eot_src.ttf')
        #     pass

        if self.pvar['test']['font'] == 1:
            print('Skipping Compile')
        else:
            print('Compiling font...')
            dumpTTX('fontout_temp.ttf')

            self.writeCMAP()
            self.writeVMTX()
            self.writeVHEA()
            self.writeTSIV()

            if os.path.exists('out/'+self.pvar['fontout']):
                os.remove('out/'+self.pvar['fontout'])
            # dircompileTTX(self.pvar['fontout'])
            os.system('ttx out/eot.ttx',)
        cleanupWorkingFiles()
        pass
    def writeCMAP(self):
        filename = 'eot._c_m_a_p.ttx'

        cmapfile = open('out/'+filename,"r")
        cmap14file = open('out/'+self.cmap14file,"r")
        w = False

        lines = []
        for line in cmapfile:
            lines.append(line)
        newmaster = open('out/'+filename,"w")
        for line in lines:
            if re.match(r'.*</cmap>.*',line) and w == False:
                w = True
                for l in cmap14file:
                    newmaster.write(l)
            newmaster.write(line)

        return
    def writeVMTX(self):
        def loadHead():
            lines = []
            lines.append('<?xml version="1.0" encoding="UTF-8"?>\n')
            lines.append('<ttFont sfntVersion="\\x00\\x01\\x00\\x00" ttLibVersion="4.27">\n')
            lines.append('\n')
            lines.append('  <vmtx>\n')
            return lines
        def loadBody():
            lines = []
            nummtx = 0
            maxvmtx = 0
            for key in self.glyphdata:
                if (key in verticalmetrics):
                    pair = verticalmetrics[key]
                    vert =   pair[0]
                    offset = pair[1]
                    maxvmtx = max(maxvmtx,vert)
                else:
                    vert   = 0
                    offset = 0
                line = '    <mtx name="'+key+'" height="'+str(vert)+'" tsb="'+str(offset)+'"/>\n'
                lines.append(line)
                nummtx += 1
            self.nummtx = nummtx
            self.maxvmtx = maxvmtx
            return lines
        def loadFoot():
            lines = []
            lines.append('  </vmtx>\n')
            lines.append('\n')
            lines.append('</ttFont>')
            return lines

        if self.pvar['vertical']:
            vmtx = []
            vmtx.extend(loadHead())
            vmtx.extend(loadBody())
            vmtx.extend(loadFoot())

            filename = 'eot._v_m_t_x.ttx'
            vmtxfile = open('out/'+filename,"w")
            for line in vmtx:
                vmtxfile.write(line)
            self.injectTable('eot.ttx','_v_m_t_x')


        pass
    def writeVHEA(self):
        def loadHead():
            lines = []
            lines.append('<?xml version="1.0" encoding="UTF-8"?>\n')
            lines.append('<ttFont sfntVersion="\\x00\\x01\\x00\\x00" ttLibVersion="4.27">\n')
            lines.append('\n')
            lines.append('  <vhea>\n')

            return lines
        def loadBody():
            #  https://docs.microsoft.com/en-us/typography/opentype/spec/vhea#:~:text=The%20vertical%20header%20table%20%28tag%20name%3A%20%27vhea%27%29%20contains,is%20general%20to%20the%20font%20as%20a%20whole.
            lines = []
            ascent = round((self.pvar['vhu'] * self.pvar['vfu'] * 0.5) + self.pvar['sb'])
            sb = self.pvar['sb']

            lines.append('    <tableVersion value="0x00010000"/>\n')
            lines.append('    <ascent value="'+str(ascent)+'"/>\n')
            lines.append('    <descent value="'+str(ascent)+'"/>\n')
            lines.append('    <lineGap value="0"/>\n')
            lines.append('    <advanceHeightMax value="'+str(self.maxvmtx)+'"/>\n')
            lines.append('    <minTopSideBearing value="'+str(sb)+'"/>\n')
            lines.append('    <minBottomSideBearing value="'+str(sb)+'"/>\n')
            lines.append('    <yMaxExtent value="'+str(sb+self.maxvmtx)+'"/>\n')
            lines.append('    <caretSlopeRise value="0"/>\n')
            lines.append('    <caretSlopeRun value="1"/>\n')
            lines.append('    <caretOffset value="0"/>\n')
            lines.append('    <reserved1 value="0"/>\n')
            lines.append('    <reserved2 value="0"/>\n')
            lines.append('    <reserved3 value="0"/>\n')
            lines.append('    <reserved4 value="0"/>\n')
            lines.append('    <metricDataFormat value="0"/>\n')
            lines.append('    <numberOfVMetrics value="'+str(self.nummtx)+'"/>\n')

            return lines
        def loadFoot():
            lines = []
            lines.append('  </vhea>\n')
            lines.append('\n')
            lines.append('</ttFont>')
            return lines

        if self.pvar['vertical']:
            vhea = []
            vhea.extend(loadHead())
            vhea.extend(loadBody())
            vhea.extend(loadFoot())

            filename = 'eot._v_h_e_a.ttx'
            vheafile = open('out/'+filename,"w")
            for line in vhea:
                vheafile.write(line)
            self.injectTable('eot.ttx','_v_h_e_a')

        pass
    def writeTSIV(self):
        filename = 'eot.t_s_i_v_.ttx'
        tsivfile = open('out/'+filename,"w")

        tsivfile.write('<?xml version="1.0" encoding="UTF-8"?>'+"\n")
        tsivfile.write('<ttFont ttLibVersion="4.27">'+"\n")
        tsivfile.write("\n")
        tsivfile.write('  <TSIV>'+"\n")
        tsivfile.write('    <source>'+"\n")

        vtpfile = open(self.writefile,"r")

        i = 0
        for line in vtpfile:
            tsivfile.write(line)
            i += 1

        tsivfile.write('    </source>'+"\n")
        tsivfile.write('  </TSIV>'+"\n")
        tsivfile.write('</ttFont>'+"\n")

        print('Wrote '+str(i)+' lines in VOLT src as TSIV table to '+filename)

        if i > 0:
            self.injectTable('eot.ttx','t_s_i_v_')

        return
    def injectTable(self,filename,table):
        ttxmaster = open("out/"+filename,"r")
        lines = []
        for line in ttxmaster:
            lines.append(line)
        newmaster = open("out/"+filename,"w")
        for line in lines:
            if re.match('</ttFont>',line):
                tablefilename = re.sub(r'(.*)(\.ttx)',r'\1.'+table+r'\2',filename)
                newmaster.write('  <DSIG src="'+tablefilename+'"/>\n')
            newmaster.write(line)
        pass

# END