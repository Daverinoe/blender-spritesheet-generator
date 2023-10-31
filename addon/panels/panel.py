import bpy

class VIEW3D_PT_render_spritesheet(bpy.types.Panel):
    bl_label = "Render Spritesheet"
    bl_idname = "VIEW3D_PT_render_spritesheet"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Tools"

    def draw(self, context):
        layout = self.layout
        
        # Access properties from the properties class
        props = context.scene.spritesheet_props
        
        layout.prop(props, "frame_skip")
        layout.prop(props, "num_rows")
        layout.prop(props, "object_to_render")

        layout.operator("object.render_spritesheet")
        layout.operator("object.render_normals")

def register():
    bpy.utils.register_class(VIEW3D_PT_render_spritesheet)

def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_render_spritesheet)