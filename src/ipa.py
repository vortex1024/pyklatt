﻿# -*- coding: utf-8 -*-
"""
CPSC 599 module: src.ipa

Purpose
=======
 Provides IPA-to-parameter lookup functions.
 
Limitations
===========
 At present, only the following IPA symbols are supported:
  - Consonants:
   - mnŋpbtdɾkgfvθðszʃʒhʔɹjlwʍ
  - Vowels:
   - ieɛæaIəʊuoʌɔ
 
Legal
=====
 All code, unless otherwise indicated, is original, and subject to the
 terms of the GPLv3, which is provided in COPYING.
 
 This project borrows algorithms, ideas, and statistical data from other
 projects. Full attribution is provided in ACKNOWLEDGEMENTS.
 
 (C) Neil Tallim, Sydni Bennie, 2009
"""
#Enumerations of consonant positions.
LABIAL = 1 #: Identifies a consonant as labial.
CORONAL = 2 #: Identifies a consonant as coronal.
DORSAL = 3 #: Identifies a consonant as dorsal.
RADICAL = 4 #: Identifies a consonant as radical.
GLOTTAL = 5 #: Identifies a consonant as glottal.

#Enumerations of vowel positions.
FRONT = 1 #: Identifies a vowel as front.
NEAR_FRONT = 2 #: Identifies a vowel as near-front.
CENTRAL = 3 #: Identifies a vowel as central.
NEAR_BACK = 4 #: Identifies a vowel as near-back.
BACK = 5 #: Identifies a vowel as back.

_IPA_MAPPING = {
 u'm': {
  'freq-glottal-pole': 0,
  'freq-glottal-zero': 1500,
  'freq-glottal-sine': 0,
  'freq-nasal-pole': 270,
  'freq-nasal-zero': 450,
  'freq (1-6)': (480, 1270, 2130, 3300, 3750, 4900),
  'bwidth-glottal-pole': 100,
  'bwidth-glottal-zero': 6000,
  'bwidth-glottal-sine': 100,
  'bwidth-nasal-pole': 100,
  'bwidth-nasal-zero': 100,
  'bwidth (1-6)': (40, 200, 200, 250, 200, 1000),
  'formant-gain (2-6)': (0, 0, 0, 0, 0),
  'formant-bypass-gain': 0,
  'formant-cascade-gain': 0,
  'formant-parallel-gain': 0,
  'voicing-linear-gain': 40,
  'voicing-sine-gain': 50,
  'nominal-duration': 100,
  'vowel': False,
  'nasal': True,
  'voice': True,
  'stop': False,
  'liquid': False,
  'regions': [LABIAL]
 },
 u'n': {
  'freq-glottal-pole': 0,
  'freq-glottal-zero': 1500,
  'freq-glottal-sine': 0,
  'freq-nasal-pole': 270,
  'freq-nasal-zero': 450,
  'freq (1-6)': (480, 1340, 2470, 3300, 3750, 4900),
  'bwidth-glottal-pole': 100,
  'bwidth-glottal-zero': 6000,
  'bwidth-glottal-sine': 100,
  'bwidth-nasal-pole': 100,
  'bwidth-nasal-zero': 100,
  'bwidth (1-6)': (40, 300, 300, 250, 200, 1000),
  'formant-gain (2-6)': (0, 0, 0, 0, 0),
  'formant-bypass-gain': 0,
  'formant-cascade-gain': 0,
  'formant-parallel-gain': 0,
  'voicing-linear-gain': 40,
  'voicing-sine-gain': 50,
  'nominal-duration': 100,
  'vowel': False,
  'nasal': True,
  'voice': True,
  'stop': False,
  'liquid': False,
  'regions': [CORONAL]
 },
 u'\u014b': { #ŋ
  'freq-glottal-pole': 0,
  'freq-glottal-zero': 1500,
  'freq-glottal-sine': 0,
  'freq-nasal-pole': 270,
  'freq-nasal-zero': 450,
  'freq (1-6)': (480, 2000, 2900, 3300, 3750, 4900),
  'bwidth-glottal-pole': 100,
  'bwidth-glottal-zero': 6000,
  'bwidth-glottal-sine': 100,
  'bwidth-nasal-pole': 100,
  'bwidth-nasal-zero': 100,
  'bwidth (1-6)': (40, 300, 300, 250, 200, 1000),
  'formant-gain (2-6)': (0, 0, 0, 0, 0),
  'formant-bypass-gain': 0,
  'formant-cascade-gain': 0,
  'formant-parallel-gain': 0,
  'voicing-linear-gain': 40,
  'voicing-sine-gain': 50,
  'nominal-duration': 100,
  'vowel': False,
  'nasal': True,
  'voice': True,
  'stop': False,
  'liquid': False,
  'regions': [DORSAL]
 },
 u'p': {
  'freq-glottal-pole': 0,
  'freq-glottal-zero': 1500,
  'freq-glottal-sine': 0,
  'freq-nasal-pole': 250,
  'freq-nasal-zero': 250,
  'freq (1-6)': (400, 1100, 2150, 3300, 3750, 4900),
  'bwidth-glottal-pole': 100,
  'bwidth-glottal-zero': 6000,
  'bwidth-glottal-sine': 100,
  'bwidth-nasal-pole': 100,
  'bwidth-nasal-zero': 100,
  'bwidth (1-6)': (300, 150, 220, 250, 200, 1000),
  'formant-gain (2-6)': (0, 0, 0, 0, 0),
  'formant-bypass-gain': 63,
  'formant-cascade-gain': 0,
  'formant-parallel-gain': 20,
  'voicing-linear-gain': 0,
  'voicing-sine-gain': 0,
  'nominal-duration': 75,
  'vowel': False,
  'nasal': False,
  'voice': False,
  'stop': True,
  'liquid': False,
  'regions': [LABIAL]
 },
 u'b': {
  'freq-glottal-pole': 0,
  'freq-glottal-zero': 1500,
  'freq-glottal-sine': 0,
  'freq-nasal-pole': 250,
  'freq-nasal-zero': 250,
  'freq (1-6)': (200, 1100, 2150, 3300, 3750, 4900),
  'bwidth-glottal-pole': 100,
  'bwidth-glottal-zero': 6000,
  'bwidth-glottal-sine': 100,
  'bwidth-nasal-pole': 100,
  'bwidth-nasal-zero': 100,
  'bwidth (1-6)': (60, 100, 130, 250, 200, 1000),
  'formant-gain (2-6)': (0, 0, 0, 0, 0),
  'formant-bypass-gain': 63,
  'formant-cascade-gain': 0,
  'formant-parallel-gain': 10,
  'voicing-linear-gain': 20,
  'voicing-sine-gain': 20,
  'nominal-duration': 75,
  'vowel': False,
  'nasal': False,
  'voice': True,
  'stop': True,
  'liquid': False,
  'regions': [LABIAL]
 },
 u't': {
  'freq-glottal-pole': 0,
  'freq-glottal-zero': 1500,
  'freq-glottal-sine': 0,
  'freq-nasal-pole': 250,
  'freq-nasal-zero': 250,
  'freq (1-6)': (400, 1600, 2600, 3300, 3750, 4900),
  'bwidth-glottal-pole': 100,
  'bwidth-glottal-zero': 6000,
  'bwidth-glottal-sine': 100,
  'bwidth-nasal-pole': 100,
  'bwidth-nasal-zero': 100,
  'bwidth (1-6)': (300, 120, 250, 250, 200, 1000),
  'formant-gain (2-6)': (0, 15, 23, 28, 32),
  'formant-bypass-gain': 0,
  'formant-cascade-gain': 0,
  'formant-parallel-gain': 20,
  'voicing-linear-gain': 0,
  'voicing-sine-gain': 0,
  'nominal-duration': 50,
  'vowel': False,
  'nasal': False,
  'voice': False,
  'stop': True,
  'liquid': False,
  'regions': [CORONAL]
 },
 u'd': {
  'freq-glottal-pole': 0,
  'freq-glottal-zero': 1500,
  'freq-glottal-sine': 0,
  'freq-nasal-pole': 250,
  'freq-nasal-zero': 250,
  'freq (1-6)': (200, 1600, 2600, 3300, 3750, 4900),
  'bwidth-glottal-pole': 100,
  'bwidth-glottal-zero': 6000,
  'bwidth-glottal-sine': 100,
  'bwidth-nasal-pole': 100,
  'bwidth-nasal-zero': 100,
  'bwidth (1-6)': (60, 100, 170, 250, 200, 1000),
  'formant-gain (2-6)': (0, 23, 30, 31, 30),
  'formant-bypass-gain': 0,
  'formant-cascade-gain': 0,
  'formant-parallel-gain': 10,
  'voicing-linear-gain': 20,
  'voicing-sine-gain': 20,
  'nominal-duration': 75,
  'vowel': False,
  'nasal': False,
  'voice': True,
  'stop': True,
  'liquid': False,
  'regions': [CORONAL]
 },
 u'\u027e': { #ɾ
  'freq-glottal-pole': 0,
  'freq-glottal-zero': 1500,
  'freq-glottal-sine': 0,
  'freq-nasal-pole': 250,
  'freq-nasal-zero': 250,
  'freq (1-6)': (300, 1600, 2600, 3300, 3750, 4900),
  'bwidth-glottal-pole': 100,
  'bwidth-glottal-zero': 6000,
  'bwidth-glottal-sine': 100,
  'bwidth-nasal-pole': 100,
  'bwidth-nasal-zero': 100,
  'bwidth (1-6)': (160, 110, 210, 250, 200, 1000),
  'formant-gain (2-6)': (0, 19, 26, 30, 31),
  'formant-bypass-gain': 0,
  'formant-cascade-gain': 0,
  'formant-parallel-gain': 15,
  'voicing-linear-gain': 10,
  'voicing-sine-gain': 10,
  'nominal-duration': 60,
  'vowel': False,
  'nasal': False,
  'voice': True,
  'stop': True,
  'liquid': False,
  'regions': [CORONAL]
 },
 u'k': {
  'freq-glottal-pole': 0,
  'freq-glottal-zero': 1500,
  'freq-glottal-sine': 0,
  'freq-nasal-pole': 250,
  'freq-nasal-zero': 250,
  'freq (1-6)': (300, 1990, 2850, 3300, 3750, 4900),
  'bwidth-glottal-pole': 100,
  'bwidth-glottal-zero': 6000,
  'bwidth-glottal-sine': 100,
  'bwidth-nasal-pole': 100,
  'bwidth-nasal-zero': 100,
  'bwidth (1-6)': (250, 160, 330, 250, 200, 1000),
  'formant-gain (2-6)': (30, 26, 22, 23, 23),
  'formant-bypass-gain': 0,
  'formant-cascade-gain': 0,
  'formant-parallel-gain': 20,
  'voicing-linear-gain': 0,
  'voicing-sine-gain': 0,
  'nominal-duration': 50,
  'vowel': False,
  'nasal': False,
  'voice': False,
  'stop': True,
  'liquid': False,
  'regions': [DORSAL]
 },
 u'g': {
  'freq-glottal-pole': 0,
  'freq-glottal-zero': 1500,
  'freq-glottal-sine': 0,
  'freq-nasal-pole': 250,
  'freq-nasal-zero': 250,
  'freq (1-6)': (200, 1990, 2850, 3300, 3750, 4900),
  'bwidth-glottal-pole': 100,
  'bwidth-glottal-zero': 6000,
  'bwidth-glottal-sine': 100,
  'bwidth-nasal-pole': 100,
  'bwidth-nasal-zero': 100,
  'bwidth (1-6)': (60, 150, 280, 250, 200, 1000),
  'formant-gain (2-6)': (30, 27, 22, 23, 23),
  'formant-bypass-gain': 0,
  'formant-cascade-gain': 0,
  'formant-parallel-gain': 10,
  'voicing-linear-gain': 20,
  'voicing-sine-gain': 20,
  'nominal-duration': 60,
  'vowel': False,
  'nasal': False,
  'voice': True,
  'stop': True,
  'liquid': False,
  'regions': [DORSAL]
 },
 u'f': {
  'freq-glottal-pole': 0,
  'freq-glottal-zero': 1500,
  'freq-glottal-sine': 0,
  'freq-nasal-pole': 250,
  'freq-nasal-zero': 250,
  'freq (1-6)': (340, 1100, 2080, 3300, 3750, 4900),
  'bwidth-glottal-pole': 100,
  'bwidth-glottal-zero': 6000,
  'bwidth-glottal-sine': 100,
  'bwidth-nasal-pole': 100,
  'bwidth-nasal-zero': 100,
  'bwidth (1-6)': (200, 120, 150, 250, 200, 1000),
  'formant-gain (2-6)': (0, 0, 0, 0, 0),
  'formant-bypass-gain': 57,
  'formant-cascade-gain': 0,
  'formant-parallel-gain': 20,
  'voicing-linear-gain': 0,
  'voicing-sine-gain': 0,
  'nominal-duration': 150,
  'vowel': False,
  'nasal': False,
  'voice': False,
  'stop': False,
  'liquid': False,
  'regions': [LABIAL]
 },
 u'v': {
  'freq-glottal-pole': 0,
  'freq-glottal-zero': 1500,
  'freq-glottal-sine': 0,
  'freq-nasal-pole': 250,
  'freq-nasal-zero': 250,
  'freq (1-6)': (220, 1100, 2080, 3300, 3750, 4900),
  'bwidth-glottal-pole': 100,
  'bwidth-glottal-zero': 6000,
  'bwidth-glottal-sine': 100,
  'bwidth-nasal-pole': 100,
  'bwidth-nasal-zero': 100,
  'bwidth (1-6)': (60, 90, 120, 250, 200, 1000),
  'formant-gain (2-6)': (0, 0, 0, 0, 0),
  'formant-bypass-gain': 57,
  'formant-cascade-gain': 0,
  'formant-parallel-gain': 20,
  'voicing-linear-gain': 47,
  'voicing-sine-gain': 47,
  'nominal-duration': 150,
  'vowel': False,
  'nasal': False,
  'voice': True,
  'stop': False,
  'liquid': False,
  'regions': [LABIAL]
 },
 u'\u03b8': { #θ
  'freq-glottal-pole': 0,
  'freq-glottal-zero': 1500,
  'freq-glottal-sine': 0,
  'freq-nasal-pole': 250,
  'freq-nasal-zero': 250,
  'freq (1-6)': (320, 1290, 2540, 3300, 3750, 4900),
  'bwidth-glottal-pole': 100,
  'bwidth-glottal-zero': 6000,
  'bwidth-glottal-sine': 100,
  'bwidth-nasal-pole': 100,
  'bwidth-nasal-zero': 100,
  'bwidth (1-6)': (200, 90, 200, 250, 200, 1000),
  'formant-gain (2-6)': (0, 0, 0, 0, 28),
  'formant-bypass-gain': 38,
  'formant-cascade-gain': 0,
  'formant-parallel-gain': 20,
  'voicing-linear-gain': 0,
  'voicing-sine-gain': 0,
  'nominal-duration': 150,
  'vowel': False,
  'nasal': False,
  'voice': False,
  'stop': False,
  'liquid': False,
  'regions': [CORONAL]
 },
 u'\xf0': { #ð
  'freq-glottal-pole': 0,
  'freq-glottal-zero': 1500,
  'freq-glottal-sine': 0,
  'freq-nasal-pole': 250,
  'freq-nasal-zero': 250,
  'freq (1-6)': (270, 1290, 2540, 3300, 3750, 4900),
  'bwidth-glottal-pole': 100,
  'bwidth-glottal-zero': 6000,
  'bwidth-glottal-sine': 100,
  'bwidth-nasal-pole': 100,
  'bwidth-nasal-zero': 100,
  'bwidth (1-6)': (60, 80, 170, 250, 200, 1000),
  'formant-gain (2-6)': (0, 0, 0, 0, 28),
  'formant-bypass-gain': 38,
  'formant-cascade-gain': 0,
  'formant-parallel-gain': 20,
  'voicing-linear-gain': 47,
  'voicing-sine-gain': 47,
  'nominal-duration': 150,
  'vowel': False,
  'nasal': False,
  'voice': True,
  'stop': False,
  'liquid': False,
  'regions': [CORONAL]
 },
 u's': {
  'freq-glottal-pole': 0,
  'freq-glottal-zero': 1500,
  'freq-glottal-sine': 0,
  'freq-nasal-pole': 250,
  'freq-nasal-zero': 250,
  'freq (1-6)': (320, 1390, 2530, 3300, 3750, 4900),
  'bwidth-glottal-pole': 100,
  'bwidth-glottal-zero': 6000,
  'bwidth-glottal-sine': 100,
  'bwidth-nasal-pole': 100,
  'bwidth-nasal-zero': 100,
  'bwidth (1-6)': (200, 80, 200, 250, 200, 1000),
  'formant-gain (2-6)': (0, 0, 0, 0, 52),
  'formant-bypass-gain': 0,
  'formant-cascade-gain': 0,
  'formant-parallel-gain': 20,
  'voicing-linear-gain': 0,
  'voicing-sine-gain': 0,
  'nominal-duration': 100,
  'vowel': False,
  'nasal': False,
  'voice': False,
  'stop': False,
  'liquid': False,
  'regions': [CORONAL]
 },
 u'z': {
  'freq-glottal-pole': 0,
  'freq-glottal-zero': 1500,
  'freq-glottal-sine': 0,
  'freq-nasal-pole': 250,
  'freq-nasal-zero': 250,
  'freq (1-6)': (240, 1390, 2530, 3300, 3750, 4900),
  'bwidth-glottal-pole': 100,
  'bwidth-glottal-zero': 6000,
  'bwidth-glottal-sine': 100,
  'bwidth-nasal-pole': 100,
  'bwidth-nasal-zero': 100,
  'bwidth (1-6)': (70, 60, 180, 250, 200, 1000),
  'formant-gain (2-6)': (0, 0, 0, 0, 52),
  'formant-bypass-gain': 0,
  'formant-cascade-gain': 0,
  'formant-parallel-gain': 20,
  'voicing-linear-gain': 47,
  'voicing-sine-gain': 47,
  'nominal-duration': 125,
  'vowel': False,
  'nasal': False,
  'voice': True,
  'stop': False,
  'liquid': False,
  'regions': [CORONAL]
 },
 u'\u0283': { #ʃ
  'freq-glottal-pole': 0,
  'freq-glottal-zero': 1500,
  'freq-glottal-sine': 0,
  'freq-nasal-pole': 250,
  'freq-nasal-zero': 250,
  'freq (1-6)': (300, 1840, 2750, 3300, 3750, 4900),
  'bwidth-glottal-pole': 100,
  'bwidth-glottal-zero': 6000,
  'bwidth-glottal-sine': 100,
  'bwidth-nasal-pole': 100,
  'bwidth-nasal-zero': 100,
  'bwidth (1-6)': (200, 100, 300, 250, 200, 1000),
  'formant-gain (2-6)': (0, 28, 24, 24, 23),
  'formant-bypass-gain': 0,
  'formant-cascade-gain': 0,
  'formant-parallel-gain': 20,
  'voicing-linear-gain': 0,
  'voicing-sine-gain': 0,
  'nominal-duration': 100,
  'vowel': False,
  'nasal': False,
  'voice': False,
  'stop': False,
  'liquid': False,
  'regions': [CORONAL]
 },
 u'\u0292': { #ʒ
  'freq-glottal-pole': 0,
  'freq-glottal-zero': 1500,
  'freq-glottal-sine': 0,
  'freq-nasal-pole': 250,
  'freq-nasal-zero': 250,
  'freq (1-6)': (300, 1840, 2750, 3300, 3750, 4900),
  'bwidth-glottal-pole': 100,
  'bwidth-glottal-zero': 6000,
  'bwidth-glottal-sine': 100,
  'bwidth-nasal-pole': 100,
  'bwidth-nasal-zero': 100,
  'bwidth (1-6)': (70, 60, 280, 250, 200, 1000),
  'formant-gain (2-6)': (0, 28, 24, 24, 23),
  'formant-bypass-gain': 0,
  'formant-cascade-gain': 0,
  'formant-parallel-gain': 20,
  'voicing-linear-gain': 47,
  'voicing-sine-gain': 47,
  'nominal-duration': 125,
  'vowel': False,
  'nasal': False,
  'voice': True,
  'stop': False,
  'liquid': False,
  'regions': [CORONAL]
 },
 u'h': {
  'freq-glottal-pole': 0,
  'freq-glottal-zero': 1500,
  'freq-glottal-sine': 0,
  'freq-nasal-pole': 250,
  'freq-nasal-zero': 250,
  'freq (1-6)': (50, 75, 100, 3300, 3750, 4900),
  'bwidth-glottal-pole': 100,
  'bwidth-glottal-zero': 6000,
  'bwidth-glottal-sine': 100,
  'bwidth-nasal-pole': 100,
  'bwidth-nasal-zero': 100,
  'bwidth (1-6)': (60, 90, 120, 250, 200, 1000),
  'formant-gain (2-6)': (0, 0, 0, 0, 0),
  'formant-bypass-gain': 0,
  'formant-cascade-gain': 0,
  'formant-parallel-gain': 0,
  'voicing-linear-gain': 25,
  'voicing-sine-gain': 0,
  'nominal-duration': 125,
  'vowel': False,
  'nasal': False,
  'voice': False,
  'stop': False,
  'liquid': False,
  'regions': [GLOTTAL]
 },
 u'\u0294': { #ʔ
  'freq-glottal-pole': 0,
  'freq-glottal-zero': 1500,
  'freq-glottal-sine': 0,
  'freq-nasal-pole': 250,
  'freq-nasal-zero': 250,
  'freq (1-6)': (100, 150, 200, 3300, 3750, 4900),
  'bwidth-glottal-pole': 100,
  'bwidth-glottal-zero': 6000,
  'bwidth-glottal-sine': 100,
  'bwidth-nasal-pole': 100,
  'bwidth-nasal-zero': 100,
  'bwidth (1-6)': (60, 90, 120, 250, 200, 1000),
  'formant-gain (2-6)': (0, 0, 0, 0, 0),
  'formant-bypass-gain': 0,
  'formant-cascade-gain': 0,
  'formant-parallel-gain': 0,
  'voicing-linear-gain': 25,
  'voicing-sine-gain': 0,
  'nominal-duration': 50,
  'vowel': False,
  'nasal': False,
  'voice': False,
  'stop': True,
  'liquid': False,
  'regions': [GLOTTAL]
 },
 u'\u0279': { #ɹ
  'freq-glottal-pole': 0,
  'freq-glottal-zero': 1500,
  'freq-glottal-sine': 0,
  'freq-nasal-pole': 250,
  'freq-nasal-zero': 250,
  'freq (1-6)': (310, 1050, 2050, 3300, 3750, 4900),
  'bwidth-glottal-pole': 100,
  'bwidth-glottal-zero': 6000,
  'bwidth-glottal-sine': 100,
  'bwidth-nasal-pole': 100,
  'bwidth-nasal-zero': 100,
  'bwidth (1-6)': (70, 100, 150, 250, 200, 1000),
  'formant-gain (2-6)': (0, 0, 0, 0, 0),
  'formant-bypass-gain': 0,
  'formant-cascade-gain': 50,
  'formant-parallel-gain': 0,
  'voicing-linear-gain': 50,
  'voicing-sine-gain': 0,
  'nominal-duration': 150,
  'vowel': False,
  'nasal': False,
  'voice': True,
  'stop': False,
  'liquid': True,
  'regions': [CORONAL]
 },
 u'l': {
  'freq-glottal-pole': 0,
  'freq-glottal-zero': 1500,
  'freq-glottal-sine': 0,
  'freq-nasal-pole': 250,
  'freq-nasal-zero': 250,
  'freq (1-6)': (310, 1050, 2880, 3300, 3750, 4900),
  'bwidth-glottal-pole': 100,
  'bwidth-glottal-zero': 6000,
  'bwidth-glottal-sine': 100,
  'bwidth-nasal-pole': 100,
  'bwidth-nasal-zero': 100,
  'bwidth (1-6)': (50, 100, 280, 250, 200, 1000),
  'formant-gain (2-6)': (0, 0, 0, 0, 0),
  'formant-bypass-gain': 0,
  'formant-cascade-gain': 0,
  'formant-parallel-gain': 0,
  'voicing-linear-gain': 50,
  'voicing-sine-gain': 0,
  'nominal-duration': 150,
  'vowel': False,
  'nasal': False,
  'voice': True,
  'stop': False,
  'liquid': True,
  'regions': [CORONAL]
 },
 u'j': {
  'freq-glottal-pole': 0,
  'freq-glottal-zero': 1500,
  'freq-glottal-sine': 0,
  'freq-nasal-pole': 250,
  'freq-nasal-zero': 250,
  'freq (1-6)': (260, 2070, 3020, 3300, 3750, 4900),
  'bwidth-glottal-pole': 100,
  'bwidth-glottal-zero': 6000,
  'bwidth-glottal-sine': 100,
  'bwidth-nasal-pole': 100,
  'bwidth-nasal-zero': 100,
  'bwidth (1-6)': (40, 250, 500, 250, 200, 1000),
  'formant-gain (2-6)': (0, 0, 0, 0, 0),
  'formant-bypass-gain': 0,
  'formant-cascade-gain': 0,
  'formant-parallel-gain': 0,
  'voicing-linear-gain': 50,
  'voicing-sine-gain': 0,
  'nominal-duration': 150,
  'vowel': False,
  'nasal': False,
  'voice': True,
  'stop': False,
  'liquid': False,
  'regions': [DORSAL]
 },
 u'w': {
  'freq-glottal-pole': 0,
  'freq-glottal-zero': 1500,
  'freq-glottal-sine': 0,
  'freq-nasal-pole': 250,
  'freq-nasal-zero': 250,
  'freq (1-6)': (290, 610, 2150, 3300, 3750, 4900),
  'bwidth-glottal-pole': 100,
  'bwidth-glottal-zero': 6000,
  'bwidth-glottal-sine': 100,
  'bwidth-nasal-pole': 100,
  'bwidth-nasal-zero': 100,
  'bwidth (1-6)': (50, 80, 60, 250, 200, 1000),
  'formant-gain (2-6)': (0, 0, 0, 0, 0),
  'formant-bypass-gain': 0,
  'formant-cascade-gain': 0,
  'formant-parallel-gain': 0,
  'voicing-linear-gain': 50,
  'voicing-sine-gain': 0,
  'nominal-duration': 125,
  'vowel': False,
  'nasal': False,
  'voice': True,
  'stop': False,
  'liquid': False,
  'regions': [LABIAL, DORSAL]
 },
 u'\u028d': { #ʍ
  'freq-glottal-pole': 0,
  'freq-glottal-zero': 1500,
  'freq-glottal-sine': 0,
  'freq-nasal-pole': 250,
  'freq-nasal-zero': 250,
  'freq (1-6)': (290, 610, 2150, 3300, 3750, 4900),
  'bwidth-glottal-pole': 100,
  'bwidth-glottal-zero': 6000,
  'bwidth-glottal-sine': 100,
  'bwidth-nasal-pole': 100,
  'bwidth-nasal-zero': 100,
  'bwidth (1-6)': (50, 80, 60, 250, 200, 1000),
  'formant-gain (2-6)': (0, 0, 0, 0, 0),
  'formant-bypass-gain': 0,
  'formant-cascade-gain': 0,
  'formant-parallel-gain': 0,
  'voicing-linear-gain': 50,
  'voicing-sine-gain': 0,
  'nominal-duration': 125,
  'vowel': False,
  'nasal': False,
  'voice': False,
  'stop': False,
  'liquid': False,
  'regions': [LABIAL, DORSAL]
 },
###############################################################################
 u'i': {
  'freq-glottal-pole': 0,
  'freq-glottal-zero': 1500,
  'freq-glottal-sine': 0,
  'freq-nasal-pole': 250,
  'freq-nasal-zero': 250,
  'freq (1-6)': (310, 2020, 2960, 3300, 3750, 4900),
  'bwidth-glottal-pole': 100,
  'bwidth-glottal-zero': 6000,
  'bwidth-glottal-sine': 100,
  'bwidth-nasal-pole': 100,
  'bwidth-nasal-zero': 100,
  'bwidth (1-6)': (45, 200, 400, 250, 200, 1000),
  'formant-gain (2-6)': (0, 0, 0, 0, 0),
  'formant-bypass-gain': 0,
  'formant-cascade-gain': 0,
  'formant-parallel-gain': 0,
  'voicing-linear-gain': 60,
  'voicing-sine-gain': 0,
  'nominal-duration': 175,
  'vowel': True,
  'nasal': False,
  'voice': True,
  'stop': False,
  'liquid': False,
  'regions': [FRONT]
 },
 u'e': {
  'freq-glottal-pole': 0,
  'freq-glottal-zero': 1500,
  'freq-glottal-sine': 0,
  'freq-nasal-pole': 250,
  'freq-nasal-zero': 250,
  'freq (1-6)': (480, 1720, 2520, 3300, 3750, 4900),
  'bwidth-glottal-pole': 100,
  'bwidth-glottal-zero': 6000,
  'bwidth-glottal-sine': 100,
  'bwidth-nasal-pole': 100,
  'bwidth-nasal-zero': 100,
  'bwidth (1-6)': (70, 100, 200, 250, 200, 1000),
  'formant-gain (2-6)': (0, 0, 0, 0, 0),
  'formant-bypass-gain': 0,
  'formant-cascade-gain': 0,
  'formant-parallel-gain': 0,
  'voicing-linear-gain': 60,
  'voicing-sine-gain': 0,
  'nominal-duration': 175,
  'vowel': True,
  'nasal': False,
  'voice': True,
  'stop': False,
  'liquid': False,
  'regions': [FRONT]
 },
 u'\u025b': { #ɛ
  'freq-glottal-pole': 0,
  'freq-glottal-zero': 1500,
  'freq-glottal-sine': 0,
  'freq-nasal-pole': 250,
  'freq-nasal-zero': 250,
  'freq (1-6)': (530, 1680, 2500, 3300, 3750, 4900),
  'bwidth-glottal-pole': 100,
  'bwidth-glottal-zero': 6000,
  'bwidth-glottal-sine': 100,
  'bwidth-nasal-pole': 100,
  'bwidth-nasal-zero': 100,
  'bwidth (1-6)': (60, 90, 200, 250, 200, 1000),
  'formant-gain (2-6)': (0, 0, 0, 0, 0),
  'formant-bypass-gain': 0,
  'formant-cascade-gain': 0,
  'formant-parallel-gain': 0,
  'voicing-linear-gain': 60,
  'voicing-sine-gain': 0,
  'nominal-duration': 175,
  'vowel': True,
  'nasal': False,
  'voice': True,
  'stop': False,
  'liquid': False,
  'regions': [NEAR_FRONT]
 },
 u'\xe6': { #æ
  'freq-glottal-pole': 0,
  'freq-glottal-zero': 1500,
  'freq-glottal-sine': 0,
  'freq-nasal-pole': 250,
  'freq-nasal-zero': 250,
  'freq (1-6)': (620, 1660, 2430, 3300, 3750, 4900),
  'bwidth-glottal-pole': 100,
  'bwidth-glottal-zero': 6000,
  'bwidth-glottal-sine': 100,
  'bwidth-nasal-pole': 100,
  'bwidth-nasal-zero': 100,
  'bwidth (1-6)': (70, 150, 320, 250, 200, 1000),
  'formant-gain (2-6)': (0, 0, 0, 0, 0),
  'formant-bypass-gain': 0,
  'formant-cascade-gain': 0,
  'formant-parallel-gain': 0,
  'voicing-linear-gain': 60,
  'voicing-sine-gain': 0,
  'nominal-duration': 175,
  'vowel': True,
  'nasal': False,
  'voice': True,
  'stop': False,
  'liquid': False,
  'regions': [NEAR_FRONT]
 },
 u'\u0251': { #ɑ
  'freq-glottal-pole': 0,
  'freq-glottal-zero': 1500,
  'freq-glottal-sine': 0,
  'freq-nasal-pole': 250,
  'freq-nasal-zero': 250,
  'freq (1-6)': (700, 1220, 2600, 3300, 3750, 4900),
  'bwidth-glottal-pole': 100,
  'bwidth-glottal-zero': 6000,
  'bwidth-glottal-sine': 100,
  'bwidth-nasal-pole': 100,
  'bwidth-nasal-zero': 100,
  'bwidth (1-6)': (130, 70, 160, 250, 200, 1000),
  'formant-gain (2-6)': (0, 0, 0, 0, 0),
  'formant-bypass-gain': 0,
  'formant-cascade-gain': 0,
  'formant-parallel-gain': 0,
  'voicing-linear-gain': 60,
  'voicing-sine-gain': 0,
  'nominal-duration': 175,
  'vowel': True,
  'nasal': False,
  'voice': True,
  'stop': False,
  'liquid': False,
  'regions': [CENTRAL]
 },
 u'I': {
  'freq-glottal-pole': 0,
  'freq-glottal-zero': 1500,
  'freq-glottal-sine': 0,
  'freq-nasal-pole': 250,
  'freq-nasal-zero': 250,
  'freq (1-6)': (400, 1800, 2570, 3300, 3750, 4900),
  'bwidth-glottal-pole': 100,
  'bwidth-glottal-zero': 6000,
  'bwidth-glottal-sine': 100,
  'bwidth-nasal-pole': 100,
  'bwidth-nasal-zero': 100,
  'bwidth (1-6)': (50, 100, 140, 250, 200, 1000),
  'formant-gain (2-6)': (0, 0, 0, 0, 0),
  'formant-bypass-gain': 0,
  'formant-cascade-gain': 0,
  'formant-parallel-gain': 0,
  'voicing-linear-gain': 60,
  'voicing-sine-gain': 0,
  'nominal-duration': 175,
  'vowel': True,
  'nasal': False,
  'voice': True,
  'stop': False,
  'liquid': False,
  'regions': [NEAR_FRONT]
 },
 u'\u0259': { #ə
  'freq-glottal-pole': 0,
  'freq-glottal-zero': 1500,
  'freq-glottal-sine': 0,
  'freq-nasal-pole': 250,
  'freq-nasal-zero': 250,
  'freq (1-6)': (500, 1400, 2300, 3300, 3750, 4900),
  'bwidth-glottal-pole': 100,
  'bwidth-glottal-zero': 6000,
  'bwidth-glottal-sine': 100,
  'bwidth-nasal-pole': 100,
  'bwidth-nasal-zero': 100,
  'bwidth (1-6)': (100, 60, 110, 250, 200, 1000),
  'formant-gain (2-6)': (0, 0, 0, 0, 0),
  'formant-bypass-gain': 0,
  'formant-cascade-gain': 0,
  'formant-parallel-gain': 0,
  'voicing-linear-gain': 50,
  'voicing-sine-gain': 0,
  'nominal-duration': 150,
  'vowel': True,
  'nasal': False,
  'voice': True,
  'stop': False,
  'liquid': False,
  'regions': [CENTRAL]
 },
 u'\u028a': { #ʊ
  'freq-glottal-pole': 0,
  'freq-glottal-zero': 1500,
  'freq-glottal-sine': 0,
  'freq-nasal-pole': 250,
  'freq-nasal-zero': 250,
  'freq (1-6)': (450, 1100, 2350, 3300, 3750, 4900),
  'bwidth-glottal-pole': 100,
  'bwidth-glottal-zero': 6000,
  'bwidth-glottal-sine': 100,
  'bwidth-nasal-pole': 100,
  'bwidth-nasal-zero': 100,
  'bwidth (1-6)': (80, 100, 80, 250, 200, 1000),
  'formant-gain (2-6)': (0, 0, 0, 0, 0),
  'formant-bypass-gain': 0,
  'formant-cascade-gain': 0,
  'formant-parallel-gain': 0,
  'voicing-linear-gain': 60,
  'voicing-sine-gain': 0,
  'nominal-duration': 150,
  'vowel': True,
  'nasal': False,
  'voice': True,
  'stop': False,
  'liquid': False,
  'regions': [NEAR_BACK]
 },
 u'u': {
  'freq-glottal-pole': 0,
  'freq-glottal-zero': 1500,
  'freq-glottal-sine': 0,
  'freq-nasal-pole': 250,
  'freq-nasal-zero': 250,
  'freq (1-6)': (350, 1250, 2200, 3300, 3750, 4900),
  'bwidth-glottal-pole': 100,
  'bwidth-glottal-zero': 6000,
  'bwidth-glottal-sine': 100,
  'bwidth-nasal-pole': 100,
  'bwidth-nasal-zero': 100,
  'bwidth (1-6)': (65, 110, 140, 250, 200, 1000),
  'formant-gain (2-6)': (0, 0, 0, 0, 0),
  'formant-bypass-gain': 0,
  'formant-cascade-gain': 0,
  'formant-parallel-gain': 0,
  'voicing-linear-gain': 60,
  'voicing-sine-gain': 0,
  'nominal-duration': 175,
  'vowel': True,
  'nasal': False,
  'voice': True,
  'stop': False,
  'liquid': False,
  'regions': [BACK]
 },
 u'o': {
  'freq-glottal-pole': 0,
  'freq-glottal-zero': 1500,
  'freq-glottal-sine': 0,
  'freq-nasal-pole': 250,
  'freq-nasal-zero': 250,
  'freq (1-6)': (540, 1100, 2300, 3300, 3750, 4900),
  'bwidth-glottal-pole': 100,
  'bwidth-glottal-zero': 6000,
  'bwidth-glottal-sine': 100,
  'bwidth-nasal-pole': 100,
  'bwidth-nasal-zero': 100,
  'bwidth (1-6)': (80, 70, 70, 250, 200, 1000),
  'formant-gain (2-6)': (0, 0, 0, 0, 0),
  'formant-bypass-gain': 0,
  'formant-cascade-gain': 0,
  'formant-parallel-gain': 0,
  'voicing-linear-gain': 60,
  'voicing-sine-gain': 0,
  'nominal-duration': 175,
  'vowel': True,
  'nasal': False,
  'voice': True,
  'stop': False,
  'liquid': False,
  'regions': [BACK]
 },
 u'\u028c': { #ʌ
  'freq-glottal-pole': 0,
  'freq-glottal-zero': 1500,
  'freq-glottal-sine': 0,
  'freq-nasal-pole': 250,
  'freq-nasal-zero': 250,
  'freq (1-6)': (620, 1220, 2550, 3300, 3750, 4900),
  'bwidth-glottal-pole': 100,
  'bwidth-glottal-zero': 6000,
  'bwidth-glottal-sine': 100,
  'bwidth-nasal-pole': 100,
  'bwidth-nasal-zero': 100,
  'bwidth (1-6)': (80, 50, 140, 250, 200, 1000),
  'formant-gain (2-6)': (0, 0, 0, 0, 0),
  'formant-bypass-gain': 0,
  'formant-cascade-gain': 0,
  'formant-parallel-gain': 0,
  'voicing-linear-gain': 60,
  'voicing-sine-gain': 0,
  'nominal-duration': 175,
  'vowel': True,
  'nasal': False,
  'voice': True,
  'stop': False,
  'liquid': False,
  'regions': [BACK]
 },
 u'\u0254': { #ɔ
  'freq-glottal-pole': 0,
  'freq-glottal-zero': 1500,
  'freq-glottal-sine': 0,
  'freq-nasal-pole': 250,
  'freq-nasal-zero': 250,
  'freq (1-6)': (600, 990, 2570, 3300, 3750, 4900),
  'bwidth-glottal-pole': 100,
  'bwidth-glottal-zero': 6000,
  'bwidth-glottal-sine': 100,
  'bwidth-nasal-pole': 100,
  'bwidth-nasal-zero': 100,
  'bwidth (1-6)': (90, 100, 80, 250, 200, 1000),
  'formant-gain (2-6)': (0, 0, 0, 0, 0),
  'formant-bypass-gain': 0,
  'formant-cascade-gain': 0,
  'formant-parallel-gain': 0,
  'voicing-linear-gain': 60,
  'voicing-sine-gain': 0,
  'nominal-duration': 175,
  'vowel': True,
  'nasal': False,
  'voice': True,
  'stop': False,
  'liquid': False,
  'regions': [BACK]
 },
###############################################################################
 u'd\u0292': { #dʒ
  'freq-glottal-pole': 0,
  'freq-glottal-zero': 1500,
  'freq-glottal-sine': 0,
  'freq-nasal-pole': 250,
  'freq-nasal-zero': 250,
  'freq (1-6)': (260, 1800, 2820, 3300, 3750, 4900),
  'bwidth-glottal-pole': 100,
  'bwidth-glottal-zero': 6000,
  'bwidth-glottal-sine': 100,
  'bwidth-nasal-pole': 100,
  'bwidth-nasal-zero': 100,
  'bwidth (1-6)': (60, 80, 270, 250, 200, 1000),
  'formant-gain (2-6)': (0, 22, 30, 26, 26),
  'formant-bypass-gain': 0,
  'formant-cascade-gain': 0,
  'formant-parallel-gain': 0,
  'voicing-linear-gain': 37,
  'voicing-sine-gain': 37,
  'nominal-duration': 125,
  'vowel': False,
  'nasal': False,
  'voice': True,
  'stop': False,
  'liquid': False,
  'regions': [CORONAL]
 },
 u't\u00283': { #tʃ
  'freq-glottal-pole': 0,
  'freq-glottal-zero': 1500,
  'freq-glottal-sine': 0,
  'freq-nasal-pole': 250,
  'freq-nasal-zero': 250,
  'freq (1-6)': (350, 1800, 2820, 3300, 3750, 4900),
  'bwidth-glottal-pole': 100,
  'bwidth-glottal-zero': 6000,
  'bwidth-glottal-sine': 100,
  'bwidth-nasal-pole': 100,
  'bwidth-nasal-zero': 100,
  'bwidth (1-6)': (200, 90, 300, 250, 200, 1000),
  'formant-gain (2-6)': (0, 22, 30, 26, 26),
  'formant-bypass-gain': 0,
  'formant-cascade-gain': 0,
  'formant-parallel-gain': 10,
  'voicing-linear-gain': 0,
  'voicing-sine-gain': 0,
  'nominal-duration': 125,
  'vowel': False,
  'nasal': False,
  'voice': False,
  'stop': False,
  'liquid': False,
  'regions': [CORONAL]
 },
 u'\u0251j': { #ɑj
  'freq-glottal-pole': 0,
  'freq-glottal-zero': 1500,
  'freq-glottal-sine': 0,
  'freq-nasal-pole': 250,
  'freq-nasal-zero': 250,
  'freq (1-6)': (660, 1200, 2550, 3300, 3750, 4900),
  'bwidth-glottal-pole': 100,
  'bwidth-glottal-zero': 6000,
  'bwidth-glottal-sine': 100,
  'bwidth-nasal-pole': 100,
  'bwidth-nasal-zero': 100,
  'bwidth (1-6)': (100, 70, 200, 250, 200, 1000),
  'formant-gain (2-6)': (0, 0, 0, 0, 0),
  'formant-bypass-gain': 0,
  'formant-cascade-gain': 0,
  'formant-parallel-gain': 0,
  'voicing-linear-gain': 60,
  'voicing-sine-gain': 0,
  'nominal-duration': 250,
  'vowel': True,
  'nasal': False,
  'voice': True,
  'stop': False,
  'liquid': False,
  'regions': [NEAR_FRONT, DORSAL]
 },
 u'\u0251w': { #ɑw
  'freq-glottal-pole': 0,
  'freq-glottal-zero': 1500,
  'freq-glottal-sine': 0,
  'freq-nasal-pole': 250,
  'freq-nasal-zero': 250,
  'freq (1-6)': (640, 1230, 2550, 3300, 3750, 4900),
  'bwidth-glottal-pole': 100,
  'bwidth-glottal-zero': 6000,
  'bwidth-glottal-sine': 100,
  'bwidth-nasal-pole': 100,
  'bwidth-nasal-zero': 100,
  'bwidth (1-6)': (80, 70, 140, 250, 200, 1000),
  'formant-gain (2-6)': (0, 0, 0, 0, 0),
  'formant-bypass-gain': 0,
  'formant-cascade-gain': 0,
  'formant-parallel-gain': 0,
  'voicing-linear-gain': 60,
  'voicing-sine-gain': 0,
  'nominal-duration': 250,
  'vowel': True,
  'nasal': False,
  'voice': True,
  'stop': False,
  'liquid': False,
  'regions': [NEAR_FRONT, LABIAL, DORSAL]
 },
 u'\u0254j': { #ɔj
  'freq-glottal-pole': 0,
  'freq-glottal-zero': 1500,
  'freq-glottal-sine': 0,
  'freq-nasal-pole': 250,
  'freq-nasal-zero': 250,
  'freq (1-6)': (550, 960, 2400, 3300, 3750, 4900),
  'bwidth-glottal-pole': 100,
  'bwidth-glottal-zero': 6000,
  'bwidth-glottal-sine': 100,
  'bwidth-nasal-pole': 100,
  'bwidth-nasal-zero': 100,
  'bwidth (1-6)': (80, 50, 130, 250, 200, 1000),
  'formant-gain (2-6)': (0, 0, 0, 0, 0),
  'formant-bypass-gain': 0,
  'formant-cascade-gain': 0,
  'formant-parallel-gain': 0,
  'voicing-linear-gain': 60,
  'voicing-sine-gain': 0,
  'nominal-duration': 250,
  'vowel': True,
  'nasal': False,
  'voice': True,
  'stop': False,
  'liquid': False,
  'regions': [BACK, DORSAL]
 },
} #: A neatly organized dictionary to make it easier for linguists to alter parameters.

#Reduce IPA data to efficient structures.
LIQUIDS = tuple([ipa_character for (ipa_character, details) in _IPA_MAPPING.iteritems() if details['liquid']]) #: A list of all liquid phonemes.
NASALS = tuple([ipa_character for (ipa_character, details) in _IPA_MAPPING.iteritems() if details['nasal']]) #: A list of all nasal phonemes.
STOPS = tuple([ipa_character for (ipa_character, details) in _IPA_MAPPING.iteritems() if details['stop']]) #: A list of all stop phonemes.
VOICED = tuple([ipa_character for (ipa_character, details) in _IPA_MAPPING.iteritems() if details['voice']]) #: A list of all voiced phonemes.
VOWELS = tuple([ipa_character for (ipa_character, details) in _IPA_MAPPING.iteritems() if details['vowel']]) #: A list of all vowel phonemes.
IPA_PARAMETERS = {} #: A collection of synthesizing parameter tuples, keyed by corresponding IPA character.
IPA_REGIONS = {} #: A collection of phoneme regions, keyed by corresponding IPA character.
IPA_DATA = {} #: A collection of both parameters and regions, in a tuple, keyed by corresponding IPA character.
_COMPLEX_CHARACTERS = {} #: A collection of multi-character IPA symboles, arranged in a tier.
for (ipa_character, details) in _IPA_MAPPING.iteritems():
	#Extract an ordered tuple of data from the dictionary.
	parameters = (
	 details['freq-glottal-pole'],
	 details['freq-glottal-zero'],
	 details['freq-glottal-sine'],
	 details['freq-nasal-pole'],
	 details['freq-nasal-zero'],
	) + details['freq (1-6)'] + (
	 details['bwidth-glottal-pole'],
	 details['bwidth-glottal-zero'],
	 details['bwidth-glottal-sine'],
	 details['bwidth-nasal-pole'],
	 details['bwidth-nasal-zero']
	) + details['bwidth (1-6)'] +	details['formant-gain (2-6)'] + (
	 details['formant-bypass-gain'],
	 details['formant-cascade-gain'],
	 details['formant-parallel-gain'],
	 details['voicing-linear-gain'],
	 details['voicing-sine-gain'],
	 details['nominal-duration']
	)
	regions = tuple(details['regions']) #Extract region data.
	
	#Place extracted data into more efficient indexes.
	IPA_PARAMETERS[ipa_character] = parameters
	IPA_REGIONS[ipa_character] = regions
	IPA_DATA[ipa_character] = (parameters, regions)
	
	if len(ipa_character) == 2: #It's a multi-character symbol.
		tails = _COMPLEX_CHARACTERS.get(ipa_character[0])
		if tails is None:
			tails = _COMPLEX_CHARACTERS[ipa_character[0]] = {}
		tails[ipa_character[1]] = ipa_character
del _IPA_MAPPING


def reduceIPAClusters(token):
	"""
	Returns the input word as a collection of IPA characters, condensing
	multi-character symbols into a single string, and leaving extension syntax
	unchanged.
	
	@type token: unicode
	@param token: The word to be reduced.
	
	@rtype: list
	@return: A list of all IPA characters in the input token, adjusted to handle
	    multi-character symbols, and containing all extension syntax.
	"""
	complex_characters = _COMPLEX_CHARACTERS #Cache for speed.
	extension_characters = (u'<', u'>', u'+', u'-')
	
	output = []
	consumed_next = False
	for (i, c) in enumerate(token[:-1]):
		if consumed_next: #Skip cycle.
			consumed_next = False
			continue
			
		if c in extension_characters: #Pass through extension syntax.
			output.append(c)
			continue
			
		#Determine whether this character forms part of a complex character.
		complex_tails = complex_characters.get(c)
		if complex_tails is None: #No match on the head.
			output.append(c)
			continue
		else: #Head matched. Check tail.
			complex_character = complex_tails.get(token[i + 1])
			if complex_character is None: #Tail didn't match, so just add head.
				output.append(c)
				continue
			else: #Tail matched, so add both the head and the tail, then skip the next cycle.
				consumed_next = True
				output.append(complex_character)
				continue
	if not consumed_next: #Don't add consumed terminals.
		output.append(token[-1])
		
	return output
	