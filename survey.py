#coding: utf8
# 
# Serves a page that laets a client answer the initial survey 
# 

from flask import Blueprint, session, render_template, request, redirect, url_for

survey = Blueprint('survey', __name__, template_folder='templates')

@survey.route('/survey_q0', methods=["POST", "GET"])
def survey_q0():
    # Collect responses on personal information
    if request.method=="POST":
        # TODO: if needed, put in database here. 
        #   Otherwise, wait to add all data at the end, and save all this in the session (Probably the latter)
        first_name = request.form['firstname']
        last_name = request.form['lastname']
        email = request.form['email']
        dob = request.form['dob']
        institution = request.form['institution']
        grad_year = request.form['graddate']
        majors = request.form['majors']

        # Add key (currently just email) to the session
        session['email'] = email
        return redirect(url_for('survey.survey_q1'))

    # Render demographic/personal information question
    return render_template('survey_q0.html')

@survey.route('/survey_q1', methods=["POST", "GET"])
def survey_q1():
    # The survey categories which are currently hardcoded, but ought to be replaced by the actual categories
    professional_categories = ['Test 1', 'Test 2', 'Test 3']
    personal_categories = ['Another Test 1','Another Test 2','Another Test 3']

    # Process submission and send user to next page
    if request.method=="POST":
        # Fetch the categories which the user selected and put them in a list
        categories = list()
        for key in request.form.keys():
            print(key)
            print(request.form[key])
            if request.form[key]:
                categories.append(key)
        # Save all categories selected
        session['categories'] = categories

        # Send the user to the next question
        return redirect(url_for('survey.survey_q2'))

    # Render question 1
    return render_template('survey_q1.html', professional = professional_categories, personal = personal_categories)

@survey.route('/survey_q2', methods=["POST", "GET"])
def survey_q2():
    if request.method=="POST":
        categories = list()
        # Fetch the categories which were selected and put them in a list
        for value in request.form.values():
            categories.append(value)

        # Save top categories selected
        session['top_categories'] = categories

        # Send the user to the next question
        return redirect(url_for('survey.survey_q3'))

    # Render question 2
    return render_template('survey_q2.html', selected_categories=session['categories'])    

@survey.route('/survey_q3', methods=["POST", "GET"])
def survey_q3():
    if request.method == "POST":
        # Fetch the categories which the user selected and put them in a list
        categories = list()
        for key in request.form.keys():
            if request.form[key]:
                categories.append(key)

        # Save categories for which they don't know everything they need
        session['question_categories'] = categories

        # Send the user to the next question
        return redirect(url_for('survey.survey_q4'))

    # Render question 3
    return render_template('survey_q3.html', top_categories=session['top_categories'])

@survey.route('/survey_q4', methods=["POST", "GET"])
def survey_q4():
    if request.method=="POST":
        q_and_a = dict()
        # Fetch the question/answer pair for the response
        for key,value in request.form.items():
            print(key)
            print(value)
            q_and_a[key] = value
        # TODO: pass all relevant information from the session off to the database
        session['q_and_a'] = q_and_a

        # Send the user to the "thank you" page
        return render_template("survey_end.html")

    # Render question 4
    return render_template("survey_q4.html", question_categories=session['question_categories'])









