forward = 'w'
backward = 's'
left = 'a'
right = 'd'
sprint = 'shift'

def keybind():
   from ursina.input_handler import bind
   bind('gamepad dpad up', forward)
   bind('gamepad dpad down', backward)
   bind('gamepad dpad left', left)
   bind('gamepad dpad right', right)
   bind('gamepad a', sprint)
   bind('arrow up', forward)
   bind('arrow down', backward)
   bind('arrow left', left)
   bind('arrow right', right)
