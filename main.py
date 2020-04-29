from flask import Flask, render_template
from werkzeug.utils import html

app = Flask(__name__)


@app.route('/')
def index()-> html:
    name = 'Mike'
    return render_template('index.html', n=name)




if __name__=='__main__':
    app.run(debug=True)