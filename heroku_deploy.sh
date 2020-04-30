#!/bin/bash

# heroku login
# heroku container:login

heroku container:push worker --app slack-bot-mecab && \
heroku container:release worker --app slack-bot-mecab
