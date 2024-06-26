word = input().strip()
vowels = "aeiou"
result = 0
for ch in word:
   if ch in vowels:
       result += 1
print(result)