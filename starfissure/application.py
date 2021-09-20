"""
Primary module for Game
"""

from constant import *
from game2d import *
from waves import *

class Invaders(GameApp):
    def start(self):
        self._state=stateinactive
        self._wave=None
        self._text=GLabel(text='Press V to Start\nspacebar - shoot laser\nb - drop bomb')
        self._text.font_name='Times.ttf'
        self._text.halign='center'
        self._text.x=gamewidth/2
        self._text.y=gameheight/2
        self._text.fillcolor='black'
        self._text.font_size=50
        self._text.linecolor='white'
        self.previous_keys=0
        self._lives=shiplives
        self._background=Backing()

    def update(self,dt):
        if self._state==stateinactive:
            self._determinestate()
        elif self._state==statenewwave:
            self._text=None
            self._wave=Wave()
            self._state=stateactive
        elif self._state==stateactive:
            self._wave.update(self.input,dt)
        if self._state==stateactive and self._wave.getship()==None and self._wave.getlives!=0:
            self._state=statepaused
            self._text=GLabel(text='ship hit. '+self._wave.getlives()+' lives remaining.\npress V to continue')
            self._text.x=gamewidth/2
            self._text.y=gameheight/2
            self._text.fillcolor='black'
            self._text.linecolor='red'
            self._text.font_name='Times.ttf'
            self._text.font_size=50
        if self._state==stateactive and self._wave.gameresult()==True:
            self._state=stateinactive
            self._text=GLabel(text='You Win!\nCongrats I thought that was impossible')
            self._text.x=gamewidth/2
            self._text.y=gameheight/2
            self._text.font_size=50
            self._text.fillcolor='black'
            self._text.linecolor='yellow'
            self._text.font_name='Times.ttf'
        if self._state==stateactive and self._wave.gameresult()==False:
            self._state=stateinactive
            self._text=GLabel(text='You Lose')
            self._text.x=gamewidth/2
            self._text.y=gameheight/2
            self._text.font_size=50
            self._text.fillcolor='black'
            self._text.linecolor='white'
            self._text.font_name='Times.ttf'
        if self._state==statepaused and self.input.iskeydown('v')==True:
            self._state=statecontinue
        if self._state==statecontinue:
            self._text=None
            self._wave.reset()
            self._state=stateactive

    def _determinestate(self):
        presskeys=self.input._keycount
        if self.previous_keys==0 and self.input.iskeydown('v')==True and presskeys>0:
            self._state=statenewwave
        self.previous_keys=presskeys

    def draw(self):
        if self._state==stateinactive or self._state==statepaused:
            self._background.draw(self.view)
            self._text.draw(self.view)
        if self._state==stateactive:
            self._background.draw(self.view)
            self._wave.draw(self.view)






        #script end
