import bpy
import numpy as np
from PIL import Image
import shutil
import os
from .utils import get_frame_range, create_spritesheet_image, render_frame, delete_frames_folder

class OBJECT_OT_render_spritesheet(bpy.types.Operator):
    bl_idname = "object.render_spritesheet"
    bl_label = "Render Spritesheet"
    bl_options = {'REGISTER', 'UNDO'}

    def render_spritesheet(self, props, action, output_path):
        increment_angle = 360 / props.num_rows

        props.object_to_render.animation_data.action = action
        action_output_path = f"{output_path}{action.name}_"
        if not (props.object_to_render.animation_data and props.object_to_render.animation_data.nla_tracks):
            return {'FINISHED'}

        for track in props.object_to_render.animation_data.nla_tracks:
            for strip in track.strips:
                if strip.action != action:
                    continue

                frame_start, frame_end = get_frame_range(strip)
                frame_width, frame_height = bpy.context.scene.render.resolution_x, bpy.context.scene.render.resolution_y
                total_frames = frame_end - frame_start + 1
                rendered_frames = np.ceil(total_frames / props.frame_skip)
                spritesheet = create_spritesheet_image(frame_width, frame_height, props.num_rows, rendered_frames)

                for row in range(props.num_rows):
                    props.object_to_render.rotation_euler.z = -np.radians(row * increment_angle)
                    x_offset = 0
                    for frame in range(frame_start, frame_end + 1, props.frame_skip):
                        bpy.context.scene.frame_set(frame)
                        frame_image = render_frame(action_output_path, row, frame)
                        spritesheet.paste(frame_image, (x_offset, row * frame_height))
                        x_offset += frame_width

                spritesheet.save(bpy.path.abspath(f"//{action.name}_spritesheet.png"))

    def execute(self, context):
        props = context.scene.spritesheet_props
        bpy.context.scene.render.image_settings.file_format = 'PNG'
        bpy.context.scene.render.image_settings.color_mode = 'RGBA'
        frames_folder = bpy.path.abspath("//frames")
        output_path = frames_folder + "/frame_"
       
        for action in bpy.data.actions:
            self.render_spritesheet(props, action, output_path)

        delete_frames_folder(frames_folder)

        return {'FINISHED'}

def register():
    bpy.utils.register_class(OBJECT_OT_render_spritesheet)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_render_spritesheet)

if __name__ == "__main__":
    register()
