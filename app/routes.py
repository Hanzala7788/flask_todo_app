from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Todo

main = Blueprint('main', __name__)

@main.route('/')
def index():
    incomplete = Todo.query.filter_by(complete=False).all()
    complete = Todo.query.filter_by(complete=True).all()
    return render_template('index.html', incomplete=incomplete, complete=complete)

@main.route('/add', methods=['POST'])
def add():
    todo = Todo(text=request.form['todoitem'], complete=False)
    db.session.add(todo)
    db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/complete/<int:todo_id>')
def complete(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    todo.complete = True
    db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/remove/<int:todo_id>')
def remove(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('main.index'))
