import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from beautifultable import BeautifulTable

#adding users to database
def add_user(fname,lname,num,mydb):
	try:
		sql_insert_query = """ INSERT INTO `users` (`firstname`, `lastname`, `contactnumber`) VALUES (%s,%s,%s)"""
		mycursor = mydb.cursor()
		result  = mycursor.execute(sql_insert_query,(fname,lname,num))
		mydb.commit()
		print(fname + " is added successfully!")
	except mysql.connector.Error as error :
		connection.rollback() #rollback if any exception occured
		print(fname + " is fail to add record!{}".format(error))
	pass

#Show data list on table
def view_user(mydb,mycursor):
	print("\t\tView Data")
	mycursor.execute("SELECT * FROM users")
	myresult = mycursor.fetchall()
	table = BeautifulTable()
	table.column_headers = ["ID", "Firstname", "Lastname", "Contact Number"]
	for row in myresult:
		table.append_row(row)
	print(table)
	pass

#delete data on database
def delete_user(row,mydb,mycursor):
	mycursor = mydb.cursor()
	sql = """ SELECT count(*) FROM users WHERE id=%s"""
	result = mycursor.execute(sql,(row,))
	myresult = mycursor.fetchone()
	if myresult[0] == 1:
		mycursor = mydb.cursor()
		sql = """ DELETE FROM users WHERE id=%s """
		mycursor.execute(sql,(row,))
		mydb.commit()
		print("Record(s) deleted")
	else:
		print("No record(s) found!")
	pass

#update data
def update_user(row,num,mydb,mycursor):
	if num == 1:
		fname = raw_input("Enter firstname : ")
		data = (fname,row)
		sql = """ UPDATE users  SET firstname=%s WHERE id=%s """
		mycursor = mydb.cursor()
		mycursor.execute(sql,data)
		mydb.commit()
		print("Firstname is successfully updated!")
	elif num == 2:
		lname = raw_input("Enter lastname : ")
		data = (lname,row)
		sql = """ UPDATE users SET lastname=%s WHERE id=%s """
		mycursor = mydb.cursor()
		mycursor.execute(sql, data)
		mydb.commit()
		print("Lastname is successfully updated!")
	elif num == 3:
		number = input("Enter Phone number : ")
		data = (number,row)
		sql = """ UPDATE users SET contactnumber=%s WHERE id=%s """
		mycursor = mydb.cursor()
		mycursor.execute(sql, data)
		mydb.commit()
		print("Contact number is successfully updated!")
	else:
		print("Invalid choice!")
#main code
def main(): 
	while True:
		mydb = mysql.connector.connect(
			user='roncajan', 
			password='kagebunshin1',
			host='localhost',
			database='Celebrity');

		print("\n\tCRUD in Python")
		print("[1] - Add")
		print("[2] - View")
		print("[3] - Update")
		print("[4] - Delete")
		print("[5] - Exit")
		choice = input("Enter number :")
	
		if choice == 1:
			print("Add User")
			fname = raw_input("Enter firstname : ")
			lname = raw_input("Enter lastname : ")
			num = raw_input("Enter phonenumber : ")
			add_user(fname = fname,lname = lname,num = num, mydb = mydb)
		elif choice == 2:
			mycursor = mydb.cursor()
			view_user(mydb = mydb, mycursor = mycursor)
		elif choice == 3:
			mycursor = mydb.cursor()
			view_user(mydb = mydb, mycursor = mycursor)
			row = raw_input("Enter ID number to update : ")
			mycursor = mydb.cursor()
			sql = """ SELECT count(*) FROM users WHERE id=%s"""
			result = mycursor.execute(sql,(row,))
			myresult = mycursor.fetchone()
			if myresult[0] == 1:
				print("Choices for update!\n")
				print("[1]-Firstname [2]-Lastname [3]-ContactNumber")
				num1 = input("Enter number : ")
				if num1 == 1 or 2 or 3:
					update_user(row = row, num = num1, mydb = mydb,mycursor = mycursor)
				else:
					print("Invalid choice!")
			else:
				print("No record(s) found!")

		elif choice == 4:
			mycursor = mydb.cursor()
			view_user(mydb = mydb, mycursor = mycursor)
			row = input("Enter id to delete : ",)
			delete_user(row = row, mydb = mydb, mycursor = mycursor)
		elif choice == 5:
			print("Thank you for using!")
			break
		else:
			print("Invalid choice!")
	pass

if __name__ == '__main__':
	main()