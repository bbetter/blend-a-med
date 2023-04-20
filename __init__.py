# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "BlendAMed",
    "author" : "Andrii",
    "description" : "",
    "blender" : (3, 5, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}

import bpy
import os


from . bmd_panel import BMD_PT_Panel
from . bmd_op import BMD_OT_ExportObject
from . bmd_op import BMD_OT_select_export_directory

classes = (
    BMD_PT_Panel,
    BMD_OT_ExportObject,
    BMD_OT_select_export_directory
)

def register():
    for c in classes:
        bpy.utils.register_class(c)

    bpy.types.Scene.export_directory = bpy.props.StringProperty(
        name="Export Directory",
        description="The directory where exported files will be saved",
        default=os.path.expanduser("~"),
        subtype="DIR_PATH",
    )

def unregister():
    for c in reversed(classes):
        bpy.utils.unregister_class(c)

    del bpy.types.Scene.export_directory

