from random import randint
chances=3
score=0
print("you have 3 chances to make a right guess")
print("enter the lower and upper bound range to start the game")
mood =str(input("you want to play:"))
l=int(input("lower bound= "))
u=int(input("upper bound= "))
rand_int = randint(l,u)

    
while chances>0:
    guess=int(input("make a guess\n"))
    if guess == rand_int:
        score+=1
        print("congrates you won")
        print("your score:",score)
        break
    elif guess>rand_int:
        chances-=1
        print("wrong guess enter lesser value , chances left:",chances)
    elif guess<rand_int:
        chances-=1
        print("wrong guess enter higher value, chances left:",chances)
    if chances==0:
        print("!!!!!!you lost!!!!!!")
        print("your score:",score)
