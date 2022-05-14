from wsgiref.validate import validator
from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, IntegerField
from wtforms.validators import DataRequired, Length, Email, NumberRange
from wiki import findBirths


class loginForm(FlaskForm):
    email = StringField(label="Enter email", validators=[DataRequired(), Email()])
    password = PasswordField(
        label="Enter password", validators=[DataRequired(), Length(min=6, max=16)]
    )
    submit = SubmitField(label="Login")

class birthdayForm(FlaskForm):
    date = DateField(label="Enter birthday", validators=[DataRequired()])
    number_of_entries = IntegerField(label="Number of results", validators=[NumberRange(min=1,max=20)])
    submit = SubmitField(label="Search")


passwords = {}
passwords["lhhung@uw.edu"] = "qwerty"

app = Flask(__name__)
app.secret_key = "a secret"


@app.route("/home")
def birthday():
    form = birthdayForm()
    date = request.args.get('date')
    number_of_entries = request.args.get('number_of_entries') or 10
    results = []
    if date:
        dateparts = date.split('-')
        daymonth=f"{dateparts[1]}/{dateparts[2]}"
        year = dateparts[0]
        results = findBirths(daymonth, year, number_of_entries)
    return render_template('birthday.html', form=form, results = results)
    


#@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():
    form = loginForm()
    if form.validate_on_submit():
        if request.method == "POST":
            user = request.form["email"]
            pw = request.form["password"]
            if user is not None and user in passwords and passwords[user] == pw:
                return redirect("/home")
    return render_template("login.html", form=form)

if __name__ == "__main__":
    #app.run(host="0.0.0.0", debug=True)
    app.run(debug=True)
