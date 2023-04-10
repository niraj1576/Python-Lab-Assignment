

     #functions on String

  # 1) .lower() : convert whole string to lowercase

name="NIRAJ"
print(name.lower())


 # 2)  .upper()   : convert whole string to uppercase

name1="Niraj"
print(name1.upper())

 # 3)  .find() : finds the begining index of given sub string in exixting string

name2="I am niraj"
print(name2.find("niraj"))

print(name2.find("z"))  # give -1 as it is not present in extisting string


 # 4)   .replace()  : replaces a sub string with another existing substrring  but not changes original string

print(name2.replace("niraj","raj"))

print(name2)

 # 5)  in  : checks wheather substring presemt in exixting string or not

print("am" in name2)

print("kamal" in name2)


 # 6) operators o string

name3="rahul"
print(name2+name3)





