from flask import request, render_template, redirect, url_for, flash, jsonify
from flask_login import login_required
import uuid
from app import app, db
from model.movie import Movie
from util.json_util import make_json_rsp


@app.route('/')
def index():
    movies = Movie.query.all()
    return render_template('index.html', movies=movies)


@app.route('/movie/add', methods=['POST'])
@login_required
def add():
    title = request.form.get('title')
    year = request.form.get('year')
    if not title or not year:
        flash('Invalid input.')
        return redirect(url_for('index'))
    movie = Movie(title=title, year=year)
    db.session.add(movie)
    db.session.commit()
    flash('Item created.')
    return redirect(url_for('index'))

@app.route('/love')
def love():
    return redirect(url_for('static', filename='love/index.html'))


# @app.route('/uploadtoken')
# def upload_token():
#     # 上传的空间
#     bucket_name = "art-vote-storage"
#     # 上传后保存的文件名
#     key = uuid.uuid4().hex
#     # 上传策略
#     policy = {
#     }
#     token = qin.upload_token(bucket_name, key, 3600, policy)
#     return make_json_rsp({ 'token': token, 'key': key })