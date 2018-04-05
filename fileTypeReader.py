import re
string=raw_input("Enter the file name :")
pattern=r'\.\w{1,10}'
match=re.findall(pattern,string)
if match:
	print("File type :")
	print(match)
else:
	print("Enter file name with their extension")