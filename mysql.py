import os
import requests

from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "mysqldb.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)

class Activity(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    num_likes = db.Column(db.Integer, nullable=False)
    comments = db.relationship('Comment', backref='activity', lazy=True)
    gh_event_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return "<num_likes: {}>".format(self.num_likes)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    message = db.Column(db.String(120), nullable=False)
    activity_id = db.Column(db.Integer, db.ForeignKey('activity.id'),
        nullable=False)

@app.route("/", methods=["GET", "POST"])
def index():
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
    return render_template("home.html", events=events)

if __name__ == '__main__':
    app.run(debug=True)
