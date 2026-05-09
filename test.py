from jinja2 import Template
from string import Template as StringTemplate

a = "My name is $name and i live in $place"
b = "My name is {{ name }} and i live in {{ place }}"

t1 = StringTemplate(a)
t2 = Template(b)

print(t1.substitute({'name': 'John', 'place': 'New York'}))
print(t2.render({'name': 'John', 'place': 'New York'}))