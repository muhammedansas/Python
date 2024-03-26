# Dictionary:
    #   dictionary is a collection of key : value pairs data
    #   dictionary is ordered,changeble and do not allow duplicates

# dic = {
#     "name":"ansas",
#     "age":21,
#     "place":"olavanna"
# }
# print(dic.get("class","not a key"))
# print(dic)

# dictionary comprehension:
# ///////////////////////////

# d = [1,2,3,4,5]
# new_d = {x:x **2 for x in d}
# print(new_d)

# expected output: {1:1,2:4,3:9,4:16,5:25}

# /////////////////////////////////////////

# add key value pairs without using update():

# a = {"name":"ansas","age":21}
# a["color"] = "red"
# print(a)

# with using update():

# a = {"name":"ansas","age":21}
# a.update({"color":"red"})
# print(a) 

# ///////////////////////////////////////////////

# loop in dictionary:
# ///////////////////////////////////////////
# get the all keys in a dictionary:

# a = {"name":"ansas","age":21,"place":"olavanna"}
# for x in a:                                           
#     print(x)


# get the all values in a dictionary:

# a = {"name":"ansas","age":21,"place":"olavanna"}
# for x in a:                                             
#     print(a[x])


# get keys and values in a dictionary using items():

# a = {"name":"ansas","age":21,"place":"olavanna"}
# for x,y in a.items():                                             
#     print(x,y)

# /////////////////////////////////////////////////////////

# nested dictionaries:
# ////////////////////////////////////

# dictinary = {"child1":{
#     "name":"ansas",
#     "age" : 21,
#     "place" : "olavanna"

# },"child2":{
#     "name":"vignesh",
#     "age":21,
#     "place":"wertyui"
# }}

# print(dictinary["child1"]["name"])

# /////////////////////////////////////////////




