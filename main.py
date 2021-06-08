from app import app
import view
from admin.blueprint import admin

app.register_blueprint(admin, url_prefix='/admin')

if __name__ == '__main__':
    app.run()