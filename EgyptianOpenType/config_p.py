#!/usr/bin/python
# egyptian opentype generator project-specific variables

pvar = {
    'scriptname' : "Egyptian hieroglyphs", # OpenType table values
    'scripttag' : "egyp",
    'langsysname' : "Default",
    'langsystag' : "dflt",
    'reffontname' : "Segoe UI Historic", # Used in test file to show reference form relative to current version
    'fontfilename' : "Egyptian Text Proto", # Font name
    'fontsrc' : "../../fonts/et/egyptiantextV3ProtoFull-COLR.ttf", # Path to source font
    'fontout' : "egyptiantextV4ProtoFull.ttf", # Path to write output font
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
    'controls2': [
        'esb', # 1 extension straight begin [13363] -> 78368 13220
        'ese', # 2 extension straight end   [13364] -> 78369 13221
        'ewb', # 3 extension walled begin   [13365] -> 78370 13222
        'ewe', # 4 extension walled end     [13366] -> 78371 13223
        'BF1', # 5 blank full               [13367] -> 78372 13224
        'df',  # 6 damaged full             [13368] -> 78373 13225
        'sts', # 7 shade top start          [13369] -> 78374 13226
        'sbs', # 8 shade bottom start       [1336A] -> 78375 13227
        'ste', # 9 shade top end            [1336B] -> 78376 13228
        'sbe', #10 shade bottom end         [1336C] -> 78377 13229
        'mr',  #11 mirror                   [1336D] -> 78378 1322A
        # 'r90', # rotate 90 degrees      [1336E] -> X
        # 'r180', # rotate 180 degrees    [1336F] -> X
        # 'r270', # rotate 270 degrees    [13370] -> X
        'BQ1', #12 blank quarter            [13371] -> 78379 1322B
        # 'BS1', # blank sixth            [13372] -> X
        'VP',  #13 verse point              [13373] -> 78380   1322C
        # 'VPr', # verse point r          [13374] -> X       id 221
        'ti',  #14 top insertion            [13376] -> 78381   1322D
        'mi',  #15 middle insertion         [13375] -> 78382   1322E
        'bi',  #16 bottom insertion         [13377] -> 78383   1322F
        'tcbb',#17 text critical bracket begin [1337C] -> 97    13230
        'tcbe',#18 text critical bracket end[1337E] ->    99    13231
        'AS1', #19 atomic shade full        [1336E] -> 78386    13232
        'AQ1', #20 atomic shade quarter     [1336F] -> 78387    13233
        'AT1', #21 atomic shade tall        [     ] -> 78388    13234
        'AW1', #22 atomic shade wide        [     ] -> 78389    13235
    ],
    'controlcodes' : [[':',';','v'],['*','.'],[],[],[],[],['+','='],['(','['],[')',']']],
    'useproxycontrols': 0, # use proxy code points for controls
    'proxycontrols' : [78368,78369,78370,78371,78372,78373,78374,78375,78376,78377,
                        78378,78379,78380,78381,78382,78383,97,99,78386,78387,
                        78388,78389],
    'extensions' : 1,
    'variations' :  1,
    'tcbs' : 1,
    # 'cartouchecodes' : ['cb','cwb','hwtb','hwttb','hwtbb','hwtwb','ce','cre','cwe','hwte','hwtte','hwtbe','hwtwe'],
    'baseline' : 1, #align singletons to baseline for Hieratic
    'mirror'  : 1,  
    'vertical': 1,
    # 'test' : {'font':0,'gdef':0,'groups':0,'haln':1,'pres':0,'abvs':1,'blws':1,'rlig':0,'psts':0,'ss01':1,'rtlm':1,'vrt2':1,'gpos':0,'langsys':0,'anchors':0,'coda':0}
    'test' : {'font':0,'gdef':0,'groups':0,'haln':0,'pres':0,'abvs':0,'blws':0,'rlig':0,'psts':0,'ss01':0,'rtlm':0,'vrt2':0,'gpos':0,'langsys':0,'anchors':0,'coda':0}
}