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
    #Lookup - Insertion ts
    {'name' : 'shapes0-ts', 'marks' : '*shape_ins0_ts',
    'details' : [
        {'attach':['shapes_0'],'to':['shapes_ts'],'anchor':'left'},
    ]},
    #Lookup - Insertion bs
    {'name' : 'shapes0-bs', 'marks' : '*shape_ins0_bs',
    'details' : [
        {'attach':['shapes_0'],'to':['shapes_bs'],'anchor':'bs'},
    ]},
    #Lookup - Insertion te
    {'name' : 'shapes0-te', 'marks' : '*shape_ins0_te',
    'details' : [
        {'attach':['shapes_0'],'to':['shapes_te'],'anchor':'te'},
    ]},
    #Lookup - Insertion be
    {'name' : 'shapes0-be', 'marks' : '*shape_ins0_be',
    'details' : [
        {'attach':['shapes_0'],'to':['shapes_be'],'anchor':'be'}
    ]},
    #Lookup - Insertion om
    {'name' : 'shapes0-om', 'marks' : '*shape_ins0_om',
    'details' : [
        {'attach':['shapes_0'],'to':['shapes_om'],'anchor':'left'},
    ]},
    #Lookup - Insertion mi
    {'name' : 'shapes0-mi', 'marks' : '*shape_ins0_mi',
    'details' : [
        {'attach':['shapes_0'],'to':['shapes_mi'],'anchor':'center'}
    ]},
    #Lookup - Corner insertion 2
    {'name' : 'shapes_ts-shapesi', 'marks' : '',
    'details' : [
        {'attach':['shapes_ts'],'to':['insertionsizes1'],'anchor':'center'},
        # {'to':['insertionsizes1R'],'anchor':'te'},
        {'to':['shapes_u'],'anchor':'center'}
    ]},
    #Lookup - Corner insertion 3
    {'name' : 'shapes_bs-shapesi', 'marks' : '',
    'details' : [
        {'attach':['shapes_bs'],'to':['insertionsizes1'],'anchor':'center'},
        # {'to':['insertionsizes1R'],'anchor':'be'},
        {'to':['shapes_u'],'anchor':'center'}
    ]},
    #Lookup - Corner insertion 4
    {'name' : 'shapes_te-shapesi', 'marks' : '',
    'details' : [
        {'attach':['shapes_te'],'to':['insertionsizes1'],'anchor':'center'},
        # {'to':['insertionsizes1R'],'anchor':'ts'},
        {'to':['shapes_u'],'anchor':'center'}
    ]},
    #Lookup - Corner insertion 5
    {'name' : 'shapes_be-shapesi', 'marks' : '',
    'details' : [
        {'attach':['shapes_be'],'to':['insertionsizes1'],'anchor':'center'},
        # {'to':['insertionsizes1R'],'anchor':'bs'},
        {'to':['shapes_u'],'anchor':'center'}
    ]},
    #Lookup - Middle insertion
    {'name' : 'shapes_mi-shapesi', 'marks' : '',
    'details' : [
        {'attach':['shapes_mi'],'to':['insertionsizes1'],'anchor':'center'},
        # {'to':['insertionsizes1R'],'anchor':'center'},
        {'to':['shapes_u'],'anchor':'center'}
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
    {'name' : 'rows-rows1', 'marks' : '*stems1-vx',
    'exceptcontexts' : [
        {'left':['r1sep'],'right':[]}
    ],
    'details' : [
        {'attach':['stems1-v'],'to':['stems1-v'],'anchor':'bottom'}
    ]},
    #Lookup
    {'name' : 'rows-rows1R', 'marks' : 'stems1-vR',
    'exceptcontexts' : [
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

    #Lookup - Insertion ts
    {'name' : 'shapes1-ts', 'marks' : '*shape_ins1_ts',
    'details' : [
        {'attach':['shapes_1'],'to':['shapes_ts2'],'anchor':'left'},
    ]},
    #Lookup - Insertion bs
    {'name' : 'shapes1-bs', 'marks' : '*shape_ins1_bs',
    'details' : [
        {'attach':['shapes_1'],'to':['shapes_bs2'],'anchor':'bs'},
    ]},
    #Lookup - Insertion te
    {'name' : 'shapes1-te', 'marks' : '*shape_ins1_te',
    'details' : [
        {'attach':['shapes_1'],'to':['shapes_te2'],'anchor':'te'},
    ]},
    #Lookup - Insertion be
    {'name' : 'shapes1-be', 'marks' : '*shape_ins1_be',
    'details' : [
        {'attach':['shapes_1'],'to':['shapes_be2'],'anchor':'be'}
    ]},
    #Lookup - Insertion om
    {'name' : 'shapes1-om', 'marks' : '*shape_ins1_om',
    'details' : [
        {'attach':['shapes_1'],'to':['shapes_om2'],'anchor':'left'},
    ]},
    #Lookup - Insertion mi
    {'name' : 'shapes1-mi', 'marks' : '*shape_ins1_mi',
    'details' : [
        {'attach':['shapes_1'],'to':['shapes_mi2'],'anchor':'center'}
    ]},
    #Lookup - Corner insertion 2
    {'name' : 'shapes_ts2-shapesi', 'marks' : '',
    'details' : [
        {'attach':['shapes_ts2'],'to':['insertionsizes2'],'anchor':'center'},
        # {'to':['insertionsizes1R'],'anchor':'te'},
        {'to':['shapes_u'],'anchor':'center'}
    ]},
    #Lookup - Corner insertion 3
    {'name' : 'shapes_bs2-shapesi', 'marks' : '',
    'details' : [
        {'attach':['shapes_bs2'],'to':['insertionsizes2'],'anchor':'center'},
        # {'to':['insertionsizes1R'],'anchor':'be'},
        {'to':['shapes_u'],'anchor':'center'}
    ]},
    #Lookup - Corner insertion 4
    {'name' : 'shapes_te2-shapesi', 'marks' : '',
    'details' : [
        {'attach':['shapes_te2'],'to':['insertionsizes2'],'anchor':'center'},
        # {'to':['insertionsizes1R'],'anchor':'ts'},
        {'to':['shapes_u'],'anchor':'center'}
    ]},
    #Lookup - Corner insertion 5
    {'name' : 'shapes_be2-shapesi', 'marks' : '',
    'details' : [
        {'attach':['shapes_be2'],'to':['insertionsizes2'],'anchor':'center'},
        # {'to':['insertionsizes1R'],'anchor':'bs'},
        {'to':['shapes_u'],'anchor':'center'}
    ]},
    #Lookup - Middle insertion
    {'name' : 'shapes_mi2-shapesi', 'marks' : '',
    'details' : [
        {'attach':['shapes_mi2'],'to':['insertionsizes2'],'anchor':'center'},
        # {'to':['insertionsizes1R'],'anchor':'center'},
        {'to':['shapes_u'],'anchor':'center'}
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
    {'name' : 'rows-rows2', 'marks' : '*stems2-vx',
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
    ]},
    #Lookup
    {'name' : 'damagedsign', 'marks' : '*shadesmkmk',
    'details' : [
        {'attach':['m0'],'to':['shapes_df'],'anchor':'center'}
    ]}
]