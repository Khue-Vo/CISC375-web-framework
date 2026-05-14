from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory task storage
tasks = []
task_id_counter = 1

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
    
    return jsonify(new_task), 201

@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """Mark task as complete or incomplete"""
    data = request.get_json()
    
    for task in tasks:
        if task['id'] == task_id:
            if 'completed' in data:
                task['completed'] = data['completed']
            return jsonify(task), 200
    
    return jsonify({'error': 'Task not found'}), 404

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Delete a task"""
    global tasks
    
    tasks = [task for task in tasks if task['id'] != task_id]
    
    return jsonify({'message': 'Task deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)