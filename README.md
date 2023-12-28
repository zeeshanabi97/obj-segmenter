 **README**

**Script Title:** Control Surface Splitter

**Description:**

This Python script, designed for Blender, automates the process of splitting a 3D control surface object into multiple separate objects based on criteria defined in an input file.

**Key Functionalities:**

- Imports a 3D object model from an OBJ file.
- Rotates the object 90 degrees around the X-axis.
- Reads face selection criteria from an input text file.
- Selects faces of the mesh based on their median point coordinates.
- Separates the selected faces into individual objects.
- Sets the origin of each separated object to its center of mass.
- Repositions the origins of objects based on bounding box coordinates.

**Requirements:**

- Blender (version 2.80 or later recommended)
- Python modules: bpy, bmesh, math, mathutils

**Usage Instructions:**

1. **Save the script:** Place this script in a convenient location within your Blender project.
2. **Edit file paths:** Update the `obj_path` and `file_path` variables with the correct paths to your OBJ file and input text file, respectively.
3. **Run the script:** Execute the script from Blender's Text Editor or Python console.

**Input File Format:**

The input text file should contain lines of comma-separated values, defining bounding box ranges for face selection:

```
min_x,max_x,min_y,max_y,min_z,max_z
```

**Additional Notes:**

- Ensure the imported OBJ file contains a mesh object.
- The script assumes a specific structure for the input text file.
- Consider adjusting the rotation and origin placement logic based on your specific model and requirements.
- For importing in Unity export the object as fbx while keeping up axis Y and forward axis -Z
