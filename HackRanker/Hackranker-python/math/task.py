# def insertionSort(A):
#     for i in range(1,len(A)):
#         j=i-1
#         while A[j]>A[j+1] and j>=0:
#             A[j],A[j+1]=A[j+1],A[j]
#             j-=1
#     return A
# def sortingA(lst):
#     lst1=[]
#     lst2=[]
#     lst5=[]
#
#     for x in lst:
#         if x%2==0:
#             lst1.append(x)
#         else:
#             lst2.append(x)
#     lst3=insertionSort(lst1)
#     lst5.extend(lst3)
#     lst4=insertionSort(lst2)
#     lst5.extend(lst4)
#     return lst5
# lst=[1,1,2,2,3,4,5,6]
# A=[]
# for x in lst:
#     if x not in A:
#         A.append(x)
# print(sortingA(A))
#
# s= 'narendra'
# n='surendra'
# z=''
# if len(s)==len(n):
#     for x in range(len(s)):
#         z=z+n[x]+s[x]
# elif len(s)>len(n):
#     for x in range(len(s)):
#         z = z + n[x] + s[x]
# else:
#     for x in range(len(n)):
#         z=z+n[x]+s[x]
# print(z)

