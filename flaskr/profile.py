from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from flaskr.blog import get_post
from flaskr.auth import login_required
from hashlib import md5

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
