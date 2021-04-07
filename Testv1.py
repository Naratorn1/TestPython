from flask import Flask ,render_template
app = Flask(__name__)

@app.route('/')
def Home():
    return render_template("home.html")
@app.route('/aboutUs')
def Home():
    return render_template("aboutus.html")
@app.route('/John')
def John():
    return "<h1>Hello John!</h1>"
@app.route('/Welcome/<name>')
def Welcome_name(name):
    return 'Welcome ' + name + ' !'
if __name__ == '__main__':
    app.debug = True
    app.run(host='10.100.4.91')
