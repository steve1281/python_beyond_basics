# COLLECTION OF NOTES

__author__ = 'steve1281'


scientists = [
'marie curie',
'albert einstein',
'niels bohr',
'isaac newton',
'dmitri mendeleev',
'antoine lavoisier',
'carl linnaeus',
'alferd wegener',
'charles darwin']

sorted(scientists, key=lambda name: name.split()[-1])
#['niels bohr', 'marie curie', 'charles darwin', 'albert einstein', 'antoine lavoisier', 'carl linnaeus', 'dmitri mendeleev', 'isaac newton', 'alferd wegener']

addit = lambda x,y: x+y
addit(3,2)
#5

"{a}<====>{b}".format(a="Oslo",b="Stavenger")
#'Oslo<====>Stavenger'


def hypervolume(length,*lengths):
    v = length
    for item in lengths:
        v *= item
    return v


def print_args(arg1,arg2,*args):
  print(arg1)
  print(arg2)
  print(args)

print_args(11,12,13,14)
#11
#12
#(13, 14)

t = (11,12,13,14)
print_args(t)
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: print_args() missing 1 required positional argument: 'arg2'

print_args(*t)
#11
#12
#(13, 14)


def color(red,green,blue,**kwargs):
    print("r =",red)
    print("g =",green)
    print("b =",blue)
    print(kwargs)

k = {'red':21, 'green':68, 'blue':120, 'alpha':52}
color(**k)

def trace(f, *args, **kwargs):
    print("args =",args)
    print("kwargs =",kwargs)
    result = f(*args, **kwargs)
    print("result =",result)
    return result



from pprint import pprint as pp

t = {10,11,12,13,14,15}
u = {20,21,22,23,24,25}

for item in zip(t,u):
   print(item)

#(10, 20)
#(11, 21)
#(12, 22)
#(13, 23)
#(14, 24)
#(15, 25)

# timing the method call
from resolver import Resolver

resolve = Resolver()

from timeit import timeit
timeit(setup="from __main__ import resolve",
       stmt="resolve('python.org')",number=1)

#----------

from sort_by_last_letter import sort_by_last_letter
sort_by_last_letter(['hello','from','a','local','function'])
#['a', 'local', 'from', 'function', 'hello']

#LEGB RULE - local, enclosing, global, builtin

g = 'global'
def outer( p = 'param'):
  l='local'
  def inner():
    print(g,p,l)
  inner()


def enclosing():
    def local_func():
        print('local func')
    return local_func

lf = enclosing()
lf()

#---- closures
# remembers - prevents needed locals from be garbaged collected

def enclosing():
    x = 'closed over'
    def local_func():
        print(x)
    return local_func

lf = enclosing()
lf()

# function factories
# functions that builds functions


#decorators
# take a function, and return a different function
# not that simple, really, but
# replace, enhance exisiting functions


def vegetable() :
    return 'blomkal'

def animal():
    return 'bjorn'

def mineral():
    return 'stal'
























