import datetime
import geoip2.database
from geoip2.errors import AddressNotFoundError


def store(mysqlConnection, request, urlInfo, cookieValue, app):
    cursor = mysqlConnection.cursor()

    if cookieValue['isVisited'] == True:
        sql = "INSERT INTO url_re_stat(TargetURL, VisitDatetime, Platform, Route, Country, Device, Browser)values (%s, %s, %s, %s, %s, %s, %s)"
    else:
        sql = "INSERT INTO url_new_stat(TargetURL, VisitDatetime, Platform, Route, Country, Device, Browser)values (%s, %s, %s, %s, %s, %s, %s)"

    targetURL = urlInfo['TargetURL']
    VisitDatetime = datetime.datetime.now()

    httpReferrer = request.referrer
    if httpReferrer:
        platform = checkPlatform(httpReferrer)
    else:
        platform = '기타'

    if httpReferrer is None:
        route = ''
    else:
        route = httpReferrer

    ip = request.remote_addr
    country = checkCountry(ip, app)

    userAgent = request.user_agent
    device = getDevice(userAgent)
    browser = getBrowser(userAgent)

    cursor.execute(sql, (targetURL, VisitDatetime, platform, route, country, device, browser))
    mysqlConnection.commit()
    mysqlConnection.close()

    return True

def checkPlatform(referer):
    platform = '기타'
    platformList = {
        'youtube.com' : 'youtube',
        'google.com' : 'google',
        'naver.com' : 'naver',
        'facebook.com' : 'facebook',
        'kakao.com' : 'kakao',
        'daum.net' : 'daum',
        'instagram.com' : 'instagram',
        'twitter.com' : 'twitter'
    }

    for key, value in platformList.items():
        if referer.contains(key):
            platform = value
            break

    return platform

def checkCountry(ip, app):
    try:
        with geoip2.database.Reader(app.root_path+'/geoip.mmdb') as reader:
            response = reader.city(ip)
            country = response.country.iso_code
    except AddressNotFoundError:
        country = ''

    return country

def getDevice(userAgent):
    return userAgent.platform

def getBrowser(userAgent):
    return userAgent.browser
