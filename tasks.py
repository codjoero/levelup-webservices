from flask import request, jsonify, abort

class Tasks:

    def __init__(self):
        self.user_tasks = [
            {
            'id': 1,
            'title': 'Gym',
            'items': 'shoes, towel, yoga mat, getorade',
            'finished': False
            }
        ]
        self.deleted_tasks = []

    def show_all(self):
        return self.user_tasks

    def create_task(self):
        if not request.json or not 'title' in request.json:
            abort(400)
        task = {
            'id': self.user_tasks[-1]['id'] + 1,
            'title': request.json['title'],
            'items': request.json.get('items', ""),
            'finished': False
        }
        self.user_tasks.append(task)
        return task

    def mark_finished(self, task_id):
        task = [task for task in self.user_tasks 
        if task['id'] == task_id]

        if len(task) == 0:
            abort(404)
        if not request.json:
            abort(400)
        if 'finished' in request.json and \
        type(request.json['finished']) is not bool:
            abort(400)
        task[0]['finished'] = request.json.get('finished',
                                task[0]['finished'])
        return task
    

    def delete_task(self,task_id):
        task = [task for task in self.user_tasks 
        if task['id'] == task_id]

        if len(task) == 0:
            abort(404)
        self.deleted_tasks.append(task[0])
        self.user_tasks.remove(task[0])
        return 'Deleted'


    def undelete_task(self, task_id):
        task = [task for task in self.deleted_tasks 
        if task['id'] == task_id]

        if len(task) == 0:
            abort(404)
        self.user_tasks.append(task[0])
        self.deleted_tasks.remove(task[0])
        return 'Recovered'

    def delete_all(self):
        self.user_tasks[:] = []
        return 'All Deleted'

    

    