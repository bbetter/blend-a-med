
import bpy
import os

from bpy.types import Operator

class BMD_OT_ExportObject(Operator):
    bl_idname = "bmd.export_objects"
    bl_label = "Export Scene Object"
    bl_description = "Export each scene object to a separate file depending on passed params"

    type: bpy.props.StringProperty()
    export_directory: bpy.props.StringProperty()

    def execute(self, context):
        scene = context.scene
    
        for obj in scene.objects:
            if obj.select_get() == False:
                continue

            os.makedirs(os.path.join(self.export_directory, obj.name))
            filename = os.path.join(self.export_directory, obj.name , obj.name + "." + self.type.lower())

            if self.type == "OBJ":
                bpy.ops.export_scene.obj(
                    filepath=filename,
                    use_selection=True,
                )
            elif self.type == "FBX":
                bpy.ops.export_scene.fbx(
                    filepath=filename,
                    use_selection=True,
                )
            elif self.type == "STL":
                bpy.ops.export_mesh.stl(
                    filepath=filename,
                    use_selection=True, 
                )
            else:
                print("NOT SUPPORTED TYPE")

        return {'FINISHED'}

class BMD_OT_select_export_directory(bpy.types.Operator):
    bl_idname = "bmd.select_export_directory"
    bl_label = "Select Export Directory"
    bl_description = "Select the directory where exported files will be saved"

    def execute(self, context):
        # Open a file dialog to select the output directory
        context.window_manager.fileselect_add(self)

        return {'RUNNING_MODAL'}

    def invoke(self, context, event):
        wm = context.window_manager
        wm.fileselect_add(self)
        return {'RUNNING_MODAL'}

