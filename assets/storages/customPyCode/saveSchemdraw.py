import subprocess
import os

def saveSchematic(element, originFile):
    fileType = ".png"
    filepath = os.path.dirname(originFile)
    name = os.path.basename(originFile).replace(".py","")
    element.save(name+fileType, dpi=300, transparent=False)
    file = filepath+os.sep+name+fileType
    
    # Run GIMP with batch commands
    gimpPath = r"C:\Program Files\GIMP 2\bin\gimp-console-2.10.exe"
    script = (f"from gimpfu import *; \
              image = pdb.gimp_file_load(\\\"{file.replace("\\","\\\\")}\\\", \\\"{file.replace("\\","\\\\")}\\\"); \
              drawable = pdb.gimp_image_get_active_layer(image); \
              pdb.python_fu_process_graphics(image, drawable, \\\"{filepath.replace("\\","\\\\")}\\\", \\\"{name.replace("\\","\\\\")}\\\"); \
              pdb.gimp_quit(0);")
    
    command = f"\"{gimpPath}\" -i --batch-interpreter=python-fu-eval -b \"{script}\""
    print(command)
    subprocess.run(command, shell=True)
    os.remove(name+fileType)
