import requests

from templates import app
from flask import render_template, request, jsonify

from templates import Activity, db

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/user/<id>')
def user(id):
    return render_template("home.html")

@app.route('/api/user/<username>')
def api_user(username):
    url = 'https://api.github.com/users/%s' % username
    headers = {"Content-Type" : "application/vnd.github.v3+json"}

    return requests.get(url, headers=headers).json()

@app.route('/api/events/<username>', methods=["GET", "POST"])
def api_events(username):
    if request.form: # POST REQUEST
        print(request.form)
        activity = Activity(num_likes=request.form.get("num_likes"))
        db.session.add(activity)
        db.session.commit()

    url = 'https://api.github.com/users/%s/events' % username
    headers = {"Content-Type" : "application/vnd.github.v3+json"}

    events = requests.get(url, headers=headers).json()
    for event in events:
        activity = Activity.query.filter_by(gh_event_id=event["id"]).first()

        if activity:
            num_likes = activity.num_likes
            comments = [dict(a.items()) for a in activity.comments]
            event["num_likes"] = num_likes
        else:
            event["num_likes"] = 0

    return jsonify(events)

@app.route('/api/like/<id>', methods=["GET", "PUT"])
def api_like(id):
    payload = request.json
    activity = Activity.query.filter_by(gh_event_id=id).first()
    if activity:
        activity.num_likes = payload["num_likes"]
        db.session.commit()
    else:
        activity = Activity(num_likes=payload["num_likes"], gh_event_id=id)
        db.session.add(activity)
        db.session.commit()
    return payload