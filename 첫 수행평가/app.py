"""
Python 에서 한줄 주석은 # 으로 시작합니다.
여러줄 주석을 사용하기 위해서는 이 텍스트처럼 "(쌍따옴표) 혹은 '(따옴표) 를 3개 연속으로 사용하시면 됩니다.
원래는

a = '''동해물과
백두산이'''

이런식으로 여러줄 문자열을 정의할때 사용하는 문법인데, 주석처럼 사용할 수도 있습니다.
"""


"""
다른 패키지나 파이썬 코드 파일을 사용하기 위해서 import 구문을 사용할 수 있습니다.
import 패키지이름

우리가 사용하는 flask 패키지 안에는 request, session, render_template, redirect 등의 변수나 함수가 있습니다.
import flask
와 같이 패키지를 불러오고나서,
flask.request, flask.session, ... 과 같이 사용할 수 있습니다.
자주 사용하는 변수나 함수를 가져오게 될 경우
from flask import request, session
구문을 사용하여 flask.request 이렇게 사용하지 않고 바로 request 변수에 접근할 수 있습니다.

flask 안에서 사용할 모든 변수/함수를 지정해줄 수도 있지만
from flask import *
구문으로 flask 내의 변수/함수를 모두 바로 사용할 수 있게 가져올 수도 있습니다.
"""
from flask import *

# Flask 인스턴스 생성
app = Flask(__name__)

"""
프로그램 내에서 변수를 사용하는 것처럼, 완성된 프로그램이 작동을 위해 참고할 수 있는 변수들이 있습니다.
환경변수라는 이름으로 OS나 쉘 등 작동 환경 내에서 관리됩니다.

flask에서는 비밀번호 등 민감정보를 별도의 설정파일에 적어둘 수 있는데,
그 설정파일의 위치를 환경변수를 통해 지정할 수 있습니다.

원래라면 프로그램 밖에서 환경변수로 파일의 위치를 지정해주는 형태가 되겠지만,
지금은 프로그램 내에서 환경변수에 파일의 위치를 직접 넣어주도록 할게요

APP_SETTINGS는 임의로 정한 값이고,
settings.cfg는 설정파일의 경로입니다.
이 파일과 같은 경로에 settings.cfg 파일을 만들 것이기 때문에, 파일 이름만 써줘도 됩니다.

당연하지만, app.py 파일과 같은 경로에 settings.cfg 파일도 만들고 적절하게 수정해주세요.
"""
import os
os.environ['APP_SETTINGS'] = 'settings.cfg'

"""
환경변수에 지정했던 값을 통해 설정파일을 불러옵니다
"""
app.config.from_envvar('APP_SETTINGS')


"""
Database 연결을 위해 관련 패키지를 불러오고, 설정하는 코드입니다.
연결 정보는 위에 설정파일에 설정한 정보를 사용합니다.
MYSQL_DATABASE_HOST = 'web.dgsw.kr'		# 접속주소
MYSQL_DATABASE_USER = 's2000'			# 접속 ID
MYSQL_DATABASE_PASSWORD = '###'			# 비밀번호
MYSQL_DATABASE_DB = 's2000'				# 사용할 DB명 (사용자ID와 같게 해주세요)
"""
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor
from datetime import datetime
mysql = MySQL(cursorclass= DictCursor)
mysql.init_app(app)


"""
DB는 제가 web.dgsw.kr 에 MariaDB(MySQL과 비슷함) 서버를 설치해두었습니다.

주소: web.dgsw.kr
포트: 3306
으로 바로 접속하거나 각자 사용하는 프로그램으로 접속할 수도 있지만,

http://web.dgsw.kr/pma
주소로 들어가서 로그인/관리하실 수도 있어요.

사용자명은 s학번(ex, s2101) 이고, 기본 비밀번호는 학번 두번(21012101) 입니다.

이번 예시에서는 사용자 테이블 하나만 사용할거에요.
테이블을 GUI로 만드는 스크린샷을 포함해두긴 했지만, 아래 쿼리로 바로 생성할 수도 있습니다.

-- 이미 테이블이 있다면 삭제
DROP TABLE IF EXISTS `users`;

-- 테이블 생성
CREATE TABLE `users` (
  `pk` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `user_id` varchar(100) NOT NULL,
  `user_name` varchar(100) NOT NULL,
  `user_pw` varchar(100) NOT NULL
) CHARSET=utf8mb4;
"""


"""
@app.route('/주소')
데코레이터를 통해, 특정 주소로 접속시 어떤 함수를 실행할지 설정할 수 있습니다.
* 주소는 반드시 / 로 시작해야합니다!

데코레이터 바로 아래에 함수를 정의해주면 됩니다.

@app.route('/abc')
def r_abc():
	return 'def'

이렇게 사용할 경우
http://~~서버주소~~/abc
로 접속시
r_abc() 함수가 실행되고, 브라우저엔 def 라는 문자열이 보이게 됩니다.
"""


# 로그인 페이지
@app.route('/login')
def login():
	"""
	return 한 문자열이 브라우저에 바로 보이게 되지만, HTML코드를 모두 파이썬에 넣어두면 복잡하겠죠?
	별도 폴더에 넣어두고 불러와서 사용할 수 있습니다.
	render_template 함수를 통해 HTML 파일을 불러오고, 일부 값들을 HTML파일로 보내서 원하는 내용을 표시할 수도 있습니다.
	render_template 함수는 templates 폴더 안에서 첫번째 인자로 넘겨준 파일을 찾습니다.
	"""
	return render_template('login.html')

"""
@app.route 를 그냥 사용할 경우, GET 메소드에만 작동합니다.
폼 전송을 할때 POST 메소드를 사용하였다면, POST 메소드를 사용하겠다고 별도로 알려주어야 합니다.
@app.route 데코레이터 안에 methods=['POST'] 이렇게 넣어주세요.

GET, POST를 동시에 쓰고 싶다면 methods=['GET', 'POST'] 로 넣어야합니다.
이 경우 함수 안에서 request.method == 'GET' 혹은 request.method == 'POST' 같은 방식으로 구분할 수 있습니다.
"""
# 로그인 폼 전송시 (로그인 처리)
@app.route('/login', methods=['POST'])
def login_post():
	"""
	사용자가 로그인에 사용한 ID, PW 정보를 가지고 와야겠죠?
	HTML 코드에서
	<input ... name="이름">
	이렇게 input 태그를 사용했을 때,
	request.values.get('이름') 으로 해당 input 태그에 입력된 값을 가져올 수 있습니다.
	입력값 이름을 제대로 지정했는지 항상 확인해주세요!
	"""
	user_id = request.values.get('uid')
	user_pw = request.values.get('upw')
	
	# DB 연결 정보 가져오기
	conn = mysql.get_db()
	cursor = conn.cursor()
	
	"""
	DB에 해당 사용자명과 비밀번호로 된 항목이 있는지 질의합니다.
	쿼리문에 %s 를 입력하고, 두번째 인자로 배열을 주면 %s 위치에 순서대로 해당 값이 SQL공격에 안전하게 처리가 된 후 쿼리문이 만들어집니다.
	"""
	cursor.execute('SELECT * FROM users WHERE user_id = %s AND user_pw = %s', [user_id, user_pw])
	row = cursor.fetchone()
	
	"""
	fetchone() 을 했을때 결과가 없다면 None (파이썬에서 null)이 반환됩니다.
	반환된 row가 None 이라면 로그인하려는 계정이 없거나 비밀번호가 틀린거겠죠?
	None 이 아니라면 DB에서 행 정보를 담은 dict 객체가 반환됩니다.
	
	우리는 테이블을
	pk, user_id, user_name, user_pw 4개의 컬럼을 가지게 만들었으니
	row = {
		'pk': 1,
		'user_id': 'admin',
		'user_name': '관리자',
		'user_pw': '1234'
	}
	같은 형태일거에요
	
	row['user_id'] 나 row['user_name'] 같은 형태로 값에 접근할 수 있습니다.
	"""
	if row is None:
		# 로그인 실패
		
		"""
		위에서 언급했듯, html 파일을 불러오면서 html 파일에 값을 넣을 수 있습니다.
		err 변수를 추가해줘서 오류 메시지가 표시되도록 할게요.
		"""
		return render_template('login.html', err=True)
	else:
		# 로그인 성공
		
		"""
		로그인 했다는 정보를 기억하기 위해, 세션에 로그인 정보를 저장합니다.
		
		보통 사용자의 PK나 아이디 같은걸 저장하는데, 지금은 이름만 있으면 되니까 이름만 저장할게요!
		"""
		session['user_name'] = row['user_name']
		
		"""
		로그인에 성공했으니 메인 페이지로 보내줄게요.
		아직 메인페이지를 만들진 않았지만, 바로 아래에서 / 주소에 해당하는 함수를 구현할거에요.
		
		redirect 함수를 사용할 경우 브라우저에게 해당 주소로 이동하라는 HTTP Response를 보내줍니다.
		"""
		return redirect('/')

# 메인페이지
@app.route('/')
def main():
	"""
	로그인이 되어 있다면 세션에 이름이 저장되어 있을 것이고,
	그 이름을 가져와서 html 파일로 보내서 이름을 표시해줄 수 있습니다.
	
	user_name = session.get('user_name', None)
	return render_template('index.html', user_name=user_name)
	
	현재 함수에서 이렇게 작성한 후, index.html에서 jinja 템플릿 문법을 이용하여
	
	{% if user_name %}
		user_name 값이 있는 경우, 즉 로그인이 된 경우
		
	{% else %}
		user_name 값이 없음, 즉 로그인되어 있지 않음
	{% endif %}
	
	이렇게 조건문을 사용하거나
	
	{{ user_name }} 으로 이름을 출력할 수 있습니다.
	
	다만, 이렇게 하려면 세션 값을 가져와서 template 으로 보내주는 과정을
	모든 render_template 을 호출할 때마다 해야하는데, 번거롭겠죠?
	여기선 일단 index.html 파일을 그대로 보내주기만 하고, 아래 함수로 넘어가볼게요
	"""
	return render_template('index.html')


"""
수업시간에 설명해주진 않았지만, @app.context_process 라는 데코레이터가 있습니다.
이 함수는 모든 render_template을 호출할 때 같이 실행되어, template 안에 동일한 변수를 설정해줄 수 있습니다.

우리는 지금 사용자가 로그인 했을 경우 session에 있는 사용자 이름을 template 으로 넘겨줘서,
(1) 로그인 버튼 대신에 로그아웃 버튼 표시
(2) 사용자 이름 표시
등의 작업을 해야합니다.

이를 위해선 render_template를 할때, session에 저장된 변수를 넘겨줘야하는데,
render_template 할 때마다 똑같은 작업을 다 해줘야하는데, 똑같은 코드를 다 복사 붙여넣기 하면 불편하겠죠?
그렇다고 빼먹으면 이미 로그인되어 있는데도 어떤 페이지에서는 로그인이 안된거처럼 보일거에요.

이 함수를 통해 모든 html 파일을 로딩할때 사용자명을 일괄적으로 넣어줄겁니다.
"""
@app.context_processor
def inject_context():
	# 사용자 이름이 있으면 가져오고, 없으면 None 반환
	user_name = session.get('user_name', None)
	return {'user_name': user_name}


"""
로그인과 비슷한 과정으로 회원가입도 만들어볼게요.
"""
# 회원가입 페이지
@app.route('/join')
def join():
	return render_template('join.html')
# 회원가입 페이지에서 폼 전송시
@app.route('/join', methods=['POST'])
def join_post():
	"""
	마찬가지로 join.html 에서 input 태그에 name attribute 를 맞게 설정했는지 확인해야합니다.
	"""
	user_id = request.values.get('uid')
	user_name = request.values.get('uname')
	user_pw = request.values.get('upw')
	
	# DB 연결 정보 가져오기
	conn = mysql.get_db()
	cursor = conn.cursor()
	
	"""
	이미 가입한 아이디인지 먼저 확인을 해서, 가입한 아이디면 오류 표시
	해당 아이디로 이미 가입이 되어있는지 확인해봅니다
	"""
	cursor.execute('SELECT * FROM users WHERE user_id = %s', [user_id])
	row = cursor.fetchone()
	
	if row is not None:
		"""
		row 가 있다면 해당 ID로 가입된 사용자가 있다는 이야기니까, 오류를 표시합니다.
		"""
		return render_template('join.html', err=True)
	
	"""
	INSERT 쿼리로 사용자 정보를 추가해줍니다.
	DB 테이블을
	pk, user_id, user_name, user_pw
	순으로 만들었으니, 그 순서에 맞게 값을 넣으면 됩니다.
	"""
	cursor.execute('INSERT INTO users VALUES (NULL, %s, %s, %s)', [user_id, user_name, user_pw])
	
	"""
	수업시간에 설명했듯, pymysql 패키지는 DB Transaction 이 기본으로 활성화됩니다.
	INSERT, UPDATE, DELETE 등 내용을 수정하는 쿼리를 수행할 경우 commit을 해서 변경사항을 반영해야합니다.
	변경 사항을 취소하고 싶으면 conn.rollback() 을 호출하면 됩니다.
	"""
	conn.commit()
	
	"""
	회원가입이 완료되고 로그인 페이지로 보내줘도 됩니다.
	return redirect('/login')
	이런식으로요.
	
	하지만 회원가입한 김에 바로 로그인 처리까지 할 수도 있겠죠?
	로그인 성공과 동일하게 세션에 값을 넣고 메인페이지로 보내줄게요.
	"""
	session['user_name'] = user_name
	return redirect('/')


@app.route('/logout')
def logout():
	"""
	로그아웃을 위해 세션정보를 지워주겠습니다.
	PPT에 있는 것처럼
	del session['user_name']
	으로 해도 되지만,
	session.clear()
	함수로 모든 세션 정보를 없앨 수도 있습니다.
	"""
	session.clear()
	
	# 로그아웃 후 메인페이지로 이동
	return redirect('/')

@app.route('/intro')
def intro():
	return render_template('intro.html')

@app.route('/guestBook')
def guestBook():
	conn = mysql.get_db()
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM guestbook')
	row = cursor.fetchall()

	if row is None:
		return render_template('guestBook.html', row=False)
	else:
		return render_template('guestBook.html', row=row)

@app.route('/guestBook', methods=['POST'])
def guestBook_post():
	conn = mysql.get_db()
	cursor = conn.cursor()

	user_name = session.get('user_name', None)
	user_content = request.values.get('content')
	nowDate = datetime.now()
	cursor.execute('INSERT INTO guestbook VALUES (NULL, %s, %s, %s)', [user_name,user_content,nowDate])
	conn.commit()
	return redirect('/guestBook')



# 내장 웹서버 실행, 코드의 가장 마지막 줄에 있어야 함
# host='0.0.0.0': 다른 컴퓨터에서도 접속할 수 있도록 설정 / port=5000: 웹 서버를 5000포트에 실행
app.run(host='127.0.0.1', port=5000, debug=True)