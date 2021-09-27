from user import Admin

eric = Admin('fayz', 'amed', 'f_amed', 'fsamed@poopoo.kom', 'baskerville')
eric.describe_user()

eric_privileges = [
    'Can reset passwords',
    'Can moderate discussions',
    'Can suspend accounts',
    'Can fart'
    ]
eric.privileges.privileges = eric_privileges

print(f"\nThe admin {eric.username} has these privileges: ")
eric.privileges.show_privileges()
