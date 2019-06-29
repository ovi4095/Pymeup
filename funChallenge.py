for x in range(5):
    if x == 0:
        print(f'''{"X" * 6}  {"X" * 2}   {"X" * 2}  {"X" * 3}     {"X" * 2}''')
    elif x == 1:
        print(f'''{"X" * 2}      {"X" * 2}   {"X" * 2}  {"X" * 2} {"X" * 2}   {"X" * 2}''')
    elif x == 2:
        print(f'''{"X" * 6}  {"X" * 2}   {"X" * 2}  {"X" * 2}  {"X" * 2}  {"X" * 2}''')
    elif x == 3:
        print(f'''{"X" * 2}      {"X" * 2}   {"X" * 2}  {"X" * 2}   {"X" * 2} {"X" * 2}''')
    elif x == 4:
        print(f'''{"X" * 2}      {"X" * 7}  {"X" * 2}     {"X" * 3}''')
    else:
        break
