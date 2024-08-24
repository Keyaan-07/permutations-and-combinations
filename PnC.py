def factorial(n):
    ans = 1
    for i in range(1, n+1):
        ans = ans*i
    return ans 

def permutations(n, r):
    ans = factorial(n)/factorial(n-r)
    print(int(ans))

def combinations(n, r):
    ans = factorial(n)/factorial(r)/factorial(n-r)
    print(int(ans))

while 1:
    print("Do You want to calculate a Permutation or Combination(only numbers) \n-[P]ermutation \n-[C]ombination \n-[E]xit")
    x = input("")

    if x == 'p' or x == 'P':
        n = int(input("enter value of n:"))
        