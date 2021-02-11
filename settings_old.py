# Imports
from ursina import window, camera
from ursina.color import gray

# Window
window.color = gray
window.title = 'Hello World'
window.borderless = False
window.fullscreen = False
window.exit_button.visible = False

# Camera
camera.eternal = True
camera.fov = 95


#camera.orthographic = True
