from ast import Str
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import validators
from wtforms.validators import DataRequired, Length, ValidationError

#custom validator, checking if string is in allowed 
class StatusCheck():
    def __init__(self, allowed, message=None):
        self.allowed = allowed
        if not message:
            "Please have some kind of status."
        self.message = message
    
    def __call__(self, form, field):
        if field.data.lower() not in (word.lower() for word in self.allowed):
            raise ValidationError(self.message)

#custom validator can be created, not including special characters in field e.g. applying that to name

class ToDoSubmitForm(FlaskForm):

    name = StringField('Note', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    status = StringField('Status - COMPLETE or NOTCOMPLETE', validators=[DataRequired(),
    StatusCheck(message="Incorrect status. COMPLETE or NOTCOMPLETE.", allowed=['COMPLETE','NOTCOMPLETE'])])
    submit = SubmitField('Submit To-Do')