"""
Primary application script for Game
"""

from constant import *
from application import *

if __name__=='__main__':
    Invaders(width=gamewidth,height=gameheight).run()
