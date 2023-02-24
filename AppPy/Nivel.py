nivel = int(input('Nível '))
if nivel <= 4 :
    bp = 2
elif nivel <= 8:
    bp = 3
elif nivel <= 12:
    bp = 4
elif nivel <= 16:
    bp = 5
elif nivel <= 20:
    bp = 6
print(bp)
