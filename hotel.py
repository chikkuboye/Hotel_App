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
        dates = input('Enter the date in the form of yyyy-mm-d : ')
        
        count = 0
        for i in l:
           count = count + i

        amount = count
        # #print(f'Total amount {count} ') 
        sql = "INSERT INTO `items`(`Name`, `Phone_number`, `Date_`, `Total_Amount`) VALUES (%s,%s,%s,%s)"
        data = (name,phone,dates,amount)
        mycursor.execute(sql,data)
        mydb.commit()
        print('Thank you Welcome to next time ')
        break
    