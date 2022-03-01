def title():
    proj_name = 'TWITTER BOT'
    print('='*20)
    print(f'{proj_name:^20}')
    print('='*20)

def menu():
    valid = [1,2,3, 4]
    while True:
        try:
            print('='*20)
            print('Order to your bot:')
            print('''
            [1] - Follow back by username
            [2] - Like by word
            [3] - Show all followers
            [4] - Exit''')
            op = int(input())
            if op not in valid:
                print('Please enter a valid option.')
            else:
                break
        except:
            print('Please enter a number.')
    return int(op)




