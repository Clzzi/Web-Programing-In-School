from flask import * # flask 패키지 불러오기

app = Flask(__name__) # 인스턴스 생성

import os
os.environ['APP_SETTINGS'] = 'settings.cfg'

# 환경변수에 저장된 경로의 설정파일을 불러옴
app.config.from_envvar('APP_SETTINGS')

from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor

mysql = MySQL(cursorclass= DictCursor)
mysql.init_app(app)

@app.route('/') # /test 주소로 접속시 실행될 함수 지정
def main():
  return render_template('index.html', userName=session.get('user_id'))

@app.route('/join') #GET만 받음
def join():
  return render_template('join.html', userName=session.get('user_id'))

# /join주소로 post요청이 오면 실행됨
# 회원가입 페이지에서
@app.route('/join', methods=['POST']) 
def join_post():
    user_id = request.values.get('user_id')
    user_name = request.values.get('user_name')
    user_pw = request.values.get('user_pw')
    
    # DB 커넥션 가져오기
    conn = mysql.get_db()
    cursor = conn.cursor()
    
    # DB에 이미 이 ID가 있는지 확인
    cursor.execute('SELECT * FROM users WHERE user_id = %s;', [user_id])
    row = cursor.fetchone()
    
    # 있으면 오류를 표시
    if row is not None: # None 이 아니면 데이터가 있다는 소리
        return render_template('join.html', error=True)
    
    # 없으면 DB에 사용자 추가
    # pk, user_id, user_name, user_pw
    cursor.execute('INSERT INTO users VALUES (NULL, %s, %s, %s)', [user_id, user_name, user_pw])
    
    # 변경사항 저장 (transaction commit)
    conn.commit()
    
    # 세션에 사용자 이름을 넣어주고
    session['name'] = user_name
    
    # 메인페이지로 이동
    return redirect('/')
  
@app.route('/login')
def login():
  return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
  user_id = request.values.get('user_id')
  user_pw = request.values.get('user_pw')

  conn = mysql.get_db()
  cursor = conn.cursor()

  cursor.execute('SELECT * FROM users WHERE user_id = %s AND user_pw = %s', [user_id, user_pw])
  id_row = cursor.fetchone()

  if id_row is None:
    return render_template('login.html', error=True)
  
  session['user_id'] = id_row['user_name']
  return redirect('/')


@app.route('/logout')
def logout():
  del session['user_id']
  return render_template('index.html')






# 내장 웹서버 실행, 코드의 가장 마지막 줄에 있어야 함
# host='0.0.0.0': 다른 컴퓨터에서도 접속할 수 있도록 설정 / port=5000: 웹 서버를 5000포트에 실행
app.run(host='0.0.0.0', port=5000, debug=True)