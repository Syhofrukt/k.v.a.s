from flask import Blueprint, render_template, request, redirect, url_for, session
from crud import user_crud
from core.db import get_connection
from blueprints import deps
from models import user
login_blueprint = Blueprint("login_blueprint", __name__, url_prefix="/register")


@login_blueprint.route('/', methods=['POST', 'GET'])
def render_login_page():
    if not session.get('password'):
        return redirect('/')
    if session.get('username'):
        return redirect(url_for('pages_blueprint.core_blueprint.render_core_page'))
    if request.method == 'POST':
        login = user.RegistrationModel(login=request.form['loginfield'], password=session.get('password_hash'))
        if deps.get_user_by_login(login.login) is None:
            with get_connection() as conn:
                user_crud.create(conn, login)
            return redirect(url_for('pages_blueprint.core_blueprint.render_core_page'))
    return render_template('login.html')