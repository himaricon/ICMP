from flask import Flask, render_template, request, redirect, url_for, session, flash
from functools import wraps
import secrets


app = Flask(__name__)
app.secret_key = secrets.token_hex(32)


reviews = []




def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            flash("You need to log in first", "error")
            return redirect(url_for('login', error_message='You need to log in first.'))
        return f(*args, **kwargs)
    return decorated_function


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/services')
def services():
    return render_template('services.html')



@app.route('/location')
def locations():
    return render_template('location.html')



@app.route('/reviews', methods=['POST', 'GET'])
def reviews_clients():
    global reviews
    if request.method == 'POST':
        review = { 
            'name': request.form['name'],
            'rating': int(request.form['rating']),
            'review': request.form['review']
        }
        reviews.append(review)
    return render_template('reviews.html', reviews = reviews)


@app.route('/contact')
def contact():
    return render_template('contact.html')



if __name__ == '__main__':
    app.run(debug = True)