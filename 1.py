#line = 'Напишите программу, удаляющую из текста все слова, содержащие абв'
#ref = "абв"
#lst = line.split()
#res = (x for x in lst if ref not in x)
#print(' '.join(res))

#line = 'Напишите программу, удаляющую из текста все слова, содержащие абв'
#ref = "абв"
#lst = line.split()
#res = filter(lambda x: 'абв'in x, lst)
#print(' '.join(res))

prices=['45.3','455.5','550.0','550.0']
tovar = ['ботинок','туфля','джинсы','кровать']
l = list(zip(prices, tovar))
print(l)



