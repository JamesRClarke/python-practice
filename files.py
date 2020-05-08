file = open ('test.txt', 'r') # opens file in read mode
content = file.read() # content of file saved in content var
tenbytes = file.read(10) # content of file saved amoubt of bytes used
singleline = file.readline() # content of file saved amoubt of bytes used

print content
print tenbytes
print singleline
file.close()
