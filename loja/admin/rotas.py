from flask import render_template, redirect, url_for, flash, request

from loja import app, db

from .formulario import RegistrationForm


@app.route('/')
def home():
    return "seja bem vindo ao sistema em flask"


@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        # user = User(form.username.data, form.email.data,
        # form.password.data)
        # db_session.add(user)
        flash('Obrigado por Registrar')
        return redirect(url_for('login'))
    return render_template('admin/registrar.html', form=form, title="Pagina de Registro")
