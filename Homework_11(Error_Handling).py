def handling():
    #lineNum = 0
    try:
        lineNum = int(input("\nWhich line number do you wanna update: "))

    except Exception as r:
        print("\nSorry", r, "is not a number")
    else :
        print("\nYes,", lineNum, "is a number")

    finally:
        def confirm():
            ask = input("\nDo you want to try again?: ")
            if ask.casefold() == "yes".casefold():
                handling()
            elif ask.casefold() == "no".casefold():
                exit()
            else:
                print("\nRequires a 'Yes' or 'No' answer")
                confirm()

        confirm()
    return True 


handling()

