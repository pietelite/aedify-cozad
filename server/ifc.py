# IFC manipulation file
import ifcopenshell
import os

def update():
    ifc_file = ifcopenshell.open('d/Projects/aedify/cozad/server/assets/sample_structure.ifc')
    print(ifc_file)

update()
