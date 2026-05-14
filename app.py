from flask import Flask, render_template, request, jsonify
from datetime import datetime
import json
import os

app = Flask(__name__)

# Load tasks from JSON file
TASKS_FILE = 'tasks.json'

def load_tasks():
    """Load tasks from JSON file"""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks():
    """Save tasks to JSON file"""
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

def get_next_id():
    """Get the next task ID"""
    if not tasks:
        return 1
    return max(task['id'] for task in tasks) + 1

# Load tasks from file at startup
tasks = load_tasks()
task_id_counter = get_next_id()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    """Return all tasks"""
    return jsonify(tasks)

@app.route('/api/tasks', methods=['POST'])
def add_task():
    """Add a new task"""
    global task_id_counter
    data = request.get_json()
    
    if not data or 'title' not in data:
        return jsonify({'error': 'Task title required'}), 400
    
    new_task = {
        'id': task_id_counter,
        'title': data['title'],
        'completed': False,
        'created_at': datetime.now().isoformat()
    }
    tasks.append(new_task)
    task_id_counter += 1
    save_tasks()
    
    return jsonify(new_task), 201

@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """Mark task as complete or incomplete"""
    data = request.get_json()
    
    for task in tasks:
        if task['id'] == task_id:
            if 'completed' in data:
                task['completed'] = data['completed']
            save_tasks()
            return jsonify(task), 200
    
    return jsonify({'error': 'Task not found'}), 404

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Delete a task"""
    global tasks
    
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks()
    
    return jsonify({'message': 'Task deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)