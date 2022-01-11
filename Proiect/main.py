from posixpath import abspath
from flask import Flask, render_template, request, redirect
from pathlib import Path
import os
import time
import shutil

app = Flask(__name__)
FILE_SYSTEM_ROOT = "d:\Facultate\Python\Proiect\Browser-Total-Commander\Proiect"
pathA = 'Files'
pathB = 'Files'
@app.route("/")
def home():
    itemListA = os.listdir(os.path.join(FILE_SYSTEM_ROOT, pathA))
    itemListA = [[x,] for x in itemListA]
    itemListB = os.listdir(os.path.join(FILE_SYSTEM_ROOT, pathB))
    itemListB = [[x,] for x in itemListB]
    for item in itemListA:
        if(os.path.isdir( os.path.join(os.path.join(FILE_SYSTEM_ROOT, pathA), item[0]))):
            item.append("DIR")
        else:
            item.append(os.path.getsize( os.path.join(os.path.join(FILE_SYSTEM_ROOT, pathA), item[0]) ))
    for item in itemListA:
        item.append(time.ctime(os.path.getctime( os.path.join(os.path.join(FILE_SYSTEM_ROOT, pathA), item[0]) ))  )
    for item in itemListB:
        if(os.path.isdir(os.path.join(os.path.join(FILE_SYSTEM_ROOT, pathB), item[0]))):
            item.append("DIR")
        else:
            item.append(os.path.getsize( os.path.join(os.path.join(FILE_SYSTEM_ROOT, pathB), item[0]) ))
    for item in itemListB:
        item.append(time.ctime(os.path.getctime( os.path.join(os.path.join(FILE_SYSTEM_ROOT, pathB), item[0]) ))  )
    return render_template('index.html', itemListA = itemListA, itemListB = itemListB, pathA = pathA, pathB = pathB)

@app.route("/create",  methods=["GET", "POST"])
def create():
    if request.method == 'POST':
        side = request.form['side']
        if(side=='A'):
            absPath = os.path.join(FILE_SYSTEM_ROOT, pathA)
        elif(side=='B'):
            absPath = os.path.join(FILE_SYSTEM_ROOT, pathB)
        if(request.form['type'] == 'file'):
            with open(os.path.join(absPath, request.form['fileName']), 'w') as fp:
                pass
        elif(request.form['type'] == 'folder'):
            os.mkdir(os.path.join(absPath, request.form['fileName']))
    return home()

@app.route("/browserA/<path>")
def browserA(path):
    global pathA
    pathA = os.path.join(pathA, path)
    abs_path = os.path.join(FILE_SYSTEM_ROOT, pathA);
    # Return 404 if path doesn't exist
    if not os.path.exists(abs_path):
        return "Eroare 404"

    # Check if path is a file and serve
    if os.path.isfile(abs_path):
        return "Este un fisier"

    # Show directory contents
    #itemListA = os.listdir(abs_path)
    #itemListB = os.listdir(os.path.join(FILE_SYSTEM_ROOT, pathB))
    #return render_template('index.html', itemListA = itemListA, itemListB = itemListB, pathA=pathA, pathB=pathB)
    return home()

@app.route("/browserB/<path>")
def browserB(path):
    global pathB
    pathB = os.path.join(pathB, path)
    abs_path = os.path.join(FILE_SYSTEM_ROOT, pathB);
    # Return 404 if path doesn't exist
    if not os.path.exists(abs_path):
        return "Eroare 404"

    # Check if path is a file and serve
    if os.path.isfile(abs_path):
        return "Este un fisier"

    # Show directory contents
    #itemListB = os.listdir(abs_path)
    #itemListA = os.listdir(os.path.join(FILE_SYSTEM_ROOT, pathA))
    #return render_template('index.html', itemListA = itemListA, itemListB = itemListB, pathA=pathA, pathB=pathB)
    return home()

@app.route("/back", methods=["GET", "POST"])
def goBack():
    global pathA, pathB
    if request.method == 'POST':
        side = request.form['side']
        if(side == 'A'):
            pathA = str(Path(pathA).parents[0])
        elif(side == 'B'):
            pathB = str(Path(pathB).parents[0])
    return redirect("/")

@app.route("/delete", methods = ["GET", "POST"])
def deleteFiles():
    listToDelete = request.form.getlist("listToDelete[]")
    side = request.form['side']
    listToDelete.pop(0);
    for element in listToDelete:
        if(side=='A'):
            absPath = os.path.join(FILE_SYSTEM_ROOT, pathA)
        elif(side == 'B'):
            absPath = os.path.join(FILE_SYSTEM_ROOT, pathB)
        absPath = os.path.join(absPath, element)
        if(os.path.isfile(absPath)):
            os.remove(absPath)
        elif(os.path.isdir(absPath)):
            shutil.rmtree(absPath, ignore_errors=True)
    return home()

@app.route("/copy", methods = ["GET", "POST"])
def copyFiles():
    listToCopy = request.form.getlist("listToCopy[]")
    side = request.form['side']
    listToCopy.pop(0)
    for element in listToCopy:
        if(side == 'A'):
            srcPath = os.path.join(FILE_SYSTEM_ROOT, pathA)
            destPath = os.path.join(FILE_SYSTEM_ROOT, pathB)
        elif(side == 'B'):
            srcPath = os.path.join(FILE_SYSTEM_ROOT, pathB)
            destPath = os.path.join(FILE_SYSTEM_ROOT, pathA)
        srcPath = os.path.join(srcPath, element)
        if(os.path.isfile(srcPath)):
            shutil.copy(srcPath, destPath)
        elif(os.path.isdir(srcPath)):
            shutil.copytree(srcPath, os.path.join(destPath, element))
    return home()

@app.route("/move", methods = ["GET", "POST"])
def moveFiles():
    listToCopy = request.form.getlist("listToCopy[]")
    side = request.form['side']
    listToCopy.pop(0)
    for element in listToCopy:
        if(side == 'A'):
            srcPath = os.path.join(FILE_SYSTEM_ROOT, pathA)
            destPath = os.path.join(FILE_SYSTEM_ROOT, pathB)
        elif(side == 'B'):
            srcPath = os.path.join(FILE_SYSTEM_ROOT, pathB)
            destPath = os.path.join(FILE_SYSTEM_ROOT, pathA)
        if(request.form['oldName'] != ''):
            srcPath = os.path.join(srcPath, request.form['oldName'])
            destPath = os.path.join(destPath, element)
        else:
            srcPath = os.path.join(srcPath, element)
        if(os.path.isfile(srcPath)):
            shutil.copy(srcPath, destPath)
            os.remove(srcPath)
        elif(os.path.isdir(srcPath)):
            shutil.copytree(srcPath, os.path.join(destPath, element))
            shutil.rmtree(srcPath)
    return home()

@app.route("/edit", methods = ["GET", "POST"])
def editFileContent():
    side = request.form['side']
    fileName = request.form['fileName']
    if(side == 'A'):
        abspath = os.path.join(FILE_SYSTEM_ROOT, pathA)
    elif(side == 'B'):
        abspath = os.path.join(FILE_SYSTEM_ROOT, pathA)
    abspath = os.path.join(abspath, fileName)
    if(os.path.isfile(abspath)):
        fd = open(abspath, 'r')
        response = fd.read()
        fd.close
    return response
if __name__ == "__main__":
    app.run(debug=True)