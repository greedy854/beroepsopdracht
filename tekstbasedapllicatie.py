def start():
    print("the story begins")
    print("choose 1or2")
    choice = input()
    if choice == '1':
        print("go mid walk to the store")
    elif choice == '2':
        print("you're gonna go home")
        
        print("shoot or look around")
    choice = input()
    if choice == '1':
        print("youre getting robbed so you grab the gun and start shooting")
    elif choice == '2':
        print("go home and look what's wrong")

        print("run or shoot")
    choice = input()
    if choice == '1':
        print("shoot him dead")
    elif choice == '2':
        print("go home fast because you see a robber on camera")

        print("hide or look around for him")
    choice = input()
    if choice == '1':
        print("you're hiding the body in the basement")
    elif choice == '2':
        print("you look around home to find the robber")

    print("hide or go attack")
    choice = input()
    if choice == '1':
        print("hide the body in the underground closet")
    elif choice == '2':
        print("You see the robber and attack him")

        print("other hide place or kidnap at home")
    choice = input()
    if choice == '1':
        print("the body stinks and find some other place ")
    elif choice == '2':
        print("you kidnapped the robber now at home")

        print("look around or put on chair")
    choice = input()
    if choice == '1':
        print("you go look around outside")
    elif choice == '2':
        print("you put him in a chair in the middle of the room")

        print("hide in barn or take mask off")
    choice = input()
    if choice == '1':
        print("you find a barn in the garden and put him in there")
    elif choice == '2':
        print("take his mask off")

        print("put in barn and shoot or you find out who he is")
    choice = input()
    if choice == '1':
        print("put him in the barn and shoot him again")
    elif choice == '2':
        print("it is your brother what now")

        print("its youre brother what now!!!")
    choice = input()
    if choice == '1':
        print("then you find out its your brother")
    elif choice == '2':
        print("still shoot him dead because you dont care")

        print("what should i do in the end 1,2,3,4")
    choice = input()
    if choice == '1':
        print("and you're still happy because you hated him")
    elif choice == '2':
        print("and you t bag him")
    if choice == '3':
        print("going to cry")
    elif choice == '4':
        print("fix a party")
        print("end")
        print("restart")
        start()
start()