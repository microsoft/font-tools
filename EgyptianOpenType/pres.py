#!/usr/bin/python
# egyptian opentype generator data

pres = [
    # Lookup - tcm start
    # TODO: Move these substitutions to the Default language
    # {'name' : 'tcm_open', 'marks' : '',
    # 'contexts' : [{'left':[],'right':['characters_latn']}],
    # 'details' : [
    #     {'sub':['uni27E8'],'target':['uni27E8.latn']},
    #     {'sub':['braceleft'],'target':['braceleft.latn']},
    #     {'sub':['tophalfbracketL'],'target':['tophalfbracketL.latn']},
    #     {'sub':['uni27EE'],'target':['uni27EE.latn']},
    #     {'sub':['uni27E6'],'target':['uni27E6.latn']},
    #     {'sub':['bar'],'target':['bar.latn']},
    # ]},
    # Lookup - tcm end
    # {'name' : 'tcm_open', 'marks' : '',
    # 'contexts' : [{'left':['characters_latn'],'right':[]}],
    # 'details' : [
    #     {'sub':['uni27E9'],'target':['uni27E9.latn']},
    #     {'sub':['braceright'],'target':['braceright.latn']},
    #     {'sub':['tophalfbracketR'],'target':['tophalfbracketR.latn']},
    #     {'sub':['uni27EF'],'target':['uni27EF.latn']},
    #     {'sub':['uni27E7'],'target':['tcuni27E7re.latn']},
    #     {'sub':['bar'],'target':['bar.latn']},
    # ]},
    # # Lookup - quarter shades
    # {'name' : 'quarterShades', 'marks' : '',
    # 'contexts' : [{'left':[],'right':[]}],
    # 'details' : [
    #     {'sub':['sts','sbs','ste'],'target':['dq123']},
    #     {'sub':['sts','sbs','sbe'],'target':['dq124']},
    #     {'sub':['sts','ste','sbe'],'target':['dq134']},
    #     {'sub':['sbs','ste','sbe'],'target':['dq234']},
    #     {'sub':['sts','sbs'],'target':['dq12']},
    #     {'sub':['sts','ste'],'target':['dq13']},
    #     {'sub':['sts','sbe'],'target':['dq14']},
    #     {'sub':['sbs','ste'],'target':['dq23']},
    #     {'sub':['sbs','sbe'],'target':['dq24']},
    #     {'sub':['ste','sbe'],'target':['dq34']},
    #     {'sub':['sts'],'target':['dq1']},
    #     {'sub':['sbs'],'target':['dq2']},
    #     {'sub':['ste'],'target':['dq3']},
    #     {'sub':['sbe'],'target':['dq4']},
    # ]},

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
    # Lookup - convert embedded tcbb to level 2
    {'name' : 'Level2_tcb', 'marks' : '*tcb12',
    'contexts' : [
        {'left':['ss','ss'],'right':['se','se']},
        {'left':['ss','corners'],'right':['se']},
        {'left':['ss','om'],'right':['se']},
        {'left':['ss','ti'],'right':['se']},
        {'left':['ss','mi'],'right':['se']},
        {'left':['ss','bi'],'right':['se']},
        ],
    'details' : [{'sub':['tcbb'],'target':['tcbb2']}]},
    # Lookup - convert embedded tcbe to level 2
    {'name' : 'Level2_tce', 'marks' : '*tce12',
    'contexts' : [{'left':['ss','ss'],'right':['se','se']}],
    'details' : [{'sub':['tcbe'],'target':['tcbe2']}]},
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
        {'sub':['om'],'target':['om1A']},
        {'sub':['ti'],'target':['ti1A']},
        {'sub':['mi'],'target':['mi1A']},
        {'sub':['bi'],'target':['bi1A']}]},
    # Lookup - convert embedded tcbb to level 1
    {'name' : 'Level1_tcb', 'marks' : '*tcb12',
    'contexts' : [{'left':['ss'],'right':['se']}],
    'details' : [{'sub':['tcbb'],'target':['tcbb1']}]},
    # Lookup - convert embedded tcbe to level 1
    {'name' : 'Level1_tce', 'marks' : '*tce12',
    'contexts' : [{'left':['ss'],'right':['se']}],
    'details' : [{'sub':['tcbe'],'target':['tcbe1']}]},
    # Lookup - merge level 1 embedding controls
    {'name' : 'mdcBE_merge1', 'marks' : 'controls_a',
    'contexts' : [{'left':[],'right':[]}],
    'details' : [{'sub':['ss','se'],'target':['cleanup']}]},
    # Lookup - convert remaining joiners and tcbs to level 0 joiners
    {'name' : 'mdcLevel0', 'marks' : '',
    'contexts' : [{'left':[],'right':[]}],
    'details' : [
        {'sub':['hj'],'target':['hj0A']},
        {'sub':['vj'],'target':['vj0A']},
        {'sub':['ts'],'target':['its0A']},
        {'sub':['bs'],'target':['ibs0A']},
        {'sub':['te'],'target':['ite0A']},
        {'sub':['be'],'target':['ibe0A']},
        {'sub':['om'],'target':['om0A']},
        {'sub':['ti'],'target':['ti0A']},
        {'sub':['mi'],'target':['mi0A']},
        {'sub':['bi'],'target':['bi0A']}]},
    # Lookup - corner0 tcbb1
    {'name' : 'corner0_tcbb1', 'marks' : '',
    'contexts' : [{'left':['corners0a'],'right':[]}],
    'details' : [{'sub':['tcbb'],'target':['tcbb1']}]},
    # Lookup - corner1 tcbb2
    {'name' : 'corner1_tcbb2', 'marks' : '',
    'contexts' : [{'left':['corners1a'],'right':[]}],
    'details' : [{'sub':['tcbb'],'target':['tcbb2']}]},
    # Lookup - corner tcbe1
    {'name' : 'corner_tcbe1', 'marks' : '*tcb01',
    'contexts' : [{'left':['tcbb1'],'right':[]}],
    'details' : [{'sub':['tcbe'],'target':['tcbe1']}]},
    # Lookup - corner tcbe2
    {'name' : 'corner_tcbe2', 'marks' : '*tcb02',
    'contexts' : [{'left':['tcbb2'],'right':[]}],
    'details' : [{'sub':['tcbe'],'target':['tcbe2']}]},
    # Lookup - tcb0
    {'name' : 'tcb0', 'marks' : '',
    'contexts' : [{'left':[],'right':[]}],
    'details' : [
        {'sub':['tcbb'],'target':['tcbb0']},
        {'sub':['tcbe'],'target':['tcbe0']}]},
    # # DYNAMIC Lookup - populated with r90 values from group data
    # {'name' : 'rninety', 'marks' : '*rotate_all',
    # 'contexts' : [{'left':[],'right':[]}],
    # 'details' : []},
    # # DYNAMIC Lookup - populated with r180 values from group data
    # {'name' : 'roneeighty', 'marks' : '*rotate_all',
    # 'contexts' : [{'left':[],'right':[]}],
    # 'details' : []},
    # # DYNAMIC Lookup - populated with r90 values from group data
    # {'name' : 'rtwoseventy', 'marks' : '*rotate_all',
    # 'contexts' : [{'left':[],'right':[]}],
    # 'details' : []},
    # DYNAMIC Lookup - populated with tsg values from group data
    {'name' : 'tsg', 'marks' : '',
    'contexts' : [{'left':[],'right':[]}],
    'details' : []},
    # Lookup - expand bases with insertions TODO: auto expand based on glyph name trigger
    {'name' : 'expansion', 'marks' : '',
    'contexts' : [{'left':[],'right':['tsh665655544544332211','D32','Qf','bi0A']}],
    'details' : [{'sub':['et56'],'target':['et66']}]},
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
    'contexts' : [],
    'exceptcontexts' : [
        {'left':['tcbb_all'],'right':[]}],
    'details' : [
        {'sub':['et_all'],'target':['Qi','et_all']},
        {'sub':['tcbb_all'],'target':['Qi','tcbb_all']},
        ]},
    # Lookup - clean up cleanup glyphs
    {'name' : 'mdcB_cleanup', 'marks' : '',
    'contexts' : [{'left':[],'right':[]}],
    'details' : [
        {'sub':['cleanup','cleanup','Qi'],'target':['Qi']},
        {'sub':['cleanup','Qi'],'target':['Qi']},
    ]},
    # DYNAMIC Lookup - insert GB1 after tbb
    {'name' : 'tbb_gb1', 'marks' : '',
    'exceptcontexts' : [
        {'left':[],'right':['et_all']},
    ],
    'contexts' : [{'left':['Qi'],'right':[]}],
    'details' : []},
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
        {'left':[],'right':['ss','ss','Qi']},
    ],
    'details' : [{'sub':['Qf','controls_b'],'target':['controls_b']}]},
    # Lookup - clean up Qi glyphs
    {'name' : 'Qi_cleanup', 'marks' : '',
    'contexts' : [{'left':[],'right':[]}],
    'details' : [{'sub':['controls_b','Qi'],'target':['controls_b']}]},
    # Lookup - clean up Qi glyphs
    {'name' : 'Qi_cleanup_tcb', 'marks' : '',
    'contexts' : [{'left':['controls_b'],'right':[]}],
    'details' : [{'sub':['tcbb_all','Qi'],'target':['tcbb_all']}]},
    # Lookup - clean up embedded Qi glyphs
    {'name' : 'Qi_dblss', 'marks' : '',
    'contexts' : [{'left':['controls_b'],'right':['ss','Qi']}],
    'details' : [{'sub':['ss'],'target':['su']}]},
    # Lookup - clean up embedded Qi glyphs
    {'name' : 'Qi_cleanup_su', 'marks' : '',
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
    'contexts' : [{'left':[],'right':['et_all']},
        {'left':[],'right':['tcbb_all','et_all']},
    ],
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
    'contexts' : [{'left':[],'right':['et_all']},
        {'left':[],'right':['tcbb_all','et_all']},
    ],
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
    # Lookup - level 2 row begin after corner before 2 end
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
    # Lookup - level 1 row begin after corner before 1 end
    {'name' : 'corner_swapandsize', 'marks' : '',
    'exceptcontexts' : [{'left':['Qf'],'right':[]}],
    'details' : [
        {'sub':['its0A'],'target':['its0B']},
        {'sub':['ibs0A'],'target':['ibs0B']},
        {'sub':['ite0A'],'target':['ite0B']},
        {'sub':['ibe0A'],'target':['ibe0B']},
        {'sub':['om0A'], 'target':['om0B' ]},
        {'sub':['ti0A'], 'target':['ti0B' ]},
        {'sub':['mi0A'], 'target':['mi0B' ]},
        {'sub':['bi0A'], 'target':['bi0B' ]},
        {'sub':['its1A'],'target':['its1B']},
        {'sub':['ibs1A'],'target':['ibs1B']},
        {'sub':['ite1A'],'target':['ite1B']},
        {'sub':['ibe1A'],'target':['ibe1B']},
        {'sub':['om1A'], 'target':['om1B' ]},
        {'sub':['ti1A'], 'target':['ti1B' ]},
        {'sub':['mi1A'], 'target':['mi1B' ]},
        {'sub':['bi1A'], 'target':['bi1B' ]},
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
    'contexts' : [
        {'left':[],'right':['et_all']},
        {'left':[],'right':['tcbb_all','et_all']},
        ],
    'details' : [
        {'sub':['vj0A'],'target':['r0eA','vj0A','r0bA']},
        {'sub':['hj0A'],'target':['r0eA','hj0A','r0bA']},
    ]},
    # Lookup - insert level 1 row begin after unbalanced corner
    {'name' : 'unbal-corner', 'marks' : '',
    'contexts' : [
        {'left':['corners0b'],'right':['r1bA']},
        {'left':['corners1b'],'right':['r2bA']}],
    'details' : [{'sub':['su'],'target':['ub']}]},
    # # Lookup - insert level 1 row begin after unbalanced corner
    # {'name' : 'unbal-corner1', 'marks' : '',
    # 'contexts' : [{'left':['corners0b'],'right':[]}],
    # 'details' : [{'sub':['su'],'target':['ub','r1bA']}]},
    # # Lookup - insert level 1 row begin after unbalanced corner
    # {'name' : 'unbal-corner2', 'marks' : '',
    # 'contexts' : [{'left':['corners1b'],'right':[]}],
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
    {'name' : 'r2begin2', 'marks' : '*parenstcbe1', #needs to block tcbe1
    'contexts' : [{'left':['r2bA'],'right':[]}],
    'details' : [
        {'sub':['r0eA'],'target':['r2eA','r1eA','r0eA']},
        {'sub':['r1eA'],'target':['r2eA','r1eA']},
    ]},
    # Lookup - insert up-level row end after level 1 begin
    {'name' : 'r2begin3', 'marks' : '*parenstcbe1',
    'contexts' : [{'left':['r2bA'],'right':['r0eA']}],
    'details' : [{'sub':['tcbe1'],'target':['r2eA','tcbe1','r1eA']}]},
    # Lookup - insert up-level row end after level 2 begin
    {'name' : 'r2begin_tcbe0', 'marks' : '*parenstcbe0',
    'contexts' : [{'left':['r2bA'],'right':['r0eA']}],
    'details' : [{'sub':['tcbe0'],'target':['r2eA','r1eA','tcbe0']}]},
    # Lookup - insert up-level row end after level 2 begin
    {'name' : 'r2begin_tcbe1', 'marks' : '*parenstcbe1',
    'contexts' : [{'left':['r2bA'],'right':['r0eA']}],
    'details' : [{'sub':['tcbe1'],'target':['r2eA','tcbe1']}]},
    # Lookup - insert up-level row begins before level 2 end 
    {'name' : 'r2end', 'marks' : 'parens',
    'contexts' : [{'left':[],'right':['r2eA']}],
    'details' : [
        {'sub':['r0bA'],'target':['r0bA','r1bA','r2bA']},
        {'sub':['r1bA'],'target':['r1bA','r2bA']}
    ]},
    # Lookup - insert up-level row end after level 1 begin
    {'name' : 'r1begin', 'marks' : '*parenstcbe0', #needs to block tcbe0
    'contexts' : [{'left':['r1bA'],'right':[]}],
    'details' : [{'sub':['r0eA'],'target':['r1eA','r0eA']}]},
    # Lookup - insert up-level row end after level 1 begin
    {'name' : 'r1begin_tcbe0', 'marks' : '*parenstcbe0',
    'contexts' : [{'left':['r1bA'],'right':['r0eA']}],
    'details' : [{'sub':['tcbe0'],'target':['r1eA','tcbe0']}]},
    # Lookup - insert up-level row begin before level 1 end 
    {'name' : 'r1end_tcbb0', 'marks' : '*parenstcbb0',
    'contexts' : [
        {'left':['r0bA'],'right':['r1eA']},
        {'left':['r0bA'],'right':['c1eA']}
    ],
    'details' : [{'sub':['tcbb0'],'target':['tcbb0','r1bA']}]},
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
    'contexts' : [
        {'left':[],'right':['r1bA']},
    ],
    'details' : [{'sub':['c0bA'],'target':['c0bA','mt43']}]},
    # Lookup - insert level 1 min default size tcbb 
    {'name' : 'default_size_level1_tcb', 'marks' : '',
    'contexts' : [
        {'left':['c0bA'],'right':['r1bA']},
    ],
    'details' : [{'sub':['tcbb0'],'target':['tcbb0','mt43']}]},
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
    # Lookup - revert unbalanced tbbe
    {'name' : 'visibleunbalancedtbbe', 'marks' : '',
    'exceptcontexts' : [
        {'left':[],'right':['c0eA']}],
    'details' : [
        {'sub':['tcbe0'],'target':['tcbe']}
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