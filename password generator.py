print('password should contain atleast 8 characters with one uppercase,one lowercase and one number and one special character \n')
password=input('Enter password:')
if len(password)>=8:
    u=0
    l=0
    n=0
    s=0
    for ch in password:
        if ch.isupper():
            u+=1
        elif ch.islower():
            l+=1
        elif ch.isnumeric():
            n+=1
        elif ch in('@','#','$','^','*'):
            s+=1
    if u>0 and l>0 and n>0 and s>0:
        print('strong password')
    else:
        print('weak password')
else:
    print('invalid password')
