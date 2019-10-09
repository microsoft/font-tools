#!/usr/bin/python
# egyptian opentype generator data

pres = [
    # Lookup 1 - convert embedded joiners to level 2 joiners
    {'name' : 'mdcLevel2_joiners', 'marks' : 'controls_a',
    'contexts' : [
        {'left':['ss','ss'],'right':[]},
        {'left':['ss','controls_joiners','ss'],'right':[]},
        {'left':['ss','controls_joiners','controls_joiners','ss'],'right':[]},
        {'left':['ss','controls_joiners','controls_joiners','controls_joiners','ss'],'right':[]}],
    'details' : [
        {'sub':['hj'],'target':['hj2A']},
        {'sub':['vj'],'target':['vj2A']}]},
    # Lookup 2 - merge level 2 embedding controls
    {'name' : 'mdcBE_merge2', 'marks' : 'controls_a',
    'contexts' : [{'left':[],'right':[]}],
    'details' : [
        {'sub':['ss','se'],'target':['cleanup']}]},
    # Lookup 3 - convert embedded joiners to level 1 joiners
    {'name' : 'mdcLevel1_joiners', 'marks' : 'controls_a',
    'contexts' : [
        {'left':['ss'],'right':[]},
        {'left':['ss','controls_joiners'],'right':[]},
        {'left':['ss','controls_joiners','controls_joiners'],'right':[]}],
    'details' : [
        {'sub':['hj'],'target':['hj1A']},
        {'sub':['vj'],'target':['vj1A']}]},
    # Lookup 4 - convert corner insertions to level 1
    {'name' : 'mdcLevel1_corners', 'marks' : 'controls_a',
    'contexts' : [{'left':['ss'],'right':[]}],
    'details' : [
        {'sub':['ts'],'target':['its1A']},
        {'sub':['bs'],'target':['ibs1A']},
        {'sub':['te'],'target':['ite1A']},
        {'sub':['be'],'target':['ibe1A']},
        {'sub':['om'],'target':['om1A']}]},
    # Lookup 5 - merge level 1 embedding controls
    {'name' : 'mdcBE_merge1', 'marks' : 'controls_a',
    'contexts' : [{'left':[],'right':[]}],
    'details' : [{'sub':['ss','se'],'target':['cleanup']}]},
    # Lookup 6 - convert remaining joiners to level 0 joiners
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
    # Lookup 6a - swap bs for cobras
    {'name' : 'mdcBE_merge1', 'marks' : '',
    'contexts' : [{'left':['cobras'],'right':[]}],
    'details' : [
        {'sub':['ibs0A'],'target':['cbr0A']},
        {'sub':['ibs1A'],'target':['cbr1A']}]},
    # DYNAMIC Lookup 7 - populated with tsg values from group data
    {'name' : 'tsg', 'marks' : '',
    'contexts' : [{'left':[],'right':[]}],
    'details' : []},
    # Lookup 8 - accommodate variation selectors
    {'name' : 'Qf_insert', 'marks' : '',
    'contexts' : [{'left':['Qf'],'right':[]}],
    'details' : [{'sub':['vss'],'target':['vss','Qf']}]},
    # Lookup 8 - accommodate variation selectors
    {'name' : 'Qf_cleanup', 'marks' : '',
    'contexts' : [{'left':[],'right':[]}],
    'details' : [{'sub':['Qf','vss'],'target':['vss']}]},
    # Lookup 8 - inserts quadat initial before all ETs
    {'name' : 'Qi_insert', 'marks' : '',
    'contexts' : [{'left':[],'right':[]}],
    'details' : [{'sub':['et_all'],'target':['Qi','et_all']}]},
    # Lookup 9 - clean up cleanup glyphs
    {'name' : 'mdcB_cleanup', 'marks' : '',
    'contexts' : [{'left':[],'right':[]}],
    'details' : [
        {'sub':['cleanup','cleanup','Qi'],'target':['Qi']},
        {'sub':['cleanup','Qi'],'target':['Qi']}
    ]},
    # DYNAMIC Lookup 9b - insert GB1 after incomplete controls
    {'name' : 'gb1', 'marks' : '',
    'contexts' : [
        {'left':['Qf'],'right':[]}
    ],
    'exceptcontexts' : [
        {'left':[],'right':['Qi']},
        {'left':[],'right':['ss']},
    ],
    'details' : []},
    # Lookup 10 - clean up Qf glyphs
    {'name' : 'Qf_cleanup', 'marks' : '',
    'contexts' : [
        {'left':[],'right':['Qi']},
        {'left':[],'right':['ss','Qi']}
    ],
    'details' : [{'sub':['Qf','controls_b'],'target':['controls_b']}]},
    # Lookup 11 - clean up Qi glyphs
    {'name' : 'Qi_cleanup', 'marks' : '',
    'contexts' : [{'left':[],'right':[]}],
    'details' : [{'sub':['controls_b','Qi'],'target':['controls_b']}]},
    # Lookup 12 - clean up embedded Qi glyphs
    {'name' : 'Qi_cleanup2', 'marks' : '',
    'contexts' : [{'left':['controls_b'],'right':[]}],
    'details' : [{'sub':['ss','Qi'],'target':['su']}]},
    # Lookup 13 - Insert level 0 row begin marker
    {'name' : 'Qi_rbegin', 'marks' : '',
    'contexts' : [{'left':[],'right':[]}],
    'details' : [{'sub':['Qi'],'target':['Qi','r0bA']}]},
    # Lookup 13a - clean up embedded Qi glyphs
    {'name' : 'Qi_cleanup3', 'marks' : '',
    'contexts' : [{'left':['ss'],'right':[]}],
    'details' : [{'sub':['Qi'],'target':['Qi','ub']}]},
    # Lookup 13b - clean up embedded Qi glyphs
    {'name' : 'Qi_cleanup4', 'marks' : '',
    'contexts' : [{'left':[],'right':[]}],
    'details' : [{'sub':['ss','Qi'],'target':['Qi']}]},
    # Lookup 14 - Insert level 0 row end marker
    {'name' : 'Qf_rend', 'marks' : '',
    'contexts' : [{'left':[],'right':[]}],
    'details' : [{'sub':['Qf'],'target':['r0eA','Qf']}]},
    # Lookup 15 - level 2 row begin and end
    {'name' : 'r2', 'marks' : '',
    'contexts' : [{'left':[],'right':['et_all']}],
    'details' : [
        {'sub':['vj2A'],'target':['r2eA','vj2A','r2bA']},
        {'sub':['hj2A'],'target':['r2eA','hj2A','r2bA']},
        {'sub':['corners1a'],'target':['corners1a','r2bA']},
    ]},
    # Lookup 16 - level 2 row end before corner after 2 begin
    {'name' : 'r2e_corner', 'marks' : 'parens',
    'contexts' : [{'left':['r2bA'],'right':[]}],
    'details' : [{'sub':['corners1a'],'target':['r2eA','corners1a']},]},
    # Lookup 18 - level 1 row begin and end
    # moved above r2b_corner to fix over inclusion of level 2, e.g., F20 bs ss Z11 hj ss X1 vj D21 se vj N35 se
    {'name' : 'r1', 'marks' : '',
    'contexts' : [{'left':[],'right':['et_all']}],
    'details' : [
        {'sub':['vj1A'],'target':['r1eA','vj1A','r1bA']},
        {'sub':['hj1A'],'target':['r1eA','hj1A','r1bA']},
        {'sub':['corners0a'],'target':['corners0a','r1bA']},
    ]},
    # Lookup 17 - level 2 row begin afer corner before 2 end
    {'name' : 'r2b_corner', 'marks' : 'parens',
    'contexts' : [{'left':[],'right':['r2eA']}],
    'details' : [{'sub':['corners0a'],'target':['corners0a','r1bA','r2bA']},]},
    # Lookup 19 - level 2 row end before corner 1 between two r2 begins
    {'name' : 'r2_om2', 'marks' : 'parens',
    'contexts' : [{'left':['r2bA'],'right':['r2bA']}],
    'details' : [{'sub':['corners1a'],'target':['r2eA','corners1a']},]},
    # Lookup 20 - level 1 row end before corner 1 between two r2 begins
    {'name' : 'r1_om1', 'marks' : 'parens',
    'contexts' : [{'left':['r1bA'],'right':['r1bA']}],
    'details' : [{'sub':['corners0a'],'target':['r1eA','corners0a']},]},
    # Lookup 22 - level 1 row begin afer corner before 1 end
    {'name' : 'corner_swapandsize', 'marks' : '',
    'exceptcontexts' : [{'left':['Qf'],'right':[]}],
    'details' : [
        {'sub':['its0A'],'target':['its0B','it22a']},
        {'sub':['ibs0A'],'target':['ibs0B','it22a']},
        {'sub':['cbr0A'],'target':['cbr0B','it43a']},
        {'sub':['ite0A'],'target':['ite0B','it22a']},
        {'sub':['ibe0A'],'target':['ibe0B','it22a']},
        {'sub':['om0A'], 'target':['om0B' ,'it66a']},
        {'sub':['its1A'],'target':['its1B','it11a']},
        {'sub':['ibs1A'],'target':['ibs1B','it11a']},
        {'sub':['cbr1A'],'target':['cbr1B','it21a']},
        {'sub':['ite1A'],'target':['ite1B','it11a']},
        {'sub':['ibe1A'],'target':['ibe1B','it11a']},
        {'sub':['om1A'], 'target':['om1B' ,'it44a']},
    ]},
    # Lookup 23 - unbalanced embedding 
    {'name' : 'unbal-embedding', 'marks' : '',
    'contexts' : [{'left':[],'right':['su']}],
    'details' : [
        {'sub':['vj0A'],'target':['r0eA','vj0A','r0bA','r1bA']},
        {'sub':['hj0A'],'target':['r0eA','hj0A','r0bA','r1bA']},
        {'sub':['vj1A'],'target':['r1eA','vj1A','r1bA','r2bA']},
        {'sub':['hj1A'],'target':['r1eA','hj1A','r1bA','r2bA']}
    ]},
    # Lookup 24 - insert level 0 row boundaries around joiners
    {'name' : 'r0', 'marks' : '',
    'contexts' : [{'left':[],'right':['et_all']}],
    'details' : [
        {'sub':['vj0A'],'target':['r0eA','vj0A','r0bA']},
        {'sub':['hj0A'],'target':['r0eA','hj0A','r0bA']},
    ]},
    # Lookup 28 - insert level 1 row begin after unbalanced corner
    # NOTE: This doesn't account for the current level, so level 1 -> 2 unbalanced is a gap
    {'name' : 'unbal-corner', 'marks' : '',
    'contexts' : [{'left':['insertionsizes1a'],'right':[]}],
    'details' : [{'sub':['su'],'target':['ub','r1bA']}]},
    # Lookup 25 - insert level 1 row begin before level 2 begin
    {'name' : 'r2begin1', 'marks' : 'parens',
    'contexts' : [{'left':[],'right':['r2bA']}],
    'details' : [{'sub':['r0bA'],'target':['r0bA','r1bA']}]},
    # Lookup 26 - insert up-level row ends after level 2 begin
    {'name' : 'r2begin2', 'marks' : 'parens',
    'contexts' : [{'left':['r2bA'],'right':[]}],
    'details' : [
        {'sub':['r0eA'],'target':['r2eA','r1eA','r0eA']},
        {'sub':['r1eA'],'target':['r2eA','r1eA']},
    ]},
    # Lookup 27 - insert up-level row begins before level 2 end 
    {'name' : 'r2end', 'marks' : 'parens',
    'contexts' : [{'left':[],'right':['r2eA']}],
    'details' : [
        {'sub':['r0bA'],'target':['r0bA','r1bA','r2bA']},
        {'sub':['r1bA'],'target':['r1bA','r2bA']}
    ]},
    # Lookup 28 - insert up-level row end after level 1 begin
    {'name' : 'r1begin', 'marks' : 'parens',
    'contexts' : [{'left':['r1bA'],'right':[]}],
    'details' : [{'sub':['r0eA'],'target':['r1eA','r0eA']}]},
    # Lookup 29 - insert up-level row begin before level 1 end 
    {'name' : 'r1end', 'marks' : 'parens',
    'contexts' : [
        {'left':[],'right':['r1eA']},
        {'left':[],'right':['c1eA']}
    ],
    'details' : [{'sub':['r0bA'],'target':['r0bA','r1bA']}]},
    # Lookup 30 - insert level 1 row end before level 0 col end 
    {'name' : 'r1end', 'marks' : 'parens',
    'contexts' : [{'left':['r1bA'],'right':[]}],
    'details' : [{'sub':['c0eA'],'target':['r1eA','c0eA']}]},
    # Lookup 31 - insert level 1 row begin after level 0 col begin 
    {'name' : 'r1end', 'marks' : 'parens',
    'contexts' : [
        {'left':[],'right':['r1eA']},
        {'left':[],'right':['r2bA']}
    ],
    'details' : [{'sub':['c0bA'],'target':['c0bA','r1bA']}]},
    # Lookup 32 - insert column begin and end 
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
    # Lookup 33 - row 0 begin cleanup 
    {'name' : 'r0b_cleanup', 'marks' : '',
    'contexts' : [{'left':['hj0A'],'right':[]}],
    'details' : [{'sub':['r0bA','c0bA'],'target':['c0bA']}]},
    # Lookup 34 - row 0 end cleanup 
    {'name' : 'r0e_cleanup', 'marks' : '',
    'contexts' : [{'left':[],'right':['hj0A']}],
    'details' : [{'sub':['c0eA','r0eA'],'target':['c0eA']}]},
    # Lookup 35 - row 1 begin cleanup 
    {'name' : 'r1b_cleanup', 'marks' : '',
    'contexts' : [{'left':['hj1A'],'right':[]}],
    'details' : [{'sub':['r1bA','c1bA'],'target':['c1bA']}]},
    # Lookup 36 - row 1 end cleanup 
    {'name' : 'r1e_cleanup', 'marks' : '',
    'contexts' : [{'left':[],'right':['hj1A']}],
    'details' : [{'sub':['c1eA','r1eA'],'target':['c1eA']}]},
    # Lookup 37 - row 2 begin cleanup 
    {'name' : 'r2b_cleanup', 'marks' : '',
    'contexts' : [{'left':['hj2A'],'right':[]}],
    'details' : [{'sub':['r2bA','c2bA'],'target':['c2bA']}]},
    # Lookup 38 - row 2 end cleanup 
    {'name' : 'r2e_cleanup', 'marks' : '',
    'contexts' : [{'left':[],'right':['hj2A']}],
    'details' : [{'sub':['c2eA','r2eA'],'target':['c2eA']}]},
    # Lookup 39 - insert level 2 min default size
    {'name' : 'default_size_2', 'marks' : '',
    'contexts' : [{'left':['c1bA'],'right':[]}],
    'details' : [{'sub':['r2bA'],'target':['mt22','r2bA']}]},
    # Lookup 40 - insert level 1 min default size 
    {'name' : 'default_size_level1', 'marks' : '',
    'contexts' : [{'left':['c0bA'],'right':[]}],
    'details' : [{'sub':['r1bA'],'target':['mt43','r1bA']}]},
    # Lookup 40 - move unbalanced ss (i.e., su) to mark mt43,mt22
    {'name' : 'insertunbalancedtoken', 'marks' : 'rowmaxes',
    'contexts' : [{'left':[],'right':['su']}],
    'details' : [
        {'sub':['mt43'],'target':['mt43','ub']},
        {'sub':['mt22'],'target':['mt22','ub']}
    ]},
    # Lookup 40 - clean up unbalanced su
    {'name' : 'cleanupunbalanced', 'marks' : '',
    'details' : [
        {'sub':['c1bA','su'],'target':['c1bA']},
        {'sub':['c2bA','su'],'target':['c2bA']}
    ]},
    # Lookup 41 - set min default size to reducible default size
    {'name' : 'default_size_level1', 'marks' : 'rowmaxes',
    'exceptcontexts' : [{'left':[],'right':['mt22']}],
    'details' : [{'sub':['mt43'],'target':['et66']}]},
]