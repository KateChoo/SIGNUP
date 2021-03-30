from flask import Flask, render_template, request, redirect, session, g
from datetime import timedelta
import mysql.connector

# from flask_mysqldb import MySQL
# import yaml
# db = yaml.load(open('dbyaml'))
# app.config['MYSQL_HOST'] = db['mysql_host']
# app.config['MYSQL_USER'] = db['mysql_user']
# app.config['MYSQL_PASSWORD'] = db['mysql_password']
# app.config['MYSQL_DB'] = db['mysql_db']
# mysql = MySQL(app)

mydb = mysql.connector.connect(host='localhost',
                               user='k',
                               password='kpython',
                               database="test"
                               )
app = Flask(__name__)
app.secret_key = 'secretkey'
app.permanent_session_lifetime = timedelta(minutes=10080)
mycursor = mydb.cursor()
#mycursor = mysql.connection.cursor()
web_info = {
    'signin_t': '歡迎光臨，請輸入帳號密碼',
    'member_t': '歡迎光臨，這是會員頁面',
    'signup_t': '歡迎光臨，註冊成功',
    'error_t': '失敗頁面',
    'signout_t': '已登出',
    'success': '成功註冊系統'
}


@app.before_request
def before_request():
    g.username = '您'
    if 'username' in session:
        username = session['username']
        g.username = username


@app.route('/')
def home():
    return render_template('home.html',
                           web_info=web_info)


@app.route('/signin', methods=['POST', 'GET'])
def signin():
    username = request.form.get('username')
    password = request.form.get('password')

    # session.pop('user_username', None)
    if request.method == 'POST':
        mycursor.execute("SELECT username, password FROM user")
        result = mycursor.fetchall()
        if ((username, password) in result):
            print((username, password))
            session['username'] = username
            # login = '成功登入系統'
            return redirect('/member/')
            # return render_template('member.html', login=login, username=username)
        elif ((username) not in result):
            error4 = '查無此帳號'
            return render_template('error.html', error4=error4)
        else:
            error3 = '帳號密碼輸入錯誤'
            return render_template('error.html', error3=error3)


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    # error = None
    # success = None

    if request.method == 'POST':
        # session.permanent = True
        uname = request.form.get('uname')
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')

        mycursor.execute("SELECT username FROM user")
        usernameresult = mycursor.fetchall()

        if (username,) in usernameresult:
            print((username,))
            error1 = '帳號已經被註冊.'
            return render_template('error.html', error1=error1)
        elif password != password2:
            error2 = '密碼輸入不同'
            return render_template('error.html', error2=error2)
        else:
            query = "INSERT into user(name, username, password) VALUES (%s,%s,%s)"
            mycursor.execute(query, (uname, username, password))
            mydb.commit()
            # mysql.connection.commit()
            # mycursor.close()
            success = '成功註冊系統'
            return redirect('/')


@app.route('/member/')
def member():
    # logout = '已登出'
    return render_template('member.html', web_info=web_info)


@ app.route('/signout')
def signout():
    session.pop('username', '您')
    return render_template('home.html',
                           web_info=web_info
                           )


@ app.route('/error/')
def error():
    return render_template('error.html',
                           web_info=web_info
                           )


if __name__ == '__main__':
    app.run(debug=True, port=3000)
