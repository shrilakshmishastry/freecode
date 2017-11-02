from flask import Flask,render_template,url_for
app=Flask(__name__,template_folder="templates")
@app.route('/', methods=['GET', 'POST'])
def data():
    return render_template('gandhi.html')
