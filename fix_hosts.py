s = open('msresort/settings.py', encoding='utf-8').read()
print('Current ALLOWED_HOSTS line:')
for line in s.split('\n'):
    if 'ALLOWED_HOSTS' in line:
        print(repr(line))
