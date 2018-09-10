from flask_login import login_user, logout_user
from .. import login_manager
from .models import User


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)
