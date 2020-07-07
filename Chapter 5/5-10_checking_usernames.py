current_users = ['Jethro', 'Jebediah', 'Tabitha', 'Yolanda', 'Lancaster']
new_users = ['Jebediah', 'Dakota', 'Dale', 'Ellie', 'Garth']

for new_user in new_users:
    if new_user in current_users:
        print('This username is not available. Please select another one.')
    else:
        print('This username is available.')