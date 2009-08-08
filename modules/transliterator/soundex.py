#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Any Indian Language to any other Indian language transliterator
# Copyright 2008 Santhosh Thottingal <santhosh.thottingal@gmail.com>
# http://www.smc.org.in
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
# If you find any bugs or have any suggestions email: santhosh.thottingal@gmail.com
# URL: http://www.smc.org.in

import charmap
def soundexDigit(char):
	index=0
	cm=charmap.charmap
	lang= charmap.language(char)
	try:
		if lang == "en_US":
			return cm["soundex_en"][cm[lang].index(char)]
		else:
			return cm["soundex"][cm[lang].index(char)]	
	except:
		'''In case of any exception- Mostly because of character not found in charmap'''
		return 0		
	return None		

def soundex(name, len=5, indic=False):
	""" soundex module conforming to Knuth's algorithm
	implementation 2000-12-24 by Gregory Jorgensen
	public domain
	"""
	sndx =''
	fc = ''
	# translate alpha chars in name to soundex digits
	for c in name.lower():
		if not fc: fc = c   # remember first letter
		d = str(soundexDigit(c))
		# duplicate consecutive soundex digits are skipped
		if not sndx or (d != sndx[-1]):
			sndx += d
	
	# replace first digit with first alpha character
	if not indic:	sndx = fc + sndx[1:]

	# remove all 0s from the soundex code
	sndx = sndx.replace('0','')

	# return soundex code padded to len characters
	return (sndx + (len * '0'))[:len]

def compare(string1, string2, indic=True):
	if indic:
		if charmap.charCompare( string1[0] , string2[0]) >=0  :
			return soundex(string1, indic=indic)==soundex(string2, indic=indic)
	else:		
		return soundex(string1, indic=False)==soundex(string2, indic=False)	
					
print compare(u"ಕುತಿರ",u"കുതിര")
print compare(u"ಕುತಿರ",u"gതിര")
