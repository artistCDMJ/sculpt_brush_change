# -*- coding: utf8 -*-
# python
# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8 compliant>


bl_info = {
    'name': 'Sculpt Brush Change',
    'author': 'artistCDMJ',
    'version': (1, 10),
    'blender': (2, 79, 0),
    'location': '3D View > Tool Bar > Tools > Sculpt Brushes',
    'warning': '',
    'description': 'Example for putting brushes inside operators and panel buttons',
    'wiki_url': '',
    'tracker_url': '',
    'category': 'Sculpt'}


import bpy


class BrushBlob(bpy.types.Operator):
    """Brush Blob"""
    bl_idname = "object.brush_blob"
    bl_label = "Brush Blob"
    bl_options = { 'REGISTER', 'UNDO' }

    def execute(self, context):

        scene = context.scene

        bpy.ops.paint.brush_select(sculpt_tool='BLOB')

        return {'FINISHED'}
    
class BrushClay(bpy.types.Operator):
    """Brush Clay"""
    bl_idname = "object.brush_clay"
    bl_label = "Brush Clay"
    bl_options = { 'REGISTER', 'UNDO' }

    def execute(self, context):

        scene = context.scene

        bpy.ops.paint.brush_select(sculpt_tool='CLAY')

        return {'FINISHED'}

class BrushClayStrip(bpy.types.Operator):
    """Brush Clay"""
    bl_idname = "object.brush_claystrips"
    bl_label = "Brush Clay Strips"
    bl_options = { 'REGISTER', 'UNDO' }

    def execute(self, context):

        scene = context.scene

        bpy.ops.paint.brush_select(sculpt_tool='CLAY_STRIPS')

        return {'FINISHED'}
    
class BrushCrease(bpy.types.Operator):
    """Brush Clay"""
    bl_idname = "object.brush_crease"
    bl_label = "Brush Crease"
    bl_options = { 'REGISTER', 'UNDO' }

    def execute(self, context):

        scene = context.scene

        bpy.ops.paint.brush_select(sculpt_tool='CREASE')

        return {'FINISHED'}

class BrushFill(bpy.types.Operator):
    """Brush Fill"""
    bl_idname = "object.brush_fill"
    bl_label = "Brush Fill"
    bl_options = { 'REGISTER', 'UNDO' }

    def execute(self, context):

        scene = context.scene

        bpy.ops.paint.brush_select(sculpt_tool='FILL')

        return {'FINISHED'}

class BrushFlatten(bpy.types.Operator):
    """Brush Flatten"""
    bl_idname = "object.brush_flatten"
    bl_label = "Brush Flatten"
    bl_options = { 'REGISTER', 'UNDO' }

    def execute(self, context):

        scene = context.scene

        bpy.ops.paint.brush_select(sculpt_tool='FLATTEN')

        return {'FINISHED'}

class BrushGrab(bpy.types.Operator):
    """Brush Grab"""
    bl_idname = "object.brush_grab"
    bl_label = "Brush Grab"
    bl_options = { 'REGISTER', 'UNDO' }

    def execute(self, context):

        scene = context.scene

        bpy.ops.paint.brush_select(sculpt_tool='GRAB')

        return {'FINISHED'}

class BrushInflate(bpy.types.Operator):
    """Brush Clay"""
    bl_idname = "object.brush_inflate"
    bl_label = "Brush Inflate"
    bl_options = { 'REGISTER', 'UNDO' }

    def execute(self, context):

        scene = context.scene

        bpy.ops.paint.brush_select(sculpt_tool='INFLATE')

        return {'FINISHED'}

class BrushLayer(bpy.types.Operator):
    """Brush layer"""
    bl_idname = "object.brush_layer"
    bl_label = "Brush Layer"
    bl_options = { 'REGISTER', 'UNDO' }

    def execute(self, context):

        scene = context.scene

        bpy.ops.paint.brush_select(sculpt_tool='LAYER')

        return {'FINISHED'}

class BrushMask(bpy.types.Operator):
    """Brush Mask"""
    bl_idname = "object.brush_mask"
    bl_label = "Brush Mask"
    bl_options = { 'REGISTER', 'UNDO' }

    def execute(self, context):

        scene = context.scene

        bpy.ops.paint.brush_select(sculpt_tool='MASK')

        return {'FINISHED'}

class BrushNudge(bpy.types.Operator):
    """Brush Nudge"""
    bl_idname = "object.brush_nudge"
    bl_label = "Brush Nudege"
    bl_options = { 'REGISTER', 'UNDO' }

    def execute(self, context):

        scene = context.scene

        bpy.ops.paint.brush_select(sculpt_tool='NUDGE')

        return {'FINISHED'}

class BrushPinch(bpy.types.Operator):
    """Brush Pinch"""
    bl_idname = "object.brush_pinch"
    bl_label = "Brush Pinch"
    bl_options = { 'REGISTER', 'UNDO' }

    def execute(self, context):

        scene = context.scene

        bpy.ops.paint.brush_select(sculpt_tool='PINCH')

        return {'FINISHED'}

class BrushScrape(bpy.types.Operator):
    """Brush Scrape"""
    bl_idname = "object.brush_scrape"
    bl_label = "Brush Scrape"
    bl_options = { 'REGISTER', 'UNDO' }

    def execute(self, context):

        scene = context.scene

        bpy.ops.paint.brush_select(sculpt_tool='SCRAPE')

        return {'FINISHED'}

class BrushSculptDraw(bpy.types.Operator):
    """Brush Sculpt Draw"""
    bl_idname = "object.brush_sculptdraw"
    bl_label = "Brush Sculpt Draw"
    bl_options = { 'REGISTER', 'UNDO' }

    def execute(self, context):

        scene = context.scene

        bpy.ops.paint.brush_select(sculpt_tool='DRAW')

        return {'FINISHED'}

class BrushSmooth(bpy.types.Operator):
    """Brush Smooth"""
    bl_idname = "object.brush_smooth"
    bl_label = "Brush Smooth"
    bl_options = { 'REGISTER', 'UNDO' }

    def execute(self, context):

        scene = context.scene

        bpy.ops.paint.brush_select(sculpt_tool='SMOOTH')

        return {'FINISHED'}

class BrushSnakeHook(bpy.types.Operator):
    """Brush Snake Hook"""
    bl_idname = "object.brush_snakehook"
    bl_label = "Brush Snake Hook"
    bl_options = { 'REGISTER', 'UNDO' }

    def execute(self, context):

        scene = context.scene

        bpy.ops.paint.brush_select(sculpt_tool='SNAKE_HOOK')

        return {'FINISHED'}

class BrushThumb(bpy.types.Operator):
    """Brush Thumb"""
    bl_idname = "object.brush_thumb"
    bl_label = "Brush Thumb"
    bl_options = { 'REGISTER', 'UNDO' }

    def execute(self, context):

        scene = context.scene

        bpy.ops.paint.brush_select(sculpt_tool='THUMB')

        return {'FINISHED'}

class BrushRotate(bpy.types.Operator):
    """Brush Rotate"""
    bl_idname = "object.brush_rotate"
    bl_label = "Brush Rotate"
    bl_options = { 'REGISTER', 'UNDO' }

    def execute(self, context):

        scene = context.scene

        bpy.ops.paint.brush_select(sculpt_tool='ROTATE')

        return {'FINISHED'}


class SculptBrushPanel(bpy.types.Panel):
    """A custom panel in the viewport toolbar"""
    bl_label = "Sculpt Brushes"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Tools"
    
    
    @classmethod
    def poll(cls, context):
        obj = context.active_object
        A = obj is not None
        B = context.mode == 'SCULPT'
        
        return A and B
    
    
    def draw(self, context):
        layout = self.layout

        
        row = layout.row()
        row.operator("object.brush_blob", text = "", icon = 'BRUSH_BLOB')
        row.operator("object.brush_clay", text="", icon = 'BRUSH_CLAY')
        row.operator("object.brush_claystrips", text="", icon = 'BRUSH_CLAY_STRIPS')
        row.operator("object.brush_crease", text="", icon = 'BRUSH_CREASE')
        row.operator("object.brush_fill", text="", icon = 'BRUSH_FILL')
        row.operator("object.brush_flatten", text="", icon = 'BRUSH_FLATTEN')
        row=layout.row()
        row.operator("object.brush_grab", text="", icon = 'BRUSH_GRAB')
        row.operator("object.brush_inflate", text="", icon = 'BRUSH_INFLATE')
        row.operator("object.brush_layer", text="", icon = 'BRUSH_LAYER')
        row.operator("object.brush_mask", text="", icon = 'BRUSH_MASK')
        row.operator("object.brush_nudge", text="", icon = 'BRUSH_NUDGE')
        row.operator("object.brush_pinch", text="", icon = 'BRUSH_PINCH')
        row = layout.row()
        row.operator("object.brush_scrape", text="", icon = 'BRUSH_SCRAPE')
        row.operator("object.brush_sculptdraw", text="", icon = 'BRUSH_SCULPT_DRAW')
        row.operator("object.brush_smooth", text="", icon = 'BRUSH_SMOOTH')
        row.operator("object.brush_snakehook", text="", icon = 'BRUSH_SNAKE_HOOK')
        row.operator("object.brush_thumb", text="", icon = 'BRUSH_THUMB')
        row.operator("object.brush_rotate", text="", icon = 'BRUSH_ROTATE')

def register():

    bpy.utils.register_module(__name__)


def unregister():

    bpy.utils.unregister_module(__name__)




if __name__ == "__main__":
    register()
