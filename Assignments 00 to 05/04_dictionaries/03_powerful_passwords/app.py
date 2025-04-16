# You want to be safe online and use different passwords for different websites. However, you are forgetful at times and want to make a program that can match which password belongs to which website without storing the actual password!
# This can be done via something called hashing. Hashing is when we take something and convert it into a different, unique identifier. This is done using a hash function. Luckily, there are several resources that can help us with this.
# For example, using a hash function called SHA256(...) something as simple as
# hello
# can be hashed into a much more complex
# 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
# Fill out the login(...) function for a website that hashes their passwords. Login should return True if an email's stored password hash in stored_logins is the same as the hash of password_to_check.
# (Hint. You will need to use the provided hash_password(...) function. You don't necessarily need to know how it works, just know that hash_password(...) returns the hash for the password!)


from hashlib import sha256

def login(email, stored_login, password_to_check):
    """
    Returns True if the hash of the password we are checking matches the one in stored_logins
    for a specific email. Otherwise, returns False.
    """
    # Check if email exists in stored_logins
    if stored_login.get(email) == hash_password(password_to_check):
        return True
    return False

# There is no need to edit code beyond this point
def hash_password(password):
    """
    Takes in a password and returns the SHA256 hashed value for that specific password.
    """
    return sha256(password.encode()).hexdigest()

def main():
    # stored_logins is a dictionary with emails as keys and hashed passwords as values
    stored_logins = {
        'example@email.com': hash_password('password'),
        'another@example.com': hash_password('another_password'),
         'code_in_placer@cip.org': hash_password('karel'),

    }

    print(login('example@email.com', stored_logins, 'password'))  # ✅ Should return True
    print(login("example@email.com", stored_logins, "wrongpassword"))  # ❌ Should return False
    print(login('another@example.com', stored_logins, 'another_password'))  # ✅ Should return True
    print(login("code_in_placer@cip.org", stored_logins, "karel"))  # ❌ Should return False
    print(login("student@stanford.edu", stored_logins, "password"))  # ❌ Should return False

if __name__ == '__main__':
    main()





