bl_info = {
    "name": "Render Spritesheet",
    "blender": (3, 6, 5),
    "category": "Object",
    "description": "Render animation frames to a spritesheet",
    "author": "Daverinoe",
    "version": (1, 0),
    "location": "View3D > Object",
    "warning": "",  
    "doc_url": "",  
    "tracker_url": "", 
}

from . import properties
from . import operators
from . import panels

def register():
    properties.register()
    operators.register()
    panels.register()

def unregister():
    panels.unregister()
    operators.unregister()
    properties.unregister()