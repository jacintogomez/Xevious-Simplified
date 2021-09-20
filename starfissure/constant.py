"""
Global constants for the game Game

Dimensions, speeds and system argument protocol
"""

import introcs
import sys

#game window
gamewidth=800
gameheight=700

#ship dimensions
shipwidth=44
shipheight=44
shipbottom=32
shipmovement=5
shiplives=3

#alin dimensions
alienwidth=33
alienheight=33
aliendist=5
alienspeed=.1
numberofaliens=3
aliennumber=numberofaliens+1
spriterate=5
alienlist=['alien1.png','alien-strip1.png']
# alienimage=['alien1.png','alien-strip1.png']

#bossdimensions
bossheight=231
bosswidth=231
bossspeed=1
shiprecoilspeed=bossspeed


#shooting dimensions
boltwidth=4
boltheight=16
boltspeed=10
boltrate=5
brate=20
#user bolt specifications
timebeforenextshot=20
distancebeforenextshot=boltspeed*timebeforenextshot

bombradius=4
bombwidth=bombradius*2
bombheight=bombwidth
bombspeed=5
bombdistance=250

#game states
stateinactive=0
statenewwave=1
stateactive=2
statepaused=3
statecontinue=4
statecomplete=5

# try:
#     asteroid=int(sys.argv[1])
#     if astroid>=1 and asteroid<=10:
#         asteroidnumber=asteroid
# except:
#     pass

try:
    alien=int(sys.argv[1])
    if alien>=1 and alien<=30:
        numberofaliens=alien
except:
    pass
