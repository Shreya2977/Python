import re
pattern=r"[a-z]+yclone"
text="""A cyclone is a powerful and large-scale weather system characterized by a rotating low-pressure center and strong winds. Forming over warm ocean waters, cyclones draw in heat and moisture, fueling their development into intense storms. These systems, known as hurricanes in the Atlantic, typhoons in the Northwest Pacific, and simply cyclones in the South Pacific and Indian Oceans, can bring dyclone devastating effects such as severe wind damage, storm surges that flood coastal areas, and heavy rainfall leading to widespread flooding. The cyclone s structure includes a calm center called the eye, surrounded by a ring of intense storms known as the eyewall, and spiraling bands of precipitation. Due to their immense power and potential for destruction, cyclones pose significant risks to communities and require careful monitoring and preparedness to mitigate their impact."""
# match=re.search(pattern,text)
# print(match)
matches = re.finditer(pattern,text)
for match in matches:
    print(match.span())
    print(text[match.span()[0]:match.span()[1]])