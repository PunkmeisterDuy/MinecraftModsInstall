import webbrowser
import time
import os

#REPLACE USERNAME_HERE WITH YOUR COMPUTERS USER NAME
main_dir = "C:/Users/USERNAME_HERE/Downloads/Mods"

if __name__ == "__main__":

    os.mkdir(main_dir)

    file = open("ModList.txt", "r")
    count = 0

    for i in file:
        webbrowser.open(i, new=2)
        print(i)
