def sleep_time():
    sleep = input('Do you want to go to sleep yes/no ?: ')
    if sleep == 'yes':
        print('Have a good sleep')
    elif sleep == "no":
        print('Keep studying Python')
    else:
        print('Must be yes or no')
    
sleep_time()
