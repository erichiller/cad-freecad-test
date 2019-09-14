# FREECADPATH = "C:\\Program Files\\FreeCAD\\lib;C:\\Users\\eric\\AppData\\Roaming\\Python\\Python36\\Scripts;C:\\Program Files\\FreeCAD\\lib;C:\\Program Files\\FreeCAD\\bin;C:\\Program Files\\FreeCAD\\bin\\Lib;C:\\Program Files\\FreeCAD\\bin\\Lib\\site-packages;C:\\Program Files\\FreeCAD\\bin\\DLLs"
# import sys


# sys.path.append(FREECADPATH)

# import FreeCAD

# import FreeCADGui
# FreeCADGui.showMainWindow()

# import Blender
# sys.path.append(FREECADPATH)


# def import_fcstd(filename):
#     try:
#         import FreeCAD
#     except ValueError:
#         Blender.Draw.PupMenu('Error%t')


# import FreeCAD


import Draft

import FreeCAD
# .Vector


myrect = Draft.makeRectangle(4, 3)
mydistance = FreeCAD.Vector(2, 2, 0)
Draft.move(myrect, mydistance)



def foo(eric) -> int:
    return 444




