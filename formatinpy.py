# 1- Basic Format 
#old -----for String----- 
print('%s %s' % ('ABC', 'XYZ')) 
#new  -----for String-----
print('{} {}'.format('ABC','XYZ'))
#old -----for double or int
print('%d %d' % (4,6))
#new -----for double or int
print('{} {}'.format(4,6))

# 2- Value conversion
class ABCD(object):
    
    def __str__(self):
        return 'str'

    def __repr__(self):
        return 'repr'

        #In %-style you usually use 
        # %s for the string representation
        # %r for a repr(...) conversion
#old
print('%s %r' % (ABCD(), ABCD()))
#new 
print('{0!s} {0!r}'.format(ABCD()))

# 3- Padding and aligning strings
#old
print('%10s' % ('ABCD',))
#new
print('{:>10}'.format('ABCD'))
#padding from center
print('{:^10}'.format('ABCD'))

# 4- Truncating long strings
#old
print('%.5s' % ('xylophone',))
#new
print('{:.5}'.format('xylophone'))

# 5- Combining truncating and padding
#old
print('%-10.5s' % ('xylophone',))
#new
print('{:10.5}'.format('xylophone'))

# 6- Numbers

#Integers
#old
print('%d' % (42,))
#new
print('{:d}'.format(42))

#float
#old
print('%f' % (3.141592653589793,))
#new
print('{:f}'.format(3.141592653589793))

# 7- Padding numbers
#old
print('%4d' % (42,))  # int
print('%06.2f' % (3.141592653589793,)) #float

#new
print('{:4d}'.format(42)) #int
print('{:06.2f}'.format(3.141592653589793)) #float

# 8 - Signed numbers

#old
print('%+d' % (42,))
#new 
print('{:+d}'.format(42))
print('{:=5d}'.format((- 23))) # with padding


#9 - Named placeholders
First = {'first': 'Hodor', 'last': 'Hodor!'}
#old
print('%(first)s %(last)s' % First)

#new
print('{first} {last}'.format(**First))
#or
print('{first} {last}'.format(first='Hodor', last='Hodor!'))

#10 - Getitem and Getattr
person = {'first': 'Jean-Luc', 'last': 'Picard'}

#new
print('{p[first]} {p[last]}'.format(p=person))