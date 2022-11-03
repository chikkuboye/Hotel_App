import mysql.connector

mydb = mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'hotel_db')

mycursor = mydb.cursor()
l = []
while True:
    print('''
        Item contain in the hotel
        1 .coffee
        2 .Tea
        3 .Chips
        4 .Biscuit
        5 .Chocolate
        6 .Billing
        7 .view all transaction
        8 .Day wise transaction summary
        9 .transaction summary for a period
        10 .Exit
    ''')
    choice = int(input('Enter the item you need from the display part : '))
    
    if(choice == 1):
        print('You had selected coffee')
        price = 15
        qua = int(input('Enter the quantity you need : '))
        total_price = price * qua
        l.append(total_price)
    elif(choice == 2):
        print('You had selected Tea')
        price = 10
        qua = int(input('Enter the quantity you need : '))
        total_price = price * qua
        l.append(total_price)
    elif(choice == 3):
        print('You had selected Chips')
        price = 30
        qua = int(input('Enter the quantity you need : '))
        total_price = price * qua
        l.append(total_price)
    elif(choice == 4):
        print('You had selected Biscuit')
        price = 50
        qua = int(input('Enter the quantity you need : '))
        total_price = price * qua
        l.append(total_price)
    elif(choice == 5):
        print('You had selected Chocolate')
        price = 18
        qua = int(input('Enter the quantity you need : '))
        total_price = price * qua
        #print(total_price)
        l.append(total_price)
        #print(l)
    elif(choice == 6):
        print('You enter into billing section')
        name = input('Enter the name : ')
        phone = input('Enter the phone number : ')
        #dates = input('Enter the date in the form of yyyy-mm-d : ')
        l1 = []
        l1.extend(l)
        count = 0
        for i in l1:
           count = count + i
           l.remove(i)
        amount = count
        # #print(f'Total amount {count} ') 
        sql = "INSERT INTO `items`(`Name`, `Phone_number`, `Date_`,`Total_Amount`) VALUES (%s,%s,now(),%s)"
        data = (name,phone,amount)
        mycursor.execute(sql,data)
        mydb.commit()
        print('Thank you Welcome to next time ')
    elif(choice == 7):
        print('Display the transaction details')
        date = input('Enter the date where you need the transaction details (yyyy-mm-d) : ')
        sql = "SELECT * FROM `items` WHERE `Date_`='"+date+"'"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print(result)
    elif(choice == 8):
        print('Display the transaction of particular day')
    elif(choice == 9):
        print('transaction summary for a period')
    elif(choice == 10):
        break
    