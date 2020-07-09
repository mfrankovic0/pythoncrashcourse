current_users = ['Jethro', 'Jebediah', 'Tabitha', 'Yolanda', 'Lancaster']
new_users = ['Jebediah', 'Dakota', 'Dale', 'Ellie', 'Garth']


current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print('This username is not available. Please select another one.')
    else:
        print('This username is available.')