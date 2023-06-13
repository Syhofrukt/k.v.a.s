from flask import Blueprint, render_template, request, redirect, url_for, session
from crud import user_crud
from core.db import get_connection
from blueprints import deps
from models import user
core_blueprint = Blueprint("core_blueprint", __name__, url_prefix="/core")


@core_blueprint.route('/')
def render_core_page():
    if not session.get('username'):
        return redirect('/')
    username = session.get('username')
    return render_template('core.html', username=username)

@core_blueprint.route('/chats')
def render_chats_page():
    if not session.get('username'):
        return redirect('/')
    username = session.get('username')
    return render_template('chats.html', username=username)

@core_blueprint.route('/chats/<chat_id>')
def render_chat_page():
    if not session.get('username'):
        return redirect('/')
    username = session.get('username')
    return render_template('chats.html', username=username)

@core_blueprint.route('/logout')
def logout():
    if not session.get('username'):
        return redirect('/')
    username = session.get('username')
    session['password'] = None
    return redirect('/')

@core_blueprint.route('/friends')
def render_friends_page():
    if not session.get('username'):
        return redirect('/')
    username = session.get('username')
    return render_template('friends.html', username=username)

@core_blueprint.route('/forum_main')
def render_forum_main_page():
    if not session.get('username'):
        return redirect('/')
    username = session.get('username')
    return render_template('forum_main.html', username=username)




