try:
    import calendar as cal
    year=int(input("Enter the year:  "))
    month=int(input("Enter the month:  ")) 
    print("\n" + "="*30)
    print(cal.month(year,month))
    print("\n" + "="*30)
except:
    print("💔 Please enter only interger! 😔")    