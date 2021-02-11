# Debugging Stuff
debug_mode = True
debug_print = True
debug_logging = True

# Module Imports
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina import Ursina, Entity, application, held_keys, window
from ursina.color import *
from time import sleep as wait
from termcolor import cprint
import json

# File Imports
from keymap_old import keybind

# Import Configuration
app = Ursina()
log_code_file = './code/debug_codes.json'

# Stats
max_health = 100
health = max_health
stamina_mult = 10
max_stamina = 100
stamina = max_stamina

# Functions
def debug():
   global debug_mode, debug_print
   if held_keys['escape']:
      application.quit()
   if held_keys['q']:
      if mouse.locked == True:
         mouse.locked = False
      else: mouse.locked = True

   if held_keys['f1']:
      if debug_mode == False:
         debug_mode = True
         print('Enabled Debug Mode')
         wait(.5)
      elif debug_mode == True:
         debug_mode = False
         print('Disabled Debug Mode')
         wait(.5)
   if debug_mode == True:
      if held_keys['f2']:
         if debug_print == False:
            debug_print = True
            print('Enabled Debug Printing')
            wait(.5)
         elif debug_print == True:
            debug_print = False
            print('Disabled Debug Printing')
            wait(.5)

def stats():
   global stamina, health

   if stamina < 0:
      if debug_print == True:
         print('Fixed stamina value less than "0"')
      stamina = 0
   if stamina > 0 and (held_keys['shift'] and (held_keys['w'] or held_keys['s'] or held_keys['a'] or held_keys['d'])):
      if held_keys['shift'] and (((held_keys['w'] and held_keys['s']) and not (held_keys['a'] or held_keys['d'])) or (held_keys['a'] and held_keys['d'] and not (held_keys['w'] or held_keys['s']))):
         pass
      else:
         if debug_print == True:
            print('Stamina: ' + str(stamina))
         if held_keys['w']:
            plr.speed = 12
         else:
            plr.speed = 10 
         stamina -= round(1)
   else:
      plr.speed = 5
      if (stamina < max_stamina) and not (held_keys['shift'] and ((held_keys['w']) or (held_keys['s']) or (held_keys['a']) or (held_keys['d']))):
         if debug_print == True:
            print('Stamina: ' + str(stamina))
         stamina += .2 * stamina_mult
         if stamina > max_stamina or (stamina > (max_stamina-2) and stamina < max_stamina):
            stamina = 100
            if debug_print == True:
               if stamina > max_stamina:
                  print('Fixed stamina value greather than "100"')
               else:
                  print('Fixed stuck stamina value')

   if plr.y < -50:
      health = 0

   if health <= 0:
      plr.rotation = (0,0,0)
      plr.x = 0
      plr.y = 0
      plr.z = 0
      health = max_health

def logging(log_type,code):
   if debug_logging == True:
      global log_title, clr
      f = open(log_code_file)
      code_file = json.load(f)
      if log_type == 'info':
         log_title = 'INFO' 
         clr = 'white'
      elif log_type == 'warn':
         log_title = 'WARN'
         clr = 'yellow'
      elif log_type == 'err' or 'error':
         log_type = 'error'
         log_title = 'ERROR'
         clr = 'red'
      for key,value in code_file[log_type].items():
         print(key+' - '+str(code))
         if key == code:
            print('Test')
            cprint(('['+log_title+' #'+key+']: '+value),clr)
   else: pass

# Temporary
from ursina import Button, scene, color, random, destroy, mouse
class Voxel(Button):
   def __init__(self, position=(0,0,0)):
         super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = .5,
            texture = 'white_cube',
            color = color.color(0, 0, random.uniform(.9, 1.0)),
            highlight_color = lime,
        )
   def input(self, key):
      if self.hovered:
         if key == 'right mouse down':
            voxel = Voxel(position=self.position + mouse.normal)
         if key == 'left mouse down':
            destroy(self)


for z in range(8):
    for x in range(8):
        voxel = Voxel(position=(x,0,z))

# Entities
# box = Entity(
#    model='cube', 
#    color=red, 
#    scale=(.5,.5,.5), 
#    collider='cube', 
#    rotation=(0,0,0),
#    position=(3,3,1)),

#-
window.fullscreen = False
window.borderless = False
window.exit_button.visible = False
def update():
   debug()
   stats()

class Controller(FirstPersonController):
  def __init__():
    super().__init__()
  def jump(self):
    pass


#controller = Controller()
keybind()
plr = FirstPersonController()
app.run()
