from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='templates')

tasks = [
    {"name": "Learn Flask", "description": "Complete the Flask tutorial", "completed": False},
    {"name": "Build a Web App", "description": "Create a simple web application using Flask", "completed": False}
]

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form['name']
    description = request.form['description']
    tasks.append({"name": task, "description": description, "completed": False})
    return redirect(url_for('index'))

@app.route('/update/<int:index>', methods=['GET', 'POST'])
def update(index):
    task = tasks[index]
    if request.method == 'POST':
        task['name'] = request.form['name']
        task['description'] = request.form['description']
        task['completed'] = 'completed' in request.form
        return redirect(url_for('index'))
    else:
        return render_template('update.html', task=task, index=index)

@app.route('/check/<int:index>')
def check(index):
    tasks[index]['completed'] = not tasks[index]['completed']
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete(index):
    tasks.pop(index)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)