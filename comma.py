spam = ['apples', 'bannas', 'tofu', 'cats']

print(spam)

output=''
for item in spam:
    if item != spam[-1]:
        output += item+', '
    else:
        output += 'and ' + item

print(output)
