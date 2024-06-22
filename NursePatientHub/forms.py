from flask_wth import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class Registration(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    confirm_password = password('confirm_password', validators=[DataRequired, EqualTo('password')])
    types = [('nurse', 'Nurse'), ('patient', 'Patient'), ('employer', 'Employer')]
    userType = RadioField('userType', validators=[DataRequired()], choices=types)
    submit = SubmitField('SignUp')

    
class Login(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    remember = BooleanField('Remember_me')
    submit = SubmitField('SignUp')