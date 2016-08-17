# slack-django-tutorial

A tutorial for getting started with making a Slack bot using Python and Django.

This repository contains code accompanying this [blog post](https://chatbotsmagazine.com/slack-bot-with-a-django-backend-101-tutorial-c1aa8ea3f15e#.2bgd648kz).

To run this code,

1. Clone the repo
2. Run `pip install -r requirements.txt`
3. Update `tutorial.settings.py`


        SLACK_CLIENT_ID = "YOUR CLIENT ID"
        SLACK_CLIENT_SECRET = "YOUR CLIENT SECRET"

4. Run the following commands


        python manage.py makemigrations
        python manage.py migrate

5. Checkout the [blog post](https://chatbotsmagazine.com/slack-bot-with-a-django-backend-101-tutorial-c1aa8ea3f15e#.2bgd648kz) for further details.