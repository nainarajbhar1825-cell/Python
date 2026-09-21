import datetime
import os


class MadLibsGenerator:

    def __init__(self):
        # Predefined story templates with placeholder tags
        self.templates = {
            "1": {
                "title": "A Day at the Zoo",
                "story": (
                    "Today, I went to the zoo and saw a very {adjective1} {noun1}. "
                    "It was {verb_ing} around its enclosure, looking for a {noun2}. "
                    "Suddenly, it started to {verb} {adverb}! Everyone at the zoo was so "
                    "{adjective2} that they ran straight to {place}."
                ),
                "prompts": [
                    ("adjective1", "Adjective (describing word)"),
                    ("noun1", "Noun (animal or object)"),
                    ("verb_ing", "Verb ending in -ING"),
                    ("noun2", "Noun (thing)"),
                    ("verb", "Verb (action word)"),
                    ("adverb", "Adverb (ends in -ly, e.g., quickly)"),
                    ("adjective2", "Adjective (emotion or feeling)"),
                    ("place", "Place"),
                ],
            },
            "2": {
                "title": "The Sci-Fi Space Mission",
                "story": (
                    "Captain {name} launched the spaceship into {place}. "
                    "The mission was to find the legendary {adjective1} {noun1}. "
                    "While floating in zero gravity, the crew decided to {verb1} "
                    "while eating {adjective2} {plural_noun}. Suddenly, the radar beeped "
                    "{adverb}! A giant space {noun2} appeared and began to {verb2}!"
                ),
                "prompts": [
                    ("name", "Proper Name"),
                    ("place", "Place in outer space"),
                    ("adjective1", "Adjective"),
                    ("noun1", "Noun"),
                    ("verb1", "Verb"),
                    ("adjective2", "Adjective"),
                    ("plural_noun", "Plural Noun"),
                    ("adverb", "Adverb"),
                    ("noun2", "Noun"),
                    ("verb2", "Verb"),
                ],
            },
            "3": {
                "title": "The Mystery Chef",
                "story": (
                    "Welcome to the Grand Cooking Competition! Today's secret ingredient is {noun1}. "
                    "Chef {name} decided to make a {adjective1} dish by {verb_ing} the ingredient "
                    "with {adjective2} {plural_noun}. The judges took a bite and said, 'This tastes "
                    "{adverb} {adjective3}!' Chef {name} was awarded a trophy made of pure {noun2}."
                ),
                "prompts": [
                    ("noun1", "Noun (food or object)"),
                    ("name", "Name"),
                    ("adjective1", "Adjective"),
                    ("verb_ing", "Verb ending in -ING"),
                    ("adjective2", "Adjective"),
                    ("plural_noun", "Plural Noun"),
                    ("adverb", "Adverb"),
                    ("adjective3", "Adjective"),
                    ("noun2", "Noun (material or object)"),
                ],
            },
        }

    def display_menu(self):
        """Displays the story selection menu."""
        print("\n========================================")
        print("      Welcome to the Mad Libs Game!      ")
        print("========================================")
        print("Choose a story template:")
        for key, template in self.templates.items():
            print(f"  [{key}] {template['title']}")
        print("  [Q] Quit Game")

    def collect_words(self, prompts):
        """Prompts the user to enter words for each category."""
        print("\n--- Enter the requested words ---")
        user_words = {}
        for key, description in prompts:
            while True:
                word = input(f"Enter a {description}: ").strip()
                if word:
                    user_words[key] = word
                    break
                print("Input cannot be empty. Please try again!")
        return user_words

    def save_story(self, title, story):
        """Saves the completed story to a text file."""
        filename = "saved_mad_libs.txt"
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(filename, "a", encoding="utf-8") as file:
            file.write(f"=== {title} ({timestamp}) ===\n")
            file.write(story + "\n\n")

        print(f"\n[Saved] Your story has been saved to '{filename}'!")

    def play(self):
        """Main game loop."""
        while True:
            self.display_menu()
            choice = input("\nSelect an option (1-3 or Q): ").strip().lower()

            if choice == "q":
                print("\nThanks for playing Mad Libs! Goodbye! 👋")
                break

            if choice in self.templates:
                selected_template = self.templates[choice]
                title = selected_template["title"]
                story_format = selected_template["story"]
                prompts = selected_template["prompts"]

                # 1. Collect inputs from user
                user_words = self.collect_words(prompts)

                # 2. Generate the story by unpacking user inputs
                completed_story = story_format.format(**user_words)

                # 3. Display the final result
                print("\n" + "=" * 40)
                print(f"       {title.upper()}       ")
                print("=" * 40)
                print(completed_story)
                print("=" * 40)

                # 4. Ask to save
                save_choice = (
                    input("\nWould you like to save this story? (y/n): ")
                    .strip()
                    .lower()
                )
                if save_choice == "y":
                    self.save_story(title, completed_story)

                # 5. Play again prompt
                again = (
                    input("\nDo you want to play another story? (y/n): ")
                    .strip()
                    .lower()
                )
                if again != "y":
                    print("\nThanks for playing Mad Libs! Goodbye! 👋")
                    break
            else:
                print("\nInvalid choice! Please select a valid option.")


if __name__ == "__main__":
    game = MadLibsGenerator()
    game.play()