import os
import requests

from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "mysqldb.db"))

app = Flask(__name__, static_folder = './public', template_folder="./static")
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

import templates.github_social.views
