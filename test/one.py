# UniqueChar Problem

def uniquechar(string):           
        print("the input string from user is" + string)        
        index=[string.index(i) for i in string if string.count(i) == 1]
        print(min(index),222)
        return min(index) if len(index) > 0 else -1
 
 
# 1) test Case Pass
# input_string = "abcdcaf" 
# output: The repeated Character is b 
####### 

# 2) test Case Fail
# input_string = "abcdefgij"
# output: There is no repeating character in the given input string a

input_string = input("Enter the character : ")
index = uniquechar(input_string)
if index==1:
    print ("The repeated Character is" + input_string[index])
else:
    print("There is no repeating character in the given input string " + input_string[index])