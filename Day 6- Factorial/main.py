# visit this website
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

# factorial

def factorial(a):
    fact = 1
    for i in range(1, a+1):
        fact = fact*i
    return(fact)


n = int(input("Please enter the number: \n"))
print(f"Factorial of {n} is {factorial(n)}")


print("===========================")
print("finding factorial using recursion")


def rec_fact(b):
    if b == 1:
        return b
    else:
        return b*rec_fact(b-1)


c = int(input("Please enter the number: \n"))
print(f"Factorial of {c} using recurssion is {rec_fact(c)}")
