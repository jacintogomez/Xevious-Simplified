"""
Subcontroller module for Game
"""
from game2d import *
from constant import *
from mod import *
import random
import math
from PIL import Image

class Wave(object):
    def __init__(self):
        self._ship=Ship()
        self._aliens=self.wavemaker()
        self._bolts=[]
        self._bombs=[]
        self._boss=0
        self._lives=shiplives
        self._time=0
        self._direction='right'
        self._countdown=self.stepsbetweenalienshots()
        self._cdown=self.stepsbetweenbossshots()
        self._countd=spriterate
        self._checkvar=0
        self._originpoint=0
        self._lastbolt=0
        self._background=Backing()
        self._sprites=[]

    def getship(self):
        return self._ship

    def setship(self,value):
        self._ship=value

    def getboss(self):
        return self._boss

    def setboss(self,value):
        self._boss=value

    def getaliens(self):
        return self._aliens

    def setaliens(self):
        self._aliens=value

    def gtbolts(self):
        return self._bolts

    def setbolts(self,value):
        self._bolts=value

    def getbombs(self):
        return self._bombs

    def setbombs(self,value):
        self._bombs=value

    def getlives(self):
        return str(self._lives)

    def setlives(self,value):
        self._lives=value

    def gettime(self):
        return self._time

    def getsprites(self):
        return self._sprites

    def setsprites(self,value):
        self._sprites=value

    def settime(self):
        self._time=value

    def reset(self):
        self._ship=Ship()

    def moveship(self,input):
        if self._ship!=None:
            if input.iskeydown('right'):
                self.shiphelperright()
            if input.iskeydown('left'):
                self.shiphelperleft()
            if input.iskeydown('up'):
                self.shiphelperup()
            if input.iskeydown('down'):
                self.shiphelperdown()
            elif self._ship.x==0:
                if input.iskeydown('right'):
                    self.shiphelperright()
                if input.iskeydown('up'):
                    self.shiphelperup()
                if input.iskeydown('down'):
                    self.shiphelperdown()
            elif self._ship.x==gamewidth:
                if input.iskeydown('left'):
                    self.shiphelperleft()
                if input.iskeydown('up'):
                    self.shiphelperup()
                if input.iskeydown('down'):
                    self.shiphelperdown()
            elif self._ship.y==0:
                if input.iskeydown('right'):
                    self.shiphelperright()
                if input.iskeydown('left'):
                    self.shiphelperleft()
                if input.iskeydown('up'):
                    self.shiphelperup()
            elif self._ship.y==gameheight:
                if input.iskeydown('right'):
                    self.shiphelperright()
                if input.iskeydown('left'):
                    self.shiphelperleft()
                if input.iskeydown('down'):
                    self.shiphelperdown()

    def shiphelperright(self):
        x=self._ship.getshipx()
        if x<=gamewidth-(shipwidth/2):
            x+=shipmovement
            self._ship.setshipx(x)

    def shiphelperleft(self):
        x=self._ship.getshipx()
        if x>=shipwidth/2:
            x-=shipmovement
            self._ship.setshipx(x)

    def shiphelperup(self):
        y=self._ship.getshipy()
        if y<=gameheight-(shipheight/2):
            y+=shipmovement
            self._ship.setshipy(y)

    def shiphelperdown(self):
        y=self._ship.getshipy()
        if y>=shipheight/2:
            y-=shipmovement
            self._ship.setshipy(y)

    def movealien(self,input,dt):
        self._time+=dt

    def alienhelperleft(self,al,mag):
        for j in range(int(mag+1)):
            x=al.getx()
            if x>alienwidth:
                x-=aliendist
                al.setx(x)
            else:
                self.alienhelperright(al,mag)

    def alienhelperright(self,al,mag):
        for j in range(int(mag+1)):
            x=al.getx()
            if x<gamewidth-alienwidth:
                x+=aliendist
                al.setx(x)
            else:
                self.alienhelperleft(al,mag)

    def alienhelperup(self,al,mag):
        for j in range(int(mag+1)):
            x=al.gety()
            if x<gameheight-alienheight:
                x+=aliendist
                al.sety(x)
            else:
                self.alienhelperdown(al,mag)

    def alienhelperdown(self,al,mag):
        for j in range(int(mag+1)):
            x=al.gety()
            if x>alienheight:
                x-=aliendist
                al.sety(x)
            else:
                self.alienhelperup(al,mag)

    def movealiens(self,dt):
        if self.part2()==False:
            self._time+=dt
            self.firealienbolt()
            options=['north','south','east','west','northeast','northwest','southeast','southwest']
            if self._time>alienspeed:
                for x in self._aliens:
                    if x!=None:
                        direction=random.choice(options)
                        magnitude=random.randint(1,3)
                        if direction=='north':
                            self.alienhelperup(x,magnitude)
                        elif direction=='south':
                            self.alienhelperdown(x,magnitude)
                        elif direction=='east':
                            self.alienhelperright(x,magnitude)
                        elif direction=='west':
                            self.alienhelperleft(x,magnitude)
                        elif direction=='northeast':
                            self.alienhelperup(x,magnitude)
                            self.alienhelperright(x,magnitude)
                        elif direction=='northwest':
                            self.alienhelperup(x,magnitude)
                            self.alienhelperleft(x,magnitude)
                        elif direction=='southeast':
                            self.alienhelperdown(x,magnitude)
                            self.alienhelperright(x,magnitude)
                        elif direction=='southwest':
                            self.alienhelperdown(x,magnitude)
                            self.alienhelperleft(x,magnitude)
                self._time=0
        else:
            if self._checkvar==0:
                self._boss=self.bossmaker()
                self._checkvar+=1
            self.moveboss(self._boss,dt)
            self._time=0

    def wavemaker(self):
        squad=[]
        Backing()
        for y in range(1,aliennumber):
            y=random.randint(int(gameheight*2/3),int(gameheight-alienheight))
            x=random.randint(int(gamewidth/4),int(gamewidth*3/4))
            et=Alien(x,y,'alien1.png')
            squad.append(et)
        return squad

    def part2(self):
        acc=[]
        for b in self._aliens:
            if b==None:
                acc.append(b)
        if len(self._aliens)==len(acc):
            return True
        else:
            return False

    def bossmaker(self):
        if self.part2():
            y=gameheight+bossheight/2
            x=gamewidth/2
            xev=Boss(x,y,bossspeed,'andor.png')
            return xev

    def fireuserbolt(self,input):
        if self._ship!=None:
            x=self._ship.getshipx()
            y=self._ship.getshipy()+(boltheight+shipheight)/2
            if input.iskeydown('spacebar')==True and self.timepermission(self._lastbolt):
                self._bolts.append(Bolt(x,y,0,boltspeed))
                self._lastbolt=self._bolts[-1]

    def fireuserbomb(self,input):
        if self._bombs==[]:
            x=self._ship.getshipx()
            y=self._ship.getshipy()+(bombheight+shipheight)/2
            if input.iskeydown('b')==True:
                self._bombs.append(Bomb(x,y,bombspeed))
                self._originpoint=y

    def firealienbolt(self):
        if alienspeed<=self._time:
            if self._countdown!=0:
                self._countdown-=1
                return None
            laser=boltspeed*(-1)
            catch=[]
            for p in self._aliens:
                if p!=None:
                    catch.append(p)
            if catch!=None:
                h=random.choice(catch)
                if h!=None:
                    x=h.getx()
                    y=h.gety()
                    self._bolts.append(Bolt(x,y,0,laser))
                    self._countdown=self.stepsbetweenalienshots()

    def trig(self,ang):
        x=math.cos(ang)
        return x

    def complement(self,prev):
        y=math.sqrt(1-prev**2)
        return y

    def firebossbolt(self):
        if bossspeed<=self._time:
            if self._cdown!=0:
                self._cdown-=1
                return None
            plus=bossheight/6
            minus=plus*(-1)
            dummy=[plus,minus]
            angles=[]
            for x in range(0,180):
                angles.append(x)
            x=self._boss.getbossx()
            y=self._boss.getbossy()
            for i in dummy:
                for j in dummy:
                    angle=random.choice(angles)
                    xv=self.trig(angle)
                    yv=self.complement(xv)
                    xlaser=float(xv*boltspeed)
                    ylaser=float(yv*boltspeed*(-1))
                    self._bolts.append(Bolt(x+i,y+j,xlaser,ylaser))
            self._cdown=self.stepsbetweenbossshots()

    def checkvelocity(self):
        '''checks if there is still a user bolt on screen;
        can be used in fireuserbolt to prevent multiple bolts
        from being fired at once, although it is not used here'''
        for x in self._bolts:
            if x.isplayerbolt():
                return True
        return False

    def timepermission(self,last):
        if self._lastbolt==0:
            return True
        elif last.permitteddistance(self._ship):
            return True
        else:
            return False

    def movebomby(self):
        for g in self._bombs:
            y=g.getbomby()
            y+=g._velocity
            g.setbomby(y)

    def movebolty(self):
        for j in self._bolts:
            y=j.getbolty()
            y+=j._yvelocity
            j.setbolty(y)

    def moveboltx(self):
        if self.part2():
            for j in self._bolts:
                x=j.getboltx()
                if not j.isplayerbolt():
                    x+=j._xvelocity
                    j.setboltx(x)

    def moveboss(self,b,dt):
        if self._boss!=None:
            self._time+=1
            t=b.getbossy()
            if t>(gameheight-bossheight/2):
                self._ship=Ship()
                self.bosshelper()
            elif t<=(gameheight-bossheight/2):
                self.firebossbolt()

    def isandormoving(self,b):
        t=b.getbossy()
        if t<gameheight+bossheight/2 and t>gameheight-bossheight/2:
            return True
        else:
            return False

    def bosshelper(self):
        y=self._boss.getbossy()
        y-=self._boss._bossvelocity
        self._boss.setbossy(y)

    def findboltbottom(self,bolt):
        u=bolt.getbolty()
        bottom=u-(.5*boltheight)
        return bottom

    def findbolttop(self,bolt):
        u=bolt.getbolty()
        top=u+(.5*boltheight)
        return top

    def collisionremove(self):
        self.removeship()
        self.removealien()
        self.crash()
        # self.removeboss()

    # def spriteflipper(self):
    #     if spriterate<=self._time:
    #         if self._countd!=0:
    #             self._countd-=1
    #             return None

    def slicer(self,input):
        dir='/Users/jacintogomez/Desktop/starfissure/Images/'
        img=Image.open(dir+input)
        width,height=img.size
        middle=width/2
        lower=height*2/3
        upper=height/3
        im1=img.crop((0,height,middle,upper))
        im2=img.crop((middle,height,width,upper))
        im3=img.crop((0,upper,middle,lower))
        im4=img.crop((middle,upper,width,lower))
        im5=img.crop((0,0,middle,height))
        im6=img.crop((middle,lower,width,0))
        im5=im5.tobytes()
        sprite=[im1,im2,im3,im4,im5,im6]
        return sprite

    # def aliendeathanimate(self,et):
    #     x=et.getx()
    #     y=et.gety()
    #     pics=self.slicer('alien-strip1.png')
    #     sheet=Sprite(x,y,'alien-strip1.png')
    #     ig=Image.frombytes('L',(3,2),pics[4])
    #     sheet.setsource(ig.getdata())
    #     self._sprites.append(sheet)
    #     return

    def removeship(self):
        for k in range(len(self._bolts)-1):
            if self._bolts[k]!=None and self._ship!=None and self._ship.shipcollision(self._bolts[k]):
                self._ship=None
                self._lives-=1
                self._bolts=[]
                self._bombs=[]
                break
            temp=[]
            for bolt in self._bolts:
                if bolt!=None:
                    temp.append(bolt)
            self._bolts=temp

    def removealien(self):
        counter=0
        for i in self._aliens:
            for x in self._bolts:
                if x.isplayerbolt() and i!=None and i.aliencollision(x):
                    self._aliens[counter]=None
                    # self.aliendeathanimate(i)
                    self._bolts.remove(x)
            counter+=1

    def removeboss(self):
        if type(self._boss)!=int:
            if len(self._bombs)==1 and self._boss!=None and self._boss.bombdetonation(self._bombs[0]):
                self._boss=None
                return True
            return False

    def crash(self):
        for z in self._aliens:
            if z!=None and self._ship!=None and self._ship.altcrash(z):
                self._ship=None
                self._lives-=1
                self._bolts=[]
                self._bombs=[]
                self._aliens.remove(z)
        if type(self._boss)!=int and self._boss!=None and self._ship!=None and self._ship.bcrash(self._boss):
            self._ship=None
            self._lives-=1
            self._bolts=[]
            self._bombs=[]


    def bombexpire(self):
        if len(self._bombs)!=0:
            subject=self._bombs[0]
            newpoint=subject.getbomby()
            origin=self._originpoint
            distance=newpoint-origin
            if distance>=bombdistance:
                return True
            else:
                return False

    def removebomb(self):
        if len(self._bombs)==1 and self.bombexpire():
            del self._bombs[0]

    def removebolt(self):
        q=0
        while q<len(self._bolts):
            if self._bolts[q].isplayerbolt() and self.findboltbottom(self._bolts[q])>=gameheight:
                del self._bolts[q]
                q-=1
            else:
                if self.findbolttop(self._bolts[q])<=0:
                    del self._bolts[q]
                    q-=1
            q+=1

    def stepsbetweenalienshots(self):
        step=random.randint(1,boltrate)
        return step

    def stepsbetweenbossshots(self):
        step=random.randint(1,brate)
        return step

    def draw(self,view):
        for z in self._aliens:
            if z!=None:
                z.draw(view)
        if self._ship!=None:
            self._ship.draw(view)
        if self.part2() and self._boss!=None and type(self._boss)!=int:
            self._boss.draw(view)
        for z in self._bolts:
            z.draw(view)
        for q in self._bombs:
            q.draw(view)
        for b in self._sprites:
            b.draw(view)

    def gameresult(self):
        if self._lives==0:
            return False
        if self._boss==None:
            return True

    def update(self,input,dt):
        self.moveship(input)
        self.movealiens(dt)
        self.fireuserbolt(input)
        self.fireuserbomb(input)
        self.moveboltx()
        self.movebolty()
        self.movebomby()
        self.removebolt()
        self.removebomb()
        self.removeboss()
        self.collisionremove()
        self.gameresult()



#script end
