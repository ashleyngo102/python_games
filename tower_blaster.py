#Ashley Ngo
#65868419
#No help

import random

def setup_bricks():
    """create a main pile (60 bricks), list from 1 - 60
        create a discard pile (0 brick), empty list
        show 2 lists"""
    # create main pile at the first state
    main_pile_first = []
    for n in range(1, 61):
        main_pile_first.append(n)
    # create a discard pile
    discard_pile_first = []
    # debug
    # print("main pile",main_pile_first)
    # print("discard pile",discard_pile_first)
    return main_pile_first, discard_pile_first


def shuffle_bricks(bricks):
    # shuffle the pile when the discarded pile is returned to main pile
    random.shuffle(bricks)


def check_bricks(main_pile, discard_pile):
    """ check if the main pile runs out of cards,
    if so, shuffles discard pile and move bricks to main pile
    then, the top brick moves to discard pile"""
    if len(main_pile) == 0:
        shuffle_bricks(discard_pile)
        # debug
        print("shuffled pile", discard_pile)
        # move to main pile
        main_pile.extend(discard_pile)
        # remove bricks from discard pile
        discard_pile.clear()
        # debug
        print("new main pile", main_pile)
        print("cleared discard pile", discard_pile)
        # top brick moves to discard pile
        discard_pile.insert(0, main_pile.pop(0))


def check_tower_blaster(tower):
    """as the computer and user have their own tower, check if towers are are stable
        return True if tower blaster is stable, return False if not"""
    # copy tower list to a new list and check
    tower_check = tower.copy()
    # sort in ascending order
    tower_check.sort()
    # if stable, 2 lists are the same
    if tower_check == tower:
        return True
    else:
        return False


def get_top_brick(brick_pile):
    """remove and return a top brick of either main or discard pile
        use when the game first starts
        use when each player takes turn to get top brick from main or discard pile
        reveal the number in integer"""
    # get the top brick
    top_brick = brick_pile[0]
    # remove from pile
    brick_pile.pop(0)
    return top_brick


def deal_initial_bricks(main_pile):
    """use at the beginning of game (one brick to each player and repeat)
        Rules: computer get dealt first and playing first, place one on top of other
        return a tuple of 2 lists (computer's hand and user's hand)"""
    # deal first 10 bricks for each in order
    for n in range(0, 10, 1):
        # draw a brick from top of main pile and for computer pile
        top_brick = get_top_brick(main_pile)
        computer_pile.insert(0, top_brick)
        # debug
        # print('computer',computer_pile)
        # print('main',main_pile)
        # draw a brick from top of main pile and for computer pile
        top_brick = get_top_brick(main_pile)
        human_pile.insert(0, top_brick)
        # debug
        # print('human', human_pile)
        # print('main', main_pile)
    # debug, how many brick left in main pile (40 bricks)
    # print("left main",len(main_pile))
    return computer_pile, human_pile


def add_brick_to_discard(brick, discard_pile):
    """add the brick to the list of discard pile"""
    # insert the brick at the top of the discard pile
    discard_pile.insert(0, brick)


def find_and_replace(new_brick, brick_to_be_replaced, tower, discard_pile):
    """find a given brick to be replaced in given tower
        replace it by new brick
        check to ensure given brick to be replaced
        the given brick is put on top oc discard pile
        True if given brick is replaced, otherwise return False"""
    if brick_to_be_replaced in tower:
        # replace given brick by new brick
        tower.insert(tower.index(brick_to_be_replaced), new_brick)
        # remove the given brick from a tower
        tower.pop(tower.index(brick_to_be_replaced))
        # put given brick to discard pile
        add_brick_to_discard(brick_to_be_replaced, discard_pile)
        return True
    else:
        return False #return False if the brick transfer is not done

def human_play(human_pile, main_pile, discard_pile):
    """this allows the user to play when it is human turn.
    Ask if wanting to pick a brick from discard or main pile
    if choose from main pile, choose to use or skip
    if choose from discard pile, have to use
    if use a brick, replace one brick in a tower"""
    #intro and info
    print("Your turn, human! Your tower is like:",human_pile)

    print("Top card on discard pile:",discard_pile[0])

    #ask to pick card
    human_choice = "n"
    #identify if "m" from main pile or "d" from discard pile
    while not ((human_choice == "m") or (human_choice == "d")):
        human_choice = input("Choose a brick from discard or main pile?, enter m for main and d for discard.")
    #prepare the chosen pile a third set
    if human_choice == "m":
        brick_given = get_top_brick(main_pile)
    elif human_choice == "d":
        brick_given = get_top_brick(discard_pile)
    #pick given brick in the selected pile
    #brick_given = get_top_brick(general_pile)
    print("Here is your brick of choice,",brick_given) #either top card on main pile or top card of discard pile
    #if a main pile
    if human_choice == "m":
        human_decision = human_choose()
        if human_decision == True:
            human_replace_card(brick_given,human_pile,discard_pile)
        elif human_decision == False:
            add_brick_to_discard(brick_given,discard_pile)
    elif human_choice == "d":
        human_replace_card(brick_given,human_pile,discard_pile)
    return human_pile

def human_replace_card(brick_given,human_pile,discard_pile):
    #replace the existing brick in tower by new given brick
    brick_to_be_replaced = 0
    while brick_to_be_replaced not in human_pile:
        brick_to_be_replaced = int(input("input the number you wanna replace in the tower "))

    print("You replace "+ str(brick_to_be_replaced) + "by "+ str(brick_given))
    find_and_replace(brick_given,brick_to_be_replaced,human_pile,discard_pile)

def human_choose():
    """ask if user wants to use the main card or not"""
    decision = "o"
    while not ((decision == "y") or (decision == "n")):
        decision = input("Do you want to use this brick? enter y for Yes or n for No")
    if decision == "y":
        return True
    if decision == "n":
        return False

def computer_play(computer_pile,main_pile,discard_pile):
    """strategy:
        compare_to_tower function:
        check if the top brick of discard pile > any value in the compputer pile, execute the pair_check function.
            if not, select main pile and compare if the given brick < any value in the computer pile, reject the card
            if the given brick > any value in the pile, execute the pair_check function
        Pair_check function:
        check if the 9th number > 10th number
        if yes, then look at the given card
        if given card > 9th, select it and replace the 10th
        repeat the process from 10th to 1st brick to check if the given brick should be selected or deny
        then double check if the tower is in ascending order or not"""
    print("Computer turn")
    print("Top card on discard pile:", discard_pile[0])

    top_card_discard = discard_pile[0]
    #make decision to get given brick from main or discard pile
    choice = compare_to_tower(top_card_discard,computer_pile)

    #prepare a working pile
    if choice == "m":
        brick_given = get_top_brick(main_pile)
    elif choice == "d":
        brick_given = get_top_brick(discard_pile)

    #pick given brick in the selected pile
    #brick_given = get_top_brick(general_pile)
    print("Here is your brick of choice,",brick_given) #either top card on main pile or top card of discard pile
    #debug
    #print("computer after", computer_pile)

    if choice == "m":
        computer_decision,brick_to_be_replaced = pair_check(brick_given,computer_pile)
        #debug
        #print(computer_decision,brick_to_be_replaced)
        if computer_decision == True:
            find_and_replace(brick_given,brick_to_be_replaced,computer_pile,discard_pile)
            #debug
            #print(brick_given)
        elif computer_decision == False:
            add_brick_to_discard(brick_given,discard_pile)
    elif choice == "d":
        computer_decision,brick_to_be_replaced = pair_check(brick_given,computer_pile)
        # debug
        #print(computer_decision, brick_to_be_replaced)
        if computer_decision == True:
            find_and_replace(brick_given, brick_to_be_replaced, computer_pile, discard_pile)
        elif computer_decision == False:#even though it is false, computer cannot reject to replace an existing brick
            brick_to_be_replaced = min(computer_pile)#find a brick at minimum value in the tower and replace it
            find_and_replace(brick_given, brick_to_be_replaced, computer_pile, discard_pile)
    #debug
    #print("computer after",computer_pile)
    return computer_pile

def compare_to_tower(top_card_discard,computer_pile):
    min_tower_value = min(computer_pile)
    if min_tower_value < top_card_discard:
        computer_choice ="d"
    else:
        computer_choice = "m"
    return computer_choice

def pair_check(brick_given,computer_pile):
    #check if the given brick value from main pile is selected, return True, otherwise return False

    if brick_given < 20:
        for x in range(2, 0, -1):  # stating the number from the 3rd to 1st brick
            brick_x_value = computer_pile[x]
            brick_x_minus_one_value = computer_pile[x - 1]
            if brick_x_value < brick_x_minus_one_value:
                if brick_x_value > brick_given:
                    return False, brick_given
                elif brick_x_value < brick_given:
                    brick_to_be_replaced = brick_x_value
                    return True,brick_to_be_replaced
            else:
                return False, brick_given
    if brick_given < 40:
        for x in range(6,3, -1):  # stating the number from the 3rd to 1st brick
            brick_x_value = computer_pile[x]
            brick_x_minus_one_value = computer_pile[x - 1]
            if brick_x_value < brick_x_minus_one_value:
                if brick_x_value > brick_given:
                    return False, brick_given
                elif brick_x_value < brick_given:
                    brick_to_be_replaced = brick_x_value
                    return True,brick_to_be_replaced
            else:
                return False, brick_given
    if brick_given < 60:
        for x in range(9,7, -1):  # stating the number from the 3rd to 1st brick
            brick_x_value = computer_pile[x]
            brick_x_minus_one_value = computer_pile[x - 1]
            if brick_x_value < brick_x_minus_one_value:
                if brick_x_value > brick_given:
                    return False, brick_given
                elif brick_x_value < brick_given:
                    brick_to_be_replaced = brick_x_value
                    return True,brick_to_be_replaced
            else:
                return False, brick_given
    if brick_given == 60:
        brick_to_be_replaced = computer_pile[9]
        return True,brick_to_be_replaced

def main():
    """start the Tower Blaster game"""
    # set up a computer pile and human pile
    global computer_pile
    global human_pile
    computer_pile = []
    human_pile = []
    # set up main pile and discard pile
    main_block, discard_block = setup_bricks()
    """# debug
    print("main",main_block)
    print("discard",discard_block)"""

    # shuffle main pile
    shuffle_bricks(main_block)
    """# debug
    print("main", main_block)
    print("discard", discard_block)"""

    # at the beginning of game, deal 10 bricks per player
    deal_initial_bricks(main_block)
    print("bricks have been dealt")
    # debug
    # print("computer",computer_pile)
    # print("human",human_pile)
    # print("main",main_block)
    print("The top brick from main pile moves to the discard pile!")
    add_brick_to_discard(get_top_brick(main_block),discard_block)
    #debug
    #print("main pile:",main_block)
    #print("discard pile:",discard_block)

    game_start = True
    #when the game is on, the while loop starts
    while game_start is True:
        #computer turn
        computer_pile = computer_play(computer_pile,main_block,discard_block)
        #check if the computer tower has achieved
        game_start = not (check_tower_blaster(computer_pile))
        if (check_tower_blaster(computer_pile)):
            print("Computer has achieved the Tower Blaster, it won.")
        #check if the main pile is empty and re-shuffle the discard pile
        check_bricks(main_block,discard_block)

        #debug
        #print("Game is one",game_start)

        #human turn
        human_pile = human_play(human_pile,main_block,discard_block)
        print("Here is human's current pile:",human_pile)

        #check if human has achieved
        game_start = not (check_tower_blaster(human_pile))
        if (check_tower_blaster(human_pile)):
            print("Human has achieved the Tower Blaster, you won.")
        #debug
        #print("Game is one",game_start)

        # check if the main pile is empty and re-shuffle the discard pile
        check_bricks(main_block, discard_block)

    print("End.")
    #pass

if __name__ == "__main__":
    main()
