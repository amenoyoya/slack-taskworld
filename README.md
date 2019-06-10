# Slack Bot｜TaskWorld連携

## What's this?

[TaskWorld](https://taskworld.com)と連携して、Slack上でタスク管理のできるBot

## Environment

- Hardware: `Synology DS218`
- Python: `3.5.1`
    - pip (package-manager): `19.1.1`
    - flask (web-app-framework): `1.0.3`
    - requests: `2.22.0`
    - sqlalchemy: `1.3.4`
- ngrok (proxy-server): `2.2.8`
- tmux (tuple-terminal-emulator): `2.3`

***

## Usage

### 準備｜config.json

TaskWorldログイン情報を記述した以下のような`config.json`を用意する

```javascript
{
    "taskworld": {
        "email": "TaskWorld登録アドレス@mail.address",
        "password": "TaskWorldログインパスワード"
    }
}
```

---

### Python｜Flaskサーバー起動

```bash
$ ssh root@xxxx.synology.me
---
# tmuxで新規セッション`flask`開始
$ tmux new -s flask

# WORK_DIRに移動
$ cd /volume1/public/www/slack-taskworld/

# Flaskサーバーをdevelopmentで起動
$ sudo export FLASK_ENV=environment # default: production
$ sudo python3 server.py
## => localhost:3030 でサーバー実行

# Ctrl + B => D でセッションをデタッチ
## バックグラウンドで実行継続される
## アタッチするときは tmux a -t flask
```

---

### ngrok｜Flaskサーバーを外部公開

```bash
# tmuxで新規セッション`ngrok`開始
$ tmux new -s ngrok

# WORK_DIRに移動
$ cd /volume1/public/www/

# ngrokで localhost:3030 を外部公開
$ ./ngrok http 3030
## => 外部公開用URLが発行される

# Ctrl + B => D でセッションをデタッチ
## バックグラウンドで実行継続される
## アタッチするときは tmux a -t ngrok
```

***

## TODO

uwsgi + nginx を使って、本番サーバーとして運用できるようにしたい

`/etc/nginx/nginx.conf`あたりの設定を調査？
