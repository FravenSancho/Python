def num_Primo(num):
    for n in range(2, num):
        if num % n == 0:
            print("{} No es primo \nporque es divisible entre {}".format(num,n))
            return False
    print("{} es PRIMO".format(num))
    return True

num_Primo(5)
