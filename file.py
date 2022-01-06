
a = 0
while a <= 10:
    with open('log.txt', 'a') as file:
     file.write('input\n')
    a = a + 1
