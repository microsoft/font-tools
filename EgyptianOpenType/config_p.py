#!/usr/bin/python
# egyptian opentype generator project-specific variables

pvar = {
    'scriptname' : "Egyptian hieroglyphs", # OpenType table values
    'scripttag' : "egyp",
    'langsysname' : "Default",
    'langsystag' : "dflt",
    'reffontname' : "Segoe UI Historic", # Used in test file to show reference form relative to current version
    'fontfilename' : "Egyptian Text Proto", # Font name
    'fontsrc' : "../../fonts/et/egyptiantextV2Proto-COLR.ttf", # Path to source font
    'fontout' : "egyptiantextV2Proto.ttf", # Path to write output font
    'sb'  : 105, # font side bearings
    'hfu' : 315, # horizontal, font units per hieroglyph unit (1372 per 6 hieroglyph units)
    'vfu' : 310, # vertical, font units per hieroglyph unit (1358 per 6 hieroglyph units)
    'vbase' : -284, # vertical baseline for hieroglyphs in font units 
    'hhu' : 8, # horizontal, hieroglyph units
    'chu' : 6, # composite horizontal units (i.e., excludes wide non-composing widths)
    'vhu' : 6, # vertical, hieroglyph units
    'issp' : 0, #Inter-sign spacing (+ allows glyph outlines to overlap, 0 no overlap)
    'scndmax' : [[6,6,6],[12,12,6],[12,12,0]], #Derivatives of chu, summed twice
    'deltamax' : [30,20,15],#Derivatives of max width [(max width * max columns) - max columns]
    'redv': [[6,5,3,4,3,2],[6,5,4,2,3,2],[6,5,4,2,3,2]], #Set size reduction priority sequence, see decrementloop()
    'redh': [[6,5,4,3,2],[6,5,4,3,2],[6,5,4,3,2]], #Set size reduction priority sequence, see decrementloop()
    'el'  : 3, # embedding levels
    'maxperlevel' : [36,30,18], #max sign width per level
    'shapekey' : ['o','s','i'], #sigla used for shape glyphs per level
    'insertionwidthmax' : [0,5,4], #max h for inserted region per level
    'insertionheightmax' : [0,5,4], #max v for inserted region per level
    'insertionwidthmin' : [4,2,0], #min h for region having nested block per level
    'insertionheightmin' : [3,2,0], #min v for region having nested block per level
    'cornerwidthmin' : [2,2,0], #min h for region having corner per level
    'cornerheightmin' : [2,2,0], #min v for region having corner per level
    'targetwidthmin' : [6,1,1], # min ideal h per level
    'targetwidthmax' : [6,6,4], # max ideal h per level
    'targetheightmin' : [6,1,1],# min ideal v per level
    'targetheightmax' : [6,6,5],# max ideal v per level
    'cyclesperlevel' : [3,3,2], #Used to repeat sum and max substitutions
    'defaultinsertionsize' : 2, #default insertion size per level
    'controls' : ['vj','hj','ts','bs','te','be','om','ss','se'],
    'controlcodes' : [[':',';','v'],['*','.'],[],[],[],[],['+','='],['(','['],[')',']']],
    'useproxycontrols': 0, # use proxy code points for controls
    'proxycontrols' : [78691,78692,78693,78694,78695,78696,78697,78698,78699],
    'extensions' : 1,
    # 'cartouchecodes' : ['cb','cwb','hwtb','hwttb','hwtbb','hwtwb','ce','cre','cwe','hwte','hwtte','hwtbe','hwtwe'],
    'mirror' : 1,
    # 'test' : {'font':0,'gdef':0,'groups':0,'haln':1,'pres':0,'abvs':1,'blws':1,'rlig':0,'psts':0,'rtlm':1,'vrt2':1,'gpos':0,'langsys':0,'anchors':0,'coda':0}
    'test' : {'font':0,'gdef':0,'groups':0,'haln':1,'pres':0,'abvs':0,'blws':0,'rlig':0,'psts':0,'rtlm':0,'vrt2':1,'gpos':0,'langsys':0,'anchors':0,'coda':0}
}