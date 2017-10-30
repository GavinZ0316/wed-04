from scene import *
import ui
import time

from main_menu_scene import *


class SplashScene(Scene):
    def setup(self):
        
    	
        
       self.start_time = time.time()
       
       
       self.background = SpriteNode(posirion = self.size / 2,
                                    color = (0.16, 0.78, 0.87),
                                    parent = self,
                                    size = self.size)
       self.school_crest = SpriteNode('./assets/sprites/MT_Crest.jpg',
                                    parent = self,
                                    posirion = self.size/2)
    
    def update(self):
    
    
        if not self.presented_scene and time.time() - self.start_time > 2:
            self.present_modal_scene(MainMenuScene())
    
    def touch_began(self, touch):
        
        pass
