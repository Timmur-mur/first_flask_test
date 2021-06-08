from app import app
from login_secret import login_secret_autoriz
import funcs
from flask import render_template




@app.route('/registration/', methods = ['GET', 'POST'])
@login_secret_autoriz
def registration():
    return funcs.registration_func()

@app.route('/enter/', methods = ['GET', 'POST'])
@login_secret_autoriz
def enter():
    return funcs.enter_func()


@app.route('/log_out/')
def log_out():
    return funcs.logout_func()


@app.route('/')
def index():
    return funcs.index_func()

@app.route('/pizza/')
def pizza():
    return funcs.pizza_func()

@app.route('/roll/')
def roll():
    return funcs.roll_func()

@app.route('/<tip>/<slug>/') 
def price_detail(slug, tip):
    return funcs.price_func(slug)

@app.route('/basket/')
def basket():
    return funcs.basket_func()

@app.route('/basket_drop/')
def drop_basket():
    return funcs.drop_basket_func()

@app.route('/pay/')
def pay_order():
    return funcs.pay_func()


@app.route('/authorization/', methods=["GET", "POST"])
def authorization():
    return funcs.authorization_func()

@app.route('/personal_area/')
def cabinet():
    return funcs.cabinet_func()

@app.route('/personal_area/edit_user_data', methods=["GET", "POST"])
def edit_user_data():
    return funcs.edit_user_data_func()


@app.errorhandler(404)
def errors(e):
    return render_template('404.html'), 404
