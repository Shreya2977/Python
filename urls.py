import re
urls="""
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
"""
pattern=re.compile(r"https?://(www\.)?(\w+)(\.\w+)")
matches=pattern.finditer(urls)
for match in matches:
    print(match.group(2),match.group(3),sep="")
# suburls=pattern.sub(r"\2\3",urls)    #to print the group use backslash\ and thw group no.
# print(suburls)