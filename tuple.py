# x=(2)
# print(x,type(x))  # 2   <class 'int'.

# a=(3,)
# print(a,type(a))  # class 'tuple' --->Anything can be hold ina single variable is called as "TUPLE".

# gh=('apple','reliance','asus','dell','samsung','hp')
# gh[1]="motorola"  # TypeError:'tuple' object does not support item assignment.{Bcoz of 'tuple' is a immutable sequence which is not specified to modify.}

# n="Hello", "World"
# print(n,type(n)) #here class is tuple bcoz it is holding multiple elements.
# print(n[2]) # IndexError:tuple index out of range.
# print(n[0]) # 'hello' # here index position '0' 
# print(n[1])

# f=(2,3.5,'hello',[5,8],('K','F'),None,True)
# print(f,type(f))  # class is tuple.

# c=(4,3.6,'lokesh',[8,4],('E','H'))
# c[0]=55 # TypeError: 'tuple' object does not support item assignment.
# c[1]='hi' # TypeError: 'tuple' object does not support item assignment.
# print(c)

# c=(4,3.6,'lokesh',[8,4],('E','H'))
# print(c.index('lokesh')) # 2.
# print(c.count([8,4])) # 1.

print(dir(tuple()))
# two methods :'count', 'index'