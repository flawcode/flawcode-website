
import smtplib, sqlite3

from email.mime.text import MIMEText
from itsdangerous import URLSafeTimedSerializer

from settings import BASE_URL
from settings import EPISODE_COUNT
from settings import DB_FILENAME
from settings import MAIL_SERVER
from settings import MAIL_PORT
from settings import MAIL_USERNAME
from settings import MAIL_PASSWORD
from settings import SECRET_KEY
from settings import UNSUBSCRIBE_TOKEN_SALT

conn = sqlite3.connect(DB_FILENAME+'.db')

cursor = conn.execute('SELECT email, confirmed FROM user')

serializer = URLSafeTimedSerializer(SECRET_KEY)

epno = str(EPISODE_COUNT)
base_url = BASE_URL

for row in cursor:
	user_email = row[0]
	user_confirmed = bool(row[1])
	token = str(serializer.dumps(user_email, salt=UNSUBSCRIBE_TOKEN_SALT))
	ep_url = base_url + '/episode/show/'+ epno
	remove_url = base_url + '/unsubscribe/' + token
	print('Sending email to', user_email)
	if user_confirmed:
		message_content = """\
		Hello!
		FlawCode has published a new podcast! <a href=\"http://{ep_url}\">Check it out!</a>
		<br><br><hr><br>
		Do not wish to receive updates from FlawCode Podcasts? Please <a href=\"http://{remove_url}\">unsubscribe.</a>
		""".format(ep_url=ep_url, remove_url=remove_url)
		message = MIMEText(message_content, 'html')
		message['From'] = MAIL_USERNAME
		message['To'] = user_email
		message['Subject'] = 'New episode published at FlawCode Podcasts!'
		s = smtplib.SMTP(MAIL_SERVER, MAIL_PORT)		
		s.starttls()
		s.login(MAIL_USERNAME, MAIL_PASSWORD)
		s.sendmail(MAIL_USERNAME, user_email, message.as_string())
		s.quit()
		print('Successful.')
	else:
		print('Failure. User has not verified email address.')
