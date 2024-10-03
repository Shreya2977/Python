import re
emails="""
CoreyMScafer@gmail.com
corey.scafer@university.edu
corey-321-scafer@my-work.net
"""
pattern=re.compile(r"[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)")
matches=pattern.finditer(emails)
for match in matches:
    print(match)
