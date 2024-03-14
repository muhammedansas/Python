
"""
njfnjvnmfvjnjdm         : #this one is module documentation
"""
def main(x):
    return x * 2

message = "ansas"

def key_generator(x):
    keywords = 0
    for i in x:
        keywords = keywords + ord(i)
    return keywords
if __name__ == "__main__":
    print("the secret code of apple:")
    print(key_generator("apple"))    


