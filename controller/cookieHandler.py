from phpserialize import *

def createAndUpdateCookieValue(request):
    isVisited = False
    visitedCookieValue = request.cookies.get('hackers_short_url')

    if visitedCookieValue is None:
        visitedCookieValueList = [
            request.base_url
        ]
        visitedCookieValueSerialized = dumps(visitedCookieValueList)
    else:
        visitedCookieValueList = loads(visitedCookieValue)
        if request.base_url in visitedCookieValueList:
            isVisited = True
        else:
            visitedCookieValueList.append(request.base_url)

        visitedCookieValueSerialized = dumps(visitedCookieValueList)

    return {
        'visitedCookieValueSerialized': visitedCookieValueSerialized,
        'isVisited': isVisited
    }
