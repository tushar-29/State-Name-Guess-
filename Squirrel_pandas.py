import pandas


data = pandas.read_csv("Squirrel_Data.csv")
fur_color = data["Primary Fur Color"].to_list()
black_fur = fur_color.count("Black")
cinnamon_fur = fur_color.count("Cinnamon")
gray_fur = fur_color.count("Gray")
print(black_fur)
print(cinnamon_fur)
print(gray_fur)

dict_fur_col = {
                        "Fur Color": ["Gray", "Black", "Cinnamon"],
                            "No. of Sq.": [gray_fur, black_fur, cinnamon_fur]
                        }
fur = pandas.DataFrame(dict_fur_col)
print(fur)
