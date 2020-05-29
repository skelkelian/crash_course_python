def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email
    # if email did not need to be changed you just return the email as is
print(replace_domain("skelkelian88@hotmail.com", "hotmail.com", "gmail.com"))

emails = ["skelkelian88@gmail.com", "rompytomp@yahoo.com", "ahsqwerty@hotmail.com"]
for email in emails:
    new_email = replace_domain(email, 'yahoo.com', 'gmail.com')
    print(new_email)

def new_replace_domain(email, new_domain):
    if not(email.endswith("gmail.com")):
        index = email.index("@")
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email

# assert new_replace_domain('skelkelian1@hotmail.com', 'gmail.com') == 'skelkelian1@gmail.com'
# assert new_replace_domain('', 'gmail.com') == ''

emails = ["skelkelian88@gmail.com", "rompytomp@yahoo.com", "ahsqwerty@hotmail.com"]
for email in emails:
    new_email = replace_domain(email, 'yahoo.com', 'gmail.com')
    print(new_email)