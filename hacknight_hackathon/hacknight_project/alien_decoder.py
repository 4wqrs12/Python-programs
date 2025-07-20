from time import *
aura= 50
completed_lvls = []
part1_key = {
    'A': '🌟',
    'B': '🍕',
    'C': '😂',
    'D': '🚀',
    'E': '💡',
    'F': '🎉',
    'G': '📱',
    'H': '🍩',
    'I': '🎯',
    'J': '🧠',
    'K': '🍔',
    'L': '🌊',
    'M': '📷',
    'N': '🎲',
    'O': '💪',
    'P': '😎',
    'Q': '📚',
    'R': '❤️',
    'S': '🧩',
    'T': '😊',
    'U': '🔒',
    'V': '⚽',
    'W': '😅',
    'X': '🕹️',
    'Y': '🙏',
    'Z': '🔥'
}

part1_answer = {
    "😊🍩💡🧩😊🌟❤️🧩🌟❤️💡🌟🌊🎯📱🎲🎯🎲📱": "Thestarsarealigning",
    "😊🍩💡🙏🌟❤️💡😂💪📷🎯🎲📱🎉💪❤️🔒🧩": "Theyarecomingforus",
    "🚀💪🎲💪😊❤️💡🧩🎯🧩😊😊🍩💡🎯❤️😂🌟🌊🌊": "Donotresisttheircall",
    "🙏💪🔒😅🎯🌊🌊🍕💡😂🍩🌟🎲📱💡🚀🎉💪❤️💡⚽💡❤️": "Youwillbechangedforever",
    "😅💡🌟❤️💡🌟🌊❤️💡🌟🚀🙏🍩💡❤️💡": "Wearealreadyhere"

}

part2_answer = {
    "dehctawgnieberaewtubecaepniemocyehT": "Theycomeinpeacebutwearebeingwatched",
    "ycneuqerfehtdnatsrednutsumuoY": "Youmustunderstandthefrequency",
    "evitamrofsnartsirewopriehT": "Theirpoweristransformative",
    "stimilruodnoyebegdelwonksureffoyehT": "Theyofferusknowledgebeyondourlimits",
    "llaflliwewrotpadalliweW": "Youmustdecidenow"
}

part3_key = {
    'A': 'D', 'B': 'E', 'C': 'F', 'D': 'G', 'E': 'H', 'F': 'I', 'G': 'J', 'H': 'K', 'I': 'L', 'J': 'M',
    'K': 'N', 'L': 'O', 'M': 'P', 'N': 'Q', 'O': 'R', 'P': 'S', 'Q': 'T', 'R': 'U', 'S': 'V', 'T': 'W',
    'U': 'X', 'V': 'Y', 'W': 'Z', 'X': 'A', 'Y': 'B', 'Z': 'C'
}

part3_answer = {
    "BRXVWDQGDWWKHFURVVURDGV": "Youstandatthecrossroads",
    "WKHWLPHKDVFRPHIRUDFWLRQ":"Thetimehascomeforaction",
    "BRXUGHFLVLRQZLOOFKDQJHWKHFRXUVH":"Yourdecisionwillchangethecourse",
    "WKHFKRLFHBRXPDNHZLOOUHVRQDWHIRUHYHU":"Thechoiceyoumakewillresonateforever",
    "ZLOOBRXVXEPLWRUWDNHFRQWURO":"Willyousubmitortakecontrol"
}

easy1_questions = {}

class Level():
    def __init__(self):
        self.key = {}
        self.difficulty = ""

    

    
    def get_difficulty(self):
        return self.difficulty

    def display_key(self):
        for k, v in self.key.items():
            print(f"{k}:{v}",end=" ")
    
    def get_difficulty(self):
        return self.difficulty
    
    def questions(self,answer_key):
        
        global aura
        if self.get_difficulty() in ("easy","medium"):
            print()
            print("Decode the following to advance to the next level: ")
            for k, v in answer_key.items():
                while True:
                    guess = input(f"Decode \"{k}\": ")
                    converted = guess.replace(" ","")
                    print("Checking...")
                    sleep(2)
                    if converted.lower() == v.lower():
                        print("Correct")
                        break
                    else:
                        aura -= 10
                        print(f"Incorrect, try again. -10 aura. {aura} aura")
                        if aura == 0:
                            print("You died!")
                            quit()
        else:
            print("Decode the following to save to Earth: ")
            for k, v in answer_key.items():
                while True:
                    guess = input(f"Decode \"{k}\": ")
                    converted = guess.replace(" ","")
                    print("Checking...")
                    sleep(2)
                    if converted.lower() == v.lower():
                        print("Correct")
                        break
                    else:
                        aura -= 10
                        print(f"Incorrect, try again. -10 aura. {aura} aura")
                        if aura == 0:
                            print("You died!")
                            quit()

        
                


    



        
    
    
class Level1(Level):
    def __init__(self,key):
        super().__init__()
        self.key = key
        self.difficulty = "easy"
        self.display_key()
        self.questions(part1_answer)

class Level2(Level):
    def __init__(self,key=None):
        super().__init__()
        self.key = key
        self.difficulty = "medium"
        self.questions(part2_answer)

class Level3(Level):
    def __init__(self,key=None):
        super().__init__()
        self.key = key
        self.difficulty = "hard"
        self.questions(part3_answer)
        

        
print('''
      Alien Decode
      Current aura: 100
      ''')

sleep(2)

def game():
    print("         PART 1")
    print(">------THE ARRIVAL------<")
    sleep(2)
    lvl1 = Level1(part1_key)
    sleep(2)
    print("         PART 2")
    print(">------The Encounter------<")
    sleep(2)
    lvl2 = Level2()

    print("         PART 3")
    print(">------The Decision------<")
    sleep(2)
    lvl3 = Level3()







game()


