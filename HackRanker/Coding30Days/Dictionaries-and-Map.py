# phone={}
# n=int(input())
# for i in range(0,n):
#     name=str(input())
#     phone[name]=str(input())
# for i in range(0,n):
#     name=str(input())
#     re=phone.get(name,"none")
#     if re!="none":
#         print("%s=%s"%(name,re))
#     else:
#         print("Not found")

n=input()
dic={}
for i in range(int(n)):
    a=input()
    b=input()
    dic[a]=b
k=input()
while(k!=" " and k!=""):
    if(k in dic):
        print (k+"="+(dic[k]))
    else:
        print ("Not found")
    k=input()