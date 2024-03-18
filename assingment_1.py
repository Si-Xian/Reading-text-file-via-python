#Using formating to form certain spaces.
def List():
	print("{0:13s}{1:20s}{2:5s}{3:10s}{4:7s}{5:5s}{6:20s}{7:20s}".format("Item Number","Item Name","Size","Brand","Price","Qty","Supplier","Contact"))
	with open("D:/Python/ass_pyython/assg.txt",'r') as file :
		for line in file :
			Item_Number,Item_Name,Size,Brand,Price,Qty,Supplier,Contact = line.split(',')
			print("{0:13s}{1:20s}{2:5s}{3:10s}{4:7s}{5:5s}{6:20s}{7:20s}".format(Item_Number,Item_Name,Size,Brand,Price,Qty,Supplier,Contact))

#use line num to control amount of "no result " printed .
def SrcByINum():
	line_number=0
	INumS = input("Search record by item number:")
	print("{0:13s}{1:20s}{2:5s}{3:10s}{4:7s}{5:5s}{6:20s}{7:20s}".format("Item Number","Item Name","Size","Brand","Price","Qty","Supplier","Contact"))
	with open("D:/Python/ass_pyython/assg.txt",'r') as file :
		for line in file:
			line_number +=1
			Item_Number,Item_Name,Size,Brand,Price,Qty,Supplier,Contact = line.split(',')
			if INumS == Item_Number:
				print("{0:13s}{1:20s}{2:5s}{3:10s}{4:7s}{5:5s}{6:20s}{7:20s}".format(Item_Number,Item_Name,Size,Brand,Price,Qty,Supplier,Contact))
				break
			elif line_number<20:
				continue
			else:
				print("No result,only from 12300 to 12319")

#The any() part is checked ,if Kw is a substring in some row ,it will return true 1 time only for that row.
def SrcByKW():
	chk=False
	line_number=0
	Kw=input("Search record by keyword:")
	with open("D:/Python/ass_pyython/assg.txt",'r') as file :
		for line in file:
			line_number +=1
			Item_Number,Item_Name,Size,Brand,Price,Qty,Supplier,Contact = line.split(',')
			if any(Kw.lower() in x.lower() for x in line.split(',')):
				print("{0:13s}{1:20s}{2:5s}{3:10s}{4:7s}{5:5s}{6:20s}{7:20s}".format(Item_Number,Item_Name,Size,Brand,Price,Qty,Supplier,Contact))
				chk=True
			elif line_number<20:
				continue
			elif chk==False:
				print("No result")

def ShowLI():
	print("{0:13s}{1:20s}{2:5s}{3:10s}{4:7s}{5:5s}{6:20s}{7:20s}".format("Item Number","Item Name","Size","Brand","Price","Qty","Supplier","Contact"))
	with open("D:/Python/ass_pyython/assg.txt",'r') as file :
		for line in file:
			Item_Number,Item_Name,Size,Brand,Price,Qty,Supplier,Contact = line.split(',')
			if int(line.split(',')[5])<10:
				print("{0:13s}{1:20s}{2:5s}{3:10s}{4:7s}{5:5s}{6:20s}{7:20s}".format(Item_Number,Item_Name,Size,Brand,Price,Qty,Supplier,Contact))

def Update():
	line_number=0
	INumS = input("Type your item number:")		
	with open("D:/Python/ass_pyython/assg.txt",'r') as file :
		for line in file:			
			line_number+=1
			Item_Number,Item_Name,Size,Brand,Price,Qty,Supplier,Contact = line.split(',')
			if INumS ==  line.split(',')[0]:
				lineToEdit=line_number-1
				Item_Name=input("Enter new item name:")
				Size=input("Enter new size:")
				Brand=input("Enter new brand:")
				Price=input("Enter new Price:")
				Qty=input("Enter new qty:")
				Supplier=input("Enter new Supplier:")
				Contact=input("Enter new Contact:")
		
				with open ("D:/Python/ass_pyython/assg.txt",'r') as file :
					lines=file.readlines()
				a=str(Item_Number) +','+str(Item_Name)+','+str(Size)+','+str(Brand)+','+str(Price)+','+str(Qty)+','+str(Supplier)+','+str(Contact)+'\n'
				lines[lineToEdit]=str(a)
				with open ("D:/Python/ass_pyython/assg.txt",'w') as file:
					for line in lines:
						file.write(line)

def Add():
	Item_Number=input("Enter new item number:")
	Item_Name=input("Enter new item name:")
	Size=input("Enter new size:")
	Brand=input("Enter new brand:")
	Price=input("Enter new Price:")
	Qty=input("Enter new qty:")
	Supplier=input("Enter new Supplier:")
	Contact=input("Enter new Contact:")
	with open("D:/Python/ass_pyython/assg.txt",'a') as file:
		file.write(Item_Number+","+Item_Name+","+Size+","+Brand+","+Price+","+Qty+","+Supplier+","+Contact)
		
#readlines from a list with each row as an item in the list,
def Delete():
	Item_Num=input("Enter the item number to delete:")
	with open("D:/Python/ass_pyython/assg.txt",'r') as file:
		lines = file.readlines()
#if Item Num not in Item Number,the line will be written back ,the specific line will be deleted 	
	with open("D:/Python/ass_pyython/assg.txt",'w') as file:
		for line in lines:
			Item_Number,Item_Name,Size,Brand,Price,Qty,Supplier,Contact = line.split(',')
			if Item_Num.strip() not in Item_Number.strip():
				file.write(line)

#The program will be stopped 
def Exit():
	
	print("All changes have been made.")
	quit()


#The main func will display options for the user,chk is used to alter the decision of user.
def main():
	
	chk = True
	while chk:	
		print("****************************************")
		print("1.Display list of records              *")	
		print("2.Search by item number                *")
		print("3.Search by keyword                    *")
		print("4.Show low inventories                 *")
		print("5.Update the record                    *")
		print("6.Add a new record to list             *")
		print("7.Delete record from list              *")
		print("8.Exit the program.                    *")
		print("****************************************")
	
		option = input("Enter an option,1 to 8.")
		if option=="1":
			List()
		elif option=="2":
			SrcByINum()
		elif option=="3":
			SrcByKW()
		elif option=="4":
			ShowLI()
		elif option=="5":
			Update()
		elif option=="6":
			Add()
		elif option=="7":
			Delete()
		elif option=="8":
			Exit()
		else:
			print("Not Valid option")
		
		repeat = input("Continue? (y/n)")
		if repeat.lower() =='n':
			chk = False
#Call the function 
if __name__=='__main__':
    main()
