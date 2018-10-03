from flask import Flask, jsonify
from tasks import Tasks
from accounts import Accounts

app = Flask(__name__)

account = Accounts()
task = Tasks()

@app.route('/todo/api/v0.1/tasks', methods=['POST'])
def create_user():
    return jsonify({'tasks': task.show_all})

@app.route('/todo/api/v0.1/tasks', methods=['PUT'])
def login_user():
    pass

@app.route('/todo/api/v0.1/tasks/<int:task_id>', methods=['PUT'])
def logout_user():
    pass

@app.route('/todo/api/v0.1/tasks', methods=['DELETE'])
def delete_user():
    pass

@app.route('/todo/api/v0.1/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': task.show_all})

@app.route('/todo/api/v0.1/tasks', methods=['POST'])
def create_task():
    pass

@app.route('/todo/api/v0.1/tasks/<int:task_id>', methods=['DELETE'])
def delete_task():
    pass

@app.route('/todo/api/v0.1/tasks', methods=['PUT'])
def delete_all():
    pass

@app.route('/todo/api/v0.1/tasks/<int:task_id>', methods=['PUT'])
def mark_finished():
    pass

@app.route('/todo/api/v0.1/tasks/<int:task_id>', methods=['PUT'])
def unmark_finished():
    pass

@app.route('/todo/api/v0.1/tasks/<int:task_id>', methods=['PUT'])
def undeleted_task():
    pass

if __name__ == '__main__':
    app.run(debug=True)