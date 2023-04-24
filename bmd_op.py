
from typing import Set
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
    
        selected_objects = []
        for obj in scene.objects:
            if obj.select_get() == True:
                selected_objects.append(obj)
                obj.select_set(False)
                continue
        
        for obj in selected_objects:
            obj.select_set(True)

            extension = self.type.lower()
            folder_name = obj.name + "_" + extension
            os.makedirs(os.path.join(self.export_directory, folder_name), exist_ok = True)
            filename = os.path.join(self.export_directory, folder_name, obj.name + "." + extension)
            
            self.report({'INFO'}, "==== BEGIN OBJECT {} ===".format(obj.name))
            if os.path.isfile(filename):
                self.report({'INFO'}, "File: {} exists".format(filename))
                self.report({'INFO'}, "Removing...")
                os.remove(filename)
                

            self.report({'INFO'}, "Exporting into {} format".format(self.type))
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

            self.report({'INFO'}, "==== END OBJ {} ===".format(obj.name))
            obj.select_set(False)

            self.report({'INFO'}, "...")


        self.report({'INFO'}, "Successfully completed export of {} objects".format(len(selected_objects)))

        while selected_objects:
            selected_objects.pop().select_set(True)

        return {'FINISHED'}
    
    def invoke(self, context, event) -> Set[str] | Set[int]:
        print(event)
        wm = context.window_manager
        if event.shift:
            return wm.invoke_confirm(self, event)
        return self.execute(context)

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

# TODO: Use this as confirmation
class BMD_OT_delete(bpy.types.Operator):
    bl_idname = "bmd.delete_file"
    bl_label = "File already exist. Delete?"
    bl_options = {'REGISTER', 'UNDO'}

    filename: bpy.props.StringProperty()

    def execute(self, context):
        print("execute with "+ self.filename)
      
        return {'RUNNING_MODAL'}
    
    def invoke(self, context, event) -> Set[str] | Set[int]:
        print("invoke with "+ self.filename)
        return context.window_manager.invoke_confirm(self, event)

