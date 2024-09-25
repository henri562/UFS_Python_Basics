a = int(input('How many hours did you sleep last night? '))
b = input('How many hours did you sleep two nights ago? ')
c = input('How many hours did you sleep three nights ago? ')


def sleep(a, b, c):
    total = int(a) + int(b) + int(c)
    average = total / 3
    if average < 5:
        statement = 'You slept %d hours over the last three nights an average of %.2f hours which is below the minimum.' % (
        total, average)
    elif average == 5:
        statement = 'You slept %d hours over the last three nights an average of %.2f hours which is the minimum.' % (
        total, average)
    else:
        statement = 'You slept %d hours over the last three nights an average of %.2f hours which is above the minimum.' % (
        total, average)
    return statement


print(sleep(a, b, c))
