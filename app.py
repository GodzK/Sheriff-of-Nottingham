class Player:
    def __init__(self, player_id):
        self.player_id = player_id
        self.name = ""
        self.coins = 50
        self.cards = []
        self.items = {"apple": 0, "bread": 0, "cheese": 0, "chicken": 0}
        self.character = None

    def set_name(self, name):
        self.name = name

    def choose_character(self, character):
        self.character = character

class SheriffGame:
    def __init__(self):
        self.players = [Player(i + 1) for i in range(4)]
        self.characters = [
            "Black Market Bartholomew 🏴",
            "Lady Raven 👑",
            "William the Wild ⚔️",
            "Cheating Chad 🎭",
            "Red Robin 🦅"
        ]
        self.available_characters = self.characters.copy()
        self.legal_goods = {
            "apple": "🍏",
            "bread": "🍞",
            "cheese": "🧀",
            "chicken": "🍗"
        }
        self.contraband_goods = {
            "pepper": "🌶️",
            "mead": "🍺",
            "silk": "🧣",
            "crossbow": "🏹"
        }

    def assign_character(self, player_id, character_choice):
        if character_choice in self.available_characters:
            self.players[player_id - 1].choose_character(character_choice)
            self.available_characters.remove(character_choice)
        else:
            print("ตัวละครนี้ถูกเลือกไปแล้ว! กรุณาเลือกใหม่")


class UI:
    def __init__(self, game_instance):
        self.game = game_instance

    def welcome(self):
        print("------------- Welcome To Sheriff of Nottingham ---------- 🔫")
        print("             Select Your Character                ")
        self.show_characters()

    def show_characters(self):
        print("Available Characters:")
        for idx, char in enumerate(self.game.available_characters):
            print(f"[{idx}] {char}")

    def get_player_names(self):
        for player in self.game.players:
            name = input(f"Enter Player {player.player_id}'s name: ")
            player.set_name(name)

    def select_characters(self):
        for player in self.game.players:
            print(f"\n{player.name}, please choose your character:")
            self.show_characters()
            while True:
                try:
                    choice = int(input("Enter the number of your chosen character: "))
                    if 0 <= choice < len(self.game.available_characters):
                        self.game.assign_character(player.player_id, self.game.available_characters[choice])
                        break
                    else:
                        print("Invalid choice! Please select a valid number.")
                except ValueError:
                    print("Please enter a number.")

    def show_players(self):
        print("\n------------- Player Information --------------")
        for player in self.game.players:
            print(f"Player {player.player_id}: {player.name} | Character: {player.character} | Coins: {player.coins}")

    def start_game(self):
        self.welcome()
        self.get_player_names()
        self.select_characters()
        self.show_players()


def main():
    game_instance = SheriffGame()
    ui_instance = UI(game_instance)
    ui_instance.start_game()


if __name__ == "__main__":
    main()