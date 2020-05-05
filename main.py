from flask import Flask, render_template,request
from werkzeug.utils import html
import os, shutil

app = Flask(__name__)

@app.route('/')
def index()-> html:
    return render_template('index.html')

@app.route('/entry', methods=['POST', 'GET'])
def move_files():
    path = request.form['in']
    path2 = request.form['out']
    global i, full_path
    count = 0
    extension_files = request.form['extension_field']

    # если нет указанного пути, создать !
    if  not os.path.exists(path):
        os.makedirs(path)
    # если нет указанного пути, создать !
    if not os.path.exists(path2):
        os.makedirs(path2)

    for i in sorted(os.listdir(path)):

        if (i.split('.')[-1]).lower() in extension_files:
            shutil.move(path + i, path2 + i)
            full_path = f'{path2}/{i}'

            count += 1

    return render_template('move_files.html',count=count, path=path, path2=path2)



@app.route('/move_files')
def move_files_page():
    return render_template('move_files.html')


if __name__=='__main__':
    app.run(debug=True)