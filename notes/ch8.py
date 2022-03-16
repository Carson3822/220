
def game_is_over(player_one_points, player_two_points):
    over_fifteen = player_one_points >= 15 or player_two_points >= 2
    won_by_two = abs(player_one_points - player_two_points) >= 2
    skunked = player_one_points >= 7 and player_two_points == 0 or player_two_points >= 7 and player_one_points == 0
    if (over_fifteen and won_by_two) or skunked:
        return True
    return False



if __name__ == "__main__":
    player_1 = 0
    player_2 = 0
    print(player_1, player_2)
    while not is_game_over(player_1, player_2):
        one_points, two_points = eval(input("enter points for player 1 and 2: "))
        player_1 = player_1 + one_points
        player_2 = player_2 + two_points
        print(player_1, player_2)
    print("GAME OVER!")

 #can break loops with keyword break will stop loop when loop hits break
 #bc of this can do things like while True
# above check
# break can be tricky to debug and tel when loop will finish
# x == and
# + == or
# 0 == False
# 1 == True

# a x 0 = 0 boolean is a and False == False
#a x 1 = a boolean is a and True == a
#a + 0 = a boolean is a or False == a
# a or True == True

#double negatives cancel out not not


#distributive property
# a or (b and c) == (a or b) and (a or c)
# a and (b or c) == (a and b) or (a and c)

#DeMorgan's law
# if we have not(a or b) == (not a) and (not b) have to switch sign in middle
# not(a and b) == (not a) or (not b)

#proof
def DeMorgan_one(a,b):
   return not(a or b) == (not a) and (not b)

def DeMoregan_test():
    tests = [[True, True], [True, False], [False, True], [False, False]]
    for test in tests:
        a = test[0]
        b = test[1]
        result = DeMorgan_one(a, b)
        print("input: {}, output: {}".format(test, result))

def DeMorgan_two():
    return not(a and b) == (not a) or (not b)

def DeMoregan_test_two():
    tests = [[True, True], [True, False], [False, True], [False, False]]
    for test in tests:
        a = test[0]
        b = test[1]
        result = DeMorgan_two(a, b)
        print("input: {}, output: {}".format(test, result))

#truthy/falsy values
#other data types that are treated like boolean data

# 0, '', [] act like false (falsy)
