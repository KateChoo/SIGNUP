from flask import Flask, render_template, request, redirect, session, g, flash
from datetime import timedelta
import os
import mysql.connector

mydb = mysql.connector.connect(host='localhost',
                               user='k',
                               password='kpython',
                               database="test"
                               )
app = Flask(__name__)
app.secret_key = 'secretkey'
app.permanent_session_lifetime = timedelta(minutes=10080)
cursor = mydb.cursor()

web_info = {
    'home_t': 'K留言板',
    'signin_t': '歡迎光臨，登入才有內容啊',
    'member_t': '歡迎光臨，這是會員頁面',
    'k_t': 'K作品連結',
    'taipei_t': '歡迎光臨，台北'
}


@app.before_request
def before_request():
    g. name = ' '
    if 'name' in session:
        name = session['name']
        g.name = name
        print(f'g.name{g.name}')


@app.route('/')
def home():
    return render_template('home.html', web_info=web_info)


@app.route('/signin', methods=['POST', 'GET'])
def signin():
    print(request.form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form.get('username')
        password = request.form.get('password')

        cursor.execute(
            'SELECT * FROM user WHERE username = %s AND password = %s', (username, password))
        result = cursor.fetchall()
        print(f'signin{result}')
        if result:
            name = result[0][1]
            session.permanent = True
            session['name'] = name
            session['username'] = username
            flash(f'Hi~ {name} 登入中～')
            print(f'result: {name}')
            return redirect('/member/')
        else:
            error3 = '帳號密碼輸入錯誤'
            return render_template('error.html', error3=error3)


@ app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'name' in request.form:
        name = request.form.get('name')
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')

        cursor.execute('SELECT * FROM user WHERE username = %s', (username,))
        result = cursor.fetchone()
        print(f'signup{result}')
        if result:
            error1 = '帳號已經被註冊'
            return render_template('error.html', error1=error1)
        elif password != password2:
            error2 = '密碼輸入不同'
            return render_template('error.html', error2=error2)
        else:
            query = "INSERT into user(name, username, password) VALUES (%s,%s,%s)"
            cursor.execute(query, (name, username, password))
            mydb.commit()
            flash(f'{name} 成功註冊系統～')
            #success = '成功註冊系統'
            return redirect('/')


@ app.route('/member/')
def member():
    return render_template('member.html', web_info=web_info)


@ app.route('/signout')
def signout():
    # session.pop('username', None)
    if 'name' in session:
        name = session['name']
        flash(f'{name} bye bye  登出啦～')
    session.pop('name', ' ')

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


@app.route('/tpe')
def taipei():
    return render_template('taipei.html', web_info=web_info)


@app.route('/k_links')
def msg():
    return render_template('k_links.html', web_info=web_info)


@app.route('/api/users', methods=['POST', 'GET'])
def make_api():  # ?username=ply  #charset='utf-8'
    # /api/users?username=ply
    try:
        user_api = request.args.get('username', '{"data": null}')
        if user_api:
            cursor.execute(
                'SELECT * FROM user where username = %s', (user_api,))
            result = cursor.fetchone()
            # print(f'api/users{result}')

            user_name = user_api
            # session.permanent = True
            session['username'] = user_name
            data = (
                {"data": {'id': result[0], 'name': result[1], 'username': result[2]}})
            print(f'user_api{data}')
            print(f'http://127.0.0.1:3000/api/users?username={user_api}')
            return data
        return render_template('member.html',
                               web_info=web_info,
                               data=data.encode('utf-8'),
                               user_api=user_api,
                               # headers=HEADERS,
                               )
    except:
        # else:
        data = '{\n"data": null\n}'
        return (data)


if __name__ == '__main__':
    app.run(debug=True, port=3000)

# if __name__ == '__main__':
#     port = int(os.environ.get("PORT", 5000))
#     app.run(debug=True, port=port, host="0.0.0.0")
