from flask_wtf import FlaskForm 
from wtforms import StringField , validators, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class MyForm(FlaskForm): 
    name = StringField('name', validators =[DataRequired()]) 
    email = StringField ('email', validators=[ DataRequired()]) 
    subject=StringField('subject', validators=[DataRequired()]) 
    message=TextAreaField('message', validators=[DataRequired()]) 
    submit = SubmitField('Send') 
    