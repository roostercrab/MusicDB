try:
    with open('music.txt', 'r') as myfile:
        mastertext = myfile.read()
        masterlist = eval(mastertext)
        print(masterlist)
except:
    masterlist = []
    
def music(choice):
    if choice == 'add':
        new = {}
        new['artist'] = input('What is the artist name? ')
        new['title'] = input('What is the song title? ')          
        new['album'] = input('What album was it from? ')         
        new['track'] = input('What was the track number? ')
        new['year'] = input('What year was it released? ')
        new['genre'] = input('What genre was it from? ')
        if len(masterlist) <= 7:
            masterlist.append(new)
        else:
            print("That's too many songs ya chode!!")
        print(masterlist)
    elif choice == 'list':
        for thing in masterlist:
            print("\nHere's a song that you saved, nerd:\n")
            for key, value in thing.items():
                print(f'{key} is {value}')
    elif choice == 'save':
        string = str(masterlist)
        myfile = open('music.txt', 'w')
        myfile.write(string)
        myfile.close()

    elif choice == 'help':
        print('I see that you need assistance.\n"add" will let you add a song to the "database"\n"list" will let you see all the things in your "database"\n"save" let\'s you save your file so that you can look at it later...for whatever reason...\n"help" brought you here\n"exit" will send you on your way\n)
        
    elif choice == 'exit':
        import sys
        sys.exit()
