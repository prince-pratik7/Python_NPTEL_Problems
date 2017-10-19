def exception():
    while(True):
        try:
            userdata=print("Enter a Number\n")
            usernum=int(userdata)
        except ValueError:
            print("Not a number.Try Again")
        else:
            break
        
