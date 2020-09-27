#!/usr/bin/python
# egyptian opentype generator data

mkmk = [
    #Lookup
    {'name' : 'rows-rows0', 'marks' : 'stems0-v',
    'details' : [
        {'attach':['stems0-v'],'to':['stems0-v'],'anchor':'bottom'}
    ]},        
    #Lookup
    {'name' : 'rows-rows0R', 'marks' : 'stems0-vR',
    'details' : [
        {'attach':['stems0-vR'],'to':['stems0-vR'],'anchor':'bottom'}
    ]},        
    #Lookup
    {'name' : 'rows-cols0', 'marks' : '',
    'details' : [
        {'attach':['stems0-v'],'to':['stems0-h'],'anchor':'top'}
    ]},
    #Lookup
    {'name' : 'rows-cols0R', 'marks' : '',
    'details' : [
        {'attach':['stems0-vR'],'to':['stems0-hR'],'anchor':'top'}
    ]},
    #Lookup
    {'name' : 'cols-cols0', 'marks' : 'stems0-h', 
    'exceptcontexts' : [
        {'left':['r0eB'],'right':[]}
    ],
    'details' : [
        {'attach':['stems0-h'],'to':['stems0-h'],'anchor':'right'}
    ]},
    #Lookup
    {'name' : 'cols-cols0R', 'marks' : 'stems0-hR',
    'exceptcontexts' : [
        {'left':['r0eBR'],'right':[]}
    ],
    'details' : [
        {'attach':['stems0-hR'],'to':['stems0-hR'],'anchor':'left'}
    ]},
    #Lookup
    {'name' : 'cols-shapes0', 'marks' : '',
    'details' : [
        {'attach':['stems0-h','stems0-hR'],'to':['shapes_0'],'anchor':'left'},
        {'to':['shapes_u'],'anchor':'left'}
    ]},
    #Lookup - Corner insertion
    # Corner shapes match the size of the shape they are inserted into. This is so that
    # the corner anchor points can carry forward with each corner shape.
    {'name' : 'shapes0-corners0', 'marks' : 'shapeinsertions0',
    'details' : [
        {'attach':['shapes_0'],'to':['shapes_ts'],'anchor':'left'},
        {'to':['shapes_bs'],'anchor':'left'},
        {'to':['shapes_te'],'anchor':'left'},
        {'to':['shapes_be'],'anchor':'left'},
        {'to':['shapes_om'],'anchor':'center'},
    ]},
    #Lookup - Corner insertion bs,te,be
    {'name' : 'multi-corners 3', 'marks' : 'shapeinsertions0',
    'details' : [
        {'attach':['shapes_ts'],'to':['shapes_bs'],'anchor':'left'},
        {'to':['shapes_te'],'anchor':'left'},
        {'to':['shapes_be'],'anchor':'left'},
    ]},

    #Lookup - Corner insertion te, be
    {'name' : 'multi-corners 2', 'marks' : 'shapeinsertions0',
    'details' : [
        {'attach':['shapes_bs'],'to':['shapes_te'],'anchor':'left'},
        {'to':['shapes_be'],'anchor':'left'},
    ]},

    #Lookup - Multi-corner insertion be
    {'name' : 'multi-corners 1', 'marks' : 'shapeinsertions0',
    'details' : [
        {'attach':['shapes_te'],'to':['shapes_be'],'anchor':'left'}
    ]},

    #Lookup - Corner insertion 2
    {'name' : 'shapes_ts-shapesi', 'marks' : '',
    'details' : [
        {'attach':['shapes_ts'],'to':['insertionsizes1'],'anchor':'ts'},
        {'to':['insertionsizes1R'],'anchor':'te'}
    ]},
    #Lookup - Corner insertion 3
    {'name' : 'shapes_bs-shapesi', 'marks' : '',
    'details' : [
        {'attach':['shapes_bs'],'to':['insertionsizes1'],'anchor':'bs'},
        {'to':['insertionsizes1R'],'anchor':'be'}
    ]},
    #Lookup - Corner insertion 4
    {'name' : 'shapes_te-shapesi', 'marks' : '',
    'details' : [
        {'attach':['shapes_te'],'to':['insertionsizes1'],'anchor':'te'},
        {'to':['insertionsizes1R'],'anchor':'ts'}
    ]},
    #Lookup - Corner insertion 5
    {'name' : 'shapes_be-shapesi', 'marks' : '',
    'details' : [
        {'attach':['shapes_be'],'to':['insertionsizes1'],'anchor':'be'},
        {'to':['insertionsizes1R'],'anchor':'bs'}
    ]},
    #Lookup - Overstrike
    {'name' : 'shapes_om-shapeses', 'marks' : '',
    'details' : [
        {'attach':['shapes_om'],'to':['shapes_u'],'anchor':'center'}
    ]},
    #Lookup
    {'name' : 'shapes0-row1', 'marks' : '',
    'details' : [
        {'attach':['shapes_0','shapes_u','insertionsizes1','shapes_om'],'to':['stems1-v'],'anchor':'left'},
    ]},
    #Lookup
    {'name' : 'shapes0-row1R', 'marks' : '',
    'details' : [
        {'attach':['shapes_0','shapes_u','insertionsizes1R','shapes_om'],'to':['stems1-vR'],'anchor':'right'},
    ]},
    #Lookup
    {'name' : 'rows-rows1', 'marks' : 'stems1-v',
    'exceptcontexts' : [
        {'left':['insertionsizes1'],'right':[]},
        {'left':['r1sep'],'right':[]}
    ],
    'details' : [
        {'attach':['stems1-v'],'to':['stems1-v'],'anchor':'bottom'}
    ]},
    #Lookup
    {'name' : 'rows-rows1R', 'marks' : 'stems1-vR',
    'exceptcontexts' : [
        {'left':['insertionsizes1R'],'right':[]},
        {'left':['r1sepR'],'right':[]}
    ],
    'details' : [
        {'attach':['stems1-vR'],'to':['stems1-vR'],'anchor':'bottom'}
    ]},
    #Lookup
    {'name' : 'rows-cols1', 'marks' : '',
    'details' : [
        {'attach':['stems1-v'],'to':['stems1-h'],'anchor':'top'}
    ]},
    #Lookup
    {'name' : 'rows-cols1R', 'marks' : '',
    'details' : [
        {'attach':['stems1-vR'],'to':['stems1-hR'],'anchor':'top'}
    ]},
    #Lookup
    {'name' : 'cols-cols1', 'marks' : 'stems1-h',
    'exceptcontexts' : [
        {'left':['r1eB'],'right':[]}
    ],
    'details' : [
        {'attach':['stems1-h'],'to':['stems1-h'],'anchor':'right'}
    ]},
    #Lookup
    {'name' : 'cols-cols1R', 'marks' : 'stems1-hR',
    'exceptcontexts' : [
        {'left':['r1eBR'],'right':[]}
    ],
    'details' : [
        {'attach':['stems1-hR'],'to':['stems1-hR'],'anchor':'left'}
    ]},
    #Lookup
    {'name' : 'cols-shapes1', 'marks' : '',
    'details' : [
        {'attach':['stems1-h','stems1-hR'],'to':['shapes_1'],'anchor':'left'},
        {'to':['shapes_u'],'anchor':'left'}
    ]},

    #Lookup - Corner insertion
    # Corner shapes match the size of the shape they are inserted into. This is so that
    # the corner anchor points can carry forward with each corner shape.
    {'name' : 'shapes1-corners2_1', 'marks' : 'shapeinsertions1',
    'details' : [
        {'attach':['shapes_1'],'to':['shapes_ts2'],'anchor':'left'},
        {'to':['shapes_bs2'],'anchor':'left'},
        {'to':['shapes_te2'],'anchor':'left'},
        {'to':['shapes_be2'],'anchor':'left'},
        {'to':['shapes_om2'],'anchor':'center'},
    ]},
    #Lookup - Corner insertion bs,te,be
    {'name' : 'multi-corners2_3', 'marks' : 'shapeinsertions1',
    'details' : [
        {'attach':['shapes_ts2'],'to':['shapes_bs2'],'anchor':'left'},
        {'to':['shapes_te2'],'anchor':'left'},
        {'to':['shapes_be2'],'anchor':'left'},
    ]},

    #Lookup - Corner insertion te, be
    {'name' : 'multi-corners2_2', 'marks' : 'shapeinsertions1',
    'details' : [
        {'attach':['shapes_bs2'],'to':['shapes_te2'],'anchor':'left'},
        {'to':['shapes_be2'],'anchor':'left'},
    ]},

    #Lookup - Multi-corner insertion be
    {'name' : 'multi-corners2_1', 'marks' : 'shapeinsertions1',
    'details' : [
        {'attach':['shapes_te2'],'to':['shapes_be2'],'anchor':'left'}
    ]},

    #Lookup - Corner insertion 2
    {'name' : 'shapes_ts2-shapesi', 'marks' : '',
    'details' : [
        {'attach':['shapes_ts2'],'to':['insertionsizes2'],'anchor':'ts'},
        {'to':['insertionsizes2R'],'anchor':'te'}
    ]},
    #Lookup - Corner insertion 3
    {'name' : 'shapes_bs2-shapesi', 'marks' : '',
    'details' : [
        {'attach':['shapes_bs2'],'to':['insertionsizes2'],'anchor':'bs'},
        {'to':['insertionsizes2R'],'anchor':'be'}
    ]},
    #Lookup - Corner insertion 4
    {'name' : 'shapes_te2-shapesi', 'marks' : '',
    'details' : [
        {'attach':['shapes_te2'],'to':['insertionsizes2'],'anchor':'te'},
        {'to':['insertionsizes2R'],'anchor':'ts'}
    ]},
    #Lookup - Corner insertion 5
    {'name' : 'shapes_be2-shapesi', 'marks' : '',
    'details' : [
        {'attach':['shapes_be2'],'to':['insertionsizes2'],'anchor':'be'},
        {'to':['insertionsizes2R'],'anchor':'bs'}
    ]},
    #Lookup - Overstrike
    {'name' : 'shapes_om2-shapeses', 'marks' : '',
    'details' : [
        {'attach':['shapes_om2'],'to':['shapes_u'],'anchor':'center'}
    ]},

    #Lookup
    {'name' : 'shapes1-row2', 'marks' : '',
    'details' : [
        {'attach':['shapes_1','shapes_u','insertionsizes2','shapes_om2'],'to':['stems2-v'],'anchor':'left'}
    ]},
    #Lookup
    {'name' : 'shapes1-row2R', 'marks' : '',
    'details' : [
        {'attach':['shapes_1','shapes_u','insertionsizes2R','shapes_om2'],'to':['stems2-vR'],'anchor':'right'}
    ]},
    #Lookup
    {'name' : 'rows-rows2', 'marks' : 'stems2-v',
    'exceptcontexts' : [
        {'left':['r2vb'],'right':[]}
    ],
    'details' : [
        {'attach':['stems2-v'],'to':['stems2-v'],'anchor':'bottom'}
    ]},
    #Lookup
    {'name' : 'rows-rows2R', 'marks' : 'stems2-vR',
    'exceptcontexts' : [
        {'left':['r2vbR'],'right':[]}
    ],
    'details' : [
        {'attach':['stems2-vR'],'to':['stems2-vR'],'anchor':'bottom'}
    ]},
    #Lookup
    {'name' : 'rows-cols2', 'marks' : '',
    'details' : [
        {'attach':['stems2-v'],'to':['stems2-h'],'anchor':'top'}
    ]},
    #Lookup
    {'name' : 'rows-cols2R', 'marks' : '',
    'details' : [
        {'attach':['stems2-vR'],'to':['stems2-hR'],'anchor':'top'}
    ]},
    #Lookup
    {'name' : 'cols-cols2', 'marks' : 'stems2-h',
    'exceptcontexts' : [
        {'left':['r2eB'],'right':[]}
    ],
    'details' : [
        {'attach':['stems2-h'],'to':['stems2-h'],'anchor':'right'}
    ]},
    #Lookup
    {'name' : 'cols-cols2R', 'marks' : 'stems2-hR',
    'exceptcontexts' : [
        {'left':['r2eBR'],'right':[]}
    ],
    'details' : [
        {'attach':['stems2-hR'],'to':['stems2-hR'],'anchor':'left'}
    ]},
    #Lookup
    {'name' : 'cols-shapes2', 'marks' : '',
    'details' : [
        {'attach':['stems2-h'],'to':['shapes_2'],'anchor':'left'}
    ]},
    #Lookup
    {'name' : 'cols-shapes2R', 'marks' : '',
    'details' : [
        {'attach':['stems2-hR'],'to':['shapes_2'],'anchor':'left'}
    ]},
    #Lookup
    {'name' : 'm0', 'marks' : '',
    'details' : [
        {'attach':['shapes_0','shapes_1','shapes_2','shapes_u'],'to':['m0'],'anchor':'center'}
    ]},
    #Lookup
    {'name' : 'glyphs', 'marks' : '',
    'details' : [
        {'attach':['m0'],'to':['glyphs_all'],'anchor':'center'},
        {'to':['mirror_all'],'anchor':'center'}
    ]}
]