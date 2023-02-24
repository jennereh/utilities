import re

def parseCitekey(strToParse):
  regex = re.compile(r'(?P<name>[a-zA-Z]+)(?P<year>[0-9]+)(?P<title>\w+)')
  res = regex.search(strToParse)
  return res


# test
testStr = "doe2020dancingdark"
result = parseCitekey(testStr)
print(result.groupdict())


