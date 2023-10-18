def sleep_time(sleep):

    if sleep == 'yes':
        print('Have a good sleep.')
    elif sleep == "no":
        print('Keep studying Python.')
    else:
        print('Must be yes or no.')
    
answer=input('Do you want to go to sleep? yes/no ')
sleep_time(answer)
