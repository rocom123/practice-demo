x=int(input())
if x%3==0 and x%5==0 and x%7==0:
    print(3,5,7)
elif x%3==0 and x%5==0:
    print(3,5)
elif x%3==0 and x%7==0:
    print (3,7)
elif x%5==0 and x%7==0:
    print (5,7)
elif x%3==0:
    print (3)
elif x%5==0:
    print (5)
elif x%7==0:
    print (7)
else:
    print ("n")
