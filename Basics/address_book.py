# regex => regular expression
import re

names_file = open("names.txt", encoding="utf-8")
data = names_file.read()
names_file.close()

# print(data)
last_name = r'Chatterjee'
first_name = r'Ronit'
# print(re.match(last_name, data))
# print(re.search(first_name, data))


# \w -> a-z, A-Z, 0-9, _
# \W -> except unicode

# \s -> white space
# \S -> not white space

# \D -> not number
# \d -> number 0-9

# \B -> Not boundry
# \b -> boundry

#### print(re.search(r'\(\d\d\d\) \d\d\d-\d\d\d\d', data))

# {3} -> repeat 3 times
# {,3} -> repeat 0 - 3 times
# {3, 5} -> 3, 4, 5 times

# generic

# ? -> optional
# * -> at least 0 time happen
# + -> at least 1 time happen

### print(re.findall(r'\w*, \w+', data))
### print(re.findall(r'\(?\d{3}\)?-?\s?\d{3}-\d{4}', data))

# set -> []

# [aple] -> apple
# [a-z]  -> all small characters
# [A-Z]  -> all capital characters
# [^2]   -> except something

# print(re.findall(r'[-\w\d+.]+@[-\w\d.]+', data))
# print(re.findall(r'\b[paravid]{7}\b', data, re.I))

# print(re.findall(r'''
# \b@[-\w\d.]* # First a word boundry, an @, and then any number of characters
# [^gov\t]+ # Ignore 1+ instances of the letters 'g', 'o' or 'v' and a tab
# \b #match another word boundry

# ''', data, re.VERBOSE | re.I))

# print(re.findall(r"""
# \b[\w]+, # Find a word boundry, 1+ hyphens or characters and a comma
# \s       # Find 1 white space
# [-\w ]+  # 1+ hyphen and character and explicit spaces
# [^\t\n]  # Ignore tabs and new lines
# """, data, re.X))


line = re.compile(r''' 
^(?P<name>(?P<last>[-\w ]*),\s(?P<first>[-\w ]+))\t # last name and first name
(?P<email>[-\w\d.+]+@[-\w\d.]+)\t # Email
(?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t # Phone
(?P<job>[\w\s]+,\s[\w\s.]+)\t? # Job and company
(?P<instagram>@[\w\d]+)?$ #Instagram
''', re.X | re.M)

#print(re.search(line, data).groupdict())

for match in line.finditer(data):
    # print(match.group('name'))
    print('{first}  {last} <{email}>'.format(**match.groupdict()))
