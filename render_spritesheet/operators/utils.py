from PIL import Image
import numpy as np
import os
import bpy
import shutil

def create_spritesheet_image(frame_width, frame_height, num_rows, rendered_frames):
    sheet_width = frame_width * rendered_frames
    sheet_height = frame_height * num_rows
    return Image.new('RGBA', (int(sheet_width), int(sheet_height)))

def get_frame_range(strip):
    return int(strip.action_frame_start), int(strip.action_frame_end)

def render_frame(action_output_path, row, frame):
    bpy.context.scene.render.filepath = f"{action_output_path}row{row}_frame{frame:04d}"
    bpy.ops.render.render(write_still=True)
    frame_filename = f"{action_output_path}row{row}_frame{frame:04d}.png"
    return Image.open(bpy.path.abspath(frame_filename))

def delete_frames_folder(folder_path):
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
