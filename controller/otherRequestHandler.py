import base64
from flask import Response

def faviconRequest():
    bytesValue = "R0lGODlhEAAQAJECAAAAzFZWzP///wAAACH5BAEAAAIALAAAAAAQABAAAAIplI+py+0PUQAgSGoNQFt0LWTVOE6GuX1H6onTVHaW2tEHnJ1YxPc+UwAAOw=="
    response = Response(response=base64.b64decode(bytesValue), status=200, mimetype="application/xml")
    response.headers['Content-Type'] = 'image/gif'
    return response

def robotRequest():
    response = Response(response="User-agent: *\nDisallow:\n", status=200, mimetype="application/xml")
    response.headers['Content-Type'] = 'text/plain; charset=utf-8'
    return response
