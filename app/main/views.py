from flask import render_template, request, redirect, url_for, abort
from flask_login import login_required, current_user
from . import main
from .forms import PostForm, CommentForm
from ..models import Post, Comment, Star, Vote
from .. import db
import markdown2


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to Codit'
    posts = Post.query.order_by(Post.posted_p.desc()).all()
    return render_template('index.html', title = title, posts = posts)

@main.route('/about')
def about():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'About - Welcome to Codit'
    return render_template('about.html', title = title)

@main.route('/posts/<language>')
def posts(language):
    '''
    View root page function that returns the index page and its data
    '''
    posts = Post.query.filter_by(language=language).order_by(Post.posted_p.desc()).all()
    return render_template('posts.html', posts=posts,language=language)

@main.route('/post/<int:id>')
def post(id):

    '''
    View a post page function that returns the post details page and its data
    '''
    posts = Post.query.filter_by(id=id)
    comments = Comment.query.filter_by(post_id=id).all()

    return render_template('post.html',posts = posts,comments = comments)

@main.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        language = form.language.data

        new_post = Post(title=title, description=description, language=language, user_p=current_user._get_current_object().id)
        new_post.save_post()
        
        posts = Post.query.order_by(Post.posted_p.desc()).all()
        return render_template('posts.html', posts=posts)

    title = 'New Post'
    return render_template('new_post.html', title=title, post_form=form)

@main.route('/comment/new/<int:post_id>', methods = ['GET','POST'])
@login_required
def new_comment(post_id):
    form = CommentForm()
    post = Post.query.get(post_id)

    if form.validate_on_submit():
        comment = form.comment.data
         
        # Updated comment instance
        new_comment = Comment(comment=comment,user_c=current_user._get_current_object().id, post_id=post_id)

        # save comment method
        new_comment.save_comment()
        return redirect(url_for('.new_comment',post_id = post_id ))

    all_comments = Comment.query.filter_by(post_id=post_id).all()
    return render_template('comment.html', form=form, comments=all_comments, post=post)

@main.route('/post/star/<int:post_id>/star', methods=['GET', 'POST'])
@login_required
def star(post_id):
    post = Post.query.get(post_id)
    user = current_user
    post_stars = Star.query.filter_by(post_id=post_id)
    posts = Post.query.order_by(Post.posted_p.desc()).all()

    if Star.query.filter(Star.user_id == user.id, Star.post_id == post_id).first():
        return render_template('posts.html', posts=posts)

    new_star = Star(post_id=post_id, user=current_user)
    new_star.save_stars()
    
    return render_template('posts.html', posts=posts)
    return render_template('index.html', title=title)


@main.route('/comment/vote/<int:comment_id>/vote', methods=['GET', 'POST'])
@login_required
def vote(comment_id):
    comment = Comment.query.get(comment_id)
    user = current_user
    comment_votes = Vote.query.filter_by(comment_id=comment_id)
    comments = Comment.query.order_by(Comment.posted_p.desc()).all()

    if Vote.query.filter(Vote.user_id == user.id, Vote.comment_id == comment_id).first():
        return render_template('posts.html', comments=comments)

    new_vote = Vote(comment_id=comment_id, user=current_user)
    new_vote.save_stars()
    
    return render_template('posts.html', posts=posts)
    return render_template('index.html', title=title)





