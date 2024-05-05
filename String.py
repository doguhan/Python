# Escape Characters

# new line
x = 'Hello \n World'
print(x)

# backslash
x = 'Hello \\ World'
print(x)

# single quote
x = 'Hello \' World'
print(x)
x = 'Hello \t World'
print(x)

y = '''
Merhaba arkadaşlar
nasılsınız
umarım iyisinizdir..
'''

print(y)

x = 5

z = f'{x} için {y}' #string içinde değişken kullanmak istiyorsan değişkenleri {} süslü parantez içine almak gerek.
print(z)

x = len(y)
print(x)


print(y.count('ka'))

name = input('Enter your name: ')
print(f'Merhaba, {name[-1].upper()}')


