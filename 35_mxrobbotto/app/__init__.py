from flask import Flask, render_template, redirect, url_for, request, session, flash, g
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from db import get_db, query_db, init_db
from forms import RegistrationForm, LoginForm, BlogForm, EntryForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'

@app.route('/')
def index():
    if 'username' in session:
        user = query_db('SELECT * FROM user WHERE username = ?', [session['username']], one=True)
        blogs = query_db('SELECT * FROM blog WHERE user_id = ?', [user['id']])
        return render_template('index.html', blogs=blogs)
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='pbkdf2:sha256')
        db = get_db()
        db.execute('INSERT INTO user (username, password) VALUES (?, ?)', [form.username.data, hashed_password])
        db.commit()
        session['username'] = form.username.data
        flash('Registration successful!', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = query_db('SELECT * FROM user WHERE username = ?', [form.username.data], one=True)
        if user and check_password_hash(user['password'], form.password.data):
            session['username'] = form.username.data
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login failed. Check your username and/or password', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

@app.route('/new_blog', methods=['GET', 'POST'])
def new_blog():
    if 'username' not in session:
        flash('Please log in first.', 'danger')
        return redirect(url_for('login'))
    form = BlogForm()
    if form.validate_on_submit():
        user = query_db('SELECT * FROM user WHERE username = ?', [session['username']], one=True)
        db = get_db()
        db.execute('INSERT INTO blog (title, user_id) VALUES (?, ?)', [form.title.data, user['id']])
        db.commit()
        flash('Blog created!', 'success')
        return redirect(url_for('index'))
    return render_template('new_blog.html', form=form)

@app.route('/blog/<int:blog_id>/new_post', methods=['GET', 'POST'])
def new_post(blog_id):
    if 'username' not in session:
        flash('Please log in first.', 'danger')
        return redirect(url_for('login'))
    form = EntryForm()
    if form.validate_on_submit():
        db = get_db()
        db.execute('INSERT INTO entry (title, content, blog_id) VALUES (?, ?, ?)', [form.title.data, form.content.data, blog_id])
        db.commit()
        flash('Post added!', 'success')
        return redirect(url_for('view_blog', blog_id=blog_id))
    return render_template('new_post.html', form=form)

@app.route('/blog/<int:blog_id>')
def view_blog(blog_id):
    blog = query_db('SELECT * FROM blog WHERE id = ?', [blog_id], one=True)
    entries = query_db('SELECT * FROM entry WHERE blog_id = ?', [blog_id])
    return render_template('view_blog.html', blog=blog, entries=entries)

@app.route('/post/<int:entry_id>/edit', methods=['GET', 'POST'])
def edit_post(entry_id):
    if 'username' not in session:
        flash('Please log in first.', 'danger')
        return redirect(url_for('login'))
    entry = query_db('SELECT * FROM entry WHERE id = ?', [entry_id], one=True)
    form = EntryForm(data=entry)
    if form.validate_on_submit():
        db = get_db()
        db.execute('UPDATE entry SET title = ?, content = ? WHERE id = ?', [form.title.data, form.content.data, entry_id])
        db.commit()
        flash('Post updated!', 'success')
        return redirect(url_for('view_blog', blog_id=entry['blog_id']))
    return render_template('edit_post.html', form=form)

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == "__main__":
    with app.app_context():
        init_db()
    app.run(debug=True)
