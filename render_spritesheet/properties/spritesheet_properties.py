import bpy

class SpritesheetProperties(bpy.types.PropertyGroup):
    frame_skip: bpy.props.IntProperty(
        name="Frame Skip",
        description="Only take every nth frame (skip this number of frames each step)",
        default=5,
        min=1
    )
    
    num_rows: bpy.props.IntProperty(
        name="Number of Rows",
        description="Number of rows in your spritesheet (each representing a different rotation)",
        default=16,
        min=1
    )
    
    object_to_render: bpy.props.PointerProperty(
        name="Object to render",
        description="Object to be rotated",
        type=bpy.types.Object
    )

def register():
    bpy.utils.register_class(SpritesheetProperties)
    bpy.types.Scene.spritesheet_props = bpy.props.PointerProperty(type=SpritesheetProperties)


def unregister():
    del bpy.types.Scene.spritesheet_props
    bpy.utils.unregister_class(SpritesheetProperties)