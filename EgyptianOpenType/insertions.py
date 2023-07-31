#!/usr/bin/python
# egyptian opentype generator font-specific variables
# Ideally this would be generated from font and not part of config.

insertions = {
	'A14' : {
		'bi' : {66:'22'},
		# 'te' : {66:'22'},
	},
	'A16' : {
		# 'bs' : {46:'22'},
		'te' : {46:'21'},
	},
	# 'A17' : {'be' : {56:'22'}},
	# 'A17a': {'be' : {56:'22'}},
	'A18' : {
		'be' : {46:'21'},
	},
	'A26' : {
		'bs' : {46:'13'},
	},
	'A28' : {
		'bs' : {56:'13y2'},
		'be' : {56:'13y2'},
	},
	'A30' : {
		'bs' : {46:'14'},
	},
	'A40' : {
		'ts' : {46:'13'},
	},
	'A41' : {'ts' : {46:'13'}},
	'A43' : {'ts' : {46:'13'}},
	'A45' : {'ts' : {46:'13'}},
	'A50' : {
		'ts' : {56:'23'},
	},
	'A55' : {
		'bi' : {64:'42'},
	},
	'B1'  : {'ts' : {46:'13'}},
	'C1'  : {'ts' : {46:'13'}},
	'C2a' : {'ts' : {36:'13'}},
	'C9'  : {'ts' : {36:'13'}},
	'C10' : {'ts' : {36:'13'}},
	'D3' : {
			'bs': {63:'22'}	
	},
	'D17' : {
			'te': {64:'32',62:'31',43:'21',32:'11'}	
	},
	'D28' : {
		'mi' : {55:'23'},
		'ti' : {55:'24'},
	},
	'D28o' : {
		'mi' : {55:'23'},
		'bi' : {55:'24'},
	},
	# 'D29' : {'bs' : {56:'22'},'ti' : {56:'11'}},
	'D32' : {
		'mi' : {56:'22'},
		'bi' : {56:'24'},
	},
	'D36' : {
		'ts' : {63:'51'},
    'ti' : {66:'43'},
	},
	# 'D37' : {'ti' : {63:'31'}},
	# 'D38' : {'ti' : {63:'31'}},
	# 'D39' : {'ti' : {63:'31'}},
	'D40' : {
		'ti' : {63:'41'},
	},
	'D41' : {
		'ts' : {66:'41'},
		# 'ti' : {63:'31'},
	},
	'D42' : {
		'ts' : {63:'51'},
		'ti' : {63:'41'},
	},
	# 'D43' : {'ti' : {63:'31'}},
	# 'D44' : {'ti' : {64:'31'}},
	'D45' : {
		'ti' : {64:'21'},
	},
	'D52' : {
		'bs' : {63:'41'},
	},
	'D53' : {
		'bs' : {63:'41x1'},
	},
	'D54' : {
		'ts' : {54:'12'},
		# 'bi' : {54:'11'},
	},
	'D55' : {
		'te' : {54:'12'},
		# 'bi' : {54:'11'},
	},
	'D56' : {
		'ts' : {36:'15'},
	},
	'D58' : {
		'ts' : {46:'24'},
	},
	'D60' : {
		'mi' : {46:'13'},
	},
	'D66' : {
		'ts' : {64:'42'},
		'ti' : {64:'22'},
	},
	'E1' : {
		'te' : {66:'31'},
	},
	'E3' : {
		'te' : {66:'41'},
	},
	'E6' : {
		'te' : {66:'32'},
		'bi' : {66:'12'},
	},
	'E7' : {
		'te' : {66:'32'},
	},
	'E8' : {
		'te' : {66:'41'},
	},
	'E8a' : {
		'bs' : {66:'32'},
		'te' : {66:'22y2'},
	},
	'E9' : {
		'bs' : {65:'51'},
		'te' : {65:'31'},
		'ti' : {65:'21'},
	},
	'E10' : {
		'te' : {65:'21'},
	},
	'E11' : {
		'te' : {65:'21'},
	},
	# 'E13' : {'te' : {56:'22'},},
	# 'E14' : {'ti' : {66:'31'}},
	'E15' : {
		'bs' : {66:'52'},
		'te' : {66:'32'},
		'ti' : {66:'21'},
	},
	'E16' : {
		'te' : {66:'32'},
		'ti' : {66:'21'},
	},
	'E16a' : {
			'te': {66:'22'}	
	},
	'E17' : {
		'te' : {66:'42'},
		# 'ti' : {66:'31'},
	},
	'E17a' : {
			'te': {66:'32'}	
	},
	'E18' : {
		'bs' : {66:'21'},
		'te' : {66:'41'},
		'be' : {66:'11'},
		# 'ti' : {66:'31'},
	},
	'E19' : {
		'te' : {66:'41'},
		# 'ti' : {66:'31'},
	},
	'E20' : {
		'te' : {66:'32'},
		'ti' : {66:'23'},
	},
	'E20a' : {
			'te': {56:'21'}	
	},
	'E21' : {
		'ti' : {65:'22'},
	},
	'E22' : {
		'te' : {64:'41'},
		# 'ti' : {64:'31'},
	},
	'E23' : {
		'te' : {63:'31'},
	},
	'E27' : {
		'te' : {46:'23'},
	},
	# 'E28' : {'te' : {66:'22'},},
	# 'E28a' : {'te': {66:'22'}},
	'E29' : {
		'te' : {56:'32'},
	},
	# 'E30' : {'te' : {66:'22'},},
	'E31' : {
		'te' : {66:'32'},
	},
	'E32' : {
		'te' : {65:'31'},
	},
	'E34' : {
		'te' : {64:'12y2'},
	},
	'E38' : {
		'te' : {65:'41'},
	},
	'E100' : {
		'te' : {64:'41'},
		# 'ti' : {64:'31'},
	},
	'F1' : {
			'ti' : {44:'11'}	
	},
	'F4' : {
			'ts': {66:'33',65:'33',64:'33',63:'32',62:'21',54:'23',52:'21',32:'11'}
	},
	'F5' : {
		'ti' : {56:'11'},
	},
	'F6' : {
		'te' : {66:'12'},
		'ti' : {66:'11'},
	},
	'F13' : {
		'ti' : {64:'24'},
	},
	'F13a' : {
			'ti' : {64:'22'}	
	},
	'F16' : {
		'te' : {64:'31'},
	},
	'F18' : {
		'te' : {62:'41'},
	},
	'F19' : {
			'ts': {63:'31'}	
	},
	'F20' : {
			'bs': {66:'54',56:'43',63:'42',33:'21'},
	},
	'F29' : {
		'bs' : {56:'22y2'},
		'be' : {56:'22y2'},
	},
	'F30' : {
		'bs' : {65:'42'},
	},
	'F39' : {
		'bs' : {55:'31'},
	},
	'F40' : {
			'bi' : {66:'42'}	
	},
	'F45' : {
			'bs': {46:'14'},
			'be': {46:'14'}	
	},
	'F45a' : {
			'bs': {46:'14'},
			'be': {46:'14'}	
	},
	'G1' : {
		'bs' : {66:'22y2'},
		# 'te' : {66:'22'},
	},
	'G2' : {
		'bs' : {66:'12y2'},
		# 'te' : {66:'22'},
	},
	'G3' : {
		'bs' : {66:'21y5'},
	},
	'G4' : {
		'bs' : {66:'12y2'},
		# 'te' : {66:'22'},
	},
	'G5' : {
		'bs' : {66:'12y2'},
		# 'te' : {66:'22'},
	},
	'G6' : {
		'bs' : {66:'12y2'},
	},
	'G6a' : {
			'te': {66:'22'}	
	},
	'G7' : {
		'bs' : {56:'21'},
		'te' : {56:'21'},
		'be' : {56:'22'},
	},
	# 'G7a' : {'te' : {66:'22'}},
	# 'G7b' : {'te' : {56:'22'}},
	'G8' : {
		'te' : {56:'11'},
	},
	'G9' : {
		'bs' : {56:'12'},
		'te' : {56:'32',55:'22',45:'22'}	
	},	
	'G10' : {
			'te': {66:'22'},
			'be': {66:'11'}	
	},	
	# 'G11' : {'te' : {63:'22'}},
	'G11a' : {
			'bs': {66:'22'},
			'te': {66:'12'}	
	},	
	'G13' : {
		'te' : {66:'33'},
	},
	'G14' : {
		'bs' : {66:'22y1'},
		# 'te' : {66:'22'},
	},
	'G15' : {
		'bs' : {66:'22y2'},
	},
	'G17' : {
		'bs' : {66:'12y2'},
		'te' : {66:'23'},
	},
	'G18' : {
		'bs' : {66:'12y2'},
		# 'te' : {66:'22'},
	},
	'G20' : {
		'bs' : {66:'22y2'},
	},
	'G21' : {
		'bs' : {66:'21y2'},
		'te' : {66:'23'},
	},
	'G22' : {
		'bs' : {65:'21y2'},
		'te' : {65:'32'},
	},
	'G23' : {
			'bs': {65:'21y2'},
			'te': {65:'32'},
			'be': {65:'21'}	
	},	
	'G25' : {
			'bs': {65:'22y2'},
			'te': {66:'22',65:'22',56:'22',55:'22',54:'22',44:'22',33:'11',22:'11'},
			'be': {65:'21'}	
	},	
	'G26' : {
		'bs' : {56:'21'},
		'te' : {56:'21'},
		'be' : {56:'21'},
	},
	'G26a' : {
		'bs' : {66:'22y2'},
		# 'te' : {66:'22'},
	},
	'G27' : {
		'bs' : {65:'22y3'},
		'te' : {65:'21'},
	},
	'G28' : {
		'bs' : {64:'22y4'},
		'te' : {64:'11'},
	},
	# 'G29' : {'bs' : {66:'22'},'te' : {66:'22'},},
	# 'G30' : {
	# 	'bs' : {86:'11y2'},
	# 	'te' : {86:'32'},
	# },
	'G31' : {
		'bs' : {66:'22y2'},
		'te' : {66:'12'},
	},
	'G32' : {
		'te' : {66:'12'},
		# 'be' : {66:'22'},
	},
	'G33' : {
		'bs' : {66:'22y2'},
		# 'te' : {66:'22'},
	},
	'G34' : {
		'bs' : {56:'22y1'},
		# 'te' : {56:'22'},
	},
	'G35' : {
		'bs' : {65:'21y3'},
		'te' : {65:'32'},
	},
	'G36' : {
		'bs' : {65:'11y4'},
		'te' : {65:'31'},
	},
	'G37' : {
		'bs' : {65:'11y4'},
		'te' : {65:'31'},
	},
	'G38' : {
		'bs' : {66:'21y1'},
		'te' : {66:'32'},
	},
	'G39' : {
		'bs' : {66:'21y1'},
		'te' : {66:'22',65:'22',56:'22',55:'22',54:'22',44:'22',43:'11',42:'11',33:'11',22:'11'},
			'be': {65:'21',44:'11',42:'11',22:'11'},	
	},	
	'G41' : {'bs' : {66:'12'},},
	'G42' : {
		'bs' : {65:'21y3'},
		'te' : {65:'31'},
	},
	'G43' : {
		'bs' : {46:'11y2'},
		# 'te' : {46:'22'},
		'be': {46:'11'},	
	},	
	'G44' : {
		'bs' : {66:'11y2'},
		'te' : {66:'21'},
	},
	'G45' : {'bs' : {66:'22y2'},},
	'G47' : {
		'bs' : {66:'11'},
		'te' : {66:'31'},
	},
	'G50' : {
		'bs' : {65:'12y2'},
		# 'te' : {65:'22'},
	},
	'G53' : {
		'te' : {66:'23'},
	},
	'I1' : {
			'bs': {66:'52',65:'52',55:'42',45:'32'}	
	},
	'I3' : {
		'te' : {62:'21'},
	},
	'I5' : {
		'te' : {63:'11'},
	},
	'I7' : {
		'te' : {66:'21'},
	},
	'I8' : {
		'bs' : {56:'42'},
		'te' : {56:'21'},
	},
	'I9' : {
		'te' : {62:'41'},
	},
	'I10' : {
			'bs': {66:'54',56:'43',63:'51',33:'21'},
			'te': {66:'31',65:'31',64:'21',56:'31',55:'31',54:'31',46:'21',45:'21',44:'21',36:'11',35:'11',34:'11'}	
	},
	'I10a' : {
			'bs': {66:'54',56:'43',63:'51',33:'21'},
			'ti': {66:'31'}	
	},
	'I11' : {
			'bs': {66:'54',56:'43',63:'51',33:'21'},
			'te': {66:'31'}	
	},
	'L1' : {'bi' : {46:'11'}},
	'M9' : {
		'bs' : {66:'52'},
	},
	'M10' : {
		'bs' : {55:'42'},
	},
	'M26' : {
		'bs' : {46:'11'},
		'be' : {46:'11'},
	},
	'M27' : {
		'bs' : {66:'21'},
		'be' : {66:'21'},
	},
	'N2' : {'bs' : {66:'22'},'be' : {66:'22'},},
	'N3' : {'bs' : {56:'22'},'be' : {56:'22'},},
	'N11' : {
		'bi' : {62:'21'},
	},
	'N36' : {
		'mi' : {62:'31'},
	},
	'N37' : {
		'mi' : {62:'51'},
	},
	'O1' : {
			'bi' : {53:'13'},
			'mi' : {53:'42'}	
	},
	# 'O1a' : {'bs' : {66:'22'},'be' : {66:'22'},},
	# 'O2'  : {'bs' : {66:'22'},'be' : {66:'22'},},
	'O6' : {
		'mi' : {36:'42'},
	},
	'O13' : {
		'mi' : {66:'34'},
	},
	'O14' : {
		'be' : {66:'44'},
	},
	'O16' : {
		'mi' : {64:'41'},
	},
	'O17' : {
		'mi' : {64:'31'},
	},
	'O18' : {
		'mi' : {66:'43'},
	},
	'O26' : {
		'mi' : {46:'24'},
	},
	'O32' : {
		'mi' : {46:'13'}, 'bi' : {46:'13'}	
	},
	'O36' : {
		'mi' : {46:'14'},
	},
	# 'O38' : {'be' : {44:'22'}},
	'Q2' : {
		'ts' : {64:'32'},
	},
	'R8' : {
		'bs' : {36:'24'},
	},
	'R12' : {
		'bs' : {64:'32'},
		'be' : {64:'12'},
	},
	'R13' : {
		# 'bs' : {56:'22'},
		'te' : {56:'11'},
		'be' : {56:'12'},
	},
	'S1' : {
		'ts' : {46:'22'},
	},
	# 'S19' : {'bi' : {55:'11'}},
	'S2' : {
		'ts' : {66:'32'},
	},
	'S22' : {
		'ti' : {64:'21'},
		'bi' : {64:'31'},
	},
	'S28' : {
		'bs' : {66:'23'},
	},
	# 'S29' : {
	# 	'be' : {26:'12'},
	# },
	# 'T2' : {
	# 	'bs' : {64:'31'},
	# 	'te' : {64:'21'},
	# },
	'T5' : {
		# 'bs' : {66:'22'},
		'bi' : {66:'12'},
	},
	'T6' : {
		'bs' : {66:'21'},
	},
	'T7a' : {
		'bs' : {36:'24'},
	},
	'T14' : {
		'bs' : {26:'14'},
	},
	# 'T30' : {
	# 	'te' : {63:'21'},
	# },
	'T32' : {
		'bs' : {65:'22y4'},
	},
	'U1' : {
		'ts' : {66:'34'},
		# 'te' : {66:'11'},
	},
	'U2' : {
		'ts' : {65:'34'},
		'te' : {65:'12'},
	},
	# 'U6' : {
	# 	'bs' : {46:'11'},
	# 	'te' : {46:'11'},
	# },
	# 'U13' : {
	# 	'bs' : {64:'11'},
	# },
	'U15' : {
		'te' : {63:'42'},
		# 'ti' : {63:'31'},
	},
	'U19' : {
		# 'bs' : {63:'21'},
		'te' : {63:'31'},
		'ti' : {63:'21'},
	},
	'U21' : {
		'te' : {62:'31'},
		'ti' : {62:'21'},
		'bi' : {62:'21'},
	},
	# 'U35' : {'bs' : {66:'22'},'be' : {66:'22'},},
	'V6' : {
		'mi' : {23:'11'},
	},
	'V7' : {
		'mi' : {23:'11'},
	},
	'V10' : {
		'mi' : {53:'32'},
	},
	'V10n' : {
		'mi' : {46:'34'},
	},
	'V12' : {
		'bs' : {53:'32'},
	},
	'V15' : {
		'bs' : {65:'21y6'},
	},
	'V22' : {
		'bs' : {64:'43'},
	},
	'V23' : {
		'bs' : {64:'43'},
	},
	'V23a' : {
				'bs': {66:'43'}	
	},
	# 'V81' : {'bs' : {66:'22'},'be' : {66:'22'},},
	# 'W15' : {'mi' : {36:'11'}},
	# 'W16' : {'mi' : {46:'11'}},
	'W4' : {
		'mi' : {66:'32'},
	},
	'Z6' : {
		'bs' : {64:'32'},
		# 'te' : {64:'21'},
	},
	# 'Z8' : {'mi' : {32:'11'}},
	'Z10' : {
		'ti' : {63:'21'},
		'bi' : {63:'21'},
	},
	'Z11' : {
		'bs' : {46:'12'},
		'be' : {46:'12'},
	},
	# 'J5' : {'be' : {44:'22'},'bi' : {44:'11'}},
	'J7' : { # AA7
		'ts' : {63:'41'},
		'ti' : {63:'21'},
	},
	'J13' : { # AA13
		'mi' : {62:'21'},
	},
	'J15' : { # AA15
		'mi' : {62:'21'},
	},
	# 'J16' : {'mi' : {32:'11'}},
	'J19' : { # AA19
		'mi' : {44:'12'},
		'bi' : {44:'12'},
	},
}


