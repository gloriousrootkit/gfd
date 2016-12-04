#!/usr/bin/env python

import ConfigParser
import shutil
import time

def ConfigSectionMap(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1


Config = ConfigParser.ConfigParser()
Config.read("nastaveni.ini")

c1 = ConfigSectionMap("cestaksouborum")['c1']
mist = ConfigSectionMap("Nastaveni")['xf']
mistozalohavni = ConfigSectionMap("mistozalohavni")['cesta']
startup = ConfigSectionMap("Nastaveni")['startupstart']



celkovypocet = mist #celkovy pocet mist
cecko = 0
now = 0 #startovni pozice
c = 6
zapsano = 0
try:
	while now < 99:
		cecko += 1
		now += 1
		celkem = ("c%s" % cecko) 
		celkem = ConfigSectionMap("cestaksouborum")[celkem]
		shutil.copy2(celkem, mistozalohavni)
		logs = open('zaloha.log', 'a')
		datal = (time.strftime("%d/%m/%Y"))
		timel = (time.strftime("%H:%M:%S"))
		logs.write ('%s-%s - Soubory zalohovany uspesne\n' % (datal, timel))
		print celkem
except:
	pass