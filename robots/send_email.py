import smtplib
from email.mime.text import MIMEText
from email.header import Header

# MIMEText 객체로 메일을 생성.
msg = MIMEText('처음으로 보내보는 이메일..크크')

# 제목에 한글이 포함될 경우 Header 객체를 사용.
msg['Subject'] = Header('메일 제목이다..', 'utf-8')
msg['To'] = 'loveskywhy@naver.com'
msg['From'] = 'chkim100617@gmail.com'

"""
이건 안보내짐...ㅠㅠ
# SMTP()의 첫번째 매개변수에 SMTP 서버의 호스트 이름을 지정.
with smtplib.SMTP('localhost') as smtp:
    # 메일을 전송
    smtp.send_message(msg)
"""

# google 계정에서 바온사준이 낮은 앱 허용: 사용안함을 활성화하면 메일을 보낼 수 있다.
# 성공함!!ㅋㅋ신기신기
with smtplib.SMTP_SSL('smtp.gmail.com') as smtp:
    smtp.login('userEmail', 'userPassword')

    smtp.send_message(msg)
