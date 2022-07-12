f = ("testarchive.txt", "x") #create archive

f = open("testarchive.txt", "a") #read archive
f.write("Archivo de texto prueba Open") #write
f.close()


f = open("testarchive.txt", "r") #show content
print(f.read())