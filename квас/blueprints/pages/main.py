from flask import Blueprint, render_template, request, redirect, url_for, session
from blueprints.deps import check_password_correct
from blueprints import deps

main_blueprint = Blueprint("main_blueprint", __name__, url_prefix="/")


@main_blueprint.route('/', methods=['POST', 'GET'])
def render_main_page():
    if request.method == 'POST':
        user_password = request.form['passfield']
        tple = check_password_correct(user_password)
        session['password'] = user_password
        if tple is None:
            session['password_incorrect'] = 'Password is incorrect'
            return redirect('/')
        else:
            session['password_hash'] = str(tple[0][0])
            # Сделать так чтобы надпись неправильный пароль не оставалась на гл станичке после ее обновления
            if tple[1] is True:
                if deps.get_user_by_password(str(tple[0][0])).activated == 0:
                    return redirect(url_for('pages_blueprint.login_blueprint.render_login_page'))
                else:
                    session['username'] = deps.get_user_by_password(str(tple[0][0])).login
                    session['password_incorrect'] = ''
                    return redirect(url_for('pages_blueprint.core_blueprint.render_core_page'))
    return render_template('main.html')
