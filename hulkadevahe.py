a={1,2,3}
b={1,3}
c=set()
for element in a:
    if element not in b:
        c.add(element)
print(c)

def teisenda(järjend):
    # teen järjendist koopia
    uus = järjend[:]

    for i in range(len(uus)):
        for j in range(i+1):
            if uus[j] < uus[i]:
                uus[i], uus[j] = uus[j], uus[i]

    return uus

print(teisenda([5, 2, 1, 4, 3]))