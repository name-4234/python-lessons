'''x = []
while True:
    y = int(input("введи рост: "))
    if y == 0:
        break
    else:
        if 160 <= y <= 180:
            x.append(y)

print(len(x))
print(min(x), max(x))
def storona(x, y):
    if x > 0 and y > 0:
        return 'I'
    if x < 0 and y > 0:
        return 'II'
    if x < 0 and y < 0:
        return "III"
    if x > 0 and y < 0:
        return 'IV'
        '''

print(storona(1,-2))
p = 'password'
def ask_password():
    for att in range (3):
        g = input('введи пароль: ')
        if g == p:
            print ("пароль принят")
            return
    print('в доступе отказано')
    return
ask_password