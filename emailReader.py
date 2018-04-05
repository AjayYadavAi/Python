import re
print("Email validator............................")
pattern= r"[\w\.-]+@[\w\.-]+\.[\w\.]+"
emails='''


 Emails ajayyadavhumble@gmail.com ,
 rohan.com , john@gmail.com ,
  dhoni.rohi.yo$  r@gmail.com,
 shyam-ram484@gmail.com,


 '''
match = re.findall(pattern,emails)
if match:
	print("Valid Emails........")
	for i in match:
		print(i)
