fo = open("hello.txt","r+")
str = fo.read(100);
vowels = 0
consonants=0
count=0
count1=0
for g in str:
    if (g.isnumeric()):
        count1=count1+1
for t in str:
    if(t.isspace()):
        count=count+1
for i in str:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
        vowels = vowels + 1
    else:
        consonants = consonants + 1
 
print("Total Number of Vowels in this String = ", vowels)
print("the String is : ", str)
print("The number of blank spaces is: ",count)
print("the numberic number is : ",count1)
fo.close()