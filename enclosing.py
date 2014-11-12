__author__ = 'steve1281'

message = 'global'

def enclosing():
    message="enclosing"

    def local():
       nonlocal  message
       message="local"

    print("enclosing:", message)
    local()
    print("still enclosing:", message)

print("global message:",message)
enclosing()
print("still global message",message)

