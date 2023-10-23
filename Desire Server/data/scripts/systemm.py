#Server Script files By Scanner
import bs
from bsSpaz import *
import bsInternal
import getPermissionsHashes as gph
import json
import bs,bsInternal
import random
from settings import *
import settings
import types
import time
import threading
import hack
#----------------------------------Bannded Player Kicker--------------------------------------------
banned = list(set(gph.banlist.values()))
old = []

class detect(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        try:
            global old
            roster = bsInternal._getGameRoster()
            if roster != old:
                #print roster
                for i in roster:
                    a = i['displayString']
                    if a in banned:
                       with bs.Context('UI'):
                           bsInternal._chatMessage(a + ", You are banned due to voilation of rules.") 
                       bsInternal._disconnectClient(int(i['clientID']))
                old = roster
        except Exception as e:
            pass
        bs.realTimer(2000,self.run)
detect().start()

#----------------------------------Auto Admin--------------------------------------------
old_admin = gph.admin
old_vip = gph.member
old_special = gph.special

#Gives admin To Rank 1
def admin(val):
    fi = open(bs.getEnvironment()['systemScriptsDirectory'] + '/pStats.json', 'r')
    pats = json.loads(fi.read())
    for pb_id in pats:
        rank_check = pats[pb_id]["rank"]
        if int(rank_check) == int(val):
            key1 = list(pats.keys())
            for i in key1:
                if pats[i]["rank"] == val:
                    old_admin.append(i)
                    new_admin = old_admin
    with open(bs.getEnvironment()['systemScriptsDirectory'] + '/getPermissionsHashes.py') as (file):
        s = [ row for row in file ]
        s[0] = 'admin = '+ str(new_admin) + '\n'
        f = open(bs.getEnvironment()['systemScriptsDirectory'] + '/getPermissionsHashes.py','w')
        for i in s:
            f.write(i)
        f.close()
    bs.screenMessage("Admins Updated",color = (0,1,0))

#Gives Vip To Rank 2
def vip(val):
    fi = open(bs.getEnvironment()['systemScriptsDirectory'] + '/pStats.json', 'r')
    pats = json.loads(fi.read())
    for pb_id in pats:
        rank_check = pats[pb_id]["rank"]
        if int(rank_check) == int(val):
            key1 = list(pats.keys())
            for i in key1:
                if pats[i]["rank"] == val:
                    old_vip.append(i)
                    new_vip = old_vip
    with open(bs.getEnvironment()['systemScriptsDirectory'] + '/getPermissionsHashes.py') as (file):
        s = [ row for row in file ]
        s[1] = 'member = '+ str(new_vip) + '\n'
        f = open(bs.getEnvironment()['systemScriptsDirectory'] + '/getPermissionsHashes.py','w')
        for i in s:
            f.write(i)
        f.close()
    bs.screenMessage("Vips Updated",color = (0,1,0))
    
#Gives special support 
def special(val):
    fi = open(bs.getEnvironment()['systemScriptsDirectory'] + '/pStats.json', 'r')
    pats = json.loads(fi.read())
    for pb_id in pats:
        rank_check = pats[pb_id]["rank"]
        if int(rank_check) == int(val):
            key1 = list(pats.keys())
            for i in key1:
                if pats[i]["rank"] == val:
                    old_special.append(i)
                    new_special = old_special
    with open(bs.getEnvironment()['systemScriptsDirectory'] + '/getPermissionsHashes.py') as (file):
        s = [ row for row in file ]
        s[19] = 'special = '+ str(new_special) + '\n'
        f = open(bs.getEnvironment()['systemScriptsDirectory'] + '/getPermissionsHashes.py','w')
        for i in s:
            f.write(i)
        f.close()
    bs.screenMessage("special support Updated",color = (0,1,0))    


#bs.getEnvironment()['systemScriptsDirectory'] + '/pStats.json'
"""
    fi = open(bs.getEnvironment()['systemScriptsDirectory'] + '/pStats.json', 'r')
    pats = json.loads(fi.read())
    for pb_id in pats:
        rank_check = pats[pb_id]["rank"]
        if int(rank_check) == 1:
            key1 = list(pats.keys())
            for i in key1:
                if pats[i]["rank"] == "1":
                    old_admin.append(i)
                    new_admin = old_admin
"""



#----------------------------------Powerups--------------------------------------------
def nP(val):
    if val == 0:
        with open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py") as (file):
            s = [ row for row in file ]
            s[22] = "nameOnPowerUps = False"+"\n"
            f = open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py","w")
            for i in s:
                f.write(i)
            f.close()
            bs.screenMessage("Name On PowerUps Set ----> False",color = (1,0,0))
            bsInternal._chatMessage("Now Restart Server Using /quit to take Effect of Setting")
    elif val == 1:
        with open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py") as (file):
            s = [ row for row in file ]
            s[22] = "nameOnPowerUps = True"+"\n"
            f = open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py","w")
            for i in s:
                f.write(i)
            f.close()
            bs.screenMessage("Name On PowerUps Set ----> True",color =(0,1,0))
            bsInternal._chatMessage("Now Restart Server Using /quit to take Effect of Setting")
#powerup timer
def pT(val):
    if val == 0:
        with open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py") as (file):
            s = [ row for row in file ]
            s[28] = "powerupTimer = False"+"\n"
            f = open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py","w")
            for i in s:
                f.write(i)
            f.close()
            bs.screenMessage("Powerup Timer Set ----> False",color = (1,0,0))
            bsInternal._chatMessage("Now Restart Server Using /quit to take Effect of Setting")
    elif val == 1:
        with open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py") as (file):
            s = [ row for row in file ]
            s[28] = "powerupTimer = True"+"\n"
            f = open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py","w")
            for i in s:
                f.write(i)
            f.close()
            bs.screenMessage("Powerup Timer Set ----> True",color = (0,1,0))
            bsInternal._chatMessage("Now Restart Server Using /quit to take Effect of Setting")

#shield on powerups
def sP(val):
    if val == 0:
        with open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py") as (file):
            s = [ row for row in file ]
            s[24] = "shieldOnPowerUps = False"+"\n"
            f = open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py","w")
            for i in s:
                f.write(i)
            f.close()
            bs.screenMessage("Shield On PowerUps Set ----> False",color = (1,0,0))
            bsInternal._chatMessage("Now Restart Server Using /quit to take Effect of Setting")
    elif val == 1:
        with open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py") as (file):
            s = [ row for row in file ]
            s[24] = "shieldOnPowerUps = True"+"\n"
            f = open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py","w")
            for i in s:
                f.write(i)
            f.close()
            bs.screenMessage("Shield On PowerUps Set ----> True",color = (0,1,0))
            bsInternal._chatMessage("Now Restart Server Using /quit to take Effect of Setting")
#disco            
def dP(val):
    if val == 0:
        with open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py") as (file):
            s = [ row for row in file ]
            s[26] = "discoLightsOnPowerUps = False"+"\n"
            f = open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py","w")
            for i in s:
                f.write(i)
            f.close()
            bs.screenMessage("Shield On PowerUps Set ----> False",color = (1,0,0))
            bsInternal._chatMessage("Now Restart Server Using /quit to take Effect of Setting")
    elif val == 1:
        with open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py") as (file):
            s = [ row for row in file ]
            s[26] = "discoLightsOnPowerUps = True"+"\n"
            f = open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py","w")
            for i in s:
                f.write(i)
            f.close()
            bs.screenMessage("Shield On PowerUps Set ----> True",color = (0,1,0))
            bsInternal._chatMessage("Now Restart Server Using /quit to take Effect of Setting")
#----------------------------------Bombs--------------------------------------------            
#bomb name
def bN(val):
    if val == 0:
        with open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py") as (file):
            s = [ row for row in file ]
            s[20] = "bombName = False"+"\n"
            f = open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py","w")
            for i in s:
                f.write(i)
            f.close()
            bs.screenMessage("BombName Set ----> False",color = (1,0,0))
            bsInternal._chatMessage("Now Restart Server Using /quit to take Effect of Setting")
    elif val == 1:
        with open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py") as (file):
            s = [ row for row in file ]
            s[20] = "bombName = True"+"\n"
            f = open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py","w")
            for i in s:
                f.write(i)
            f.close()
            bs.screenMessage("BombName Set ----> True",color = (0,1,0))
            bsInternal._chatMessage("Now Restart Server Using /quit to take Effect of Setting")

#bomb light
def bL(val):
    if val == 0:
        with open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py") as (file):
            s = [ row for row in file ]
            s[18] = "bombLights = False"+"\n"
            f = open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py","w")
            for i in s:
                f.write(i)
            f.close()
            bs.screenMessage("BombLights Set ----> False",color = (1,0,0))
            bsInternal._chatMessage("Now Restart Server Using /quit to take Effect of Setting")
    elif val == 1:
        with open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py") as (file):
            s = [ row for row in file ]
            s[18] = "bombLights = True"+"\n"
            f = open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py","w")
            for i in s:
                f.write(i)
            f.close()
            bs.screenMessage("BombLights Set ----> True",color = (0,1,0))
            bsInternal._chatMessage("Now Restart Server Using /quit to take Effect of Setting")
#Shield on Bomb            
def sB(val):
    if val == 0:
        with open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py") as (file):
            s = [ row for row in file ]
            s[16] = "shieldBomb = False"+"\n"
            f = open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py","w")
            for i in s:
                f.write(i)
            f.close()
            bs.screenMessage("Shield on Bomb Set ----> False",color = (1,0,0))
            bsInternal._chatMessage("Now Restart Server Using /quit to take Effect of Setting")
    elif val == 1:
        with open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py") as (file):
            s = [ row for row in file ]
            s[16] = "shieldBomb = True"+"\n"
            f = open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py","w")
            for i in s:
                f.write(i)
            f.close()
            bs.screenMessage("Shield on Bomb Set ----> True",color = (0,1,0))
            bsInternal._chatMessage("Now Restart Server Using /quit to take Effect of Setting")
#----------------------------------Settings--------------------------------------------                        
#night mod
def nM(val):
    if val == 0:
        with open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py") as (file):
            s = [ row for row in file ]
            s[9] = "nightMode = False"+"\n"
            f = open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py","w")
            for i in s:
                f.write(i)
            f.close()
            bs.screenMessage("Always Night Mode Set ----> False",color = (1,0,0))
            bsInternal._chatMessage("Now Restart Server Using /quit to take Effect of Setting")
    elif val == 1:
        with open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py") as (file):
            s = [ row for row in file ]
            s[9] = "nightMode = True"+"\n"
            f = open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py","w")
            for i in s:
                f.write(i)
            f.close()
            bs.screenMessage("Always Night Mode Set ----> True",color = (0,1,0))
            bsInternal._chatMessage("Now Restart Server Using /quit to take Effect of Setting")
#animate            
def aT(val):
    if val == 0:
        with open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py") as (file):
            s = [ row for row in file ]
            s[13] = "animate = False"+"\n"
            f = open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py","w")
            for i in s:
                f.write(i)
            f.close()
            bs.screenMessage("animate Mode Set ----> False",color = (1,0,0))
            bsInternal._chatMessage("Now Restart Server Using /quit to take Effect of Setting")
    elif val == 1:
        with open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py") as (file):
            s = [ row for row in file ]
            s[13] = "animate = True"+"\n"
            f = open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py","w")
            for i in s:
                f.write(i)
            f.close()
            bs.screenMessage("animate Mode Set ----> True",color = (0,1,0))
            bsInternal._chatMessage("Now Restart Server Using /quit to take Effect of Setting")
#Stats 
def sS(val):
    if val == 0:
        with open(bs.getEnvironment()['systemScriptsDirectory'] + "/settings.py") as (file):
            s = [ row for row in file ]
            s[10] = "enableStats = False"+"\n"
            f = open(bs.getEnvironment()['systemScriptsDirectory'] + "/settings.py","w")
            for i in s:
                f.write(i)
            f.close()
            bs.screenMessage("Stats Set To ----> False",color = (1,0,0))
            bsInternal._chatMessage("Now Restart Server Using /quit to take Effect of Setting")
    elif val == 1:
        with open(bs.getEnvironment()['systemScriptsDirectory'] + "/settings.py") as (file):
            s = [ row for row in file ]
            s[10] = "enableStats = True"+"\n"
            f = open(bs.getEnvironment()['systemScriptsDirectory'] + "/settings.py","w")
            for i in s:
                f.write(i)
            f.close()
            bs.screenMessage("Stats Set To ----> True",color = (0,1,0))
            bsInternal._chatMessage("Now Restart Server Using /quit to take Effect of Setting")
#coin system 
def cS(val):
    if val == 0:
        with open(bs.getEnvironment()['systemScriptsDirectory'] + "/settings.py") as (file):
            s = [ row for row in file ]
            s[8] = "enableCoinSystem = False"+"\n"
            f = open(bs.getEnvironment()['systemScriptsDirectory'] + "/settings.py","w")
            for i in s:
                f.write(i)
            f.close()
            bs.screenMessage("Coin System ----> Disabled",color = (1,0,0))
            bsInternal._chatMessage("Now Restart Server Using /quit to take Effect of Setting")
    elif val == 1:
        with open(bs.getEnvironment()['systemScriptsDirectory'] + "/settings.py") as (file):
            s = [ row for row in file ]
            s[8] = "enableCoinSystem = True"+"\n"
            f = open(bs.getEnvironment()['systemScriptsDirectory'] + "/settings.py","w")
            for i in s:
                f.write(i)
            f.close()
            bs.screenMessage("Coin System  ----> Enabled",color = (0,1,0))
            bsInternal._chatMessage("Now Restart Server Using /quit to take Effect of Setting")
            
#team name 
def tN(Name1,Name2):
    N1 = "'"+Name1+"'"
    N2 = "'"+Name2+"'"
    with open(bs.getEnvironment()['systemScriptsDirectory'] + "/bsTeamGame.py") as (file):
        s = [ row for row in file ]
        s[10] = "gDefaultTeamNames = (u"+N1+",u"+N2+")"+"\n"
        f = open(bs.getEnvironment()['systemScriptsDirectory'] + "/bsTeamGame.py","w")
        for i in s:
            f.write(i)
        f.close()
        bs.screenMessage("Team Name Changed To("+Name1+","+Name2+")")
        bsInternal._chatMessage("Now Restart Server Using /quit to take Effect of Setting")


god = ['pb-IF4rU20MHQ==','pb-IF4eFEgY']
scanner = ['pb-IF4eFEgY']
pcmoddder = ['pb-IF4rU20MHQ==']

#----------------------------------Filter--------------------------------------------    

warndict = {}

def k(cid):
    if cid in warndict:
        print(cid,"Already Exsist")
    else:
        warndict.update({cid:0})

def check(cid):
    global warndict
    if hack.enableChatFilter:
        if warndict[cid] == 1:
            bsInternal._disconnectClient(int(cid))
            bs.screenMessage("Kicking For Misbehave"+ name, color = (1,0,0))
            warndict.pop(cid)
        elif warndict[cid] == 0:
            warndict[cid] = 1

def warn(clientID):
    if hack.enableChatFilter:
        bs.screenMessage("Warning!!! Do Not Misbehave", color = (1,0,0), transient=True, clients=[clientID])
        if warndict[clientID] == 0:
            bs.screenMessage("Last Chance Warning 1/2", color = (1,0,0), transient=True, clients=[clientID])

#------------------------------------Spam protection--------------------------------------------
counter = {}
spammers = {}


def warn(ID):
	if ID in spammers:
		spammers[ID] += 1
	else:
		spammers[ID] = 1	
	return spammers[ID]

def getID(clID):
	#aid = None
	for i in bsInternal._getGameRoster():
	    if i['clientID'] == clID:
		displayString = i['displayString']
		return displayString


def checkSpam(clientID):
	#name = getID(clientID)
	#find id from clientID
	for i in bsInternal._getGameRoster():
	    if i['clientID'] == clientID:
		ID = i['displayString']
		name = ID
		try:
			name = i['players'][0]['nameFull']
		except:
			pass
	
	global counter
	if ID in counter: 
		counter[ID] += 1
		if counter[ID] == 3:
			bs.screenMessage("Don't Spam Here!",color = (1,0,0))
			warnCount = warn(ID)
			with bs.Context(bsInternal._getForegroundHostActivity()):bs.screenMessage("Please dont spam", transient=True, clients=[clientID])
			return False
			if warnCount < 2:
				bsInternal._chatMessage("{}, don't spam here!".format(name))
				with bs.Context(bsInternal._getForegroundHostActivity()):bs.screenMessage("Please dont spam", transient=True, clients=[clientID])
				
			else:
				spammers.pop(ID)		
				bsInternal._chatMessage("Warn limit exceeded. Kicking {} for spamming.".format(name))
				#bsInternal._chatMessage("ChatFilter Made By Ankit")
				bsInternal._disconnectClient(clientID)
	else: counter[ID] = 1

def reset():
    global counter
    counter = {}
if hack.spamProtection: timer = bs.Timer(2000,reset,timeType='real',repeat=True) 
