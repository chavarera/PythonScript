## Escaping Metacharacters

Escaping Metacharacters in regular Expression

### Metacharacters
- Metacharacters are characters that have special meaning within regular expressions. 
- The period (.) ,brackets []  are some example of  metacharacters.
- To escape a special metacharacter use \ before that metacharacter.

Syntax:
```python
pattern=r'\metacharacters'
```

Example normal :
```python
#import required module
import re

#input string
input_string="a=[hi] this is simple"

# find out the text inside the []
#pattern=r'[\w+]' Wrong pattern 

pattern=r'[\w+]'
result=re.findall(pattern,input_string)
print(result)

#Result:['a', 'h', 'i', 't', 'h', 'i', 's', 'i', 's', 's', 'i', 'm', 'p', 'l', 'e']
```

Example Using escape metacharacters
```python
#import required module
import re


input_string="a=[hi] this is simple"

# find out the text inside the []
#pattern=r'[\w+]' Wrong pattern 

pattern=r'\[\w+\]'
result=re.findall(pattern,input_string)
print(result)

#Result:['[hi]']

#here [] is escaped using \  character as \[\] 
```

Example 3:

Findout . occurence in given string
```
input_string='this is simple.python easy is programming language.'
```

```python
import re

input_string='this is simple.python easy is programming language.'

pattern=r'\.'
result=re.findall(pattern,input_string)
print(result)

#Result:['.', '.']
```
