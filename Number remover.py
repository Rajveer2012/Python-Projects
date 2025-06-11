a = {1,2,3,4,5,6,7}

while True:
    print('\n')
    print (a)
    
    e = int(input('Enter a number which you want to remove:'))

    if  e in a:
    
        (a.discard(e))
        print('Your choosen number is:' ,e) 
        print('The updated list is:',a)
        print('\nIf you want to continue press 1, else press 0')
        choice = int(input('Enter your choice:'))
        print('\n')
        if choice == 0:
            break
    
    else: 
        
        print('Your choosen number is:' ,e)
        print(' The number is not in the set')




 


                                   

        
















        