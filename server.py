#!/usr/local/bin/python3
# encoding: utf-8
from libs.utils import *
from libs.frasco import Frasco, Response, request
from libs.tw import TaskWorld
import shlex

app = Frasco(__name__)

# index.html
@app.get('/')
def index():
    return Response.template('index.html')

# Slack slash bot /tw
def taskworld_api(args):
    cmd = geta(args, 0)
    arg = geta(args, 1)

    # TaskWorld Authenication
    try:
        with open('config.json') as f:
            config = json.load(f)
        api = TaskWorld(config['taskworld']['email'], config['taskworld']['password'])
    except ValueError as e:
        return {'text': e}
    
    # プロジェクト列挙（default: 10個）
    if cmd == 'projects':
        return {
            'text': sprint(
                api.exec('project.get-all', {
                    'limit': arg if type(arg) is int else 10
                })['projects']
            )
        }
    # プロジェクト探索
    elif cmd == 'project' and type(arg) is str:
        for project in api.exec('project.get-all')['projects']:
            if project['title'] == arg:
                return {'text': sprint(project)}
        return {'text': 'no project named "' + arg + '"'}
    
    # 一致コマンドなし
    return {'text': sprint(request.form)}
    

@app.post('/tw')
def tw():
    return Response.json(
        taskworld_api(shlex.split(request.form['text']))
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='3030', debug=True)
