adminUser = 'Admin'
users = ['Burp', 'Fart', 'Corn', 'Puu', 'Admin']
for users in users:
    if adminUser in users:
        print(f"Hello, {adminUser}. Need a status report?")
    else:
        print(f"Bye, {users}.")
