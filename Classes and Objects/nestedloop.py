for i in range(1, 10):
    for j in range (1, 10):
        if j % 2 == 0:
            continue
        print (j)
    if i % 2 == 1:
        break
    print (i)

