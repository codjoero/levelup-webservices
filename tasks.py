from flask import request, jsonify

class Tasks:

    def __init__(self):
        self.user_tasks = []
        self.deleted_tasks = []

    def create_task(self):
        pass

    def delete_task(self):
        pass

    def delete_all(self):
        pass

    def mark_finished(self):
        pass

    def recover_deleted(self):
        pass

    def show_all(self):
        return self.user_tasks