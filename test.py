def main():
    your_name = input("Enter your name: ")
    print("Hello, ", your_name + "!")
    l_resp = input("Are you done? [y/n]: ")
    if l_resp == "y":
        exit()
    else:
        main()



if __name__ == "__main__":
    main()