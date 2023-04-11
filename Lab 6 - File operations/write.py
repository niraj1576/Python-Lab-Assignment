f = open("demofile.txt", "a")
f.write("lets write something!\n")
f.close()

f = open("demofile.txt", "r")
print(f.read())
