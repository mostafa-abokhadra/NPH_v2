from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class Registration(FlaskForm):
    username = StringField(
        'username', validators=[DataRequired(),
        Length(min=4, max=20)], render_kw={'placeholder':'username'})
    email = StringField(
        'email', validators=[DataRequired(), Email()],
        render_kw={'placeholder': 'email'})
    password = PasswordField(
        'password', validators=[DataRequired()],
        render_kw={'placeholder':'password'})
    confirm_password = PasswordField(
        'confirm_password', validators=[DataRequired(),
        EqualTo('password')], render_kw={'placeholder': 'confirm password'})
    types = [('N', 'Nurse'), ('P', 'Patient'), ('E', 'Employer')]
    userType = RadioField('userType', validators=[DataRequired()], choices=types)
    submit = SubmitField('SignUp')

    
class Login(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email()], render_kw={'placeholder': 'email'})
    password = PasswordField('password', validators=[DataRequired()], render_kw={'placeholder': 'password'})
    remember = BooleanField('Remember_me')
    submit = SubmitField('Login')