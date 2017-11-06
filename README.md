# getRawHtmlRequestPy3
Python Requests usage to generate random user agent and cookies\n

# ### Usage \n

from getRawHtmlRequestPy3 import getRawHtmlRequestPy3\n
page = 'https://api.ipify.org/?format=json'
obj = getRawHtmlRequestPy3(page)\n

# Print Results\n
print(obj.getPageResponseRawHtml())\n
print(obj.getPageResponseHeader())\n
print(obj.getPageResponseHeaderDate())\n
print(obj.getPageResponseStatusCode())\n
print(obj.getSomeException())\n
