# Descriptor for a type-checked attribute
class TypeCheck:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type
    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('Expected ' + str(self.expected_type))
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]

# Class decorator that applies it to selected attributes
def typeassert(**kwargs):
    def decorate(cls):
        for name, expected_type in kwargs.items():
            # Attach a Typed descriptor to the class
            setattr(cls, name, TypeCheck(name, expected_type))
        return cls
    return decorate


class Structure:
    _field =[]
    def __init__(self, *args, **kwargs):
        #print(len(args), len(self._field), len(kwargs))
        if(len(args)) > len(self._field):
            raise TypeError("Expected {} arguments.".format(len(self._field)))
        # According to position for initialization parameters
        for name, value in zip(self._field, args):
            setattr(self, name, value)

        for name in self._field[len(args):]:
            setattr(self, name, kwargs.pop(name))

        if kwargs:
            raise TypeError('Invalid argument(s): {}'.format(','.join(kwargs)))