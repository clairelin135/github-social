import requests

from templates import app
from flask import render_template, request

#from templates.__init__ import Activity
from templates import Activity
from templates import db

@app.route('/')
@app.route('/hello')
def index():
    return render_template("index.html")
    #return "hello"

@app.route("/lel", methods=["GET", "POST"])
def lel():
    if request.form: # POST REQUEST
        print(request.form)
        activity = Activity(num_likes=request.form.get("num_likes"))
        db.session.add(activity)
        db.session.commit()

    url = 'https://api.github.com/users/clairelin135/events'
    headers = {"Content-Type" : "application/vnd.github.v3+json"}

    events = requests.get(url, headers=headers).json()
    for event in events:
        activity = Activity.query.filter_by(gh_event_id=event["id"]).first()

        if activity:
            num_likes = activity.num_likes
            comments = [dict(a.items()) for a in activity.comments]
            print(num_likes)
            print(comments)
        print(event)

    #activities = Activity.query.all()
    #return render_template("../home.html", events=events)
    return str(events)
