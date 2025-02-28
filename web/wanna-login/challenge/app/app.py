from flask import Flask, request, redirect, session, render_template, send_file
import os
import json

app = Flask(__name__)
app.secret_key = os.urandom(32)

FLAG = os.environ.get('FLAG', 'shellmates{4wh_GAwD_jS0N_INJeCt1oN_M44A44N}')
users_db = {
    'guest': 'guest',
    'admin': os.environ.get('PASSWORD', 'TEST_PWD')
}


@app.route("/", methods=['GET'])
def index():

    def valid_user(user):
        return users_db.get(user['username']) == user['password']

    if not session or 'user_data' not in session:
        return render_template("login.html", message="Login Please :D")
    user = json.loads(session['user_data'])
    if valid_user(user):
        if user['flag'] == True and user['username'] != 'guest':
            return FLAG
        else:
            return render_template("welcome.html", username=user['username'])

    return render_template("login.html", message="Verify Failed :(")


@app.route("/login", methods=['POST'])
def login():
    data = '{"flag": false, "username": "%s", "password": "%s"}' % (
        request.form["username"], request.form['password']
    )
    session['user_data'] = data
    return redirect("/")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@app.route("/hint")
def hint():
    return send_file('./hint.txt', mimetype="text/plain")


if __name__ == '__main__':
    app.run(threaded=True, debug=False)
