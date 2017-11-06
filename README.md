# getRawHtmlRequestPy3
Python Requests usage to generate random user agent and cookies

# ### Usage

from getRawHtmlRequestPy3 import getRawHtmlRequestPy3

page = 'https://api.ipify.org/?format=json'

obj = getRawHtmlRequestPy3(page)

# Print Results

print(obj.getPageResponseRawHtml())

print(obj.getPageResponseHeader())

print(obj.getPageResponseHeaderDate())

print(obj.getPageResponseStatusCode())

print(obj.getSomeException())
