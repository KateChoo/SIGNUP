from flask import Flask, render_template, request, redirect, session, g
from datetime import timedelta
import mysql.connector

mydb = mysql.connector.connect(host='localhost',
                               user='k',
                               password='kpython',
                               database="test"
                               )
app = Flask(__name__)
app.secret_key = 'secretkey'
app.permanent_session_lifetime = timedelta(minutes=10080)
mycursor = mydb.cursor()

web_info = {
    'signin_t': '歡迎光臨，請輸入帳號密碼',
    'member_t': '歡迎光臨，這是會員頁面',
    'signup_t': '歡迎光臨，註冊成功',
    'error_t': '失敗頁面',
    'signout_t': '已登出',
}


@app.before_request
def before_request():
    g.username = '您'
    g.name = '您'
    if 'username' in session:
        username = session['username']
        g.username = username
    if 'name' in session:
        name = session['name']
        g.name = name


@app.route('/')
def home():
    return render_template('home.html',
                           web_info=web_info)


@app.route('/signin', methods=['POST', 'GET'])
def signin():
    name = ''
    username = request.form.get('username')
    password = request.form.get('password')

    if request.method == 'POST':
        mycursor.execute("SELECT username, password FROM user")
        result1 = mycursor.fetchall()
        # for n in range(len(result)):
        #     name = result[n][0]
        #     # print(name)
        #     print(result[n][1])
        #     print(result[n][2])
        # print(result[0][0])
        # print(result1)
        if ((username, password) in result1):
            session['username'] = username
            u = session['username']

            # mycursor.execute(
            #     "SELECT name FROM user where username = 'u'")
            # result2 = mycursor.fetchall()
            # session['name'] = name
            # print(session['name'])
            # print(result2)
            # name = session['name']
            # print(session['name'])
            # print(result2)
            # if result1[1] == result2[1]:
            #     print(result2[0])

            return redirect('/member/')
        elif ((username) not in result):
            error4 = '查無此帳號'
            return render_template('error.html', error4=error4)
        else:
            error3 = '帳號密碼輸入錯誤'
            return render_template('error.html', error3=error3)


@ app.route('/signup', methods=['POST', 'GET'])
def signup():

    if request.method == 'POST':
        name = request.form.get('name')
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
            mycursor.execute(query, (name, username, password))
            mydb.commit()
            success = '成功註冊系統'
            return redirect('/')


@ app.route('/member/')
def member():
    return render_template('member.html', web_info=web_info)


@ app.route('/signout')
def signout():
    session.pop('username', '您')
    return render_template('home.html',
                           web_info=web_info
                           )


@ app.route('/error/')
def error():
    msg = request.args.get('message', '有error')
    message = 'errorrrrrrr'
    if msg == '1':
        msg = '帳號或密碼輸入錯誤'

    return render_template('error.html',
                           web_info=web_info,
                           msg=msg
                           )


if __name__ == '__main__':
    app.run(debug=True, port=3000)
