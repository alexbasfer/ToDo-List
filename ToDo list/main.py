from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)

def save_tasks():
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f)

def load_tasks():
    with open('tasks.json', 'r') as f:
        return json.load(f)

tasks = load_tasks()

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = {'name': request.form['task'], 'completed': False}
    tasks.append(task)
    save_tasks()
    return redirect('/')

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    tasks.pop(task_id)
    save_tasks()
    return redirect('/')

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    tasks[task_id]['completed'] = True
    save_tasks()
    return redirect('/')

@app.route('/edit/<int:task_id>', methods=['POST'])
def edit_task(task_id):
    tasks[task_id]['name'] = request.form['task']
    save_tasks()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
