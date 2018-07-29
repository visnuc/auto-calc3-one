def main():
    your_name = input("Enter your name: ")
    print("Hello, ", your_name + "!")
    user_resp = input("Are you done? [y/n]: ")
    user_resp_l = user_resp.lower()
    if user_resp_l == "n":
        main()
    else:
        exit()

if __name__ == "__main__":
    main()