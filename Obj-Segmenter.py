import bpy
import bmesh
import math
from mathutils import Vector

bpy.ops.object.mode_set(mode='OBJECT')
# Delete existing objects
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Import the object
obj_path = "F:\\unity.obj"  # Replace with your file path
bpy.ops.wm.obj_import(filepath=obj_path)

file_path = "F:\\inputfile.txt"

# Get the active object
obj = bpy.context.active_object

# Rotate 90 degrees around the X-axis
bpy.ops.transform.rotate(value=math.pi/2, orient_axis='X')
bpy.ops.transform.rotate(value=math.pi, orient_axis='Z')

bpy.ops.object.mode_set(mode='EDIT')

# Ensure it's a mesh object
if obj.type == 'MESH':
    bm = bmesh.from_edit_mesh(obj.data)

# Deselect all faces initially
    bm.select_mode = {'FACE'}
    bm.select_flush_mode()

    # Select faces based on the x value of their median point
file = open(file_path)
for line in file:
    ab = line.split(",")
    for face in bm.faces:
        median_point = face.calc_center_median()
        if (median_point.x > float(ab[0]) and median_point.x < float(ab[1]) and median_point.y > float(ab[2]) and median_point.y < float(ab[3]) and median_point.z > float(ab[4]) and median_point.z < float(ab[5])):
            face.select = True

     
    bpy.ops.mesh.separate(type='SELECTED')
bpy.ops.object.mode_set(mode='OBJECT')    
file.close()
for obj in bpy.context.selected_objects:
    bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')  # Set origin to center of mass

# Get all objects in the scene
all_objects = bpy.data.objects

bpy.ops.object.select_all(action='DESELECT')

# Select all objects except the first one
for obj in all_objects[1:]:
    obj.select_set(True)  # Set the object as selected
    
for obj in bpy.context.selected_objects:
    bbox = obj.bound_box
    print(bbox[0][0])

