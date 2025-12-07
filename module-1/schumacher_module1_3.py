# calebSchumacher07122025module1_3
# Take user input for number of beer bottles in "100 Bottles of Beer" song



def bottleCounter():

    bottles = input("Please enter how many bottles of beer are on the wall: ")
    
    try:
        remaining = int(bottles)
    except ValueError:
        print("Please enter a valid number of bottles.")
        return

    while remaining > 0:

        if remaining == 1:

            print(f"{remaining} bottle of beer on the wall, {remaining} bottle of beer,")
            print("Take one down, pass it around,")
            remaining = remaining - 1
            print(f"{remaining} bottles of beer on the wall.")
        else:
            print(f"{remaining} bottles of beer on the wall, {remaining} bottles of beer,")
            print("Take one down, pass it around,")
            remaining = remaining - 1
            if remaining == 1:
                print(f"{remaining} bottle of beer on the wall.")
            else:
                print(f"{remaining} bottles of beer on the wall.")

    print("Time to buy more bottles of beer.")
        












def main():
    bottleCounter()


if __name__ == "__main__":
    main()

