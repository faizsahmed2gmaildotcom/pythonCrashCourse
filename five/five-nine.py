adminUser = 'Admin'
users = []
if not users:
    print("No users available...")
for users in users:
    if adminUser in users:
        print(f"Hello, {adminUser}. Need a status report?")
    else:
        print(f"Bye, {users}.")
