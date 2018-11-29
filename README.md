# pycal

### Version 0.0.1

### Author

**Daniel Gisolfi** - *All current work* - [dgisolfi](https://github.com/dgisolfi)

## Section 1 - Introduction

Pycal (pronounced “pie cal”) is a simple, modern, object-oriented, and dynamically-typed programming language. Based on Python and Pascal, but differing in the following ways:

### 1.1 - Genealogy

![Genealogy](/static/images/Genealogy.png)

### 1.2 - Hello World

The most basic of programs implemented in pycal.

```python
#!/usr/bin/env pycal
Program HelloWorld
print('Hello World!')
```

### 1.3 - Program structure

pycal key organizational concepts

* In the very first line of a pycal file a shebang should be placed, the pycal shebang is as follows `#!/usr/bin/env pycal`
* Programs should be declared and given a name, this should be done at the begeining of the file following the shebang
* Imports must be declared after the program name

```python
#!/usr/bin/env pycal
Program PizzaClass
class Food
	def __init__(self, dish_name, place_origin) =
        self.dish_name := dish_name
        self.place_origin := place_origin
        print('creating food object')
    
    def getDishName(self) =
        return self.dish_name

    def getOrigin(self) = 
        return self.place_origin
    
    def __del__(self) =
        print('destroying food object')
        
class Pizza(Food):
    def __init__(self, toppings, size, price) =
        Food.__init__(self, 'Pizza', 'Italy')
        self.toppings := toppings
        self.size := size
        self.price := price

    def getToppings(self) = 
        return self.toppings
    
    def getSize(self) = 
        return self.size
    
    def getPrice(self) = 
        return self.price
       
large_pepperoni_pie := Pizza(['pepperoni', 'cheese'], 'Large', 17.99)
```

declares a class named Food which has the methods such as, `getDishName` and  `getOrigin`. The Pizza class inherits all members of the Food class as well as contains methods of its own like `getToppings`, `getSize` and `getPrice`. Each class also contains a initilizer as well as a destructor for the Food class.

### 1.4 - Types and Variables

There is two kind of type in pycal: **value types** 

### 1.5 - Statements Differeing from Python and Pascal

**Expression Statement**

```python
i := 10
str := 'fish'
```

**Block Creation Indicator**


```python
def foo() = 
	print('foo')
```

**String Decleration**

```bash
str := `fish` # String decleration can also be done with the ' and " characters
```

**String Concatanation**

```bash
word1 := `method`
word2 := `totaly`
str := `This ${word1} of concatanation is ${word2} not stolen from javascript.`
```

**Type Inference**

```python
# When assigning values to variables, the type can be either inferred or specified. 
# Type Inference...
i := 3
# Specific type decleration, must be done before start of function(for globals must be done after imports)
def add(a, b) =
    a: int
    b: int
	return a + b
```

