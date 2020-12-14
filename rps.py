import random

class Game: 

    CHOICES = ['r', 'p', 's']

    def __init__(self): 
        self.scores = {
            'player' : 0,
            'computer' : 0,
        }
    
    def check_player_validity(self, player): 
        if player != 'player' and player != 'computer': 
            raise ValueError("Argument 'player' is not valid")

    def get_score(self, player):
        self.check_player_validity(player)
        return self.scores[player]

    def increment_score(self, player): 
        self.check_player_validity(player)
        self.scores[player] += 1

    def validatate_player_input(self, player_input): 
        if not (player_input == 'r' or  player_input == 'p' or player_input == 's' or player_input == 'q'):
            return False
        else: return True
        
    def print_round_result(self, winner, player_score, computer_score):
        if winner == 'player': 
            message = "You win!"
        elif winner == 'computer': 
            message = "Computer wins!" 
        elif winner == 'tie': 
            message = "Tie!"
        else: 
            raise ValueError("Argument 'winner' is not valid")

        if player_score < 0 or computer_score < 0: 
            raise ValueError("Player and computer score must be >= 0")
        
        print("%s Score: Player = %s, Computer = %s\n" % (message, player_score, computer_score))

    def end_game(self): 
        print("Game ended. Final score: Player = %s, Computer = %s" % (self.get_score('player'), self.get_score('computer')))
        quit()

    def game_logic(self, player_input, computer_input): # assume player_input has already been checked
        player_choice = player_input
        computer_choice = computer_input
        if player_choice == 'q': 
            return -999
        if ((player_choice == 'r' and computer_choice == 's') 
                or (player_choice == 's' and computer_choice == 'p') 
                or (player_choice == 'p' and computer_choice == 'r')):
            return 1
        elif player_choice == computer_choice: 
            return 0
        else: 
            return -1

    def game_controller(self, result): 
        if result == 1: # Win
            self.increment_score('player')
            self.print_round_result('player', self.get_score('player'), self.get_score('computer'))
        elif result == 0: # Tie
            self.print_round_result('tie', self.get_score('player'), self.get_score('computer'))
        elif result == -1: 
            self.increment_score('computer')
            self.print_round_result('computer', self.get_score('player'), self.get_score('computer'))
        elif result == -999: 
            self.end_game()

    def play(self): 
        while True: # continue until game is ended
            player_choice = input("Please enter your choice ('r/p/s'). Enter 'q' to quit: ")
            computer_choice = random.choice(self.CHOICES)
            if self.validatate_player_input(player_choice): 
                print("You chose %s, the computer chose %s." % (player_choice, computer_choice))
                result = self.game_logic(player_choice, computer_choice)
                self.game_controller(result)
            else: 
                print("Invalid entry, please enter 'r', 'p', 's', or 'q'.\n")
  
if __name__ == '__main__': 
    gm = Game()
    gm.play()
    
