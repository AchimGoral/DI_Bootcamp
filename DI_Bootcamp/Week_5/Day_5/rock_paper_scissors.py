from game import Game
game = Game()

def get_user_menu_choice():
    print("\nMenu:")
    print("(g) Play a new game")
    print("(x) Show scores and exit")
    choice = str(input(": "))
    return choice


def print_results(results):
    print("\nHere are your results:")
    for key, value in results.items():
        print(key,value)
    print("")

def main():
    while True:
        menu = get_user_menu_choice()
        while menu not in ("g", "x"):
            menu = get_user_menu_choice()
        if menu == 'g':
            results = game.play() 
        else:
            print_results(results)
            return False

main()