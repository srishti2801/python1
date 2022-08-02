# wap to generate a list of acronyms from a list of words using generators & *args

def acronym(*words):
    for word in words:
        yield ''.join([i[0].upper() for i in word.split()])

for item in acronym('Project Manager', 'Software Engineer','Data Analyst'):
    print(item)

print(list(acronym('Project manager','Software engineer','Team leading')))