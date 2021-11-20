from app import create_app, db, admin
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from flask_admin.contrib.sqla import ModelView
from app.models import User,Comment, Post

app = create_app('development')
manager = Manager(app)
manager.add_command('server',Server)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Post, db.session))
admin.add_view(ModelView(Comment, db.session))
@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User, Post = Post )
if __name__ == '__main__':
    manager.run()
