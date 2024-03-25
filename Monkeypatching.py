class math:
    def multi(self,a,b):
        return a * b
    
    def add(self,c,d):
        return c + d
    
math.multi = math.add

obj = math()

print(obj.multi(4,5))  