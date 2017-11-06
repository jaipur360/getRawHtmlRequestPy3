##### IMP :: Give a URL and it will Return Raw HTML , Headers and Last Modified Date from Headers
##### IMP :: Changes to work with Python 3.4

import requests
from random import randint
import logging
import os
import simplejson as json
# debug(), info(), warning(), error() and critical()
## Modules for Logging

class getRawHtmlRequestPy3:
    """A simple raw html extractor """
    pageLink = None
    pageStatusCode = None
    pageResponseHeader = None
    pageResponseHeaderDate = None
    pageResponseRawHtml = None
    someException = None
    randomUserAgent = None

    def __init__(self, pageLink, urlProxies=None,randomUserAgent = None):
       
        logFile = 'getRawHtmlRequestPy3.log'
        logging.basicConfig(filename=logFile,level=logging.ERROR, format='%(asctime)s %(message)s')
        logging.info('Constructor Started')
        self.pageLink = pageLink
        if not ((randomUserAgent is None) or (randomUserAgent.upper() == 'TRUE') or (randomUserAgent.upper() == 'FALSE')):   
            raise Exception('User: Invalid parameters Passed')
        if (randomUserAgent is None):
            self.randomUserAgent = 1
        elif(randomUserAgent.upper() == 'TRUE'):
            self.randomUserAgent = 1
        else:
            self.randomUserAgent = 0
        #print self.randomUserAgent

        def getRandomUserAgent():
            userAgentList=[
            'Mozilla/4.0 (X11; Linux) KHTML/4.9.1 (like Gecko) Konqueror/4.9',
            'Mozilla/4.0 (X11) KHTML/4.9.1 (like Gecko) Konqueror/4.9',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Deepnet Explorer 1.5.3; Smart 2x2)',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Deepnet Explorer 1.5.3; Smart 2x2; .NET CLR 2.0.50727; .NET CLR 1.1.4322; InfoPath.1)',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; MyIE2; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0)',
            'Mozilla/4.0 (Android 4.1; Linux; Opera Mobi/ADR-1111101157; U; en-US) Presto/2.9.201 Version/12.02',
            'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; Avant Browser; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)',
            'Mozilla/4.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko',
            'Mozilla/4.0 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16',
            'Mozilla/4.0 (compatible; MSIE 7.0; America Online Browser 1.1; Windows NT 5.1; (R1 1.5); .NET CLR 2.0.50727; InfoPath.1)'
            ]
            tmpUserAgent = None
            if self.randomUserAgent == 0:
                tmpUserAgent = userAgentList[0]
            else:
                randomNo = randint(0,9)
                tmpUserAgent = userAgentList[randomNo]
            #print tmpUserAgent
            return (tmpUserAgent)

        # Set Cookies
        cookies = dict(cookies_are='working')

        try:
            headers = {'user-agent': getRandomUserAgent()}
            headersJson = json.dumps(headers)
            r = None
            if(urlProxies is None):
                r = requests.get(self.pageLink, headers=headers)
                #print('Proxy None')
            else:
                r = requests.get(self.pageLink, headers=headers, proxies=urlProxies)
                #print('Proxy Not None')

            # r.request.headers
            # r.headers

            self.pageResponseRawHtml = r.text
            self.pageStatusCode = r.status_code
            self.pageResponseHeader = r.headers
            self.pageResponseHeaderDate = r.headers.get('last-modified', '')

            r.connection.close()
            # print dir(r.headers)
            # print type(r.headers)
            
            #print r.status_code
            #print r.headers
            #print r.headers['last-modified']
            #return unicodeToAscii(r.text)
            #print r.cookies
            #return(self.rawHtml) 
        ### pubDate
        except requests.exceptions.RequestException as e:    # This is the correct syntax
            #print str(e)
            logging.error(str(e))
        logging.info('Constructor Ended')

    def getPageResponseRawHtml(self):
        return(self.pageResponseRawHtml)

    def getPageResponseHeader(self):
        return(self.pageResponseHeader)

    def getPageResponseHeaderDate(self):
        return(self.pageResponseHeaderDate)

    def getPageResponseStatusCode(self):
        return(self.pageStatusCode)

    def getSomeException(self):
        return(self.someException)  

# ### Usage 
# from getRawHtmlRequestPy3 import getRawHtmlRequestPy3
# page = 'https://api.ipify.org/?format=json'
# obj = getRawHtmlRequestPy3(page)

# print(obj.getPageResponseRawHtml())
# print(obj.getPageResponseHeader())
# print(obj.getPageResponseHeaderDate())
# print(obj.getPageResponseStatusCode())
#print(obj.getSomeException())
