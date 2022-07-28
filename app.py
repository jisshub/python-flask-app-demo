from flask import Flask, redirect, url_for, render_template, request

# create flask app instance
app = Flask(__name__)

# define a home page and set a route to this page.
@app.route('/')
def home():
    name = 'jissmon'
    return render_template("index.html")

@app.route('/test')
def test():
    return render_template("new.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['name']
        return redirect(url_for('user', usr=user))
    else:
        return render_template('login.html')

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

# run the app
if __name__ == "__main__":
    app.run(debug=True)

