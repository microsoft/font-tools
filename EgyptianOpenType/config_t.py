#!/usr/bin/python
# egyptian opentype generator project-specific variables

pvar = {
    'scriptname' : "Egyptian hieroglyphs", # OpenType table values
    'scripttag' : "egyp",
    'langsysname' : "Default",
    'langsystag' : "dflt",
    'reffontname' : "Segoe UI Historic", # Used in test file to show reference form relative to current version
    'fontfilename' : "Egyptian Text", # Font name
    'fontsrc' : "../../fonts/et/egyptiantextV2Proto-COLR.ttf", # Path to source font
    'fontout' : "eot_src.ttf", # Path to write output font
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
        'ti',    # 1 top insertion            [13376] -> 78372   13224
        'mi',    # 2 middle insertion         [13375] -> 78373   13225
        'bi',    # 3 bottom insertion         [13377] -> 78374   13226
        'mr',    # 4 mirror                   [1336D] -> 78375   13227
        'BF1',   # 5 blank full               [13367] -> 78376   13228
        'BQ1',   # 6 blank quarter            [13371] -> 78377   13229
        'AS1',   # 7 atomic shade full        [1336E] -> 78378   1322A
        'AQ1',   # 8 atomic shade quarter     [1336F] -> 78379   1322B
        'AT1',   # 9 atomic shade tall        [     ] -> 78380   1322C
        'AW1',   #10 atomic shade wide        [     ] -> 78381   1322D
        'df',    #11 damaged full             [13368] -> 78382   1322E
        'dq1',   #12 damaged quarter 1        [     ] -> 78383   1322F
        'dq12',  #13 damaged quarter 12       [     ] -> 78384   13230
        'dq123', #14 damaged quarter 123      [     ] -> 78385   13231
        'dq124', #15 damaged quarter 124      [     ] -> 78386   13232
        'dq13',  #16 damaged quarter 13       [     ] -> 78387   13233
        'dq134', #17 damaged quarter 134      [     ] -> 78388   13234
        'dq14',  #18 damaged quarter 14       [     ] -> 78389   13235
        'dq2',   #19 damaged quarter 2        [     ] -> 78390   13236
        'dq23',  #20 damaged quarter 23       [     ] -> 78391   13237
        'dq234', #21 damaged quarter 234      [     ] -> 78392   13238
        'dq24',  #22 damaged quarter 24       [     ] -> 78393   13239
        'dq3',   #23 damaged quarter 3        [     ] -> 78394   1323A
        'dq34',  #24 damaged quarter 34       [     ] -> 78395   1323B
        'dq4',   #25 damaged quarter 4        [     ] -> 78396   1323C
        'VP',    #26 verse point              [13373] -> 78397   1323D
        'tcbb',  #27 text critical bracket begin [1337C] -> 97    13230
        'tcbe',  #28 text critical bracket end[1337E] ->    99    13231
    ],
    'controlcodes' : [[':',';','v'],['*','.'],[],[],[],[],['+','='],['(','['],[')',']']],
    'useproxycontrols': 1, # use proxy code points for controls
    'proxycontrols' : [78368,78369,78370,78371,78372,78373,78374,78375,78376,78377,
                        78378,78379,78380,78381,78382,78383,78384,78385,78386,78387,
                        78388,78389,78390,78391,78392,78393,97,99],
    'extensions' : 1,
    'tcbs' : 1,
    # 'cartouchecodes' : ['cb','cwb','hwtb','hwttb','hwtbb','hwtwb','ce','cre','cwe','hwte','hwtte','hwtbe','hwtwe'],
    'baseline' : 1, #align singletons to baseline for Hieratic
    'mirror' : 1,
    'vertical': 1,
    'variations' :  1,
    'expansions' : 0,
    'test' : {
        'font':         0,
        'gdef':         0,
        'groups':       0,
        'haln':         1,
        'pres':         0,
        'abvs':         1,
        'blws':         1,
        'rlig':         0,
        'psts':         0,
        'ss01':         1,
        'rtlm':         1,
        'vrt2':         1,
        'gpos':         0,
        'langsys':      0,
        'anchors':      0,
        'coda':         0,
    }
}