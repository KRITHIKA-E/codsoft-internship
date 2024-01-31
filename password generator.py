import random
import string

length=int(input("enter required password length :"))
ch=string.ascii_letters+string.digits
random=''.join(random.choice(ch) for _ in range(length))
print(random)
