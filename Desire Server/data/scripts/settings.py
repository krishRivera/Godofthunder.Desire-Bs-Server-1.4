import bs
from datetime import datetime
date = datetime.now().strftime('%d')

enableTop5effects = False

enableTop5commands = False

enableCoinSystem = False

enableStats = True

RainboweffectOwner = True

welcomeMessage = u"WELCOME TO STORMX Epic Teams\n make sure to join discord server"

chatfilter = ['cum','cumshot','boob','boobies','tit','titz','fuck','fucker','shit','shithead','pussy','PuSSy','fucked','bitch','bitches','bietch','sex','Sex','bastard','Fuck','Fucker']

name_filter = ['cum','cumshot','boob','boobies','tit','titz','fuck','fucker','shit','shithead','pussy','PuSSy','fucked','bitch','bitches','bietch','sex','Sex','bastard','Fuck','Fucker']

questionDelay = 2 #60 #seconds
questionsList = {'Which virus is spreading currently?': 'corona', 'Which country Corona is originated?': 'china', 'Effiel Tower is located in which city?': 'paris', 'Largest Planet in our solar system?': 'jupiter',
       'add': None, 
       'multiply': None}

availableCommands = {'/nv': 50, 
   '/ooh': 5, 
   '/playSound': 10, 
   '/box': 30, 
   '/boxall': 60, 
   '/spaz': 50, 
   '/spazall': 100, 
   '/inv': 40, 
   '/invall': 80, 
   '/tex': 20, 
   '/texall': 40, 
   '/freeze': 60, 
   '/freezeall': 100, 
   '/sleep': 40, 
   '/sleepall': 80, 
   '/thaw': 50, 
   '/thawall': 70, 
   '/kill': 80, 
   '/killall': 150, 
   '/end': 100, 
   '/hug': 60, 
   '/hugall': 100, 
   '/tint': 90, 
   '/sm': 50, 
   '/fly': 50, 
   '/flyall': 100, 
   '/heal': 50, 
   '/healall': 70, 
   '/gm': 200, 
   '/custom': 250}

availableEffects = {'ice': 500, 
   'sweat': 750, 
   'scorch': 500, 
   'glow': 400, 
   'distortion': 750, 
   'slime': 500, 
   'metal': 500, 
   'surrounder': 1000}
def return_yielded_game_texts():
    for text in gameTexts:
        yield text


def return_players_yielded(bs):
    for player in bs.getSession().players:
        yield player
