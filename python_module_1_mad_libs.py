import datetime

stories = {
    "1": (
        "A Day at the Zoo",
        "Today I saw a {adj} {noun}. It was {verb_ing} around "
        "and suddenly started to {verb} {adverb}!"
    ),
    "2": (
        "Space Mission",
        "Captain {name} went to {place} to find a {adj} {noun}. "
        "Suddenly, a space {noun2} appeared!"
    ),
    "3": (
        "Mystery Chef",
        "Chef {name} made a {adj} dish using {noun}. "
        "The judges said it tasted {adverb}!"
    )
}

while True:
    print("\n--- MAD LIBS GAME ---")
    print("1. A Day at the Zoo")
    print("2. Space Mission")
    print("3. Mystery Chef")
    print("Q. Quit")

    choice = input("Choose: ").lower()

    if choice == "q":
        print("Thanks for playing!")
        break

    if choice not in stories:
        print("Invalid choice!")
        continue

    title, story = stories[choice]
    words = {}

    for word in ["adj", "noun", "verb_ing", "verb", "adverb",
                 "name", "place", "noun2"]:
        if "{" + word + "}" in story:
            words[word] = input(f"Enter {word}: ")

    result = story.format(**words)

    print("\n---", title, "---")
    print(result)

    save = input("Save story? (y/n): ").lower()

    if save == "y":
        with open("saved_mad_libs.txt", "a") as f:
            time = datetime.datetime.now()
            f.write(f"{title} ({time})\n{result}\n\n")
        print("Story saved!")
