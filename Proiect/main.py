from flask import Flask, render_template, request, redirect
from pathlib import Path
import os
import time

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
        item.append(os.path.getsize( os.path.join(os.path.join(FILE_SYSTEM_ROOT, pathA), item[0]) ))
    for item in itemListA:
        item.append(time.ctime(os.path.getctime( os.path.join(os.path.join(FILE_SYSTEM_ROOT, pathA), item[0]) ))  )
    for item in itemListB:
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
if __name__ == "__main__":
    app.run(debug=True)