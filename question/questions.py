from flask import Blueprint, render_template

from question.forms import CommentForm

comment_bp = Blueprint('comments', __name__, url_prefix='/comment')


@comment_bp.route('/add-comment', methods=['GET', 'POST'])
def add_comment():
    form = CommentForm()
    return render_template('add-comment.html', form=form)
