from openai import OpenAI

client = OpenAI(
    api_key="enter your api key for openai inside these quotes"
)

running = True
stories = {}
story_titles = []
class Story:
    def __init__(self):
        while True:
            self.title = input("Enter the title of your story: ")
            if self.title in story_titles:
                print("You already made a story with this title!")
                continue
            else:
                break
            
        self.theme = input("Enter the theme(s) of your story: ")
        self.characters = input("Enter the names of all the characters in the story: ")

    def get_title(self):
        return self.title

    def get_theme(self):
        return self.theme

    def get_characters(self):
        return self.characters
    



while running:
        print()
        opt = input("New story, (n), view past stories (v), or quit (q)?: ")
        print()
        if opt.lower() == "n":

            story = Story()
            generate_story = [
              
                {"role": "system",
                "content": "You are a narrator who narrates a story of " + story.get_title() +", and the theme of the story is: " + story.get_theme() + ", and the names of all characters of the story are: " + story.get_characters() + "."}
             ]

            response = client.chat.completions.create(model="gpt-3.5-turbo", messages=generate_story)

            my_story = response.choices[0].message.content
            stories[story.get_title()] = my_story
            story_titles.append(story.get_title())
            print(story.get_title())
            print(my_story)
            print()

        elif opt.lower() == "v":
            if stories:
                print("Here are your stories:")
                for i in range(len(story_titles)):
                    print(story_titles[i])

                while True:
                    choice = input("Enter the title of the story that you want to view: ")
                    if choice in story_titles:
                        print()
                        print(stories[choice])
                        break
                    else:
                        continue
            else:
                print("You do not have any stories!")

        elif opt.lower() == "q":
            running = False
