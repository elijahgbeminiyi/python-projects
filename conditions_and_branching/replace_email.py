def replace_domain(email, new_domain):
    if "@" in email:
        position = email.index("@")
        new_email = email[:position] + "@" + new_domain
        return new_email
    return email


email = input("Enter your email: ")
new_email = replace_domain(email, "zed.com")
print("Your new email is, " + new_email)
