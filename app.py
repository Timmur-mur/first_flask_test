from flask import Flask
from config import Conf
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_ckeditor import CKEditor
from flask_mail import Mail



app = Flask(__name__)
app.config.from_object(Conf)
ckeditor = CKEditor(app)
db = SQLAlchemy(app)





migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

mail = Mail(app)

