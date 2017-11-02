# pythonspot.com
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import database
import sqlite3
from database import createdb
# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
 
class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    email = TextField('Email:', validators=[validators.required(), validators.Length(min=6, max=35)])
    password = TextField('Password:', validators=[validators.required(), validators.Length(min=3, max=35)])
 
 
@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)
 
    print(form.errors)
    if request.method == 'POST':
        name=request.form['name']
        password=request.form['password']
        email=request.form['email']
        print(name, " ", email, " ", password)
        db = database
        conn = sqlite3.connect("database.db")
        print("Opened database successfully!!")
        #
        # conn.execute('Create Table If not EXISTS users (id INTEGER  PRIMARY Key Autoincrement , name Text NOT NULL ,email text NOT NULL ,password Text NOT NULL )')
        conn.execute("Insert into users(name, email, password) VALUES (?, ?, ?)", [name, email, password])
        for r in conn.execute('SELECT * from users'):
            print(r)
        conn.commit()

        conn.close()

        if form.validate():
            # Save the comment here.
            flash('Thanks for registration ' + name)
        else:
            flash('Error: All the form fields are required. ')
 
    return render_template('hello.html', form=form)
 
if __name__ == "__main__":
    app.run(debug= True)
