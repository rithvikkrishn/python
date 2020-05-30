name=input("enter ur  name:")
mathsmark=int(input("enter ur mathsmark:"))
sciencemark=int(input("enter ur sciencemark:"))
socialmark=int(input("enter ur socialmark:"))
englishmark=int(input("enter ur englishmark:"))
tamilmark=int(input("enter ur tamilmark:"))
total=int(mathsmark)+int(sciencemark)+int(socialmark)+int(englishmark)+int(tamilmark)
avg=(total/5)*100
per=((total/500)*100)
print("=============================================student mark sheet=================================================")
print("the student name is :",name)

print("the mathsmark is :",mathsmark)
print("the sciencemark is :",sciencemark) 	
print("the socialmark is :",socialmark)
print("the englishmark is :",englishmark)
print("the tamilmark is :",tamilmark)
print("the mark of all subjects is :",total)
print("the avg mark is",avg)
if ((mathsmark>=35) and (sciencemark>=35) and (socialmark>=35) and (englishmark>=35) and (tamilmark>=35)):
	print("the student is pass")
else:
	print("the student is fail")

if((avg>=70)):
	print("the avg is good")
else:
	print("th avg is bad")
print("the percentage=",per)
if(per>=90):
	print("grade=a")
elif(per>=80):
	print("grade=b")
elif(per>=70):
	print("grade=c")
elif(per>=60):
	print("grade=d")
elif(per>=40):
	print("grade=e")
else:
		print("fail")