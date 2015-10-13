from a import burn
from a import Toaster

print 'In b.py, at import time:', burn
print 'In b.py, at import time, Toaster:', Toaster

def toast():
    print 'In b.py, at runtime:', burn
    print 'In b.py, at runtime, Toaster:', Toaster
    print 'In b.py, at runtime, Toaster.burn:', Toaster.burn
    burn()
    Toaster.burn()
    return True
