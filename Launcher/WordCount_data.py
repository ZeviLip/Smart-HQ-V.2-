#Takes site input from user 
test_string = input("Type document: ")
#Reprints user input 
print ("The original string is : " +  test_string) 
#calculates length in words of users using len() command and .split() configuration
res = len(test_string.split())
#Prints final outcome
print ("The number of words in string are : " +  str(res))


