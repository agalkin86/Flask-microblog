from app import blog, db
from app.models import User, Post


@blog.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}