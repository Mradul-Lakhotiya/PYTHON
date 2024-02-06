from GameData import data
import random

person1 = random.choice(data)
person2 = random.choice(data)

game_over = False
ans = 'A'
count = 0

while(not game_over):
    print("Which has more Followers")
    print(f"\nA: {person1['name']} from {person1['country']} is a {person1['description']}\n\t\tVS")
    #print(person1['follower_count'])
    print(f"B: {person2['name']} from {person2['country']} is a {person2['description']}\n")
    #print(person2['follower_count'])

    print("Ans : ")
    ans = input()[0].upper()

    if (ans == 'A' and person1['follower_count'] > person2['follower_count']):
        print("\nYOU WIN\n")
        person2 = random.choice(data)
        count += 1
    elif (ans == 'B' and person2['follower_count'] > person1['follower_count']):
        print("\nYOU WIN\n")
        person1 = person2
        person2 = random.choice(data)
        count += 1
    else:
        game_over = True

print("GAME OVER")
print(f"Your Total Score Was : {count}")