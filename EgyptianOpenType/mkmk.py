#!/usr/bin/python
# egyptian opentype generator data

mkmk = [
    #Lookup
    {'name' : 'rows-rows0', 'marks' : '*stems0-v',
    'details' : [
        {'attach':['stems0-v'],'to':['stems0-v'],'anchor':'bottom'}
    ]},        
    #Lookup
    {'name' : 'rows-rows0R', 'marks' : '*stems0-vR',
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
    {'name' : 'cols-cols0', 'marks' : '*stems0-hx', 
    'exceptcontexts' : [
        {'left':['r0eB'],'right':[]}
    ],
    'details' : [
        {'attach':['stems0-h'],'to':['stems0-h'],'anchor':'right'}
    ]},
    #Lookup
    {'name' : 'cols-cols0R', 'marks' : '*stems0-hxR',
    'exceptcontexts' : [
        {'left':['r0eB'],'right':[]}
    ],
    'details' : [
        {'attach':['stems0-hR'],'to':['stems0-hR'],'anchor':'left'}
    ]},
    #Lookup
    {'name' : 'cols-shapes0', 'marks' : '*stems0_shapes0',
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
        {'attach':['shapes_0'],'to':['shapes_om'],'anchor':'center'},
    ]},
    #Lookup - Insertion ti
    {'name' : 'shapes0-ti', 'marks' : '*shape_ins0_ti',
    'details' : [
        {'attach':['shapes_0'],'to':['shapes_ti'],'anchor':'ti'}
    ]},
    #Lookup - Insertion mi
    {'name' : 'shapes0-mi', 'marks' : '*shape_ins0_mi',
    'details' : [
        {'attach':['shapes_0'],'to':['shapes_mi'],'anchor':'center'}
    ]},
    #Lookup - Insertion bi
    {'name' : 'shapes0-bi', 'marks' : '*shape_ins0_bi',
    'details' : [
        {'attach':['shapes_0'],'to':['shapes_bi'],'anchor':'bi'}
    ]},
    #Lookup - Corner insertion 2
    {'name' : 'shapes_ts-shapesi', 'marks' : '',
    'details' : [
        {'attach':['shapes_ts'],'to':['insertionsizes1'],'anchor':'center'},
        {'to':['insertionsizes1R'],'anchor':'center'},
        {'to':['shapes_u'],'anchor':'center'}
    ]},
    #Lookup - Corner insertion 3
    {'name' : 'shapes_bs-shapesi', 'marks' : '',
    'details' : [
        {'attach':['shapes_bs'],'to':['insertionsizes1'],'anchor':'center'},
        {'to':['insertionsizes1R'],'anchor':'center'},
        {'to':['shapes_u'],'anchor':'center'}
    ]},
    #Lookup - Corner insertion 4
    {'name' : 'shapes_te-shapesi', 'marks' : '',
    'details' : [
        {'attach':['shapes_te'],'to':['insertionsizes1'],'anchor':'center'},
        {'to':['insertionsizes1R'],'anchor':'center'},
        {'to':['shapes_u'],'anchor':'center'}
    ]},
    #Lookup - Corner insertion 5
    {'name' : 'shapes_be-shapesi', 'marks' : '',
    'details' : [
        {'attach':['shapes_be'],'to':['insertionsizes1'],'anchor':'center'},
        {'to':['insertionsizes1R'],'anchor':'center'},
        {'to':['shapes_u'],'anchor':'center'}
    ]},
    #Lookup - Middle-top insertion
    {'name' : 'shapes_ti-shapesi', 'marks' : '',
    'details' : [
        {'attach':['shapes_ti'],'to':['insertionsizes1'],'anchor':'ti'},
        {'to':['insertionsizes1R'],'anchor':'ti'},
        {'to':['shapes_u'],'anchor':'ti'}
    ]},
    #Lookup - Middle-middle insertion
    {'name' : 'shapes_mi-shapesi', 'marks' : '',
    'details' : [
        {'attach':['shapes_mi'],'to':['insertionsizes1'],'anchor':'center'},
        {'to':['insertionsizes1R'],'anchor':'center'},
        {'to':['shapes_u'],'anchor':'center'}
    ]},
    #Lookup - Middle-bottom insertion
    {'name' : 'shapes_bi-shapesi', 'marks' : '',
    'details' : [
        {'attach':['shapes_bi'],'to':['insertionsizes1'],'anchor':'bi'},
        {'to':['insertionsizes1R'],'anchor':'bi'},
        {'to':['shapes_u'],'anchor':'bi'}
    ]},
    #Lookup - Overstrike
    {'name' : 'shapes_om-shapesi', 'marks' : '',
    'details' : [
        {'attach':['shapes_om'],'to':['insertionsizes1'],'anchor':'center'},
        {'to':['insertionsizes1R'],'anchor':'center'},
        {'to':['shapes_u'],'anchor':'center'}
    ]},
    #DYNAMIC LOOKUP - Distance adjustments
    {'name' : 'offsets1', 'marks':'', 'details':[]},
    #Lookup
    {'name' : 'shapes0-row1', 'marks' : '',
    'details' : [
        {'attach':['shapes_0','shapes_u','insertionsizes1'],'to':['stems1-v'],'anchor':'left'},
    ]},
    #Lookup
    {'name' : 'shapes0-row1R', 'marks' : '',
    'details' : [
        {'attach':['shapes_0','shapes_u','insertionsizes1R'],'to':['stems1-vR'],'anchor':'right'},
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
    {'name' : 'rows-rows1R', 'marks' : '*stems1-vxR',
    'exceptcontexts' : [
        {'left':['r1sepR'],'right':[]}
    ],
    'details' : [
        {'attach':['stems1-vR'],'to':['stems1-vxR'],'anchor':'bottom'}
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
    {'name' : 'cols-cols1', 'marks' : '*stems1-hx',
    'exceptcontexts' : [
        {'left':['r1eB'],'right':[]}
    ],
    'details' : [
        {'attach':['stems1-h'],'to':['stems1-h'],'anchor':'right'}
    ]},
    #Lookup
    {'name' : 'cols-cols1R', 'marks' : '*stems1-hxR',
    'exceptcontexts' : [
        {'left':['r1eB'],'right':[]}
    ],
    'details' : [
        {'attach':['stems1-hR'],'to':['stems1-hR'],'anchor':'left'}
    ]},
    #Lookup
    {'name' : 'cols-shapes1', 'marks' : '*stems1_shapes1',
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
        {'attach':['shapes_1'],'to':['shapes_om2'],'anchor':'center'},
    ]},
    #Lookup - Insertion mi
    {'name' : 'shapes1-ti', 'marks' : '*shape_ins1_ti',
    'details' : [
        {'attach':['shapes_1'],'to':['shapes_ti2'],'anchor':'ti'}
    ]},
    #Lookup - Insertion mi
    {'name' : 'shapes1-mi', 'marks' : '*shape_ins1_mi',
    'details' : [
        {'attach':['shapes_1'],'to':['shapes_mi2'],'anchor':'center'}
    ]},
    #Lookup - Insertion mi
    {'name' : 'shapes1-bi', 'marks' : '*shape_ins1_bi',
    'details' : [
        {'attach':['shapes_1'],'to':['shapes_bi2'],'anchor':'bi'}
    ]},
    #Lookup - Corner insertion 2
    {'name' : 'shapes_ts2-shapesi', 'marks' : '',
    'details' : [
        {'attach':['shapes_ts2'],'to':['insertionsizes2'],'anchor':'center'},
        {'to':['insertionsizes2R'],'anchor':'center'},
        {'to':['shapes_u'],'anchor':'center'}
    ]},
    #Lookup - Corner insertion 3
    {'name' : 'shapes_bs2-shapesi', 'marks' : '',
    'details' : [
        {'attach':['shapes_bs2'],'to':['insertionsizes2'],'anchor':'center'},
        {'to':['insertionsizes2R'],'anchor':'center'},
        {'to':['shapes_u'],'anchor':'center'}
    ]},
    #Lookup - Corner insertion 4
    {'name' : 'shapes_te2-shapesi', 'marks' : '',
    'details' : [
        {'attach':['shapes_te2'],'to':['insertionsizes2'],'anchor':'center'},
        {'to':['insertionsizes2R'],'anchor':'center'},
        {'to':['shapes_u'],'anchor':'center'}
    ]},
    #Lookup - Corner insertion 5
    {'name' : 'shapes_be2-shapesi', 'marks' : '',
    'details' : [
        {'attach':['shapes_be2'],'to':['insertionsizes2'],'anchor':'center'},
        {'to':['insertionsizes2R'],'anchor':'center'},
        {'to':['shapes_u'],'anchor':'center'}
    ]},
    #Lookup - Middle-top insertion
    {'name' : 'shapes_ti2-shapesi', 'marks' : '',
    'details' : [
        {'attach':['shapes_ti2'],'to':['insertionsizes2'],'anchor':'ti'},
        {'to':['insertionsizes2R'],'anchor':'ti'},
        {'to':['shapes_u'],'anchor':'ti'}
    ]},
    #Lookup - Middle-middle insertion
    {'name' : 'shapes_mi2-shapesi', 'marks' : '',
    'details' : [
        {'attach':['shapes_mi2'],'to':['insertionsizes2'],'anchor':'center'},
        {'to':['insertionsizes2R'],'anchor':'center'},
        {'to':['shapes_u'],'anchor':'center'}
    ]},
    #Lookup - Middle-bottom insertion
    {'name' : 'shapes_bi2-shapesi', 'marks' : '',
    'details' : [
        {'attach':['shapes_bi2'],'to':['insertionsizes2'],'anchor':'bi'},
        {'to':['insertionsizes2R'],'anchor':'bi'},
        {'to':['shapes_u'],'anchor':'bi'}
    ]},
    #Lookup - Overstrike
    {'name' : 'shapes_om2-shapesi', 'marks' : '',
    'details' : [
        {'attach':['shapes_om2'],'to':['insertionsizes2'],'anchor':'center'},
        {'to':['insertionsizes2R'],'anchor':'center'},
        {'to':['shapes_u'],'anchor':'center'}
    ]},
    #DYNAMIC LOOKUP - Distance adjustments
    {'name' : 'offsets2', 'marks':'', 'details':[]},
    #Lookup
    {'name' : 'shapes1-row2', 'marks' : '',
    'details' : [
        {'attach':['shapes_1','shapes_u','insertionsizes2'],'to':['stems2-v'],'anchor':'left'}
    ]},
    #Lookup
    {'name' : 'shapes1-row2R', 'marks' : '',
    'details' : [
        {'attach':['shapes_1','shapes_u','insertionsizes2R'],'to':['stems2-vR'],'anchor':'right'}
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
    {'name' : 'rows-rows2R', 'marks' : '*stems2-vxR',
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
    {'name' : 'cols-cols2', 'marks' : '*stems2-hx',
    'exceptcontexts' : [
        {'left':['r2eB'],'right':[]}
    ],
    'details' : [
        {'attach':['stems2-h'],'to':['stems2-h'],'anchor':'right'}
    ]},
    #Lookup
    {'name' : 'cols-cols2R', 'marks' : '*stems2-hxR',
    'exceptcontexts' : [
        {'left':['r2eB'],'right':[]}
    ],
    'details' : [
        {'attach':['stems2-hR'],'to':['stems2-hR'],'anchor':'left'}
    ]},
    #Lookup
    {'name' : 'cols-shapes2', 'marks' : '*stems2_shapes2',
    'details' : [
        {'attach':['stems2-h','stems2-hR'],'to':['shapes_2'],'anchor':'left'},
        {'to':['shapes_u'],'anchor':'left'}
    ]},
    #Lookup
    {'name' : 'm0b0', 'marks' : '',
    'details' : [
        {'attach':['shapes_0','shapes_1','shapes_2','shapes_u'],'to':['m0'],'anchor':'center'},
        {'to':['b0'],'anchor':'bi'}
    ]},
    #Lookup
    {'name' : 'glyphs', 'marks' : '',
    'details' : [
        {'attach':['m0'],'to':['glyphs_all'],'anchor':'center'},
        {'to':['mirror_all'],'anchor':'center'}
    ]},
    # #Lookup
    # {'name' : 'tcbb', 'marks' : '',
    # 'details' : [
    #     {'attach':['stems0-h','stems1-h','stems2-h'],'to':['tcbb_mks'],'anchor':'top'}
    # ]},
    # #Lookup
    # {'name' : 'tcbe0', 'marks' : '*tcbe0_mfc',
    # 'details' : [
    #     {'attach':['shapes_0'],'to':['tcbe0_mks'],'anchor':'right'}
    # ]},
    # #Lookup
    # {'name' : 'tcbe1', 'marks' : '*tcbe1_mfc',
    # 'details' : [
    #     {'attach':['shapes_1'],'to':['tcbe1_mks'],'anchor':'right'}
    # ]},
    # #Lookup
    # {'name' : 'tcbe2', 'marks' : '*tcbe2_mfc',
    # 'details' : [
    #     {'attach':['shapes_2'],'to':['tcbe2_mks'],'anchor':'right'}
    # ]},
    # #Lookup
    # {'name' : 'damagedsign', 'marks' : '*shadesmkmk',
    # 'details' : [
    #     {'attach':['m0'],'to':['shapes_df'],'anchor':'center'},
    #     {'to':['shapes_dq'],'anchor':'center'}
    # ]},
    #Lookup
    {'name' : 'glyphs', 'marks' : '',
    'details' : [
        {'attach':['b0'],'to':['glyphs_all'],'anchor':'bi'},
        {'to':['mirror_all'],'anchor':'bi'}
    ]},
    # #Lookup
    # {'name' : 'damagedsign', 'marks' : '*shadesmkmk',
    # 'details' : [
    #     {'attach':['b0'],'to':['shapes_df'],'anchor':'bi'},
    #     {'to':['shapes_dq'],'anchor':'bi'}
    # ]}
]