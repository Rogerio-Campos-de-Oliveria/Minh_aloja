from wtforms import Form, BooleanField, StringField, PasswordField, validators


class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    usuario = StringField('Usuario', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('Confirmar sua senha',
                           message='Sua senhas não são iguais')
    ])
    confirm = PasswordField('Digite sua senha novamente')
  
