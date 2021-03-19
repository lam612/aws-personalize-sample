import random
for i in range(2000):
    user_id = random.randrange(1, 26)
    item_id = 1
    if user_id % 5 == 1:
        item_id = random.choice([1, 2, 3])
    elif user_id % 5 == 2:
        item_id = random.choice([4, 8, 7])
    elif user_id % 5 == 3:
        item_id = random.choice([1, 6, 9])
    elif user_id % 5 == 4:
        item_id = random.choice([6, 7, 10])
    elif user_id % 5 == 0:
        item_id = random.choice([4, 5, 9])
    else:
        item_id = random.randrange(1, 10)
    timestamp = random.randrange(1416122968, 1616122968)
    print(str(user_id) + ',' + str(item_id) + ',' + str(timestamp))
