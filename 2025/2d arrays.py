# 2d list is just a list made up of lists
# each individual list resembles a row
# each individual element resembles a column

fruits =     ["apple", "orange", "banana", "coconut"] #row 0
vegetables = ["celery", "carrots", "potatoes"] #row 1
meats =      ["chicken", "fish", "turkey"] # row 2

groceries = [["apple", "orange", "banana", "coconut"], ["celery", "carrots", "potatoes"], ["chicken", "fish", "turkey"]]

# [row][column]

for collection in groceries:
    for food in collection:
        pass
        #print(food)
    #print()


# create a 2d keypad, like on a flip phone
numpad = [[1,2,3], [4,5,6], [7,8,9]]

# print the number
for number in numpad:
    pass
    #print(number)

# add numpad up, should equal 6, 15, 24
counter = 0
for row in numpad:
    for number in row:
        counter = number + counter
    print(counter)
    counter = 0