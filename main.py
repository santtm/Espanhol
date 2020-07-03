# -*- coding: utf-8 -*-

# code by: Thiago Santiago
# images by: Julia Rezende

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.video import Video 
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import FadeTransition, SlideTransition
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition

class Logo(Screen):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.layout = FloatLayout()
        self.add_widget(self.layout)
        
        # background
        self.img = Image(source='images/logo.jpg',
                         allow_stretch=True,
                         keep_ratio=False)
        self.layout.add_widget(self.img)
        
        Clock.schedule_once(self.change_screen, 20.5)
        
    def change_screen(self, event):
        self.manager.transition = FadeTransition()
        self.manager.transition.duration = 0.5
        self.manager.current = 'account'

class Account(Screen):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.layout = FloatLayout()
        self.add_widget(self.layout)
        
        # background
        self.img = Image(source='images/account.jpg',
                         allow_stretch=True,
                         keep_ratio=False)

        # button
        self.bt = Button(size_hint=(None,None),
                         size=(267,82),
                         pos=(389,350),
                         opacity=0)
        
        # loading widgets
        self.layout.add_widget(self.img)        
        self.bt.bind(on_press=self.change_screen)
        self.layout.add_widget(self.bt)
        

    def change_screen(self, event):
        self.manager.transition = SlideTransition()
        self.manager.transition.direction = 'left'
        self.manager.transition.duration = 0.5
        self.manager.current = 'login'
        
class Login(Screen):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout = FloatLayout()
        self.add_widget(self.layout)
        
        # background
        self.img = Image(source='images/login.jpg',
                         allow_stretch=True,
                         keep_ratio=False)
        # email input
        self.email = TextInput(hint_text='escriba aquí...', font_size=32,
                             size_hint=(None,None),
                             multiline=False,
                             size=(620,50),
                             pos=(30,960),
                             background_color=(0,0,0,0))
        # password input
        self.psw = TextInput(hint_text='escriba aquí...', font_size=32,
                             size_hint=(None,None),
                             multiline=False,
                             size=(620,50),
                             pos=(30,960-182),
                             background_color=(0,0,0,0),
                             password=True)

        # button
        self.bt = Button(size_hint=(None,None),
                         size=(592,86),
                         pos=(63.5,610),
                         opacity=0)
        
        # loading widgets
        self.layout.add_widget(self.img)
        self.layout.add_widget(self.email)
        self.layout.add_widget(self.psw)
        
        self.bt.bind(on_press=self.change_screen)
        self.layout.add_widget(self.bt)
        
    def change_screen(self, event):
        self.manager.transition.direction = 'left'
        self.manager.transition.duration = 0.5
        self.manager.current = 'menu'

class Menu(Screen):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.layout = FloatLayout()
        self.add_widget(self.layout)
        
        # background
        self.img = Image(source='images/menu.jpg',
                         allow_stretch=True,
                         keep_ratio=False)
        self.img2 = Image(source='images/menu2.jpg',
                         allow_stretch=True,
                         keep_ratio=False)
        
        # button
        self.bt = Button(size_hint=(None,None),
                         size=(688.3,114),
                         pos=(17,1134),
                         opacity=0)
        
        # loading widgets
        self.layout.add_widget(self.img)        
        self.bt.bind(on_press=self.change_screen)
        self.layout.add_widget(self.bt)
        
    def change_screen(self, event):
        self.layout.add_widget(self.img2)
        self.manager.transition = SlideTransition()
        self.manager.transition.direction = 'left'
        self.manager.transition.duration = 0.5
        self.manager.current = 'text1'

class Text1(Screen):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.layout = FloatLayout()
        self.add_widget(self.layout)
        
        # background
        self.img = Image(source='images/text_1.jpg',
                         allow_stretch=True,
                         keep_ratio=False)

        # button
        self.bt = Button(size_hint=(None,None),
                         size=(580,100),
                         pos=(25,323),
                         opacity=0.1)
        
        # loading widgets
        self.layout.add_widget(self.img)        
        self.bt.bind(on_press=self.change_screen)
        self.layout.add_widget(self.bt)
        
    def change_screen(self, event):        
        self.manager.transition = NoTransition()
        self.manager.current = 'text2'

class Text2(Screen):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.layout = FloatLayout()
        self.add_widget(self.layout)
        
        # background
        self.img = Image(source='images/text_2.jpg',
                         allow_stretch=True,
                         keep_ratio=False)
        self.img2 = Image(source='images/text_3.jpg',
                         allow_stretch=True,
                         keep_ratio=False)

        # button
        self.bt = Button(size_hint=(None,None),
                         size=(188,205),
                         pos=(263,982),
                         opacity=0.1)
        
        # loading widgets
        self.layout.add_widget(self.img)        
        self.bt.bind(on_press=self.change_screen)
        self.layout.add_widget(self.bt)

    def change_screen(self, event):   
        self.layout.add_widget(self.img2)
        self.manager.transition = FadeTransition()
        self.manager.transition.duration = 0.5
        self.manager.current = 'luminaria'
    
class Luminaria(Screen):
        
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.layout = FloatLayout()
        self.add_widget(self.layout)
        
        # background
        self.img = Image(source='images/luminaria.jpg',
                         allow_stretch=True,
                         keep_ratio=False)
        self.msg = Video(source='images/msg.MOV', size_hint=(None,None),size=(220,100), pos=(251, 730), options={'eos':'loop'}, play=True)
        self.layout.add_widget(self.img)
        self.layout.add_widget(self.msg)

# adicionando telas
sm = ScreenManager()
sm.add_widget(Logo(name='logo'))
sm.add_widget(Account(name='account'))
sm.add_widget(Login(name='login'))
sm.add_widget(Menu(name='menu'))
sm.add_widget(Text1(name='text1'))
sm.add_widget(Text2(name='text2'))
sm.add_widget(Luminaria(name='luminaria'))

class LuzyAmor(App):
    def build(self):
        return sm

# Burn, baby! BURN! (Apollo 11)
if __name__ == '__main__':
    LuzyAmor().run()