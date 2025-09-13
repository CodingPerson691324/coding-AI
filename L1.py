print('hello i am ai bot. Whats ur name?: ')

name = input()

print(f'nice to meet you, {name}')

print('how r u feeling today?(good/bad): ')
mood = input().lower()

if mood == 'good':
    print(f'im glad too hear that{name}!')

elif mood == 'bad':
    print(f'i am very sorry to hear that {name}. I really hope things get better for you soon')

else:
    print(f'i understand that its hard to express feelings some times {name}')

print(f'it was nice meeting you, bye!')