from application import app, db
from application.models import Todo
from flask import render_template, url_for, request
from datetime import date, timedelta
from application.forms import ToDoSubmitForm

#routes
# <p>Add to-do - /home/add."NOTETEXT"</p>
# <p>View to-do's - /home/view</p>
# <p>Update to-do - /home/update."ID"."NOTETEXT"</p>
# <p>Delete to-do - /home/delete."ID"</p>
# <p>Search for item - /home/search."TEXT"</p>
# <p>Show statistics - /home/statistics</p>

accepted = ["complete", "notcomplete"]

@app.route('/home')
def home():
    return render_template('homepage.html')

@app.route('/home/add', methods=['GET', 'POST'])
def addnoteform():
    form = ToDoSubmitForm()
    msg = ''

    if request.method == 'POST':
        name = form.name.data
        description = form.description.data
        status = form.status.data

        if form.validate_on_submit():
            msg = f"Note: {name}. Submitting to database."
            duedate = date.today() + timedelta(days=14)
            new_note = Todo(name=name, description=description, duedate=duedate, status=status)
            db.session.add(new_note)
            db.session.commit()
            #IMPLEMENTED adding to DB functionality
        else:
            msg = "Incorrect validation."
            
    return render_template('addtodo.html', form=form, message=msg)

@app.route('/home/add.<name>.<description>.<status>')
def addnote(name, description, status):
    duedate = date.today() + timedelta(days=14)
    new_note = Todo(name=name, description=description, duedate=duedate, status=status)
    if status not in accepted:
        return "Error. Status must be complete or notcomplete."
    db.session.add(new_note)
    db.session.commit()
    return "Note added to database."

@app.route('/home/view')
def todoview():
    currentdb = Todo.query.all()
    notes = ''
    notelist = []
    for i in currentdb:
        notes = notes + " " + str(i.noteid) + " " + i.name + " " + i.description + " " + str(i.duedate) + " " + i.status
        notelist.append(notes)
    return render_template('viewtodo.html', notelist=notelist)

@app.route('/home/update.<int:id>.<notetext>')
def updatenote(id, notetext):
    currentnote = Todo.query.get(id)
    currentnote.description = notetext
    db.session.commit()
    return "Note " + str(id) + " updated."

@app.route('/home/delete.<int:id>')
def deletenote(id):
    currentnote = Todo.query.get(id)
    db.session.delete(currentnote)
    db.session.commit()
    return "Note " + str(id) + " deleted."

#search

@app.route('/home/search.<name>')
def searchdb(name):
    msg = []
    currenti = ''
    currentdb = Todo.query.all()
    for i in currentdb:
        currenti = str(i.noteid) + " " + i.name + " " + i.description + " " + str(i.duedate) + " " + i.status
        msg.append(currenti)
    return "<br>".join(msg)


#statistics /home/statistics
@app.route('/home/statistics')
def returnstatics():
    currentdbcount = Todo.query.count()
    return "Current count: " + str(currentdbcount)