import re
chrfiles = [ '9', '10', '1', '3', '11' ]
chrfiles.sort(key = lambda x:int(re.match('(\d+)',x).group(1)))
print chrfiles
