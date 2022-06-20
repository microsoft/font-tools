#!/usr/bin/python
# egyptian opentype generator project-specific variables

pvar = {
    'scriptname' : "Egyptian hieroglyphs", # OpenType table values
    'scripttag' : "egyp",
    'langsysname' : "Default",
    'langsystag' : "dflt",
    'reffontname' : "Segoe UI Historic", # Used in test file to show reference form relative to current version
    'fontfilename' : "Egyptian Text Proto", # Font name
    'fontsrc' : "../../fonts/et/egyptiantextU12core-COLR.ttf", # Path to source font
    'fontout' : "eot.ttf", # Path to write output font
    'fontprior' : "egyptiantextU12.ttf", # Path to prior test font
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
        'mi',    # 6 middle insertion         [13375] -> 78373   13225 -> 78368   13220 -> 13439
        'ti',    # 5 top insertion            [13376] -> 78372   13224 -> 78369   13221 -> 1343A
        'bi',    # 7 bottom insertion         [13377] -> 78374   13226 -> 78370   13222 -> 1343B
        'esb',   # 2 begin enclosure          [     ] -> 78368   13220 -> 78371   13223 -> 1343C
        'ese',   # 1 end enclosure            [     ] -> 78369   13221 -> 78372   13224 -> 1343D
        'ewb',   # 3 begin walled enclosure   [     ] -> 78370   13222 -> 78373   13225 -> 1343E
        'ewe',   # 4 end walled enclosure     [     ] -> 78371   13223 -> 78374   13226 -> 1343F
        'mr',    # 8 mirror horizontally      [1336D] -> 78375   13227 -> 78375   13227 -> 13440
        'BF1',   # 9 blank full               [13367] -> 78376   13228 -> 78376   13228 -> 13441
        'BQ1',   #10 blank half               [13371] -> 78377   13229 -> 78377   13229 -> 13442
        'AS1',   #11 lost sign full           [1336E] -> 78378   1322A -> 78378   1322A -> 13443
        'AQ1',   #12 lost sign quarter        [1336F] -> 78379   1322B -> 78379   1322B -> 13444
        'AT1',   #13 lost sign tall           [     ] -> 78380   1322C -> 78380   1322C -> 13445
        'AW1',   #14 lost sign wide           [     ] -> 78381   1322D -> 78381   1322D -> 13446
        'dq1',   #16 damaged quarter 1        [     ] -> 78383   1322F -> 78382   1322E -> 13447
        'dq2',   #23 damaged quarter 2        [     ] -> 78390   13236 -> 78383   1322F -> 13448
        'dq12',  #17 damaged quarter 12       [     ] -> 78384   13230 -> 78384   13230 -> 13449
        'dq3',   #27 damaged quarter 3        [     ] -> 78394   1323A -> 78385   13231 -> 1344A
        'dq13',  #20 damaged quarter 13       [     ] -> 78387   13233 -> 78386   13232 -> 1344B
        'dq23',  #24 damaged quarter 23       [     ] -> 78391   13237 -> 78387   13233 -> 1344C
        'dq123', #18 damaged quarter 123      [     ] -> 78385   13231 -> 78388   13234 -> 1344D
        'dq4',   #29 damaged quarter 4        [     ] -> 78396   1323C -> 78389   13235 -> 1344E
        'dq14',  #22 damaged quarter 14       [     ] -> 78389   13235 -> 78390   13236 -> 1344F
        'dq24',  #26 damaged quarter 24       [     ] -> 78393   13239 -> 78391   13237 -> 13450
        'dq124', #19 damaged quarter 124      [     ] -> 78386   13232 -> 78392   13238 -> 13451
        'dq34',  #28 damaged quarter 34       [     ] -> 78395   1323B -> 78393   13239 -> 13452
        'dq134', #21 damaged quarter 134      [     ] -> 78388   13234 -> 78394   1323A -> 13453
        'dq234', #25 damaged quarter 234      [     ] -> 78392   13238 -> 78395   1323B -> 13454
        'df',    #15 damaged full    1234     [13368] -> 78382   1322E -> 78396   1323C -> 13455
        # 'VP',    #30 verse point              [13373] -> 78397   1323D
        # 'tcbb',  #31 text critical bracket begin [1337C] -> 91   13230
        # 'tcbe',  #32 text critical bracket end[1337E] ->    93   13231
        # 'AS2',   #11 atomic shade full exp    [1336E] -> 78398   1322A #temp, needs to move to a VS AS1 VS -> AS
    ],
    'controlcodes' : [[':',';','v'],['*','.'],[],[],[],[],['+','='],['(','['],[')',']']],
    'useproxycontrols': 0, # use proxy code points for controls
    'proxycontrols' : [78905,78906,78907,78908,78909,78910,78911,78912,78913,78914,
                        78915,78916,78917,78918,78919,78920,78921,78922,78923,78924,
                        78925,78926,78927,78928,78929,78930,78931,78932,78933,
                        91,93],
    'internalligatures'  : 1,  
    'extensions' : 1,
    'variations' : 1,
    'tcbs' : 1,
    # 'cartouchecodes' : ['cb','cwb','hwtb','hwttb','hwtbb','hwtwb','ce','cre','cwe','hwte','hwtte','hwtbe','hwtwe'],
    'baseline' : 1, #align singletons to baseline for Hieratic
    'mirror'  : 1,  
    'vertical': 1,
    'variations' :  1,
    'expansions' : 0,
    'glyphproperties' : 1,
    'test' : {
        'font':         1,
        'gdef':         1,
        'groups':       1,
        'haln':         0,
        'pres':         1,
        'abvs':         1,
        'blws':         1,
        'rlig':         1,
        'psts':         1,
        'ss01':         1,
        'rtlm':         1,
        'vrt2':         1,
        'gpos':         1,
        'langsys':      1,
        'anchors':      1,
        'coda':         1,
    }
}