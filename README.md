# pycal

### Version 0.0.1

### Author

**Daniel Gisolfi** - *All current work* - [dgisolfi](https://github.com/dgisolfi)

- [pycal](#pycal)
  - [Author](#author)
  - [Section 1 Introduction](#section-1-introduction)
    - [1.1 Genealogy](#1.1-genealogy)
    - [1.2 Hello World](#1.2-hello-world)
    - [1.3 Program structure](#1.3-program-structure)
    - [1.4 Types and Variables](#1.4-types-and-variables)
    - [1.5 Statements Differing from Python and Pascal](#1.5-statements-differing-from-python-and-pascal)
  - [Section 2 Lexical Structure](#section-2-lexical-structure)
    - [2.1 Programs](#2.1-programs)
    - [2.2 Grammers](#2.2-grammers)
      - [2.2.1 Lexical grammar in Pycal differing from Python and Pascal](#2.2.1-Lexical-grammar-in-pycal-differing-from-python-and-pascal)
      - [2.2.2 Syntactic grammar in Pycal differing from Python and Pascal](#2.2.2-syntactic-grammar-in-pycal-differing-from-python-and-pascal)
    - [2.3 Lexical Analysis](#2.3-lexical-analysis)
      - [2.3.1 Comments](#2.3.1-comments)
    - [2.4 Tokens](#2.4-tokens)
      - [2.4.1 Keywords in Pycal differing from Python and Pascal](#2.4.1-keywords-in-pycal-differing-from-Python-and-pascal)
  - [Section 3 Types](#section-3-types)
    - [3.1 Value Types in Pycal differing from Python and Pascal](#3.1-value-types-in-pycal-differing-from-python-and-pascal)			
    - [3.2 Reference Types in Pycal differing from Python and Pascal](#3.2-reference-types-in-pycal-differing-from-python-and-pascal)
  - [Section 4 Example Programs](#section-4-example-programs)
    - [4.1 Caesar Cipher](#4.1-caesar-cipher)
    - [4.2 Fibonacci](#4.2-fibonacci)
    - [4.3 Bubble Sort](#4.3-bubble-sort)
    - [4.4 Lambda Functions](#4.5-lambda-functions)
    - [4.5 Stack](#4.5-stack)

## Section 1 Introduction

Pycal (pronounced “pie cal”) is a simple, modern, object-oriented, and dynamically-typed programming language. Based on Python and Pascal, but differing in the following ways:

### 1.1 Genealogy

![Genealogy](./images/Genealogy.png)

### 1.2 Hello World

The most basic of programs implemented in pycal.

File `hello.py`:

```python
#!/usr/bin/env pycal
Program HelloWorld
print('Hello World!')
```

### 1.3 Program structure

pycal key organizational concepts

* In the very first line of a pycal file a shebang should be placed, the pycal shebang is as follows `#!/usr/bin/env pycal`
* Programs should be declared and given a name, this should be done at the beginning of the file following the shebang
* Imports must be declared after the program name

File `PizzaClass.py`:

```python
#!/usr/bin/env pycal
Program := PizzaClass
class Food =
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

declares a class named Food which has methods such as, `getDishName` and  `getOrigin`. The Pizza class inherits all members of the Food class as well as contains methods of its own like `getToppings`, `getSize` and `getPrice`. Each class also contains an initializer as well as a destructor for the Food class.

### 1.4 Types and Variables

There is two kind of type in pycal: value types and reference types. Variables classified as value types store their assigned data directly reference types however store references to the assigned data. Reference types are also known as objects.

### 1.5 Statements Differing from Python and Pascal

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

**String Declaration**

```bash
str := `fish` # String declaration can also be done with the ' and " characters
```

**String Concatenation**

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
# Specific type declaration must be done before the start of the function(for globals must be done after imports)
def add(a, b) =
    a: int
    b: int
    return a + b
```

## Section 2 Lexical Structure

### 2.1 Programs

A pycal program consists of one or more source files. A source file is an ordered sequence of Unicode characters. 

Conceptually speaking, a program is compiled using three steps: 

1. Transformation, which converts a file from a particular character repertoire and encoding scheme into a sequence of Unicode characters. 
2. Lexical analysis, which translates a stream of Unicode input characters into a stream of tokens. 
3. Syntactic analysis, which translates the stream of tokens into executable code. 

### 2.2 Grammers

The following are occurrences where pycal differs from Python and Pascal.
#### 2.2.1 Lexical grammar in Pycal differing from Python and Pascal

Pycal syntax is a combination of many it's two parent languages so it is quite similar however like it's parent Python it removes the character data type instead for a string value of length 1. 
```ruby
<null_value>     => null
<negated_value> => neg <val>
                => -<val
<char>          => <string>
```

#### 2.2.2 Syntactic grammar in Pycal differing from Python and Pascal

```ruby
<function_stmt>    => <identifier> =
                    <stmt>
# All other if else blocks follow the same syntax
<if_stmt>         => <conditional_stmt> =
                    <stmt>
# All loop statements use the same syntax
<loop_stmt>         => <logic_expr> = 
                    <stmt>
```

### 2.3 Lexical Analysis

#### 2.3.1 Comments

WIthin Pycal there are two forms of comments, both inherited from its parent languages.

**Single-line Comments** can be done using similar syntax as python for example:

```python
# A single line Comment.
```

**Multi-line Comments** can be done using similar syntax as Pascal for example:

```pascal
(*
 This is a multi-line comment.
 Additionally, curly braces can be used in place of 
 the characters used in this example
*)
```

**Comment Nesting**

Much like how Pascal can nest comments using the following syntax `{comment 1 (* comment 2 *)}` pycal can achieve the same effect 

Example 1: `(* Comment 1 #Comment 2 *)` 

Example 2: `{Comment 1 #Comment 2 }`

### 2.4 Tokens

**Identifier** derived from both parent languages - These are names of symbols that the programmer defines. Like both parent languages, they can be changed and re-used. 

**Operator**(OP)  derived from both parent languages - Symbols used to denote operations example: `+, =`.

**Keyword** derived from both parent languages - Also known as reserved words, they are used to define the syntax and structure of the Pycal language.

**Literals** derived from Python - Are the smallest elements within programs and are unbreakable.

**Separators** derived from Pascal - AKA white space.

**Constants** derived from Pascal - Numerical or character constants that denote actual values.

#### 2.4.1 Keywords in Pycal differing from Python and Pascal

A ***keyword***, also known as reserved words, are used to define the syntax and structure of the Pycal language. Much like Python, all keywords are in lowercase, this allows programmers to use keywords however they must capitalize on one or all of the letters of the word.

*New Keywords*:

**neg** 

*Removed Keywords*:

**goto**     **None**

*Altered Keywords*:

**true**     **false**

## Section 3 Types

### 3.1 Value Types in Pycal differing from Python and Pascal

**float** derived from python replaces the **Real** datatype from Pascal. Can be defined as a single-precision floating point value.


### 3.2 Reference Types in Pycal differing from Python and Pascal
**string** derived from python replaces the **Char** datatype from Pascal. In Pycal a char can be thought of or represented as a string of length 


## Section 4 Example Programs

### 4.1 Caesar Cipher

File `CeasarCipher.py`:

```python
#!/usr/bin/env pycal
Program := CeasarCipher
    
# CeasarCipher module written in pycal
og:string := `hal`
key:int := 6

def encrypt(str, key) = 
    a := ord(`a`)
    return ''.join(chr((ord(char) - a + key) % 26 + a) for char in str.lower())

def decrypt(str, key) = 
    return encrypt(str, -key)

def solve(string, cur, lim) = 
    print(`Ceasar ${str(cur)}: ${encrypt(string, cur)}`)
    if cur != lim =
        solve(string, cur+1, lim)
    else =
        print(`done`)

Encrypted := encrypt(og, key)
Decrypted := decrypt(Encrypted, key)
print(`Original  --> ${og}`)
print(`Encrypted --> ${Encrypted}`)
print(`Decrypted --> ${Decrypted}`)
solve(og, 0, 26)
```

### 4.2 Fibonacci

File `Fibonacci.py`:

```python
#!/usr/bin/env pycal
Program := Fibonacci
    
# Fibonacci function written in pycal
def fibonacci(n) = 
    n:int
    if n <= 1 =
        return n
    else =  
        return fibonacci(n-1) + fibonacci(n-2)

print(`fibonacci ${fibonacci(7)}`)
```

### 4.3 Bubble Sort

File `BubbleSort.py`:

```python
#!/usr/bin/env pycal
Program := BubbleSort

# Bubble sort function written in pycal
def bubblesort(l) =
  for i in range(len(l)) =
    for j in range(len(l) - 1, i, neg(1)) =
      if (l[j] < l[j - 1]) =
        swap(A, j, j - 1)
 
def swap(l, x, y) =
  tmp := l[x]
  l[x] := l[y]
  l[y] := tmp
```

### 4.4 Lambda Functions

File `Lambda.py`:

```python
#!/usr/bin/env pycal
Program := Lambda
    
double := lambda x = x * 2
square := lambda x = x * x
    
nums := [ 1, 2, 3, 4, 5]
num_list := list(map(lambda x: x * 2 , num_list))

print(double(5))
print(square(5))
print(num_list)
```

### 4.5 Stack

File `Stack.py`:

```python
#!/usr/bin/env pycal
Program := Stack

class Stack:
     def __init__(self) =
        self.items = []

     def isEmpty(self) =
        return self.items == []

     def push(self, item) =
        self.items.append(item)

     def pop(self) =
        return self.items.pop()

     def peek(self) =
        return self.items[len(self.items)-1]

     def size(self) =
        return len(self.items)

     def __del__(self) =
        print('destroying stack')


s = Stack()
s.push('a')
s.push('b')
s.push('c')

# returns 3
num := s.size()
# Returns top element
topElement = s.peek()
# Returns last element in the stack
element := s.pop()
```

