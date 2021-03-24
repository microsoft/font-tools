#!/usr/bin/python
# egyptian opentype generator data

pres = [
    # Lookup - tcm start
    {'name' : 'tcm_open', 'marks' : '',
    'contexts' : [{'left':[],'right':['characters_all']}],
    'details' : [
        {'sub':['uni27E8'],'target':['tcab']},
        {'sub':['bracketleft'],'target':['tcbb']},
        {'sub':['braceleft'],'target':['tccb']},
        {'sub':['tophalfbracketL'],'target':['tchb']},
        {'sub':['uni27EE'],'target':['tcpb']},
        {'sub':['uni27E6'],'target':['tcrb']},
        {'sub':['bar'],'target':['tcv']},
    ]},
    # Lookup - tcm end
    {'name' : 'tcm_open', 'marks' : '',
    'contexts' : [{'left':['characters_all'],'right':[]}],
    'details' : [
        {'sub':['uni27E9'],'target':['tcae']},
        {'sub':['bracketright'],'target':['tcbe']},
        {'sub':['braceright'],'target':['tcce']},
        {'sub':['tophalfbracketR'],'target':['tche']},
        {'sub':['uni27EF'],'target':['tcpe']},
        {'sub':['uni27E7'],'target':['tcre']},
        {'sub':['bar'],'target':['tcv']},
    ]},
    # Lookup - quarter shades
    {'name' : 'quarterShades', 'marks' : '',
    'contexts' : [{'left':[],'right':[]}],
    'details' : [
        {'sub':['sts','sbs','ste','sbe'],'target':['DQ6_1234']},
        {'sub':['sts','sbs','ste'],'target':['DQ6_123']},
        {'sub':['sts','sbs','sbe'],'target':['DQ6_124']},
        {'sub':['sts','ste','sbe'],'target':['DQ6_134']},
        {'sub':['sbs','ste','sbe'],'target':['DQ6_234']},
        {'sub':['sts','sbs'],'target':['DQ6_12']},
        {'sub':['sts','ste'],'target':['DQ6_13']},
        {'sub':['sts','sbe'],'target':['DQ6_14']},
        {'sub':['sbs','ste'],'target':['DQ6_23']},
        {'sub':['sbs','sbe'],'target':['DQ6_24']},
        {'sub':['ste','sbe'],'target':['DQ6_34']},
        {'sub':['sts'],'target':['DQ6_1']},
        {'sub':['sbs'],'target':['DQ6_2']},
        {'sub':['ste'],'target':['DQ6_3']},
        {'sub':['sbe'],'target':['DQ6_4']},
    ]},
    # Lookup - extensions outer dbl extensions begin outer
    {'name' : 'extensionsouterB', 'bases':'SKIP','marks' : 'extensioncontrols',
    'contexts' : [
        {'left':[],'right':['esb']},
        {'left':[],'right':['ewb']}],
    'details' : [{'sub':['esb'],'target':['eob']}]},
    # Lookup - extensions dbl extensions begin inner
    {'name' : 'extensionsinnerB', 'bases':'SKIP','marks' : 'extensioncontrols',
    'contexts' : [{'left':['eob'],'right':[]}],
    'details' : [
        {'sub':['esb'],'target':['edb']},
        {'sub':['ewb'],'target':['efb']}
        ]},
    # Lookup - extensions dbl extensions end inner
    {'name' : 'extensionsdblE', 'bases':'SKIP','marks' : 'extensioncontrols',
    'contexts' : [
        {'left':['edb'],'right':[]},
        {'left':['efb'],'right':[]}],
    'details' : [
        {'sub':['ese'],'target':['ede']},
        {'sub':['ewe'],'target':['efe']}
    ]},
    # Lookup - extensions dbl extensions end outer
    {'name' : 'extensionsouterE', 'bases':'SKIP','marks' : 'extensioncontrols',
    'contexts' : [
        {'left':['ede'],'right':[]},
        {'left':['efe'],'right':[]}
        ],
    'details' : [{'sub':['ese'],'target':['eoe']}]},
    # Lookup - convert embedded joiners to level 2 joiners
    {'name' : 'mdcLevel2_joiners', 'marks' : 'controls_a',
    'contexts' : [
        {'left':['ss','ss'],'right':[]},
        {'left':['ss','controls_joiners','ss'],'right':[]},
        {'left':['ss','controls_joiners','controls_joiners','ss'],'right':[]},
        {'left':['ss','controls_joiners','controls_joiners','controls_joiners','ss'],'right':[]}],
    'details' : [
        {'sub':['hj'],'target':['hj2A']},
        {'sub':['vj'],'target':['vj2A']}]},
    # Lookup - merge level 2 embedding controls
    {'name' : 'mdcBE_merge2', 'marks' : 'controls_a',
    'contexts' : [{'left':[],'right':[]}],
    'details' : [
        {'sub':['ss','se'],'target':['cleanup']}]},
    # Lookup - convert embedded joiners to level 1 joiners
    {'name' : 'mdcLevel1_joiners', 'marks' : 'controls_a',
    'contexts' : [
        {'left':['ss'],'right':[]},
        {'left':['ss','controls_joiners'],'right':[]},
        {'left':['ss','controls_joiners','controls_joiners'],'right':[]}],
    'details' : [
        {'sub':['hj'],'target':['hj1A']},
        {'sub':['vj'],'target':['vj1A']}]},
    # Lookup - convert corner insertions to level 1
    {'name' : 'mdcLevel1_corners', 'marks' : 'controls_a',
    'contexts' : [{'left':['ss'],'right':[]}],
    'details' : [
        {'sub':['ts'],'target':['its1A']},
        {'sub':['bs'],'target':['ibs1A']},
        {'sub':['te'],'target':['ite1A']},
        {'sub':['be'],'target':['ibe1A']},
        {'sub':['om'],'target':['om1A']}]},
    # Lookup - merge level 1 embedding controls
    {'name' : 'mdcBE_merge1', 'marks' : 'controls_a',
    'contexts' : [{'left':[],'right':[]}],
    'details' : [{'sub':['ss','se'],'target':['cleanup']}]},
    # Lookup - convert remaining joiners to level 0 joiners
    {'name' : 'mdcLevel0', 'marks' : '',
    'contexts' : [{'left':[],'right':[]}],
    'details' : [
        {'sub':['hj'],'target':['hj0A']},
        {'sub':['vj'],'target':['vj0A']},
        {'sub':['ts'],'target':['its0A']},
        {'sub':['bs'],'target':['ibs0A']},
        {'sub':['te'],'target':['ite0A']},
        {'sub':['be'],'target':['ibe0A']},
        {'sub':['om'],'target':['om0A']}]},
    # DYNAMIC Lookup - populated with r90 values from group data
    {'name' : 'rninety', 'marks' : '*rotate_all',
    'contexts' : [{'left':[],'right':[]}],
    'details' : []},
    # DYNAMIC Lookup - populated with r180 values from group data
    {'name' : 'roneeighty', 'marks' : '*rotate_all',
    'contexts' : [{'left':[],'right':[]}],
    'details' : []},
    # DYNAMIC Lookup - populated with r90 values from group data
    {'name' : 'rtwoseventy', 'marks' : '*rotate_all',
    'contexts' : [{'left':[],'right':[]}],
    'details' : []},
    # DYNAMIC Lookup - populated with tsg values from group data
    {'name' : 'tsg', 'marks' : '',
    'contexts' : [{'left':[],'right':[]}],
    'details' : []},
    # Lookup - accommodate base modifiers
    {'name' : 'Qf_insert', 'marks' : '',
    'contexts' : [{'left':['Qf'],'right':[]}],
    'details' : [{'sub':['modifiers'],'target':['modifiers','Qf']}]},
    # Lookup - accommodate base modifiers
    {'name' : 'Qf_cleanup', 'marks' : '',
    'contexts' : [{'left':[],'right':[]}],
    'details' : [{'sub':['Qf','modifiers'],'target':['modifiers']}]},
    # Lookup - inserts quadat initial before all ETs
    {'name' : 'Qi_insert', 'marks' : '',
    'contexts' : [{'left':[],'right':[]}],
    'details' : [{'sub':['et_all'],'target':['Qi','et_all']}]},
    # # Lookup - tcm start - MOVED UP
    # {'name' : 'tcm_open', 'marks' : '',
    # 'contexts' : [{'left':[],'right':['Qi']}],
    # 'details' : [{'sub':['bracketleft'],'target':['tcbb']}]},
    # # Lookup - tcm end
    # {'name' : 'tcm_open', 'marks' : '',
    # 'contexts' : [{'left':['Qf'],'right':[]}],
    # 'details' : [{'sub':['bracketright'],'target':['tcbe']}]},
    # # DYNAMIC Lookup - populated with tsg values from group data
    # {'name' : 'tcm', 'marks' : '',
    # 'contexts' : [{'left':[],'right':[]}],
    # 'details' : []},
    # Lookup - clean up cleanup glyphs
    {'name' : 'mdcB_cleanup', 'marks' : '',
    'contexts' : [{'left':[],'right':[]}],
    'details' : [
        {'sub':['cleanup','cleanup','Qi'],'target':['Qi']},
        {'sub':['cleanup','Qi'],'target':['Qi']}
    ]},
    # DYNAMIC Lookup - insert GB1 after incomplete controls
    {'name' : 'gb1', 'marks' : '',
    'exceptcontexts' : [
        {'left':[],'right':['Qi']},
        {'left':[],'right':['ss']}
    ],
    'contexts' : [
        {'left':['Qf'],'right':[]},
        {'left':['Qf','controls_b'],'right':[]},
        {'left':['Qf','controls_b','ss'],'right':[]}
    ],
    'details' : []},
    # Lookup - clean up Qf glyphs
    {'name' : 'Qf_cleanup', 'marks' : '',
    'contexts' : [
        {'left':[],'right':['Qi']},
        {'left':[],'right':['ss','Qi']},
        {'left':[],'right':['ss','ss','Qi']}
    ],
    'details' : [{'sub':['Qf','controls_b'],'target':['controls_b']}]},
    # Lookup - clean up Qi glyphs
    {'name' : 'Qi_cleanup', 'marks' : '',
    'contexts' : [{'left':[],'right':[]}],
    'details' : [{'sub':['controls_b','Qi'],'target':['controls_b']}]},
    # Lookup - clean up embedded Qi glyphs
    {'name' : 'Qi_dblss', 'marks' : '',
    'contexts' : [{'left':['controls_b'],'right':['ss','Qi']}],
    'details' : [{'sub':['ss'],'target':['su']}]},
    # Lookup - clean up embedded Qi glyphs
    {'name' : 'Qi_cleanup2', 'marks' : '',
    'contexts' : [
        {'left':['controls_b'],'right':[]},
        {'left':['su'],'right':[]}
    ],
    'details' : [{'sub':['ss','Qi'],'target':['su']}]},
    # # Lookup - Insert level 1 row begin marker for dbl unbalanced begin
    # {'name' : 'Qi_dblss_begin', 'marks' : '',
    # 'contexts' : [{'left':['ss','ss'],'right':[]}],
    # 'details' : [{'sub':['Qi'],'target':['Qi','ub','r1bA']}]},
    # # Lookup - Double to single unbalanced begin
    # {'name' : 'Qi_dblss_cleanup', 'marks' : '',
    # 'contexts' : [{'left':['ss'],'right':['ub']}],
    # 'details' : [{'sub':['ss','Qi'],'target':['Qi']}]},
    # # Lookup - Insert level 1 row begin marker for dbl unbalanced begin
    # {'name' : 'Qi_ss_begin', 'marks' : '',
    # 'contexts' : [{'left':['ss'],'right':[]}],
    # 'details' : [{'sub':['Qi'],'target':['Qi','ub','r0bA']}]},
    # # Lookup - Double to single unbalanced begin
    # {'name' : 'Qi_ss_cleanup', 'marks' : '',
    # 'contexts' : [{'left':[],'right':['ub']}],
    # 'details' : [{'sub':['ss','Qi'],'target':['Qi']}]},
    # Lookup - Insert level 0 row begin marker
    {'name' : 'Qi_rbegin', 'marks' : '',
    'exceptcontexts' : [{'left':[],'right':['ub','r0bA']}],
    'details' : [{'sub':['Qi'],'target':['Qi','r0bA']}]},
    # Lookup - clean up embedded Qi glyphs
    {'name' : 'Qi_cleanup3', 'marks' : '',
    'contexts' : [{'left':['ss'],'right':[]}],
    'details' : [{'sub':['Qi'],'target':['Qi','ub']}]},
    # Lookup - clean up embedded Qi glyphs
    {'name' : 'Qi_cleanup4', 'marks' : '',
    'contexts' : [{'left':[],'right':[]}],
    'details' : [{'sub':['ss','Qi'],'target':['Qi']}]},
    # Lookup - Insert level 0 row end marker
    {'name' : 'Qf_rend', 'marks' : '',
    'contexts' : [{'left':[],'right':[]}],
    'details' : [{'sub':['Qf'],'target':['r0eA','Qf']}]},
    # Lookup - level 2 row begin and end
    {'name' : 'r2', 'marks' : '',
    'contexts' : [{'left':[],'right':['et_all']}],
    'details' : [
        {'sub':['vj2A'],'target':['r2eA','vj2A','r2bA']},
        {'sub':['hj2A'],'target':['r2eA','hj2A','r2bA']},
        {'sub':['corners1a'],'target':['corners1a','r2bA']},
    ]},
    # Lookup - level 2 row end before corner after 2 begin
    {'name' : 'r2e_corner', 'marks' : 'parens',
    'contexts' : [{'left':['r2bA'],'right':[]}],
    'details' : [{'sub':['corners1a'],'target':['r2eA','corners1a']},]},
    # Lookup - level 1 row begin and end
    # moved above r2b_corner to fix over inclusion of level 2, e.g., F20 bs ss Z11 hj ss X1 vj D21 se vj N35 se
    {'name' : 'r1', 'marks' : '',
    'contexts' : [{'left':[],'right':['et_all']}],
    'details' : [
        {'sub':['vj1A'],'target':['r1eA','vj1A','r1bA']},
        {'sub':['hj1A'],'target':['r1eA','hj1A','r1bA']},
        {'sub':['corners0a'],'target':['corners0a','r1bA']},
    ]},
    # Lookup - level 1 row begin
    {'name' : 'r1_su', 'marks' : '',
    'contexts' : [
        {'left':['corners0a'],'right':['et_all']},
        {'left':['corners0a'],'right':['su','et_all']}
    ],
    'details' : [
        {'sub':['su'],'target':['su','r1bA']},
    ]},
    # Lookup - level 2 row begin
    {'name' : 'r2_su', 'marks' : '',
    'contexts' : [
        {'left':['corners1a'],'right':['et_all']},
        {'left':['corners1a','su','r1bA'],'right':['et_all']}
    ],
    'details' : [
        {'sub':['su'],'target':['su','r2bA']},
    ]},
    # Lookup - level 2 row begin afer corner before 2 end
    {'name' : 'r2b_corner', 'marks' : '*parensub',
    'contexts' : [{'left':[],'right':['r2eA']}],
    'details' : [{'sub':['corners0a'],'target':['corners0a','r1bA','r2bA']},]},
    # Lookup - level 2 row end before corner 1 between two r2 begins
    {'name' : 'r2_om2', 'marks' : 'parens',
    'contexts' : [{'left':['r2bA'],'right':['r2bA']}],
    'details' : [{'sub':['corners1a'],'target':['r2eA','corners1a']},]},
    # Lookup - level 1 row end before corner 1 between two r2 begins
    {'name' : 'r1_om1', 'marks' : 'parens',
    'contexts' : [{'left':['r1bA'],'right':['r1bA']}],
    'details' : [{'sub':['corners0a'],'target':['r1eA','corners0a']},]},
    # Lookup - level 1 row begin afer corner before 1 end
    {'name' : 'corner_swapandsize', 'marks' : '',
    'exceptcontexts' : [{'left':['Qf'],'right':[]}],
    'details' : [
        {'sub':['its0A'],'target':['its0B','it00a']},
        {'sub':['ibs0A'],'target':['ibs0B','it00a']},
        {'sub':['ite0A'],'target':['ite0B','it00a']},
        {'sub':['ibe0A'],'target':['ibe0B','it00a']},
        {'sub':['om0A'], 'target':['om0B' ,'it00a']},
        {'sub':['its1A'],'target':['its1B','it00a']},
        {'sub':['ibs1A'],'target':['ibs1B','it00a']},
        {'sub':['ite1A'],'target':['ite1B','it00a']},
        {'sub':['ibe1A'],'target':['ibe1B','it00a']},
        {'sub':['om1A'], 'target':['om1B' ,'it00a']},
    ]},
    # Lookup - unbalanced embedding 
    {'name' : 'unbal-embedding', 'marks' : '',
    'contexts' : [{'left':[],'right':['su']}],
    'details' : [
        {'sub':['vj0A'],'target':['r0eA','vj0A','r0bA','r1bA']},
        {'sub':['hj0A'],'target':['r0eA','hj0A','r0bA','r1bA']},
        {'sub':['vj1A'],'target':['r1eA','vj1A','r1bA','r2bA']},
        {'sub':['hj1A'],'target':['r1eA','hj1A','r1bA','r2bA']}
    ]},
    # Lookup - insert level 0 row boundaries around joiners
    {'name' : 'r0', 'marks' : '',
    'contexts' : [{'left':[],'right':['et_all']}],
    'details' : [
        {'sub':['vj0A'],'target':['r0eA','vj0A','r0bA']},
        {'sub':['hj0A'],'target':['r0eA','hj0A','r0bA']},
    ]},
    # Lookup - insert level 1 row begin after unbalanced corner
    {'name' : 'unbal-corner', 'marks' : '',
    'contexts' : [
        {'left':['corners0b','it00a'],'right':['r1bA']},
        {'left':['corners1b','it00a'],'right':['r2bA']},
    ],
    'details' : [{'sub':['su'],'target':['ub']}]},
    # # Lookup - insert level 1 row begin after unbalanced corner
    # {'name' : 'unbal-corner1', 'marks' : '',
    # 'contexts' : [{'left':['corners0b','it00a'],'right':[]}],
    # 'details' : [{'sub':['su'],'target':['ub','r1bA']}]},
    # # Lookup - insert level 1 row begin after unbalanced corner
    # {'name' : 'unbal-corner2', 'marks' : '',
    # 'contexts' : [{'left':['corners1b','it00a'],'right':[]}],
    # 'details' : [{'sub':['su'],'target':['ub','r2bA']}]},
    # Lookup - insert level 1 row begin after unbalanced corner
    {'name' : 'unbal-dblcorner', 'marks' : '',
    'contexts' : [{'left':['ub','r1bA'],'right':[]}],
    'details' : [{'sub':['su'],'target':['ub','r2bA']}]},
    # Lookup - insert level 1 row begin before level 2 begin
    {'name' : 'r2begin1', 'marks' : 'parens',
    'contexts' : [{'left':[],'right':['r2bA']}],
    'details' : [{'sub':['r0bA'],'target':['r0bA','r1bA']}]},
    # Lookup - insert up-level row ends after level 2 begin
    {'name' : 'r2begin2', 'marks' : 'parens',
    'contexts' : [{'left':['r2bA'],'right':[]}],
    'details' : [
        {'sub':['r0eA'],'target':['r2eA','r1eA','r0eA']},
        {'sub':['r1eA'],'target':['r2eA','r1eA']},
    ]},
    # Lookup - insert up-level row begins before level 2 end 
    {'name' : 'r2end', 'marks' : 'parens',
    'contexts' : [{'left':[],'right':['r2eA']}],
    'details' : [
        {'sub':['r0bA'],'target':['r0bA','r1bA','r2bA']},
        {'sub':['r1bA'],'target':['r1bA','r2bA']}
    ]},
    # Lookup - insert up-level row end after level 1 begin
    {'name' : 'r1begin', 'marks' : 'parens',
    'contexts' : [{'left':['r1bA'],'right':[]}],
    'details' : [{'sub':['r0eA'],'target':['r1eA','r0eA']}]},
    # Lookup - insert up-level row begin before level 1 end 
    {'name' : 'r1end', 'marks' : 'parens',
    'contexts' : [
        {'left':[],'right':['r1eA']},
        {'left':[],'right':['c1eA']}
    ],
    'details' : [{'sub':['r0bA'],'target':['r0bA','r1bA']}]},
    # Lookup - insert level 1 row end before level 0 col end 
    {'name' : 'r1end', 'marks' : 'parens',
    'contexts' : [{'left':['r1bA'],'right':[]}],
    'details' : [{'sub':['c0eA'],'target':['r1eA','c0eA']}]},
    # Lookup - insert level 1 row begin after level 0 col begin 
    {'name' : 'r1end', 'marks' : 'parens',
    'contexts' : [
        {'left':[],'right':['r1eA']},
        {'left':[],'right':['r2bA']}
    ],
    'details' : [{'sub':['c0bA'],'target':['c0bA','r1bA']}]},
    # Lookup - insert column begin and end 
    {'name' : 'c012', 'marks' : '',
    'contexts' : [{'left':[],'right':[]}],
    'details' : [
        {'sub':['r0bA'],'target':['r0bA','c0bA']},
        {'sub':['r1bA'],'target':['r1bA','c1bA']},
        {'sub':['r2bA'],'target':['r2bA','c2bA']},
        {'sub':['r0eA'],'target':['c0eA','r0eA']},
        {'sub':['r1eA'],'target':['c1eA','r1eA']},
        {'sub':['r2eA'],'target':['c2eA','r2eA']},
    ]},
    # Lookup - row 0 begin cleanup 
    {'name' : 'r0b_cleanup', 'marks' : '',
    'contexts' : [{'left':['hj0A'],'right':[]}],
    'details' : [{'sub':['r0bA','c0bA'],'target':['c0bA']}]},
    # Lookup - row 0 end cleanup 
    {'name' : 'r0e_cleanup', 'marks' : '',
    'contexts' : [{'left':[],'right':['hj0A']}],
    'details' : [{'sub':['c0eA','r0eA'],'target':['c0eA']}]},
    # Lookup - row 1 begin cleanup 
    {'name' : 'r1b_cleanup', 'marks' : '',
    'contexts' : [{'left':['hj1A'],'right':[]}],
    'details' : [{'sub':['r1bA','c1bA'],'target':['c1bA']}]},
    # Lookup - row 1 end cleanup 
    {'name' : 'r1e_cleanup', 'marks' : '',
    'contexts' : [{'left':[],'right':['hj1A']}],
    'details' : [{'sub':['c1eA','r1eA'],'target':['c1eA']}]},
    # Lookup - row 2 begin cleanup 
    {'name' : 'r2b_cleanup', 'marks' : '',
    'contexts' : [{'left':['hj2A'],'right':[]}],
    'details' : [{'sub':['r2bA','c2bA'],'target':['c2bA']}]},
    # Lookup - row 2 end cleanup 
    {'name' : 'r2e_cleanup', 'marks' : '',
    'contexts' : [{'left':[],'right':['hj2A']}],
    'details' : [{'sub':['c2eA','r2eA'],'target':['c2eA']}]},
    # Lookup - insert level 2 min default size
    {'name' : 'default_size_2', 'marks' : '',
    'contexts' : [
        {'left':[],'right':['r2bA']},
        {'left':[],'right':['ub','r2bA']}
    ],
    'details' : [{'sub':['c1bA'],'target':['c1bA','mt22']}]},
    # Lookup - insert level 1 min default size 
    {'name' : 'default_size_level1', 'marks' : '',
    'contexts' : [{'left':[],'right':['r1bA']}],
    'details' : [{'sub':['c0bA'],'target':['c0bA','mt43']}]},
    # Lookup - move unbalanced ss (i.e., su) to mark mt43,mt22
    {'name' : 'insertunbalancedtoken', 'marks' : 'rowmaxes',
    'contexts' : [{'left':[],'right':['su']}],
    'details' : [
        {'sub':['mt43'],'target':['mt43','ub']},
        {'sub':['mt22'],'target':['mt22','ub']}
    ]},
    # Lookup - clean up unbalanced su
    {'name' : 'cleanupunbalanced', 'marks' : '',
    'details' : [
        {'sub':['c1bA','su'],'target':['c1bA']},
        {'sub':['c2bA','su'],'target':['c2bA']}
    ]},
    # Lookup - set min default size to reducible default size
    {'name' : 'default_size_level1', 'marks' : 'rowmaxes',
    'exceptcontexts' : [{'left':[],'right':['mt22']}],
    'details' : [{'sub':['mt43'],'target':['et66']}]},
    # Lookup - isolated dbl segment 1
    {'name' : 'isolated_dblss1', 'marks' : '',
    'contexts' : [{'left':[],'right':['ss']}],
    'details' : [{'sub':['ss'],'target':['Qi','ub','r0bA','c0bA']}]},
    # Lookup - isolated dbl segment 2
    # {'name' : 'isolated_dblss2', 'marks' : '',
    # 'contexts' : [{'left':['Qi','ub','r0bA','c0bA'],'right':[]}],
    # 'details' : [{'sub':['ss'],'target':['ub','r1bA','c1bA','et66','tsh666564636261565554535251464544434241363534333231262524232221161514131211','GB1','c1eA','r1eA','c0eA','r0eA','Qf']}]},
    # Lookup - isolated segment start
    # {'name' : 'isolated_ss', 'marks' : '',
    # 'details' : [{'sub':['ss'],'target':['Qi','ub','r0bA','c0bA','et66','tsh666564636261565554535251464544434241363534333231262524232221161514131211','GB1','c0eA','r0eA','Qf']}]},
]