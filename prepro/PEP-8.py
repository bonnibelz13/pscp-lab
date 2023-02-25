def print_something():
    print(
    'This is a really long line,', \
    'but we can make it across multiple lines.'
    )

print(print_something())


def print_something():
    print('Wow, this also works?',
          'I never knew!')
print(print_something())


queryText= "SELECT * FROM TABLE1 AS T1"\
"JOIN TABLE2 AS T2 ON T1.SOMETHING = T2.SOMETHING"\
"JOIN TABLE3 AS T3 ON T3.SOMETHING = T2.SOMETHING"\
"WHERE SOMETHING BETWEEN <WHATEVER> AND <WHATEVER ELSE>"\
"ORDER BY WHATEVERS DESC"

print(queryText)

def print_something():
    print ('Look at us,',
    'printing this sentence on multiple lines.')


print_something()