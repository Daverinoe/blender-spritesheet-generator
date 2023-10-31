from . import render_spritesheet
from . import render_normals

def register():
    render_spritesheet.register()
    render_normals.register()

def unregister():
    render_spritesheet.unregister()
    render_normals.unregister()