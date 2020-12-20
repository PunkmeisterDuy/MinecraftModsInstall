import os
from ModDownload import main_dir
import shutil
from zipfile import ZipFile 

dir = main_dir.split("/")[2]
minecraft_dir = "C:/Users/" + dir + "/AppData/Roaming/.minecraft/mods"

print(main_dir)
print(dir)
print(minecraft_dir)



ask = input("Are these directories correct. Did you remember to move mods inside mods folder inside downloads y/n: ")
if (ask == "y"):
    files = os.listdir(main_dir)

    for f in files:
        file = main_dir + "/" + f

        if (f.find("zip")>0):
            with ZipFile(file, 'r') as zip: 
                extract_dir = file.replace(".zip","")
                print(extract_dir)
                os.mkdir(extract_dir)
                os.chdir(extract_dir)
                zip.extractall() 
            print("Extracting: " + file)
        
        if (file.find("ini") < 0):
            print("Moving: " + f)
            dest = shutil.move(file, minecraft_dir)
