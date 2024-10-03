with open("this.txt","r") as f:
    content1=f.read()

with open("this_copy.txt","r") as f:
    content2=f.read()

if (content1==content2):
    print("yes they are identical")
else:
    print("they are not identical")