import bpy
import numpy as np
from PIL import Image
import os
import shutil
from .utils import get_frame_range, create_spritesheet_image, render_frame, delete_frames_folder

class OBJECT_OT_render_normals(bpy.types.Operator):
    bl_idname = "object.render_normals"
    bl_label = "Render Normals"
    bl_options = {'REGISTER', 'UNDO'}

    def create_normal_material(self):
        normal_material = bpy.data.materials.new(name="NormalMaterial")
        normal_material.use_nodes = True
        nodes = normal_material.node_tree.nodes
        nodes.clear()

        geometry_node = nodes.new(type='ShaderNodeNewGeometry')
        emission_node = nodes.new(type='ShaderNodeEmission')
        material_output_node = nodes.new(type='ShaderNodeOutputMaterial')

        normal_material.node_tree.links.new(
            geometry_node.outputs['Normal'],
            emission_node.inputs['Color']
        )
        normal_material.node_tree.links.new(
            emission_node.outputs['Emission'],
            material_output_node.inputs['Surface']
        )
        
        return normal_material

    def render_normals(self, context, props, action, normal_material, output_path):
        increment_angle = 360 / props.num_rows

        props.object_to_render.animation_data.action = action
        action_output_path = f"{output_path}{action.name}_"
        for track in props.object_to_render.animation_data.nla_tracks:
            for strip in track.strips:
                if strip.action != action:
                    continue
                frame_start, frame_end = get_frame_range(strip)
                frame_width, frame_height = context.scene.render.resolution_x, context.scene.render.resolution_y
                total_frames = frame_end - frame_start + 1
                rendered_frames = np.ceil(total_frames / props.frame_skip)

                # Now calculate the sheet_width based on the number of rendered frames
                spritesheet = create_spritesheet_image(frame_width, frame_height, props.num_rows, rendered_frames)

                # Find all mesh objects in the scene
                mesh_objects = [obj for obj in bpy.data.objects if obj.type == 'MESH']

                # Backup original materials and assign the normal material
                original_materials = {}
                for obj in mesh_objects:
                    original_materials[obj] = obj.data.materials[:]
                    obj.data.materials.clear()
                    obj.data.materials.append(normal_material)

                for row in range(props.num_rows):
                    props.object_to_render.rotation_euler.z = -np.radians(row * increment_angle)

                    x_offset = 0 
                    for frame in range(frame_start, frame_end + 1, props.frame_skip):
                        context.scene.frame_set(frame)
                        context.scene.render.filepath = f"{action_output_path}row{row}_frame{frame:04d}"
                        bpy.ops.render.render(write_still=True)
                        
                        frame_image = render_frame(action_output_path, row, frame)
                        spritesheet.paste(frame_image, (x_offset, row * frame_height))
                        x_offset += frame_width
                
                spritesheet.save(bpy.path.abspath(f"//{action.name}_normal_map_spritesheet.png"))

                # Restore original materials
                for obj, materials in original_materials.items():
                    obj.data.materials.clear()
                    for material in materials:
                        obj.data.materials.append(material)

    def execute(self, context):
        props = context.scene.spritesheet_props
        bpy.context.scene.render.image_settings.file_format = 'PNG'
        bpy.context.scene.render.image_settings.color_mode = 'RGBA'
        frames_folder = bpy.path.abspath("//frames")
        output_path = frames_folder + "/frame_"

        for action in bpy.data.actions:
            self.render_normals(context, props, action, self.create_normal_material(), output_path)
        
        delete_frames_folder(frames_folder)
        return {'FINISHED'}

def register():
    bpy.utils.register_class(OBJECT_OT_render_normals)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_render_normals)

if __name__ == "__main__":
    register()
