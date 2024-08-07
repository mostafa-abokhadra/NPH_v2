from NursePatientHub import bcrypt
from flask_wtf import FlaskForm
from NursePatientHub.models import User
from wtforms import StringField, PasswordField, SubmitField, BooleanField, RadioField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class Registration(FlaskForm):
    username = StringField(
        'username', validators=[DataRequired(),
        Length(min=4, max=20)], render_kw={'placeholder':'username'})
    email = StringField(
        'email', validators=[DataRequired(), Email()],
        render_kw={'placeholder': 'email'})
    password = PasswordField(
        'password', validators=[DataRequired(), Length(min=8, max=20)],
        render_kw={'placeholder':'password'})
    confirm_password = PasswordField(
        'confirm_password', validators=[DataRequired(),
        EqualTo('password')], render_kw={'placeholder': 'confirm password'})
    types = [('N', 'Nurse'), ('P', 'Patient'), ('E', 'Employer')]
    userType = RadioField('userType', validators=[DataRequired()], choices=types)
    submit = SubmitField('SignUp')

    def validata_email(self, email):
        user = User.query.filter(User.email == email.data).first()
        if user:
            return 1
    
class Login(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email()], render_kw={'placeholder': 'email'})
    password = PasswordField('password', validators=[DataRequired()], render_kw={'placeholder': 'password'})
    remember = BooleanField('Remember_me')
    submit = SubmitField('Login')
