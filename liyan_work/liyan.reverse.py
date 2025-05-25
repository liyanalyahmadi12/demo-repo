#declaration
list=[]
copy_list = []

#input
while True:
 
 user_list= input("write your list(and we will reverse it): ")
 if user_list == 'done':
  break
 list.append(user_list)

#process input
copy_list = list [::-1]

#print 
print(copy_list)
print(list)
