n = int(input())
patients=[]
for i in range(n):
    x=int(input())
    patients.append(x)
if 9 in patients:
    first_nine_index= patients.index(9)
    patients[first_nine_index]="urgent"
if len(patients)>0 and patients[-1]==9:
    patients[-1]="emergency"
if "urgent" in patients:
    first_nine_index= patients.index("urgent")
    for i in range(first_nine_index):
        patients[i]+=5
print(patients)
