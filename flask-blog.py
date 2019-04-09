from flask import Flask, render_template, url_for, flash,redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '210649bc55b0af1748b87dd502628825'

posts = [
    {
        "author": "Jazmeen Smith",
        "title": "First Post",
        "content": "This is so coool",
        "date_posted": "January 26,2019"
    },

    {
        "author": "Jazmeen Smith",
        "title": "2nd Post",
        "content": "This is so coool",
        "date_posted": "January 26,2019"
    },

    {
        "author": "Obama Smith",
        "title": "Hi Sparkbox!",
        "content": "This is my presentation",
        "date_posted": "March 20,2019"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html",title ="About")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template("register.html",title ="Register", form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html",title ="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)
