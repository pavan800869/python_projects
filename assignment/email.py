import re

text = "Please contact support@example.com for assistance or john.doe123@subdomain.domain.co.uk for more information."

email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'


email = re.findall(email_pattern, text)

for mail in email:
    print(mail)
