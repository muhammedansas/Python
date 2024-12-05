# /////////// Palindrome \\\\\\\\\\\\\\\\

# a = "malayalam"

# if a == a[::-1]:
#     print("Its Palindrome")
# else:
#     print("not a palindrome")



# //////////// Anagram \\\\\\\\\\\\\\

# a = ["ansas","anssa","sos","jjrr","rrjj","rjrj","jrjr"]

# dic = {}

# for word in a:
#     sorted_word = "".join(sorted(word))
#     if sorted_word in dic:
#         dic[sorted_word].append(word)
#     else:
#         dic[sorted_word] = [word]

# result = list(dic.values())

# print(result)



# /////////////// Sort String Without using sorted method \\\\\\\\\\\\\\\\\\\

# a = "ansas"

# b = list(a)

# for i in range(len(b)):
#     for j in range(len(b)-1):
#         if b[j] > b[j+1]:
#             b[j],b[j+1] = b[j+1],b[j]

# sorted_string = "".join(b)

# print(sorted_string)



# //////////////////// fibinocci \\\\\\\\\\\\\\\\\\\\

# def fibinocci(n):
#     fib = [0,1]
#     if n <=1 :
#         return fib[:n]
#     else:
#         for i in range(2,n):
#             fib.append(fib[-1]+fib[-2])
#     return fib
    
# print(fibinocci(5))



# //////////// Capitalize repeated values in a String \\\\\\\\\\\

# a = "ansas"
# b = ""

# for i in a:
#     if a.count(i) > 1:
#         b += i.upper()
#     else:
#         b += i
        
# print(b)



# /////// Find the count of str values \\\\\\\\

# a = "ansas"

# b = {}

# for i in a:
#     b[i] = a.count(i)
    
# print(b)


