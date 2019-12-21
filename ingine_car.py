startted = False
call = input('> ')
if call.upper() == 'HELP' or call.lower() == 'help' :
    print('start -> for start car')
    print('stop -> for stop car')
    print('quit -> for exit')
    while True:
        choice = input('> ')
        if choice.lower() == 'start' or choice.upper() == 'START':
            if startted :
                print('car already started')
            else:
                print('car started')
                startted = True
        elif choice.lower() == 'stop' or choice.upper() == 'STOP':
            if not startted:
                print('car already stopped')
            else:
                print('car stopped')
                startted = False
        elif choice.upper() == 'QUIT' or choice.lower() == 'quit':
            break
        else:
            print("I don't understand")
else:
    print("I don't understand")