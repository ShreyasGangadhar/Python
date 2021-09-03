letter= '''Dear, <|Name|> \n You are selected \n <|date|> '''
name = input("enter your name\n")
date = input("enter date\n") 
letter= letter.replace('<|Name|>',name)
letter= letter.replace('<|date|>',date)          
print(letter)