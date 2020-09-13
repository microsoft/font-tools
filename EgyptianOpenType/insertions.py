#!/usr/bin/python
# egyptian opentype generator font-specific variables
# Ideally this would be generated from font and not part of config.


# TODO: specify ratios for each position, and then overrides to derived
# values from for ratios for specific sizes.
# TODO: specify offsets from corner, and alignment?.

insertions = {
	'default' : {
		'ts': {},
		'bs': {66:'22',65:'22',56:'22',55:'22',45:'22',44:'22',33:'11',22:'-1'},
		'te': {66:'11',65:'11',56:'11',55:'11',45:'11',44:'11',33:'11',22:'-1'},
		'be': {}
	},
	'D17' : {
		'ts': {},
		'bs': {},
		'te': {64:'41',62:'31',61:'-1',43:'21',32:'11',21:'-1'},
		'be': {}
	},
	'F4' : {
		'ts': {66:'33',65:'33',64:'33',63:'32',62:'21',54:'23',52:'21',32:'11',21:'-1'},
		'bs': {},
		'te': {66:'41',65:'41',56:'31',55:'31',45:'31',44:'31',33:'-1',22:'-1'},
		'be': {}
	},
	'F20' : {
		'ts': {},
		'bs': {66:'54',65:'53',56:'43',55:'43',45:'33',44:'32',33:'21',22:'21'},
		'te': {66:'41',65:'41',56:'31',55:'31',45:'31',44:'31',33:'-1',22:'-1'},
		'be': {}
	},
	'G25' : {
		'ts': {},
		'bs': {},
		'te': {66:'22',65:'22',56:'22',55:'22',54:'22',44:'22',33:'11',22:'11'},
		'be': {}
	},	
	'G39' : {
		'ts': {},
		'bs': {},
		'te': {66:'22',65:'22',56:'22',55:'22',54:'22',44:'22',33:'11',22:'11'},
		'be': {}
	},	
	'I10' : {
		'ts': {},
		'bs': {66:'22',65:'22',56:'12',55:'11',45:'11',44:'11',33:'11',22:'-1'},
		'te': {66:'32',65:'32',56:'22',55:'22',45:'22',44:'22',33:'11',22:'11'},
		'be': {66:'21',65:'21',56:'21',55:'21',45:'11',44:'11',33:'-1',22:'-1'}
	}
}


