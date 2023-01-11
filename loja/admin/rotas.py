from flask import render_template, session, request, url_for, flash, redirect

from loja import app, db, bcrypt
from .formulario import RegistrationForm
from .models import User
import os


@app.route("/")
def homepage():
    return "homepage"


@app.route('/registar', methods=['GET', 'POST'])

def registar():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(username =form.username.data, usuario=form.usuario.data, email=form.email.data,
        password=hash_password)
        db.session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('homepage'))
    return render_template('admin/registar.html', form=form, title="Pagina de Registos")

#db.create_all()