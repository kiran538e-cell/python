#String Slicer and Manipulator with the name initials through slicing [s:e] & indexing 0 to ... e.g: "M.A."
name = input("Enter your full name: ")

first_name = name[:name.index(" ")]                 #slice first & last name for making initials throuogh indexing
last_name = name[name.index(" ") + 1:]              #by which both after separating names initials starts with 0th index

initials = first_name[0] + ". " + last_name[0] + "."

print("Initials:", initials)
print("Uppercase Name:", name.upper())               #for name in uppercase
print("Reversed Name:", name[::-1])                  #for reversed name name[::-1] short-cut