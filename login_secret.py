from models import User
from flask import url_for, redirect, request, session, render_template
from functools import wraps
from app import app

def login_secret(f):
    @wraps(f)
    def wrraper(*args, **kwargs):
        if 'status' in session and session['status']:
            Us = User.query.filter(User.hesh == session['status']).first()
            if Us.role[0].name != 'admin':
                return redirect(url_for('enter'))
        else:
            return redirect(url_for('enter'))
        return f(*args, **kwargs)
    return wrraper



def login_secret_autoriz(f):
    @wraps(f)
    def wrraper(*args, **kwargs):
        if 'status' in session and session['status']:
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return wrraper



