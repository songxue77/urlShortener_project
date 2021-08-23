from flask import Flask
from flask import render_template
from flask import request
from controller import otherRequestHandler
from controller import validator
from controller import connectionResolver
from controller import urlInfoEntity
from controller import cookieHandler
from controller import urlStatistics
from controller import redirect
import datetime


app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello World!'

@app.errorhandler(404)
def not_found(e):
	return render_template('not_found.html')

@app.route('/favicon.ico')
def faviconRequest():
	return otherRequestHandler.faviconRequest()

@app.route('/robots.txt')
def robotRequeest():
	return otherRequestHandler.robotRequest()

@app.route('/<shortCode>')
def performRedirect(shortCode):
	if validator.validateShortCode(shortCode) == False:
		return render_template('not_found.html')

	if validator.validateShortCodeLength(shortCode) == False:
		return render_template('not_found.html')

	mysqlConnection = connectionResolver.getMysqlConnection()

	urlInfo = urlInfoEntity.find(request.base_url, mysqlConnection)
	if urlInfo is None:
		return render_template('not_found.html')

	if datetime.datetime.now() > urlInfo['ValidEndPeriod']:
		return render_template('expired.html')

	if datetime.datetime.now() < urlInfo['ValidBeginPeriod']:
		return render_template('not_found.html')

	cookieValue = cookieHandler.createAndUpdateCookieValue(request)
	if cookieValue is None:
		return render_template('not_found.html')

	insertResult = urlStatistics.store(mysqlConnection, request, urlInfo, cookieValue, app)

	return redirect.performRedirect(urlInfo, cookieValue)

if __name__ == '__main__':
	app.run(host='0.0.0.0')
	#app.run(debug=True)
