from flask import Blueprint, render_template, redirect, url_for, request, send_file
from flask_login import login_required, current_user
from ..models import Comment, Showroom, Vehicle
from .. import db
import csv
import io

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('/home')
@login_required
def user_home():
    # Display summary, recent comments, etc.
    comments = Comment.query.limit(10).all()
    return render_template('user_home.html', comments=comments)

@user_bp.route('/comments')
@login_required
def comments():
    comments = Comment.query.all()
    return render_template('comments.html', comments=comments)

@user_bp.route('/graphs')
@login_required
def graphs():
    # Sentiment counts
    positive = Comment.query.filter_by(sentiment='positive').count()
    neutral = Comment.query.filter_by(sentiment='neutral').count()
    negative = Comment.query.filter_by(sentiment='negative').count()
    return render_template('graphs.html', positive=positive, neutral=neutral, negative=negative)

@user_bp.route('/download')
@login_required
def download():
    # Create CSV with comments and sentiment
    si = io.StringIO()
    cw = csv.writer(si)
    cw.writerow(['Source', 'Comment', 'Sentiment'])
    comments = Comment.query.all()
    for c in comments:
        cw.writerow([c.source, c.text, c.sentiment])
    output = io.BytesIO()
    output.write(si.getvalue().encode('utf-8'))
    output.seek(0)
    return send_file(output, mimetype='text/csv', as_attachment=True, attachment_filename='comments.csv')

@user_bp.route('/showrooms')
@login_required
def showrooms():
    showrooms = Showroom.query.all()
    return render_template('showrooms.html', showrooms=showrooms)

@user_bp.route('/compare')
@login_required
def compare():
    vehicles = Vehicle.query.all()
    return render_template('compare.html', vehicles=vehicles)
