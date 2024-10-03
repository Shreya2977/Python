import re
text=""" 123-456-7890
123.456.7890
900-456-7890
800-456-7890
stfbtgyjh
gfgvk
ASDGF
Assjjkdh
Bjdjfrdj
cat
pat mat bat
"""
# pattern=re.compile(r"[89]00[-.]\d\d\d[-.]\d\d\d\d")
pattern=re.compile(r"[^b]at")
matches=pattern.finditer(text)
for match in matches:
    print(match)