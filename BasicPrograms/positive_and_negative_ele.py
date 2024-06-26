l = list(map(int, input().split()))
positive, negative = 0, 0 
for ele in l:
    if ele > 0:
        positive += 1 
    elif ele < 0:
        negative += 1 
        
print(positive, negative)