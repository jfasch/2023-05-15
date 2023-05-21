class MyException(Exception):
    pass

class BadEmployee(MyException):
    def __init__(self, obj):
        self.obj = obj
        super().__init__('Bad type: '+self.obj.fullname)

class SelfCycle(MyException):
    pass

class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    @property
    def fullname(self):
        return f'{self.firstname} {self.lastname}'

    def say_hello(self, phrase = 'Hallo'):
        print(f'{phrase}, my name is {self.firstname} {self.lastname}')

    @classmethod
    def make_child(cls, name, person1, person2):
        return cls(name, person1.lastname + ' ' + person2.lastname)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

    def __repr__(self):
        return f'Person("{self.firstname}", "{self.lastname}")'

class Employee(Person):
    def __init__(self, firstname, lastname, salary):
        super().__init__(firstname, lastname)
        self.salary = salary

    def title(self):
        return f'{self.fullname} ({self.salary})' 

class Manager(Employee):
    def __init__(self, firstname, lastname, salary, employees):
        super().__init__(firstname, lastname, salary)
        self.employees = employees
    
    def title(self):
        return f'{super().title()} (manages {len(self.employees)} employees)'

    def add_employee(self, emp):
        if not isinstance(emp, Employee):
            raise BadEmployee(emp)
        if emp is self:
            raise SelfCycle('ui!')
        if self.has_employee(emp):
            raise SelfCycle('ui! (nur komplexer)')
        self.employees.append(emp)

    def has_employee(self, emp):
        assert isinstance(emp, Employee)
        for e in self.employees:
            if e is emp:
                return True
            if isinstance(e, Manager):
                return e.has_employee(emp)

joerg = Employee('Joerg', 'Faschingbauer', 3000)
mgr = Manager('Isolde', 'Haubentaucher', 6000, [joerg])

johanna = Person('Johanna', 'Faschingbauer')
mgr.add_employee(johanna)

caro = Employee('Caro', 'Faschingbauer', salary=1000)
mgr.add_employee(caro)
mgr.add_employee(mgr)

print(mgr.title())
