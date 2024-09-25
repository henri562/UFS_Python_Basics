def check_username(username):
    if len(username) < 5:
        return 'Too short'
    if len(username) > 10:
        return 'Too long'

    first_ok = False
    if 'A' <= username[0] <= 'Z':
        first_ok = True
    if first_ok == False:
        return 'First character not uppercase'

    has_lowercase = False
    for char in username:
        if 'a' <= char <= 'z':
            has_lowercase = True
    if has_lowercase == False:
        return 'Must have a lowercase letter'
    return True


username = input('Please enter your requested username: ')
result = check_username(username)
if result == True:
    print('Username is valid')
else:
    print(result)
