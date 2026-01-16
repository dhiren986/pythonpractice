'''
fh = open("sample.txt", "xt")
fh.write('This is a sample text file.\n')
fh.write('It contains multiple lines.')
fh.close()
fhr = open("sample.txt", "rt")
for line in fhr.readlines():
    print(line)
fhr.close()
'''

try:
    with open("sample.txt", "rt") as fh:
        i=1
        print("Reading file content:")
        for line in fh:
            print(f"Line {i}: {line.strip()}")
            i+=1
except FileNotFoundError:
    print("Error: file 'sample.txt' was not found.")
