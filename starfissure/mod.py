"""
Classes for Game.
Alien objects get standard nomenclature
Anything appearing on screen is taken from here
"""

from constant import *
from game2d import *

class Backing(GRectangle):
    def __init__(self):
        super().__init__(x=gamewidth/2,y=gameheight/2,width=gamewidth,height=gameheight,fillcolor='black')

class Ship(GImage):
    def __init__(self):
        super().__init__(x=gamewidth/2,y=shipbottom+shipheight/2,width=shipwidth,height=shipheight,source='ship.png')

    def getshipx(self):
        return self.x

    def setshipx(self,value):
        self.x=value

    def getshipy(self):
        return self.y

    def setshipy(self,value):
        self.y=value

    def shipcollision(self,bolt):
        left=bolt.getboltx()-boltwidth/2
        right=bolt.getboltx()+boltwidth/2
        top=bolt.getbolty()+boltheight/2
        bottom=bolt.getbolty()-boltheight/2
        if self.contains((left,top)) or self.contains((left,bottom)) or self.contains((right,top)) or self.contains((right,bottom)):
            return True
        else:
            return False

    def altcrash(self,alien):
        left=alien.getx()-alienwidth/2
        right=alien.getx()+alienwidth/2
        top=alien.gety()+alienheight/2
        bottom=alien.gety()-alienheight/2
        if self.contains((left,top)) or self.contains((left,bottom)) or self.contains((right,top)) or self.contains((right,bottom)):
            return True
        else:
            return False

    # def bcrash(self,boss):
    #     x=self.x
    #     y=self.y+shipheight/2
    #     left=boss.getbossx()-(bosswidth+shipwidth)/2
    #     right=boss.getbossx()+(bosswidth+shipwidth)/2
    #     top=boss.getbossy()+bossheight/2
    #     bottom=boss.getbossy()-bossheight/2
    #     if y>=bottom and y<=top and x>=left and x<=right:
    #         return True
    #     else:
    #         return False

    def bcrash(self,boss):
        left=boss.getbossx()-bosswidth/2
        center=boss.getbossx()
        cent=boss.getbossy()
        right=boss.getbossx()+bosswidth/2
        bottom=boss.getbossy()-bossheight/2
        top=boss.getbossy()+bossheight/2
        x1=boss.getbossx()-bosswidth*.3
        x2=boss.getbossx()-bosswidth*.14
        x3=boss.getbossx()+bosswidth*.14
        x4=boss.getbossx()+bosswidth*.3
        y1=boss.getbossy()-bosswidth*.3
        y2=boss.getbossy()-bosswidth*.14
        y3=boss.getbossy()+bosswidth*.14
        y4=boss.getbossy()+bosswidth*.3
        if self.contains((left,y2)) or self.contains((x1,y1)) or self.contains((x2,bottom)) \
        or self.contains((x3,bottom)) or self.contains((x4,y1)) or self.contains((right,y2)) \
        or self.contains((right,y3)) or self.contains((left,y3)) or self.contains((x1,y4)) \
        or self.contains((x4,y4)) or self.contains((x2,top)) or self.contains((x3,top)) \
        or self.contains((center,bottom)) or self.contains((left,cent)) or self.contains((right,cent)):
            return True
        else:
            return False

class Alien(GImage):
    def __init__(self,x,y,source):
        super().__init__(x=x,y=y,width=alienwidth,height=alienheight,source='alien1.png')

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def setx(self,value):
        self.x=value

    def sety(self,value):
        self.y=value

    # def flipbook(self,et):
    #     sprite=slicer()
    #     for z in sprite:
    #
    #     return exp

    def aliencollision(self,bolt):
        left=bolt.getboltx()-boltwidth/2
        right=bolt.getboltx()+boltwidth/2
        top=bolt.getbolty()+boltheight/2
        bottom=bolt.getbolty()-boltheight/2
        if self.contains((left,top)) or self.contains((left,bottom)) or self.contains((right,top)) or self.contains((right,bottom)):
            return True
        else:
            return False

class Sprite(GImage):
    def __init__(self,x,y,source):
        super().__init__(x=x,y=y,width=alienwidth,height=alienheight,source='alien-strip1.png')
        self._source=source

    def getspritesource(self):
        return self.source

    def setsource(self,image):
        self.source=image

class Boss(GImage):
    def __init__(self,x,y,velocity,source):
        super().__init__(x=x,y=y,width=bosswidth,height=bossheight,source='andor.png')
        self._bossvelocity=velocity

    def getbossx(self):
        return self.x

    def getbossy(self):
        return self.y

    def setbossx(self,value):
        self.x=value

    def setbossy(self,value):
        self.y=value

    def bombdetonation(self,bomb):
        x=bomb.getbombx()
        y=bomb.getbomby()
        left=self.getbossx()-bosswidth*0.0694+bombwidth/2
        right=self.getbossx()+bosswidth*0.0694-bombwidth/2
        top=self.getbossy()+bossheight*0.0694-bombheight/2
        bottom=self.getbossy()-bossheight*0.0694+bombheight/2
        if y>=bottom and y<=top and x>=left and x<=right:
            return True
        else:
            return False

class Bomb(GEllipse):
    def __init__(self,x,y,velocity):
        super().__init__(x=x,y=y,width=bombwidth,height=bombheight,fillcolor='gray')
        self._velocity=velocity

    def getbomby(self):
        return self.y

    def setbomby(self,value):
        self.y=value

    def getbombx(self):
        return self.x

    def setbombx(self,value):
        self.x=value

class Bolt(GRectangle):
    def __init__(self,x,y,xvelocity,yvelocity):
        super().__init__(x=x,y=y,width=boltwidth,height=boltheight,fillcolor='red')
        self._xvelocity=xvelocity
        self._yvelocity=yvelocity

    def isplayerbolt(self):
        if self._yvelocity>0:
            return True
        elif self._yvelocity<0:
            return False

    def permitteddistance(self,ship):
        run=self.getbolty()
        base=ship.getshipy()
        d=run-base
        if d>=distancebeforenextshot:
            return True
        elif run>=gameheight:
            return True
        else:
            return False

    def getboltx(self):
        return self.x

    def getbolty(self):
        return self.y

    def setboltx(self,value):
        self.x=value

    def setbolty(self,value):
        self.y=value
