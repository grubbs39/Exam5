import random

def all_permutations(permList, nameList):
    size = len(nameList)

    if size == 0:
        for i in range(len(permList)):
            print(permList[i], end=', ')
        print()
    else:
        for i in range(size):
            newPerms = permList.copy()
            newPerms.append(nameList[i])
            newNames = nameList.copy()
            newNames.pop(i)
            all_permutations(newPerms, newNames)

if __name__ == "__main__":
    print("paste in your list of names and press enter: ")

    my_Donuts = ["Chocolate", "Strawberry", "Glazed", "Blueberry", "Powdered", "Bavarian Kreme", "Cinnamon", "Toasted Coconut",
    "Jelly Stick", "Old Fashioned Cake", "Vanilla Frosted with Sprinkles", "Original Stick", "Boston Kreme", "Jelly", "Butternut",
    "Double Chocolate", "Strawberry Frosted with Sprinkles", "Maple Frosted", "French Cruller","Choclate Stick","Glazed Stick"]
    hdozen_list = random.choices(my_Donuts, k=6)

    nameList = hdozen_list
    permList = []
    all_permutations(permList, nameList)

    print("\n")

    hdozen_list = random.choices(my_Donuts, k=6)
    nameList = hdozen_list
    permList = []
    all_permutations(permList, nameList)

    print("\n")
    hdozen_list = random.choices(my_Donuts, k=6)
    nameList = hdozen_list
    permList = []
    all_permutations(permList, nameList)
