from forms import *
from models import *
from flask import request
from flask import render_template, g
from flask import redirect
from flask import url_for
from werkzeug.security import generate_password_hash, check_password_hash
from app import app, db
from flask import flash
from flask import session
from datetime import datetime
from flask_ckeditor import upload_success, upload_fail
from app import mail
from flask_mail import Message
import random


user = None

@app.before_request
def before():
    global user
    user = get_user() 
    

def send_mail(subject, recipient, template, sender=app.config['MAIL_DEFAULT_SENDER']):
    msg = Message(subject=subject, sender = sender, recipients=recipient)
    msg.html = template()
    mail.send(msg)
    return True

def send_mail_reg(subject, recipient, template, sender=app.config['MAIL_DEFAULT_SENDER']):
    msg = Message(subject=subject, sender = sender, recipients=recipient)
    msg.html = template
    mail.send(msg)
    return True

def get_user():
    if not hasattr(g, 'us'):
        try:
            g.us = User.query.filter(User.hesh == session['status']).first()
            return g.us
        except:
            return None


def mail_reg(name, code):
    return render_template('regist_mail.html', name = name, code = code)


def registration_func():
    form = NewUserForm()
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        password = generate_password_hash(request.form['password'])

        if email == User.query.filter(User.email == email).first():
            flash('Пользователь с такой почтой уже зарегестрирован')
            return render_template('redistration.html', form = form)
        else:
            cod = random.randrange(15, 2587)
            template_mail = mail_reg(name, cod)
            send_mail_reg(subject='Вы зарегестрировались', recipient=[email], template=template_mail)
            if 'checkbox' in request.form:
                hesh = generate_password_hash('qwerty')
                session['status'] = hesh
                session['admin'] = False
                us = User(name = name, email = email, phone = phone, password = password, code = cod,
                        active = False, hesh = hesh, basket = Basket())
                us.role.append(Role.query.filter(Role.id == 2).first())
                db.session.add(us)
                db.session.commit()
               
                return redirect(url_for('authorization'))
            else:
                us = User(name = name, email = email, phone = phone, password = password, code = cod,
                        active = False, hesh = '', basket = Basket())
                us.role.append(Role.query.filter(Role.id == 2).first())
                db.session.add(us)
                db.session.commit()
                return redirect(url_for('enter'))

    return render_template('registration.html', form = form)


def authorization_func():
    form = Authorization()
    if request.method == 'POST':
        if user.code == int(request.form['body']):
            user.active = True
            db.session.commit()
            return redirect(url_for('index'))
        else:
            return 'проверьте почту и введите код'
    return render_template('authorization.html', name = user.name, form = form)

def enter_func():

    form = FormAutent()
    
    if form.validate_on_submit():
    
        email = request.form['email']
        password = request.form['password']
        
        try:
            user = User.query.filter(User.email == email).first()
            if user.email and check_password_hash(user.password, password):
                
                hesh = generate_password_hash('qwerty')
                session['status'] = hesh
                user.hesh = hesh
                db.session.commit()
                if user.role[0].name == 'admin':
                    session['admin'] = True
                else:
                    session['admin'] = False
                if user.active:
                    return redirect(url_for('index'))
                else:
                    return redirect(url_for('authorization'))
        except:
            flash('введен не верно емайл или пароль')
            return render_template('enter.html', form = form)
            
    return render_template('enter.html', form = form)


def pizza_func():
    page = request.args.get('page')
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1
    allpizza = Eat.query.filter(Eat.tipe == 'p').all()
    pages = Peginatuion(allpizza, 3, page)
    return render_template('pizza1.html', pages = pages)


def roll_func():
    page = request.args.get('page')
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1
    allroll = Eat.query.filter(Eat.tipe == 'r').all()
    pages = Peginatuion(allroll, 3, page)
    return render_template('roll.html', pages = pages)


def price_func(slug):
    detail = Eat.query.filter(Eat.slug == slug).first()
    return render_template('price_detail.html', detail = detail)

def logout_func():
    session.pop('status', None)
    session.pop('admin', None)
    return redirect(url_for('index'))


def index_func():
    news = News_page.query.all()
    if user:
        return render_template('index.html', name = user.name, news = news)
    return render_template('index.html', news = news)


def admin_func():
    all_eat = Eat.query.all()
    return render_template('admin/admin.html', eat = all_eat)


def del_func(slug):
    eat = Eat.query.filter(Eat.slug == slug).first()
    db.session.delete(eat)
    db.session.commit()
    return redirect(url_for('admin.index'))


def edit_func(slug):
    eat = Eat.query.filter(Eat.slug == slug).first()

    if request.method == 'POST':
        form = NewEatForm(formdata = request.form, obj = eat)
        form.populate_obj(eat)
        items_file = request.files['image']

        if items_file.filename.split('.')[-1].lower() in ['jpeg', 'jpg', 'png']:
            items_file.seek(0, 2)
            size = items_file.tell()
            items_file.seek(0,0)
            if size > 1000000:
                print (size)
                return 'to big file'
            else:
                items_file.save('/home/murlo/flasky/app/static/images/'+ eat.namefoto)
        db.session.commit()

        return redirect(url_for('index'))
    form = NewEatForm(obj = eat)
    return render_template('admin/edit.html', eat = eat, form = form)


def create_func():
    form = NewEatForm()
    print(dir(form))
    if form.validate_on_submit():
        tipe = request.form['tipe']
        name = request.form['name']
        price = request.form['price']
        body = request.form['body']
        items_file = request.files['image']



        if items_file.filename.split('.')[-1].lower() in ['jpeg', 'jpg', 'png']:
            items_file.seek(0, 2)
            size = items_file.tell()
            items_file.seek(0,0)
            if size > 1000000:
                print (size)
                return 'to big file'
            else:
                name_data = str(datetime.now())
                namef = name_data.split(' ')
                name_data = '-'.join(namef)
                
                if tipe == 'r':
                    tipe_name = 'roll'
                else:
                    tipe_name = 'pizza'

                items_file.filename = tipe_name + name_data + '.jpg'
                items_file.save('/home/murlo/flasky/app/static/images/'+items_file.filename)
   
        else:
            print(items_file.filename.split('.')[-1])
            return redirect(url_for('errors'))
        try:
            new = Eat(tipe = tipe, namefoto = items_file.filename, name = name, price = price, body = body)
            db.session.add(new)
            db.session.commit()
        except:
            print('Проблема с добав в базу')
            return 'problem witsh database'
        return redirect(url_for('admin.index'))
    
    return render_template('admin/create.html', form = form)


def news_func():
    form = News()
    if request.method == "POST":
        body =  request.form['body']
        news = News_page(body = body)
        db.session.add(news)
        db.session.commit()
        print(body)
    return render_template('admin/create_news.html', form = form )

def basket_func():
    if 'status' in session and session['admin'] == False:
        if user.active:
            if 'slug' in request.args:
                slug = request.args['slug']
                detail = Eat.query.filter(Eat.slug == slug).first()
                user.basket.items_order.append(detail)
                db.session.commit()
            order = user.basket.items_order
            return render_template('basket.html', order = order)
        else:
            return redirect(url_for('authorization'))
    return redirect(url_for('enter'))


def new_order_func():
    if Orders.query.filter(Orders.user is User()):
        orders = Orders.query.all()
        
    return render_template('admin/orders.html', orders = orders)

def send_order_func():
    if 'order_id' in request.args:
        order_id = int(request.args['order_id'])
        order = Orders.query.filter(Orders.id == order_id).first()
        order.status = False
        db.session.commit()
        return redirect(url_for('admin.orders'))



def drop_basket_func():
    slug = request.args['slug']
    order = Eat.query.filter(Eat.slug == slug).first()
    pr = user.basket.items_order.index(order)
    user.basket.items_order.pop(pr)
    order = user.basket.items_order
    db.session.commit()
    return redirect(url_for('basket'))

def pay_func():
    order = basket_func
    send_mail(subject='Заказ в магазне', recipient=['###########'], template=order)
    send_mail(subject='Заказ новый ', recipient=['#############'], template=order, sender=user.email)
    order = Orders(user = user, items_order = user.basket.items_order, status=True)
    user.basket.items_order = []
    db.session.add(order)
    db.session.commit()
    return redirect(url_for('index'))

def get_users_func():
    users = User.query.all()
    return render_template('admin/users.html', users = users)

def get_history_func():
    if 'user_id' in request.args:
        user_id = int(request.args['user_id'])
        user = User.query.filter(User.id == user_id).first()
        orders = Orders.query.all()
        rez = []
        for order in orders:
            if order.user.email == user.email:
                rez.append(order)
        return render_template('admin/history.html', orders = rez, user = user)

def cabinet_func():
    if 'status' in session and session['admin'] == False:
        if user.active:
            orders = Orders.query.all()
            rez = []
            for order in orders:
                if order.user.email == user.email:
                    rez.append(order)
            return render_template('personal_area.html', orders = rez, user = user )
        else:
            return redirect(url_for('authorization'))
    return redirect(url_for('enter'))

def edit_user_data_func():
    user_id = int(request.args['user_id'])
    user = User.query.filter(User.id == user_id).first()
    if request.method == 'POST':
        form = NewUserForm(formdata = request.form, obj = user)
        form.populate_obj(user)
        db.session.commit()
        return redirect(url_for('cabinet'))
    
    form = NewUserForm(obj = user)
    return render_template('edit_user_data.html', user = user, form = form)


class Peginatuion():
    
    def __init__(self, massiv, output_volume, page):
        self.page = page
        self.massiv = massiv
        self.output_volume = output_volume
        self.offset = (self.page*self.output_volume)- self.output_volume
        

    def get_pages(self):
        current_page = self.massiv[self.offset:(self.offset+self.output_volume)]
        if current_page == []:
            return self.massiv[:self.output_volume]
        else:
            return current_page

    def get_all_pages(self):
        all_pages = len(self.massiv) // self.output_volume
        last_page = len(self.massiv) % self.output_volume
        if last_page > 0:
            return all_pages + 1
        else:
            return all_pages
    
    def get_prev(self):
        page = self.massiv[(self.offset - self.output_volume):self.output_volume + (self.offset - self.output_volume)]
        if page == []:
            return False
        return page

    def get_next(self):
        page = self.massiv[(self.offset+self.output_volume):self.output_volume + (self.offset+self.output_volume)]
        if page == []:
            return False
        else:
            return page

    def prev_num(self):
        if self.page > 1:
            return self.page - 1
        else:
            return 1

    
    def next_num(self):
        all_pages = len(self.massiv) // self.output_volume
        last_page = len(self.massiv) % self.output_volume
        if last_page > 0:
            pages = all_pages + 1
        else:
            pages = all_pages
        if self.page < pages:
            return self.page + 1
        else:
            return pages
    





