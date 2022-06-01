import re


source_text_file = 'log.txt'
dest_text_file = 'log2.txt'
result = []

with open(source_text_file, 'r') as f:
    for i in f:
        if re.match(r'10.1.192.38', str(i)):
            index1 = i.find('?sid=/')
            index2 = i.find('/&type')
            result.append(i[index1+6:index2])
    print(result)

with open(dest_text_file, 'a+') as f:
    for i in result:
        f.write(i+'\n')

