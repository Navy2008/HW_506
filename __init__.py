import os

from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY', default='dev'),
    )
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    from .models import db, Menu
    db.init_app(app)
    
    @app.route('/')
    def index():
        return redirect(url_for('menu'))
    @app.route('/Menu')
    def menu():
        menu = Menu.query.all()
        return render_template('menu_index.html', menu = menu)
    
    @app.route() 
    
