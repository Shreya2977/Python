p1="Make lots of money"
p2="buy now"
p3="subscribe this"
p4="click this"
message=input("Enter your comment:")
if (p1 in message) or (p2 in message) or(p3 in message) or (p4 in message):
    print("this is spam")
else:
    print("this is not a spam")