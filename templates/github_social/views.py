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
        '''
        activity = Activity.query.filter_by(gh_event_id=event["id"]).first()

        if activity:
            num_likes = activity.num_likes
            comments = [dict(a.items()) for a in activity.comments]
            print(num_likes)
            print(comments)
        print(event)
        '''

    #activities = Activity.query.all()
    #return render_template("../home.html", events=events)
    return jsonify(events)
    #return render_template("index.html", events=events)
