# Render Spritesheet Add-on

Render Spritesheet is a Blender add-on that allows you to render out spritesheets and normal maps from your 3D models, which can be useful for game development or other projects. Here are the steps to use this add-on:

## Installation

### Obtaining the Add-on

1. **Option A: Downloading a Release:**
   - Go to the [Releases](https://github.com/Daverinoe/blender-spritesheet-generator/releases/tag/1.0) page of the Render Spritesheet repository.
   - Download the latest release ZIP file.

2. **Option B: Downloading the Repository:**
   - Clone or download the entire [Render Spritesheet repository](https://github.com/Daverinoe/blender-spritesheet-generator).
   - Locate the add-on folder (`render_spritesheet`), and create a ZIP file containing the `render_spritesheet` folder.

### Installing the Add-on in Blender

1. Open Blender.
2. Go to `Edit` -> `Preferences` -> `Add-ons` -> `Install...`.
3. Navigate to where the ZIP file is located (from either Option A or Option B above), select it, and click `Install Add-on`.

## Usage

### Preparing Your Scene

1. **Set Render Resolution:**
   - Set the desired resolution for your render in the Render Properties panel.

2. **Select the Object:**
   - Select the object you want to render in the 3D viewport.
   - In the Render Spritesheet panel, use the `Object to Render` field to specify the object you have selected.

3. **Prepare Animations:**
   - Make sure your animations are pushed down into NLA (Non-Linear Animation) strips.
   - Each different NLA strip will be considered as a separate animation.

4. **Set Frame Skip:**
   - In the Render Spritesheet panel, set the `Frame Skip` value to determine how many frames to skip in the animation.
   - A smaller value will result in more frames being rendered, and a larger value will result in fewer frames being rendered.

5. **Set Rotation Steps:**
   - In the Render Spritesheet panel, set the `Number of Rows` value to determine how many rotation steps you want.
   - This value determines how many times the object will be rotated and rendered to cover a full 360-degree rotation. For example, a value of 4 will result in four rotations of 90 degrees each.

### Rendering Spritesheets and Normal Maps

1. **Render Spritesheets:**
   - Click the `Render Spritesheet` button in the Render Spritesheet panel to render out the spritesheets for each animation.
   - The spritesheets will be saved to the same directory as your Blender file, with the naming convention `<animation_name>_spritesheet.png`.

2. **Render Normal Maps:**
   - Click the `Render Normals` button in the Render Spritesheet panel to render out the normal maps for each animation.
   - The normal maps will be saved to the same directory as your Blender file, with the naming convention `<animation_name>_normal_map_spritesheet.png`.

Your spritesheets and normal maps are now ready for use in your game or project!

If you have any problems or suggestions, please create an issue!