table=['I','am','jiaer','maomao','children']
for item in table:
    print(item)
    print("next:")
print("table print end!")
for value in range(1,6):
    print("value:",value)
print("range() end!")
even_numbers=list(range(2,11,3))
print(even_numbers)
print("min:",min(even_numbers))
print("max:",max(even_numbers))
print("sum:",sum(even_numbers))
print(".......................................")
squares=[value**2 for value in range(1,11)]
print(squares)
print(squares[1:4])
message=squares[:]
