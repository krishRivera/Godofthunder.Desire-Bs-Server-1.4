import bs
import random
import bsUtils
import hack
import BuddyBunny

defaultPowerupInterval = 8000

class PowerupMessage(object):
    """
    category: Message Classes

    Tell something to get a powerup.
    This message is normally recieved by touching
    a bs.Powerup box.
    
    Attributes:
    
       powerupType
          The type of powerup to be granted (a string).
          See bs.Powerup.powerupType for available type values.

       sourceNode
          The node the powerup game from, or an empty bs.Node ref otherwise.
          If a powerup is accepted, a bs.PowerupAcceptMessage should be sent
          back to the sourceNode to inform it of the fact. This will generally
          cause the powerup box to make a sound and disappear or whatnot.
    """
    def __init__(self,powerupType,sourceNode=bs.Node(None)):
        """
        Instantiate with given values.
        See bs.Powerup.powerupType for available type values.
        """
        self.powerupType = powerupType
        self.sourceNode = sourceNode

class PowerupAcceptMessage(object):
    """
    category: Message Classes

    Inform a bs.Powerup that it was accepted.
    This is generally sent in response to a bs.PowerupMessage
    to inform the box (or whoever granted it) that it can go away.
    """
    pass

class _TouchedMessage(object):
    pass

class SleepMessage(object):
    pass

class PowerupFactory(object):
    """
    category: Game Flow Classes
    
    Wraps up media and other resources used by bs.Powerups.
    A single instance of this is shared between all powerups
    and can be retrieved via bs.Powerup.getFactory().

    Attributes:

       model
          The bs.Model of the powerup box.

       modelSimple
          A simpler bs.Model of the powerup box, for use in shadows, etc.

       texBox
          Triple-bomb powerup bs.Texture.

       texPunch
          Punch powerup bs.Texture.

       texIceBombs
          Ice bomb powerup bs.Texture.

       texStickyBombs
          Sticky bomb powerup bs.Texture.

       texShield
          Shield powerup bs.Texture.

       texImpactBombs
          Impact-bomb powerup bs.Texture.

       texHealth
          Health powerup bs.Texture.

       texLandMines
          Land-mine powerup bs.Texture.

       texCurse
          Curse powerup bs.Texture.

       healthPowerupSound
          bs.Sound played when a health powerup is accepted.

       powerupSound
          bs.Sound played when a powerup is accepted.

       powerdownSound
          bs.Sound that can be used when powerups wear off.

       powerupMaterial
          bs.Material applied to powerup boxes.

       powerupAcceptMaterial
          Powerups will send a bs.PowerupMessage to anything they touch
          that has this bs.Material applied.
    """

    def __init__(self):
        """
        Instantiate a PowerupFactory.
        You shouldn't need to do this; call bs.Powerup.getFactory()
        to get a shared instance.
        """

        self._lastPowerupType = None

        self.model = bs.getModel("powerup")
        self.modelSimple = bs.getModel("powerupSimple")

        self.texBomb = bs.getTexture("powerupBomb")
        self.texPunch = bs.getTexture("powerupPunch")
        self.texIceBombs = bs.getTexture("powerupIceBombs")
        self.texStickyBombs = bs.getTexture("powerupStickyBombs")
        self.texShield = bs.getTexture("powerupShield")
        self.texImpactBombs = bs.getTexture("powerupImpactBombs")
        self.texBanana = bs.getTexture("menuButton")
        self.texGod = bs.getTexture("powerupSpeed")
        self.texArtillery = bs.getTexture('buttonBomb')
        self.shockWaveTex = bs.getTexture('smoke')
        self.texRadioactiveBombs = bs.getTexture("rgbStripes")
        self.texHighJump = bs.getTexture('buttonJump')
        self.texEnderPearls = bs.getTexture("ouyaOButton")
        self.texStickyForce = bs.getTexture("ouyaUButton")       
        self.texHealth = bs.getTexture("powerupHealth")
        self.texSleepPotionBombs = bs.getTexture("ouyaYButton")
        self.texLandMines = bs.getTexture("powerupLandMines")
        self.texElonMuskMine = bs.getTexture('achievementMine')
        self.texweedbomb = bs.getTexture("egg2")
        self.texParty = bs.getTexture("eggTex1")
        self.texBunny = bs.getTexture('achievementFreeLoader')
        self.texRchar = bs.getTexture("achievementEmpty")
        self.texInv = bs.getTexture("achievementMedalSmall")
        self.texCurse = bs.getTexture("powerupCurse")

        self.healthPowerupSound = bs.getSound("healthPowerup")
        self.powerupSound = bs.getSound("powerup01")
        self.powerdownSound = bs.getSound("powerdown01")
        self.dropSound = bs.getSound("boxDrop")

        # material for powerups
        self.powerupMaterial = bs.Material()

        # material for anyone wanting to accept powerups
        self.powerupAcceptMaterial = bs.Material()

        # pass a powerup-touched message to applicable stuff
        self.powerupMaterial.addActions(
            conditions=(("theyHaveMaterial",self.powerupAcceptMaterial)),
            actions=(("modifyPartCollision","collide",True),
                     ("modifyPartCollision","physical",False),
                     ("message","ourNode","atConnect",_TouchedMessage())))

        # we dont wanna be picked up
        self.powerupMaterial.addActions(
            conditions=("theyHaveMaterial",
                        bs.getSharedObject('pickupMaterial')),
            actions=( ("modifyPartCollision","collide",False)))

        self.powerupMaterial.addActions(
            conditions=("theyHaveMaterial",
                        bs.getSharedObject('footingMaterial')),
            actions=(("impactSound",self.dropSound,0.5,0.1)))

        self._powerupDist = []
        for p,freq in getDefaultPowerupDistribution():
            for i in range(int(freq)):
                self._powerupDist.append(p)

    def getRandomPowerupType(self,forceType=None,excludeTypes=['punch','shield']):
        """
        Returns a random powerup type (string).
        See bs.Powerup.powerupType for available type values.

        There are certain non-random aspects to this; a 'curse' powerup,
        for instance, is always followed by a 'health' powerup (to keep things
        interesting). Passing 'forceType' forces a given returned type while
        still properly interacting with the non-random aspects of the system
        (ie: forcing a 'curse' powerup will result
        in the next powerup being health).
        """
        if forceType:
            t = forceType
        else:
            # if the last one was a curse, make this one a health to
            # provide some hope
            if self._lastPowerupType == 'curse':
                t = 'health'
            else:
                while True:
                    t = self._powerupDist[
                        random.randint(0, len(self._powerupDist)-1)]
                    if t not in excludeTypes:
                        break
        self._lastPowerupType = t
        return t


def getDefaultPowerupDistribution():
    if hack.mPowerup:
        return hack.desire_powerup_dist
    else:
        return hack.getDefaultPowerupDistribution

class Powerup(bs.Actor): #By Desire
    """
    category: Game Flow Classes

    A powerup box.
    This will deliver a bs.PowerupMessage to anything that touches it
    which has the bs.PowerupFactory.powerupAcceptMaterial applied.

    Attributes:

       powerupType
          The string powerup type.  This can be 'tripleBombs', 'punch',
          'iceBombs', 'impactBombs', 'landMines', 'stickyBombs', 'shield',
          'health', or 'curse'.

       node
          The 'prop' bs.Node representing this box.
    """

    def __init__(self,position=(0,1,0),powerupType='tripleBombs',expire=True):
        """
        Create a powerup-box of the requested type at the requested position.

        see bs.Powerup.powerupType for valid type strings.
        """
        
        bs.Actor.__init__(self)

        factory = self.getFactory()
        self.powerupType = powerupType;
        self._powersGiven = False

        if powerupType == 'tripleBombs': 
          tex = factory.texBomb
          name = "| | Trio | |"
        elif powerupType == 'punch': 
          tex = factory.texPunch
          name = "| | Gloves | |"
        elif powerupType == 'iceBombs': 
          tex = factory.texIceBombs
          name = "| | Ice | |"
        elif powerupType == 'shockwave':
            tex = factory.shockWaveTex
            name = "| | Shockwave | |"
        elif powerupType == 'impactBombs': 
          tex = factory.texImpactBombs
          name = "| | Impact | |"
        elif powerupType == 'stickyForce':
            tex = factory.texStickyForce
            name = "| | Sticky Force | |"        
        elif powerupType == 'artillery':
            tex = factory.texArtillery
            name = "| | Airstrike | |"
        elif powerupType == 'sleepPotionBombs': 
        	tex = factory.texSleepPotionBombs
        	name = "| | Sleep | |"
        elif powerupType == 'landMines': 
          tex = factory.texLandMines
          name = "| | Landmines | |"
        elif powerupType == 'banana':
            tex = factory.texBanana
            name = "| | Banana | |"
        elif powerupType == 'elonMine': 
          tex = factory.texElonMuskMine
          name = "| | Traker | |"
        elif powerupType == 'toxicBombs': 
        	tex = factory.texRadioactiveBombs
        	name = "| | Toxic | |"
        elif powerupType == 'enderPearls': 
          tex = factory.texEnderPearls
          name = "| | EnderPearl | |"
        elif powerupType == 'highJump':
            tex = factory.texHighJump
            name = "| | High Jump | |"
        elif powerupType == 'stickyBombs': 
          tex = factory.texStickyBombs
          name = "| | Sticky | |"
        elif powerupType == 'shield': 
          tex = factory.texShield
          name = "| | Shield | |"
        elif powerupType == 'god': 
            tex = factory.texGod
            name = "| | Speed | |"
        elif powerupType == 'health': 
          tex = factory.texHealth
          name = "| | Health | |"
        elif powerupType == 'weedbomb': 
          tex = factory.texweedbomb
          name = "| | Weed | |"
        elif powerupType == 'Party':
            tex = factory.texParty
            name = "| | Party | |"          
        elif powerupType == 'Bunny':
            tex = factory.texBunny
            name = "| | Bot | |"          
        elif powerupType == 'Rchar':
            tex = factory.texRchar
            name = "| | Rchar | |"  
        elif powerupType == 'Inv':
            tex = factory.texInv
            name = "| | Invisible | |"            
        elif powerupType == 'curse': 
          tex = factory.texCurse
          name = "| | Death | |"
        else: raise Exception("invalid powerupType: "+str(powerupType))

        if len(position) != 3: raise Exception("expected 3 floats for position")
        
        self.node = bs.newNode(
            'prop',
            delegate=self,
            attrs={'body':'box',
                   'position':position,
                   'model':factory.model,
                   'lightModel':factory.modelSimple,
                   'shadowSize':0.5,
                   'colorTexture':tex,
                   'reflection':'powerup',
                   'reflectionScale':[1.0],
                   'materials':(factory.powerupMaterial,
                                bs.getSharedObject('objectMaterial'))})

        prefixAnim = {0: (1, 0, 0), 250: (1, 1, 0), 250 * 2: (0, 1, 0), 250 * 3: (0, 1, 1), 250 * 4: (1, 0, 1),
                      250 * 5: (0, 0, 1), 250 * 6: (1, 0, 0)}
        color = (1,1,1)
        if hack.nameOnPowerUps:
            m = bs.newNode('math', owner=self.node, attrs={'input1': (0, 0.7, 0), 'operation': 'add'})
            self.node.connectAttr('position', m, 'input2')
            self.nodeText = bs.newNode('text',
                                       owner=self.node,
                                       attrs={'text': str(name),
                                              'inWorld': True,
                                              'shadow': 1.0,
                                              'flatness': 1.0,
                                              'color': color,
                                              'scale': 0.0125,
                                              'hAlign': 'center'})
            m.connectAttr('output', self.nodeText, 'position')
            #bs.animate(self.nodeText, 'scale', {0: 0, 140: 0.16, 200: 0.01})
            if hack.animate:
                bs.animateArray(self.nodeText,'color',3,{0:(0,0,2),500:(0,2,0),1000:(2,0,0),1500:(2,2,0),2000:(2,0,2),2500:(0,1,6),3000:(1,2,0)},True)
                bs.emitBGDynamics(position=self.nodeText.position, velocity=self.node.position, count=75, scale=1.0, spread=1.3, chunkType='spark')
        if hack.shieldOnPowerUps:                      
            self.nodeShield = bs.newNode('shield', owner=self.node, attrs={'color': ((0+random.random()*6.0),(0+random.random()*6.0),(0+random.random()*6.0)),
                                                                           'position': (
                                                                               self.node.position[0],
                                                                               self.node.position[1],
                                                                               self.node.position[2] + 0.5),
                                                                           'radius': 1.2})
            self.node.connectAttr('position', self.nodeShield, 'position')
            #bs.animateArray(self.powerupShield,'gravityScale',3,{0:(0,0,2),500:(0,2,0),1000:(2,0,0),1500:(2,2,0),2000:(2,0,2),2500:(0,1,6),3000:(1,2,0)},True)
            if hack.animate:
                bsUtils.animateArray(self.nodeShield, 'color', 3, prefixAnim, True)

        if hack.discoLightsOnPowerUps:
            self.nodeLight = bs.newNode('light',
                                        attrs={'position': self.node.position,
                                               'color': color,
                                               'radius': 0.05,
                                               'volumeIntensityScale': 0.03})
            self.node.connectAttr('position', self.nodeLight, 'position')
            bsUtils.animateArray(self.nodeLight, 'color', 3, prefixAnim, True)
            
            self.shield = bs.newNode('shield', owner=self.node,
                               attrs={'color':(random.random()*2,random.random()*2,random.random()*2), 'radius':1.0})
            self.node.connectAttr('position', self.shield, 'position') 
            
        if hack.powerupTimer:
            self.powerupHurt = bs.newNode('shield', owner=self.node, attrs={'color':(1,1,1), 'radius':0.1, 'hurt':1, 'alwaysShowHealthBar':True})
            self.node.connectAttr('position',self.powerupHurt, 'position')
            bs.animate(self.powerupHurt, 'hurt', {0:0, defaultPowerupInterval-1000:1})          
        # animate in..
        curve = bs.animate(self.node,"modelScale",{0:0,140:1.6,200:1})
        bs.gameTimer(200,curve.delete)

        if expire:
            bs.gameTimer(defaultPowerupInterval-2500,
                         bs.WeakCall(self._startFlashing))
            bs.gameTimer(defaultPowerupInterval-1000,
                         bs.WeakCall(self.handleMessage, bs.DieMessage()))

    @classmethod
    def getFactory(cls):
        """
        Returns a shared bs.PowerupFactory object, creating it if necessary.
        """
        activity = bs.getActivity()
        if activity is None: raise Exception("no current activity")
        try: return activity._sharedPowerupFactory
        except Exception:
            f = activity._sharedPowerupFactory = PowerupFactory()
            return f
            
    def _startFlashing(self):
        if self.node.exists(): self.node.flashing = True

        
    def handleMessage(self, msg):
        self._handleMessageSanityCheck()

        if isinstance(msg, PowerupAcceptMessage):
            factory = self.getFactory()
            if self.powerupType == 'health':
                bs.playSound(factory.healthPowerupSound, 3,
                             position=self.node.position)
            bs.playSound(factory.powerupSound, 3, position=self.node.position)
            self._powersGiven = True
            self.handleMessage(bs.DieMessage())
            
        elif isinstance(msg, _TouchedMessage):
            if not self._powersGiven:
                node = bs.getCollisionInfo("opposingNode")
                if node is not None and node.exists():
                    if self.powerupType == 'Bunny':
                        p = node.getDelegate().getPlayer()
                        if 'bunnies' not in p.gameData:
                            p.gameData['bunnies'] = BuddyBunny.BunnyBotSet(p)
                        p.gameData['bunnies'].doBunny()
                        self._powersGiven = True
                        self.handleMessage(bs.DieMessage())
                    else:
                        node.handleMessage(PowerupMessage(self.powerupType, sourceNode=self.node))
                        
        elif isinstance(msg, _TouchedMessage):
            if not self._powersGiven:
                node = bs.getCollisionInfo("opposingNode")
                if node is not None and node.exists():
                    node.handleMessage(PowerupMessage(self.powerupType,
                                                      sourceNode=self.node))

        elif isinstance(msg, bs.DieMessage):
            if self.node.exists():
                if (msg.immediate):
                    self.node.delete()
                else:
                    curve = bs.animate(self.node, "modelScale", {0:1,100:0})
                    bs.gameTimer(100, self.node.delete)

        elif isinstance(msg ,bs.OutOfBoundsMessage):
            self.handleMessage(bs.DieMessage())

        elif isinstance(msg, bs.HitMessage):
            # dont die on punches (thats annoying)
            if msg.hitType != 'punch':
                self.handleMessage(bs.DieMessage())
        else:
            bs.Actor.handleMessage(self, msg)
