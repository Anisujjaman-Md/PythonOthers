# What 3 Number Addition is 13 [12, 1, 8, 5, 6 , 4, 5] 

num = [12, 3, 8, 5, 6 , 4, 5]

def main():  
    for item in num:
        for item_ in num:
            for item__ in num:
                if item != item_ and item != item__ and item_ != item__ and item + item_ + item__ == 13:
                    # print(item, item_, item__)
                    # break
                    return print(item, item_, item__)

main()