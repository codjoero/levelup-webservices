from flask import request, jsonify, abort

class Accounts:

    accounts = []

    def create_user(self):
        if not request.json or not 'username' in request.json:
            abort(400)
        user = {
            'username': request.json['username'],
            'password': request.json['password'],
            'active': False
        }
        self.accounts.append(user)
        return user

    def credential_check(self):
        user = [user for user in self.accounts 
                if user['username'] == request.json['username'] and 
                user['password'] == request.json['password']]
        if len(user) == 0:
            abort(401)
        user[0]['active'] = True
        return user

    def login_user(self):
        user = self.credential_check()
        if user[0]['active'] == True:
            return 'Logged in'


    def logout_user(self, user_name):
        user = [user for user in self.accounts 
                if user['username'] == user_name]
        if user[0]['active'] == False:
            abort(400)
        user[0]['active'] == False
        return 'Logged out'
        

    def delete_user(self):
        user = self.credential_check()
        if user[0]['active'] == True:
            self.accounts.remove(user[0])
            return 'User deleted'
