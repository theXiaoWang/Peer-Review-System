from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, ValidationError,Regexp  


# Start of No.8 Reporting Issues Xiao Wang
# Report Form
class ReportForm(FlaskForm):
    firstName = StringField('First Name',
    validators=[DataRequired(), Length(min=2, max=20),
    Regexp('^[A-za-z]*$', message='First name should only be letters.')])

    lastName = StringField('Last Name',
    validators=[DataRequired(), Length(min=2, max=20),
    Regexp('^[A-za-z]*$', message='Last name should only be letters.')])

    studentNumber = StringField('Student Number',
    validators=[DataRequired(), Length(min=8, max=8),
    Regexp('^[A-za-z0-9]*$', message='Student number should only be letters and numbers.')])

    email = StringField('Email',
    validators=[DataRequired(), Email()])

    reasonSpecified = TextAreaField('More Reasons / Details Specified', 
    validators=[DataRequired(), Length(min=2, max=800)])

    firstNameReport = StringField('First Name',
    validators=[DataRequired(), Length(min=2, max=20),
    Regexp('^[A-za-z]*$', message='First name should only be letters.')])

    lastNameReport = StringField('Last Name',
    validators=[DataRequired(), Length(min=2, max=20),
    Regexp('^[A-za-z]*$', message='Last name should only be letters.')])

    studentNumberReport = StringField('Student Number',
    validators=[DataRequired(), Length(min=8, max=8),
    Regexp('^[A-za-z0-9]*$', message='Student number should only be letters and numbers.')])

    submit = SubmitField('Submit')
# End of No.8 Reporting Issues Xiao Wang

# Contribution Form by Kestrina Santikai
class ContributionForm(FlaskForm):
    firstName = StringField('First Name',
    validators=[DataRequired(), Length(min=2, max=20),
    Regexp('^[A-za-z]*$', message='First name should only be letters.')])

    lastName = StringField('Last Name',
    validators=[DataRequired(), Length(min=2, max=20),
    Regexp('^[A-za-z]*$', message='Last name should only be letters.')])

    studentNumber = StringField('Student Number',
    validators=[DataRequired(), Length(min=8, max=8),
    Regexp('^[A-za-z0-9]*$', message='Student number should only be letters and numbers.')])

    email = StringField('Email',
    validators=[DataRequired(), Email()])

    reasonSpecified = TextAreaField('You can add more explanation below', 
    validators=[DataRequired(), Length(min=2, max=800)])

    firstNameReport = StringField('First Name',
    validators=[DataRequired(), Length(min=2, max=20),
    Regexp('^[A-za-z]*$', message='First name should only be letters.')])

    lastNameReport = StringField('Last Name',
    validators=[DataRequired(), Length(min=2, max=20),
    Regexp('^[A-za-z]*$', message='Last name should only be letters.')])

    studentNumberReport = StringField('Student Number',
    validators=[DataRequired(), Length(min=8, max=8),
    Regexp('^[A-za-z0-9]*$', message='Student number should only be letters and numbers.')])

    submit = SubmitField('Submit')
