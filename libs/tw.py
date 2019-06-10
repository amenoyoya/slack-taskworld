# encoding: utf-8
'''
TaskWorld API wrapper
'''
import requests
from .utils import *

class TaskWorld:
    @staticmethod
    def post_api(api, data):
        return requests.post(
            'http://asia-api.taskworld.com/v1/' + api,
            json.dumps(data),
            headers = {
                'Content-Type': 'application/json'
            }
        ).json()

    def __init__(self, email, password):
        auth = TaskWorld.post_api('auth', {
            'email': email, 'password': password
        })
        if not auth['ok']:
            raise ValueError(sprint(auth))
        self.token = auth['access_token']
        self.default_workspace = auth['default_space_id']
        self.workspaces = auth['workspaces']
    
    def exec(self, api, data={}):
        params = {
            'access_token': self.token,
            'space_id': self.default_workspace
        }
        params.update(data)
        return TaskWorld.post_api(api, params)
