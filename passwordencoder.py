import base64

password = input("Enter your password : ").encode("utf-8")

encoded = base64.b64encode(password)
print(f"Your encoded password is : {encoded}")

decoded = base64.b64decode(encoded)
print(f"Your decoded password is : {decoded}")\
