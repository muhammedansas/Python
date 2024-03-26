# find the odd number:
# /////////////////////////
# a = [1,2,3,4,5]
# odd = [x for x in a if x%2 == 1]
# print(odd)


# get the square of elements:
# /////////////////////////////
# a = [1,2,3,4,5]
# sqr = [x **2 for x in a]
# print(sqr)

# get string:
# //////////////////////////////
# string = [x for x in "ansas"]
# print(string)



fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
new=[x.capitalize() for x in fruits]
print(new)
