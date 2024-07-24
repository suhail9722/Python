
from collections  import  OrderedDict

list_with_duplicates = [1,1,1,1,2,2,2,3,3,3,3,4,4,5]

#1 First approch is using set fucntion bcz set does not contains duplicate values.
#new_list=list(set(list_with_duplicates))
#print(new_list)

#2 Remove duplicates from the list using list comprehension

print("The Original List with duplicates",list_with_duplicates)

#create an empty list
#res = []
#now we are comprehneding each elements
#[res.append(x) for x in list_with_duplicates if x not in res]

# print the list after removing the duplicates.
#print("The list after the removing the duplicates",res)

#3. using collections.OrderedDict.fromkeys()
#res = list(OrderedDict.fromkeys(list_with_duplicates))
#print("The list after removing Duplicates: "+str(res))

#Using in and not in operators

res = []

for i in list_with_duplicates:
    if i not in res:
        res.append(i)

print("List After removing the ",res)






