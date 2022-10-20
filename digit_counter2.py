def digit_count(num):
    num_str = str(num)
    s=[]
    for i in range(10):
        s.append(num_str.count(str(i)))
    s.append(sum(s))
    x = num_str.rstrip("0")
    s.append(len(num_str) - len(x))
    s.append(num)
    return s
num = int(input("inter your number: "))
s= digit_count(num)
for l in range (10):    
       print("score of digit",l,"is",s[l])  
print("score of all digit is",s[10])
print(num,"= X * 10^",s[11]) 
print(".............................................")
