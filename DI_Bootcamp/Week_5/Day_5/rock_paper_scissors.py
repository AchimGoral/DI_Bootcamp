from game import Game
game = Game()

def get_user_menu_choice():
    print("Menu:")
    print("(g) Play a new game")
    print("(x) Show scores and exit")
    choice = str(input(": "))
    return choice


def print_results(results):
    for key, value in results.items():
        print(key,value)

def main():
    menu = get_user_menu_choice()
    
    while menu not in ("g", "x"):
        menu = get_user_menu_choice()
    
    if menu == 'g':

        game.play()
        
    else:
        results = game.play()
        print_results(results)

main()