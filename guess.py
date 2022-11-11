secret_num=9
guess_num=0
guess_limit =3
while guess_num<guess_limit:
    guess = int(input("guess the number: "))
    guess_num += 1
    if guess == secret_num:
        print("you won!")
        break
else:
 print("try again")