#import sys
#sys.path.append('../piplib')

from flask import make_response, redirect

def performRedirect(urlInfo, cookieValue):
    response = make_response(redirect(urlInfo['SourceURL']))
    response.set_cookie('hackers_short_url', cookieValue['visitedCookieValueSerialized'], 86400)

    return response
