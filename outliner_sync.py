bl_info = {
    "name": "Outliner Sync",
    "author": "high_byte",
    "version": (1, 0, 0),
    "blender": (3, 40, 0),
    "location": "Outliner",
    "description": "Always show active object in outliner",
    "warning": "",
    "wiki_url": "",
    "category": "Tools",
}

import bpy

def use_outliner():
  for area in bpy.context.screen.areas:
    if area.type != 'OUTLINER':
      continue

    for region in area.regions:
      if region.type != 'WINDOW':
        continue

      return bpy.context.temp_override(area=area, region=region)

  raise Exception('outliner not found')

def msgbus_callback():
  with use_outliner():
    bpy.ops.outliner.show_active()

addon_owner = '_owner_placeholder_'

def register():
  bpy.msgbus.subscribe_rna(
      key=(bpy.types.LayerObjects, 'active'),
      owner=addon_owner,
      args=(),
      notify=msgbus_callback
  )

def unregister():
    bpy.msgbus.clear_by_owner(addon_owner)

if __name__ == "__main__":
    register()
