# 1
import re

text = "Contact emails are: john.doe@example.com and jane.doe@example.com."
emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-z]{2,}", text)
print(emails)


# 2
import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
pattern = r"\b[A-Za-z0-9._%+-]+@(?!exclude)[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
emails = re.findall(pattern, text)
print(emails)



