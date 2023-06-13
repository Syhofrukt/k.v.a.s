from .password_hashing import PasswordHandler
# user_password = str(input("Put your password: "))
hash_algoritm = 'sha256'
coding_algoritm = 'b64encode'
pepper = None

ClassName = PasswordHandler(hash_algoritm, coding_algoritm, pepper)
# hashed_password = ClassName.hash_password_with_salt(user_password)
# verify = ClassName.verify_password(user_password, hashed_password)

# print("Hashed password: " + hashed_password)
# print("Password equal: " + str(verify))
"areyoureal?yesyouare!"
'trumpkrutoi'

# row = [('bebra',),('oleg',),('12345',),(0,),(0,)]
# id, login, password, admin, activated = row
# print(admin)