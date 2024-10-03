import re
text=""" 123-456-7890
123.456.7890
Mr. Schwann
Mr Sooo
Ms Pooo
Mrs Goo
Mr. T"""
# pattern=re.compile(r"\d\d\d[-.]\d\d\d[-.]\d\d\d\d")
# pattern=re.compile(r"(\d){3}[-.](\d){3}[-.](\d){4}")
# pattern=re.compile(r"\d{3}[-.]\d{3}[-.]\d{4}")
pattern=re.compile(r"(Mr|Ms|Mrs)\.?\s[A-Z]\w*")
matches=pattern.finditer(text)
for match in matches:
    print(match)
