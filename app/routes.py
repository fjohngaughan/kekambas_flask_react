from app import app, db, mail, Message
from flask import render_template, request, flash, redirect, url_for
from app.forms import UserInfoForm, PostForm, LoginForm
from app.models import User, Post
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash

@app.route('/')
@app.route('/index')
def index():
    context = {
        'title': 'Kekambas Blog | HOME',
        'posts': Post.query.all()
    }
    return render_template('index.html', **context)


@app.route('/register', methods=['GET', 'POST'])
def register():
    title = "Kekambas Blog | REGISTER"
    form = UserInfoForm()
    if request.method == 'POST' and form.validate():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        # print(username, email, password)
        
        # create a new instance of User
        new_user = User(username, email, password)
        # add new instance to our database
        db.session.add(new_user)
        # commit database
        db.session.commit()

        # Send email to new user
        msg = Message(f'Welcome, {username}', [email])
        msg.body = "Thank you for signing up for the Kekambas blog. I hope you enjoy our app!"
        msg.html = "<p>Thank you so much for signing up for the Kekambas blog. I hope you enjoy our app!</p>"

        mail.send(msg)

        flash("You have succesfully signed up!", "success")
        return redirect(url_for('index'))
    return render_template('register.html', title=title, form=form)


@app.route('/createpost', methods=['GET', 'POST'])
@login_required
def createpost():
    title = "Kekambas Blog | CREATE POST"
    post = PostForm()
    if request.method == 'POST' and post.validate():
        post_title = post.title.data
        content = post.content.data
        user_id = current_user.id
        # print(post_title, content)
        # Create new Post instance
        new_post = Post(post_title, content, user_id)
        # Add new post instance to database
        db.session.add(new_post)
        # Commit
        db.session.commit()
        # flash a message
        flash("You have successfully created a post!", 'success')
        # redirect back to create post
        return redirect(url_for('createpost'))
    return render_template('create_post.html', post=post, title=title)


@app.route('/login', methods=['GET', 'POST'])
def login():
    title = "Kekambas Blog | LOGIN"
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()

        if user is None or not check_password_hash(user.password, password):
            flash("Incorrect Email/Password. Please try again", 'danger')
            return redirect(url_for('login'))
        
        login_user(user, remember=form.remember_me.data)
        flash("You have successfully logged in!", 'success')
        next_page = request.args.get('next')
        if next_page:
            return redirect(url_for(next_page.lstrip('/')))
        return redirect(url_for('index'))

    return render_template('login.html', title=title, form=form)


@app.route('/logout')
def logout():
    logout_user()
    flash("You have succesfully logged out", 'primary')
    return redirect(url_for('index'))
