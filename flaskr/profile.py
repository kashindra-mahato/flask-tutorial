from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from flaskr.blog import get_post
from flaskr.auth import login_required
from hashlib import md5
from flaskr.db import get_db

bp = Blueprint('profile', __name__)

class Avatar():
    def avatar(self, size):
        digest = md5(g.user['email'].lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)

@bp.route('/user')
@login_required
def user():
    avatar = Avatar()
    return render_template('blog/user.html', avatar=avatar)


@bp.route('/<int:id>/update_user', methods=('GET', 'POST'))
@login_required
def update_user(id):
    if request.method == "POST":
        username =  request.form['username']
        error = None

        if not username:
            error = "Username is required."
        
        if error is not None:
            flash(error)

        else:
            db = get_db()
            db.execute(
                'UPDATE user SET username = ?'
                ' WHERE id = ?',
                (username, id)
            )
            db.commit()
            return redirect(url_for('profile.user'))

    return render_template('blog/edit_user.html')
