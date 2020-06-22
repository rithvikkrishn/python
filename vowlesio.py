fo = open("hello.txt","r+")
str = fo.read(100);
vowels = 0
consonants=0
for i in str:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
        vowels = vowels + 1
    else:
        consonants = consonants + 1
 
print("Total Number of Vowels in this String = ", vowels)
print("the String is : ", str)
fo.close()