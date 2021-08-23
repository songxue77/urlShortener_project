import re

def validateShortCode(shortCode):
    result = False
    regExp = re.compile('^([a-zA-Z0-9]+)$')

    if regExp.match(shortCode):
        result = True

    return result

def validateShortCodeLength(shortCode):
    result = False

    if len(shortCode) == 6:
        result = True

    return result

