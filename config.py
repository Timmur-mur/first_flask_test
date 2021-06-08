class Conf():
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://#######:1234@localhost/test'
    UPLOADED_IMAGES_DEST = 'app/static/images'
    SECRET_KEY = 'secretkeyururur'
    CKEDITOR_SERVE_LOCAL = True
    CKEDITOR_FILE_UPLOADER = 'admin.upload_image_on_server'
    CKEDITOR_HEIGHT = 600
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = '############'
    MAIL_DEFAULT_SENDER = '###############'
    MAIL_PASSWORD = '#######'

    
