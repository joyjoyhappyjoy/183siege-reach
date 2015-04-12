from getch import getch
from constants import *
import time, random
import select
import sys
import multiprocessing
from multiprocessing import Pipe
import threading
import time
random.seed()

################################################################################
#                        Toggle Student AI / Story Mode                        #
################################################################################
USE_AI = False                                                                 #
STORY_MODE = True                                                              #
################################################################################

# A dictionary for 'passing' information between your functions
ACTION_INFO = {}

def combat_action(options):
    global ACTION_INFO # Necessary for reading and writing the global ACTION_INFO dictionary
    """
    Return 'x' to attack the enemy
    Return 'c' to defend against the enemy's next attack
    Return 'i' to use a potion and heal yourself
    Return 'e' to use a Babylon Candle and attempt to escape combat
    NEW: Return 'f' to use a fireball and attack the enemy
    NEW: Return '1' to swap one of your weapons to your Main Hand, you may only swap 
         if your 'backpack_weapons' is not empty
    NEW: Return '2' to swap one of your weapons to your Off-Hand, you may only swap 
         if your 'backpack_weapons' is not empty
    """
    return 'x'

def movement_action(options):
    global ACTION_INFO # Necessary for reading and writing the global ACTION_INFO dictionary
    """
    Return 'w', 'a', 's', 'd', or 'x' to navigate around the map
    Return 'i' to use a potion and heal
    Return 'h' to hide
    NEW: Return 'r' to use a repel potion
    """
    return random.choice(['w', 'a', 's', 'd'])

def item_action(options):   
    global ACTION_INFO # Necessary for reading and writing the global ACTION_INFO dictionary
    """
    Return '1' to place the item in your main hand
    Return '2' to place the item in your off-hand
    NEW: If your backpack is not full, you may return '8' to add the item to your backpack
         otherwise you may return a key from the 'backpack_weapons' dictionary to
         replace the item associated with that key
    NEW: Return '9' to ignore the item
    """
    return '9'

def swap_select_weapon(options):
    global ACTION_INFO # Necessary for reading and writing the global ACTION_INFO dictionary
    """
    *** NEW FUNCTION AND SCENARIO ***
    *** Called during the SWAP scenario ***
    Return one of the keys from the 'backpack_weapons' dictionary to place that item
        in 'swap_weapon_to_hand'
    WARNING: The only valid values you may return are the keys in the 'backpack_weapons'
             dictionary!
    WARNING: If the weapon you choose cannot be placed in 'swap_weapon_to_hand' your 
             the swap will not be succesfful and your combat_action() function will be 
             called again
    """
    return options['inventory']['backpack_weapons'].keys()[0]




#####################################################################################
#                Game Driver for your AI. Don't modify this section.                #
#####################################################################################
def _check_loop():                                                                  #
    raw_input()                                                                     #
    USE_AI = False                                                                  #
                                                                                    #
class User(object):                                                                 #
    def __init__(self):                                                             #
        self.input_check = None                                                     #
        self.set_ai(USE_AI)                                                         #
                                                                                    #
    def select(self, options):                                                      #
        if options['situation'] == 'COMBAT': return combat_action(options)          #
        elif options['situation'] == 'ITEM': return item_action(options)            #
        elif options['situation'] == 'MOVE': return movement_action(options)        #
        elif options['situation'] == 'SWAP': return swap_select_weapon(options)     #
        else: raise Exception("Bad move option: {0}".format(options['situation']))  #
                                                                                    #
    def set_ai(self, setting):                                                      #
        global USE_AI                                                               #
        if setting:                                                                 #
            # launch subprocess to handle input                                     #
            USE_AI = True                                                           #
            self.input_check = threading.Thread(target=_check_loop)                 #
            self.input_check.daemon = True                                          #
            self.input_check.start()                                                #
        else:                                                                       #
            # end the subprocess                                                    #
            if self.input_check and self.input_check.is_alive():                    #
                self.input_check.join(GAME_SPEED)                                   #
            USE_AI = False                                                          #
                                                                                    #
                                                                                    #
    def __move__(self, options):                                                    #
        if not USE_AI:                                                              #
            usr = getch()                                                           #
            if ord(usr) == 13:                                                      #
                self.set_ai(True)                                                   #
                return self.select(options).lower()                                 #
            return usr.lower()                                                      #
                                                                                    #
        time.sleep(GAME_SPEED)                                                      #
        if self.input_check and not self.input_check.is_alive():                    #
            self.set_ai(False)                                                      #
            return getch().lower()                                                  #
        return self.select(options).lower()                                         #
                                                                                    #
                                                                                    #
#####################################################################################
