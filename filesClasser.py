#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import glob
import shutil
import tkinter as tk
from tkinter import filedialog
rep = 'Y'
root = tk.Tk()
root.withdraw()
while rep == 'Y':
    cwd = filedialog.askdirectory()
    print('Current directory :', cwd)
    nbrExtention = int(input('How many folder : '))
    directories = []
    extentions = []
    for i in range(nbrExtention):
        directorie = input(f'Name of folder {i + 1} : ')
        extention = input('Name of extention : ')
        directories.append(directorie)
        extentions.append("/*." + extention)
    for i in range(nbrExtention):
        files = [f for f in glob.glob(cwd + extentions[i])] 
        inPath = "/" + directories[i]
        path = cwd + inPath            
        try:
            os.mkdir(path)
        except OSError:
            print ("Creation of the directory %s failed" % path)
        else:
            print ("Successfully created the directory %s " % path)
        try:
            for file in files : 
                shutil.move(file, path)
        except OSError:
            print ("Error !")
        else:
            print(f"Successfully moved all {directories[i]} files !")    
    rep = input('Do it again ? (Y/N) : ')
input('Press any button to exit')
