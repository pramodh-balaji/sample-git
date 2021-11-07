from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def g():
    return render_template('int.html')

app.run(debug=True)
