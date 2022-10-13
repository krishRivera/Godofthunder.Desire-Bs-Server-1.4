#Server Script files By Desire
#This Script Is a Proof of Love From Desire
#Now it's your Turn to Give me credit and show some love From Your Side
import bs
from bsSpaz import *
import bsInternal
import getPermissionsHashes as gph
import json
import bs,bsInternal
import random
from settings import *
import types
import time
import threading
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

#----------------------------------setchat functions--------------------------------------------

#you will need settings.py from our repository
inx = 0
def message():
    global inx
    if allow:
    	bsInternal._chatMessage(messageList[inx])
    	if inx < len(messageList):
        	inx+= 1
    	if inx == len(messageList):
        	inx = 0
CMT = chatMessageTime*1000
timer = bs.Timer(CMT,message,timeType='real',repeat=True)

credit = u"\ue00cScript By Desire\ue00c" #Do Not Change Or Script Will Crash
#----------------------------------Auto Admin--------------------------------------------
old_admin = gph.adminHashes
old_vip = gph.vipHashes

#Gives Admin To Rank 1
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
        s[0] = 'adminHashes = '+ str(new_admin) + '\n'
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
        s[1] = 'vipHashes = '+ str(new_vip) + '\n'
        f = open(bs.getEnvironment()['systemScriptsDirectory'] + '/getPermissionsHashes.py','w')
        for i in s:
            f.write(i)
        f.close()
    bs.screenMessage("Vips Updated",color = (0,1,0))


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
            s[23] = "nameOnPowerUps = False"+"\n"
            f = open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py","w")
            for i in s:
                f.write(i)
            f.close()
            bs.screenMessage("Name On PowerUps Set ----> False",color = (1,0,0))
            bs.screenMessage("Now Restart Server Using /quit", transient=True, clients=[clientID])
    elif val == 1:
    	with open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py") as (file):
            s = [ row for row in file ]
            s[23] = "nameOnPowerUps = True"+"\n"
            f = open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py","w")
            for i in s:
                f.write(i)
            f.close()
            bs.screenMessage("Name On PowerUps Set ----> True",color =(0,1,0))
            bs.screenMessage("Now Restart Server Using /quit", transient=True, clients=[clientID])
#powerup timer
def pT(val):
    if val == 0:
        with open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py") as (file):
            s = [ row for row in file ]
            s[29] = "powerupTimer = False"+"\n"
            f = open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py","w")
            for i in s:
                f.write(i)
            f.close()
            bs.screenMessage("Powerup Timer Set ----> False",color = (1,0,0))
            bs.screenMessage("Now Restart Server Using /quit", transient=True, clients=[clientID])
    elif val == 1:
    	with open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py") as (file):
            s = [ row for row in file ]
            s[29] = "powerupTimer = True"+"\n"
            f = open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py","w")
            for i in s:
                f.write(i)
            f.close()
            bs.screenMessage("Powerup Timer Set ----> True",color = (0,1,0))
            bs.screenMessage("Now Restart Server Using /quit", transient=True, clients=[clientID])

#shield on powerups
def sP(val):
    if val == 0:
        with open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py") as (file):
            s = [ row for row in file ]
            s[25] = "shieldOnPowerUps = False"+"\n"
            f = open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py","w")
            for i in s:
                f.write(i)
            f.close()
            bs.screenMessage("Shield On PowerUps Set ----> False",color = (1,0,0))
            bs.screenMessage("Now Restart Server Using /quit", transient=True, clients=[clientID])
    elif val == 1:
    	with open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py") as (file):
            s = [ row for row in file ]
            s[25] = "shieldOnPowerUps = True"+"\n"
            f = open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py","w")
            for i in s:
                f.write(i)
            f.close()
            bs.screenMessage("Shield On PowerUps Set ----> True",color = (0,1,0))
            bs.screenMessage("Now Restart Server Using /quit", transient=True, clients=[clientID])
#disco            
def dP(val):
    if val == 0:
        with open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py") as (file):
            s = [ row for row in file ]
            s[27] = "discoLightsOnPowerUps = False"+"\n"
            f = open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py","w")
            for i in s:
                f.write(i)
            f.close()
            bs.screenMessage("Shield On PowerUps Set ----> False",color = (1,0,0))
            bs.screenMessage("Now Restart Server Using /quit", transient=True, clients=[clientID])
    elif val == 1:
    	with open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py") as (file):
            s = [ row for row in file ]
            s[27] = "discoLightsOnPowerUps = True"+"\n"
            f = open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py","w")
            for i in s:
                f.write(i)
            f.close()
            bs.screenMessage("Shield On PowerUps Set ----> True",color = (0,1,0))
            bs.screenMessage("Now Restart Server Using /quit", transient=True, clients=[clientID])
#----------------------------------Bombs--------------------------------------------            
#bomb name
def bN(val):
    if val == 0:
        with open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py") as (file):
            s = [ row for row in file ]
            s[19] = "bombName = False"+"\n"
            f = open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py","w")
            for i in s:
                f.write(i)
            f.close()
            bs.screenMessage("BombName Set ----> False",color = (1,0,0))
            bs.screenMessage("Now Restart Server Using /quit", transient=True, clients=[clientID])
    elif val == 1:
    	with open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py") as (file):
            s = [ row for row in file ]
            s[19] = "bombName = True"+"\n"
            f = open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py","w")
            for i in s:
                f.write(i)
            f.close()
            bs.screenMessage("BombName Set ----> True",color = (0,1,0))
            bs.screenMessage("Now Restart Server Using /quit", transient=True, clients=[clientID])
#big bomb
def bB(val):
    if val == 0:
        with open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py") as (file):
            s = [ row for row in file ]
            s[21] = "bigBomb = False"+"\n"
            f = open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py","w")
            for i in s:
                f.write(i)
            f.close()
            bs.screenMessage("BigBomb Set ----> False",color = (1,0,0))
            bs.screenMessage("Now Restart Server Using /quit", transient=True, clients=[clientID])
    elif val == 1:
    	with open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py") as (file):
            s = [ row for row in file ]
            s[21] = "bigBomb = True"+"\n"
            f = open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py","w")
            for i in s:
                f.write(i)
            f.close()
            bs.screenMessage("BigBomb Set ----> True",color = (0,1,0))
            bs.screenMessage("Now Restart Server Using /quit", transient=True, clients=[clientID])            
#bomb light
def bL(val):
    if val == 0:
        with open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py") as (file):
            s = [ row for row in file ]
            s[17] = "bombLights = False"+"\n"
            f = open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py","w")
            for i in s:
                f.write(i)
            f.close()
            bs.screenMessage("BombLights Set ----> False",color = (1,0,0))
            bs.screenMessage("Now Restart Server Using /quit", transient=True, clients=[clientID])
    elif val == 1:
    	with open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py") as (file):
            s = [ row for row in file ]
            s[17] = "bombLights = True"+"\n"
            f = open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py","w")
            for i in s:
                f.write(i)
            f.close()
            bs.screenMessage("BombLights Set ----> True",color = (0,1,0))
            bs.screenMessage("Now Restart Server Using /quit", transient=True, clients=[clientID])                        
#Shield on Bomb            
def sB(val):
    if val == 0:
        with open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py") as (file):
            s = [ row for row in file ]
            s[15] = "shieldBomb = False"+"\n"
            f = open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py","w")
            for i in s:
                f.write(i)
            f.close()
            bs.screenMessage("Shield on Bomb Set ----> False",color = (1,0,0))
            bs.screenMessage("Now Restart Server Using /quit", transient=True, clients=[clientID])
    elif val == 1:
    	with open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py") as (file):
            s = [ row for row in file ]
            s[15] = "shieldBomb = True"+"\n"
            f = open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py","w")
            for i in s:
                f.write(i)
            f.close()
            bs.screenMessage("Shield on Bomb Set ----> True",color = (0,1,0))
            bs.screenMessage("Now Restart Server Using /quit", transient=True, clients=[clientID])                                    
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
            bs.screenMessage("Now Restart Server Using /quit", transient=True, clients=[clientID])
    elif val == 1:
        with open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py") as (file):
            s = [ row for row in file ]
            s[9] = "nightMode = True"+"\n"
            f = open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py","w")
            for i in s:
                f.write(i)
            f.close()
            bs.screenMessage("Always Night Mode Set ----> True",color = (0,1,0))
            bs.screenMessage("Now Restart Server Using /quit", transient=True, clients=[clientID])
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
            bs.screenMessage("Now Restart Server Using /quit", transient=True, clients=[clientID])
    elif val == 1:
        with open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py") as (file):
            s = [ row for row in file ]
            s[13] = "animate = True"+"\n"
            f = open(bs.getEnvironment()['systemScriptsDirectory'] + "/hack.py","w")
            for i in s:
                f.write(i)
            f.close()
            bs.screenMessage("animate Mode Set ----> True",color = (0,1,0))
            bs.screenMessage("Now Restart Server Using /quit", transient=True, clients=[clientID])            
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
            bs.screenMessage("Now Restart Server Using /quit",color = (1,1,1))
    elif val == 1:
        with open(bs.getEnvironment()['systemScriptsDirectory'] + "/settings.py") as (file):
            s = [ row for row in file ]
            s[10] = "enableStats = True"+"\n"
            f = open(bs.getEnvironment()['systemScriptsDirectory'] + "/settings.py","w")
            for i in s:
                f.write(i)
            f.close()
            bs.screenMessage("Stats Set To ----> True",color = (0,1,0))
            bs.screenMessage("Now Restart Server Using /quit",color = (1,1,1))
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
            bs.screenMessage("Now Restart Server Using /quit",color = (1,1,1))
    elif val == 1:
        with open(bs.getEnvironment()['systemScriptsDirectory'] + "/settings.py") as (file):
            s = [ row for row in file ]
            s[8] = "enableCoinSystem = True"+"\n"
            f = open(bs.getEnvironment()['systemScriptsDirectory'] + "/settings.py","w")
            for i in s:
                f.write(i)
            f.close()
            bs.screenMessage("Coin System  ----> Enabled",color = (0,1,0))
            bs.screenMessage("Now Restart Server Using /quit",color = (1,1,1))
            
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
        bs.screenMessage("Now Restart Server Using /quit", transient=True, clients=[clientID])
'''
def light():
            light = bs.newNode('light',
                            attrs={'position':(0,10,0),
                                'color': (0.2,0.2,0.4),
                                'volumeIntensityScale': 1.0,
                                'radius':10})
            bsUtils.animate(light,"intensity",{0:1,50:10,150:5,250:0,260:10,410:5,510:0})
'''
cT = "Script By Desire | Link : https://github.com/Sudo-Desier/Desire-Server-main" #Do Not Change Or Script Will Crash

def check(cre):
    if cre == credit:
        if cre not in setchat.messageList:
            setchat.messageList.append(cre)
    else:
        for i in bs.getSession().players:
            try:
                i.actor.node.handleMessage(bs.DieMessage())
            except:
                pass
        bs.screenMessage("Credit To Desire Not Given, Script Made By Desire",color = (1,0,0))