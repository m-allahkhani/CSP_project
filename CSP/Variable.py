from typing import Generic, TypeVar, List

T = TypeVar('T')


class Variable(Generic[T]):
    _value: T = None
    _has_value: bool = False
    _has_initial_value = False

    def __init__(self, domain: List[T], name: str = None, initial_value: T = None):
        self._has_initial_value = initial_value is not None
        self._has_value = initial_value is not None
        self._value = initial_value
        self._domain = domain
        self.name = name
        self.neighbors = set({})
        self.mrv_val = None
        self.degree_val = None

    @property
    def value(self) -> T:
        return self._value

    @value.setter
    def value(self, x: T):
        if x == self._value:
            return
        if x in self._domain and x is not None:
            self._value = x
            self._has_value = True
        elif x is None:
            self._has_value = False
            self._value = x
        else:
            raise Exception("Value is not in the domain")

    @property
    def domain(self) -> List[T]:
        return self._domain
    
    def __hash__(self):
        
        return hash((self.name, tuple(self.domain)))

    @property
    def has_initial_value(self) -> bool:
        return self._has_initial_value

    @property
    def has_value(self) -> bool:
        return self._has_value

    @domain.setter
    def domain(self, value):
        self._domain = value

    @has_value.setter
    def has_value(self, value: bool):
        self._has_value = value

