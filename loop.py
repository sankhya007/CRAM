import fileinput 

stream = fileinput.input(files=('example.txt',
                                'example1.txt'))

for data in stream: 
    print(data)