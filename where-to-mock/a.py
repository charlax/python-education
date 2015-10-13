def burn():
    pass


class Toaster(object):

    @classmethod
    def burn(cls):
        return True

print 'In a.py:', burn
print 'In a.py, Toaster:', Toaster
print 'In a.py, Toaster.burn:', Toaster.burn
