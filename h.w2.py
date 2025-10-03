for i in range(3):
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == "admin" and password == "1234":
        print("login ")
        N = int(input("Enter a number: "))

        for num in range(2, N+1):
            is_prime = True
            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                print(num)

        break
    else:
        if i == 2:
            print("Account locked")