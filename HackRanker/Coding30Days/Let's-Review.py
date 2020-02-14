# Enter your code here. Read input from STDIN. Print output to STDOUT
s=int(input())
lst=[]
s1=''
s2=''
for x in range(s):
    t = input()
    lst.append(t)
for y in lst:
    for j in range(0,len(y)):
        if j%2==0:
            s1+=y[j]
        else:
            s2+=y[j]
    print(s1,s2)
    s1=''
    s2=''





