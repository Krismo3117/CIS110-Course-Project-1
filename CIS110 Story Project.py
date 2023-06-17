print("Welcome, adventurer, to the mystical realm of Dungeons and Dragons!")
print("Before we embark on our epic journey, let me ask you a few questions.")
print("After answering each question, press the enter key to proceed.")
input("\nPress the enter key to begin...")
#5 Questions Before the story begins
characterClass = input("\nChoose a character class (e.g., wizard, warrior, rogue):  ")
while len(characterClass) == 0:
    characterClass = input("Please enter a character class:  ")
#Second Question
characterName = input("What is your character's name:  ")
while len(characterName) == 0:
    characterName = input("Please enter a character name:  ")
#Third Question
hometown = input("Where is your character's hometown:  ")
while len(hometown) == 0:
    hometown = input("Please enter a hometown:  ")
#Fourth Question
favoriteWeapon = input("What is your character's favorite weapon:  ")
while len(favoriteWeapon) == 0:
    favoriteWeapon = input("Please enter a favorite weapon:  ")
#Fifth Question
number = input("What is your favorite number:  ")
while not number.isdigit():
    number = input("Value not recognized. Please enter a numeric value:  ")

#Story Starts
print("\nLET'S BEGIN!!!")
print(f"\nOnce upon a time, in the mystical land of {hometown}, there was a brave {characterClass} named {characterName}. ")
print(f"{characterName} always dreamt of embarking on an epic adventure. ")
print(f"Today was {characterName}'s chance. A magical portal appeared before them! ")
print(f"{characterName} stepped into the portal, ready to face the unknown. ")
print(f"While traversing through the portal, {characterName} arrived at a dark dungeon. The air was heavy with anticipation. ")

#Decision 1
exploreDungeon = input("\nShould your character explore the dungeon? Type yes or no:  ")
while exploreDungeon.lower() != "yes" and exploreDungeon.lower() != "no":
    exploreDungeon = input("Please type yes or no:  ")

if exploreDungeon == "yes":
    print(f"\n{characterName} cautiously enters the dungeon, {favoriteWeapon} in hand. ")
    print(f"As {characterName} ventures deeper, they encounter dangerous traps and fearsome monsters. ")
    print(f"{characterName} fights valiantly, defeating {number} enemies and collecting valuable treasures. ")
    print(f"However, the dungeon is vast and filled with perils. {characterName} must proceed with caution. ")
    print(f"Their journey through the dungeon continues, with the promise of glory and riches awaiting them. ")
else:
    print(f"\n{characterName} decides it's too risky to enter the dungeon alone. ")
    print(f"Preferring safety over adventure, {characterName} explores the surrounding area of {hometown} instead. ")
    print(f"{characterName} spends {number} hours enjoying the familiar sights and sounds of their hometown. ")
    print(f"While it may not be an epic quest, {characterName} finds solace in the comforts of home. ")

print(f"After a day of exploration, {characterName} stumbles upon a mysterious cave. ")
print(f"The cave entrance emanates an otherworldly glow. It beckons {characterName} to enter. ")

#Decision 2
enterCave = input(f"\nShould {characterName} enter the mysterious cave? Type yes or no:  ")
while enterCave.lower() != "yes" and enterCave.lower() != "no":
    enterCave = input(f"Please type yes or no:  ")

if enterCave == "yes":
    print(f"\nWith curiosity driving them forward, {characterName} enters the cave, {favoriteWeapon} at the ready. ")
    print(f"The cave's interior is filled with enchanting crystals and ethereal beings. ")
    print(f"{characterName} discovers a hidden treasure chest and unlocks it using their skills. ")
    print(f"Inside, they find {number} magical artifacts that grant incredible powers. ")
    print(f"Now equipped with these newfound abilities, {characterName} is ready to face even greater challenges. ")
else:
    print(f"\n{characterName} decides to resist the temptation and avoids entering the mysterious cave. ")
    print(f"Feeling content with their current abilities and possessions, {characterName} continues their journey elsewhere. ")
    print(f"There are still many adventures to be had and mysteries to unravel. ")

#Alternate Endings
if exploreDungeon == "yes" and enterCave == "yes":
    print(f"\nAfter a day of daring exploration in the dungeon and discovering the treasures of the mysterious cave, ")
    print(f"{characterName} becomes a legendary hero, revered by all in {hometown}. ")
    print(f"Their name echoes through the land, forever etched in the annals of adventure. ")
elif exploreDungeon == "no" and enterCave == "no":
    print(f"\nAfter a day of leisurely exploration and resisting the allure of the mysterious cave, ")
    print(f"{characterName} returns to {hometown} with fond memories and a heart full of contentment. ")
    print(f"Their journey may not have been grand, but it was uniquely their own. ")
else:
    print(f"\nAfter a day of exploration in the dungeon and resisting the allure of the mysterious cave, ")
    print(f"{characterName} returns to {hometown} with newfound knowledge and experiences. ")
    print(f"Their adventures have only just begun, and the path ahead holds infinite possibilities. ")
print(f"\nThe End")

keepPlaying = input(f"\nDo you want to play again? Enter yes or no:  ")
while keepPlaying.lower() != "yes" and keepPlaying.lower() != "no":
    keepPlaying = input(f"Please type yes or no:  ")
