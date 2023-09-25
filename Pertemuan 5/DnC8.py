def longestCommonPrefix(a):
     size = len(a)
     
     # If size is 0, return empty string
     if(size == 0):
          return ""
     # Sort the array of strings
     a.sort()
     # Find the minimum length from
     # First and last string
     end = min(len(a[0]), len(a[size-1]))

     # Find the common prefix between
     # The first and last string
     i = 0
     while(i < end and a[0][i] == a[size-1][i]):
          i = i + 1

     pre = a[0][0:i]
     return pre

arr = ["nasipadang","nasigoreng", "nasinasian", "nasirih"]
result = longestCommonPrefix(arr)
print(result,"\n")

arr = ["apple", "ape", "april"]
result = longestCommonPrefix(arr)
print(result)
