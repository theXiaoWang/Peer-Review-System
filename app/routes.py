import os
import secrets
from flask import render_template, url_for, flash, redirect, request
from app import app, db, mail
from app.forms import *
from app.models import *
from flask_mail import Mail, Message


# Home Page
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

# About Page
@app.route("/about")
def about():
    return render_template('about.html')

# Start of No.8 Reporting Issues Xiao Wang
# Report Page 
@app.route("/report", methods=['GET', 'POST'])
def report():
    form = ReportForm()
    first_name = form.firstName.data
    last_name = form.lastName.data
    student_number = form.studentNumber.data
    email = form.email.data
    first_name_report = form.firstNameReport.data
    last_name_report = form.lastNameReport.data
    student_number_report = form.studentNumberReport.data
    reason = request.form.get('reason')
    reason_specified = form.reasonSpecified.data

    def send_cofirmation_email():
        confirmation_mail = Message(subject=f'No-Reply: Report Confirmation {student_number}',
        recipients=[email], sender='noreply@demo.com')
        confirmation_mail.body = f"Hi, {first_name} {last_name}. This is a confirmation email regarding your report as following:\n"\
        f"\nName: {first_name_report} {last_name_report}\nStudent Number: {student_number_report}"\
        f"\nReason: {reason}\nMore Reasons / Details Specified:\n{reason_specified}\n"\
        "\nYour lecturer may contact you soon for further discussion. This is an automated email. Please do not reply to it."
        mail.send(confirmation_mail)

    def send_report_email():
        report_mail = Message(subject=f'No-Reply: Report Alert from {student_number}',
        recipients=['WangX227@cardiff.ac.uk'], sender='noreply@demo.com')
        report_mail.body = f"Dear lecturer. This is a report email, please check out details below:\n"\
        f"\nReport Student Info:\nName: {first_name} {last_name}\nStudent Number: {student_number}\n"\
        f"\nStudent Being Reported Info:\nName: {first_name_report} {last_name_report}\nStudent Number: {student_number_report}\n"\
        f"\nReason: {reason}\n\nMore Reasons / Details Specified:\n{reason_specified}\n"\
        "\nThis is an automated email. Please do not reply to it."
        mail.send(report_mail)

    if form.validate_on_submit():
        send_cofirmation_email()
        send_report_email()
        flash('Report submitted successful, you will receive a confirmation email shortly. Your lecturer will contact you soon.', 'success')
        return redirect(url_for('home'))
    return render_template('report.html', form=form)
# End of No.8 Reporting Issues Xiao Wang

# Contribution form by Kestrina Santikai
@app.route("/contribution_form", methods=['GET', 'POST'])
def contribution_form():
    form = ContributionForm()
    first_name = form.firstName.data
    last_name = form.lastName.data
    student_number = form.studentNumber.data
    email = form.email.data
    first_name_report = form.firstNameReport.data
    last_name_report = form.lastNameReport.data
    student_number_report = form.studentNumberReport.data
    reason = request.form.get('reason')
    reason_specified = form.reasonSpecified.data


    def send_form_email():
        contribution_mail = Message(subject=f'No-Reply: Contribtuion Form from {student_number}',
        recipients=['SantikaiK@cardiff.ac.uk'], sender='noreply@demo.com')
        contribution_mail.body = f"Dear lecturer. This is a contribution assessement email, please check out details below:\n"\
        f"\nStudent who filled the Contribution Form:\nName: {first_name} {last_name}\nStudent Number: {student_number}\n"\
        f"\nStudent Being Assessed:\nName: {first_name_report} {last_name_report}\nStudent Number: {student_number_report}\n"\
        f"\nContribution statement: {reason}\n\nAdditional thoughts:\n{reason_specified}\n"\
        "\nThis is an automated email. Please do not reply to it."
        mail.send(contribution_mail)


    if form.validate_on_submit():
        send_form_email()
        flash('Your assessement was submited successfuly', 'success')
        return redirect(url_for('contribution_form'))
    return render_template('contribution_form.html', form=form)