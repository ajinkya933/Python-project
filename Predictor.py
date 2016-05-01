from collections import Counter
cnt = Counter ()

for line in open ('pos-neg-semantics.txt', 'r'):
  for word in line.split ():
    cnt [word] += 1

print (cnt)


print(cnt['pos'])
print(cnt['neg'])

a=cnt['pos']
b=cnt['neg']
c=a+b

d=(b/c)*100
print(d)
e=(a/c)*100
print(e)

if(d>70):

        print ("Predicted to be highly succesful")

elif(d<=70):

        print("Predicted to be moderate")


else:
        print("going to be failure in box office")



