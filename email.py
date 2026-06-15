import re
import email.utils

n = int(input())

for _ in range(n):
    name, email_addr = email.utils.parseaddr(input())

    if re.match(r'^[A-Za-z][A-Za-z0-9._-]*@[A-Za-z]+\.[A-Za-z]{1,3}$', email_addr):
        print(email.utils.formataddr((name, email_addr)))