colori = ['rosso', 'verde', 'blu']

colori_iteratore = iter(colori)
print(colori_iteratore)
# output: <list_iterator object at 0x000001CD75537D60>

colore = next(colori)
# output error: 
#   TypeError: 'list' object is not an iterator

colore = next(colori_iteratore)
print(colore)
# output: rosso

colore = next(colori_iteratore)
print(colore)
# output: verde

colore = next(colori_iteratore)
print(colore)
# output: blu

colore = next(colori_iteratore)
print(colore)
# output error: 
# Traceback (most recent call last):
#   File "", line 22, in <module>
#       colore = next(colori_iteratore)
# StopIteration