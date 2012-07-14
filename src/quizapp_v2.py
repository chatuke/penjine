''' Sample web application using bottle.py'''

from bottle import (Bottle, run, debug, template, request)
import MySQLdb

APP = Bottle()

def _fetch_result(sql, params):
    """ Get questions from the database. """
    conn = MySQLdb.connect('localhost', 'quiz', 'quiz', 'quizengine')
    cursor = conn.cursor()
    cursor.execute(sql, params)
    result = cursor.fetchone()
    return result

@APP.route("/")
def register():
    '''Registration of users'''
    return template('registration.tpl')

@APP.route("/quiz/:question_id", method="POST")
def quiz(question_id):
    """ 
    Play. 
    Ask the fist question. If there was an answer posted, give the user their
    results and ask the next question. Otherwise, repeat asking the same
    question.
    """ 

    name = request.POST.get("name")
    choice = request.POST.get("choice")

    sql = """ SELECT id,question, answer 
        FROM question WHERE id > %s
        ORDER by id ASC LIMIT 1 """
    params = (question_id, )
    result = _fetch_result(sql, params)

    if not result:
        return "Thank you for playing"

    answer = request.POST.get('answer', '').strip().lower()
    if answer:
        if answer == choice.lower():
            message =  "Correct, %s" % name
        else:
            message =  "Wrong, %s" % name

        return template('question.tpl', question=result[1], name=name,
            question_id=result[0], message=message, choice=result[2])
    else:
        message = ""
        return template('question.tpl', question=result[1], name=name,
            question_id=result[0], message=message, choice=result[2])

debug(True)
run(APP, host="localhost", port="8081", reloader=True) 
