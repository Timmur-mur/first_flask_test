from flask import Blueprint, request
from login_secret import login_secret
from flask import render_template, redirect, url_for, send_from_directory
import funcs
from flask_ckeditor import upload_success, upload_fail
from datetime import datetime




admin = Blueprint('admin', __name__, template_folder = 'templates')




@admin.route('/')
@login_secret
def index():
    return funcs.admin_func()


@admin.route('/<slug>/edit/', methods = ['GET', 'POST'])
@login_secret
def edit(slug):
    return funcs.edit_func(slug)


@admin.route('/create/', methods = ['POST', 'GET'])
@login_secret
def create():
    return funcs.create_func()


@admin.route('/<slug>/delite/')
@login_secret
def delit(slug):
    return funcs.del_func(slug)

@admin.route('/create_news/', methods = ['POST', 'GET'])
@login_secret
def create_new():
    return funcs.news_func()

@admin.route('/uploads/<path:filename>')
def upload_file(filename):
    path = '/home/murlo/flasky/app/uploads/'
    return send_from_directory(path,filename)


@admin.route('/upload/', methods = ['POST'])
def upload_image_on_server():
    f = request.files.get('upload')
    extension = f.filename.split('.')[-1].lower()
    if extension not in ['jpg','png', 'gif', 'jpeg']:
        return upload_fail(message='это не картинка')
    f.filename = str(datetime.now()) + '.' + extension
    f.save('/home/murlo/flasky/app/uploads/'+ f.filename)
    url = url_for('admin.upload_file', filename = f.filename)
    return upload_success(url = url)

@admin.route('/orders/')
def orders():
    return funcs.new_order_func()

@admin.route('/orders/send/')
def send_order():
    return funcs.send_order_func()

@admin.route('/users/')
def users():
    return funcs.get_users_func()

@admin.route('/users/history/')
def history():
    return funcs.get_history_func()