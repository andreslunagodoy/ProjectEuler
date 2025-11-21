#This is a bunch of functions I use recurrently

#Primes related
prime_bound = 10000000
print(f"Generating primes under {prime_bound}")

def is_prime_aux(n):
    if n < 2:
        return False
    else:
        for j in my_list_of_primes:
            if j**2 > n:
                return True
            elif n % j == 0:
                return False

my_list_of_primes = [2,3]
n = 1
while 6*n + 1 < prime_bound:
    if is_prime_aux(6*n - 1):
        my_list_of_primes.append(6*n - 1)
    if is_prime_aux(6*n + 1):
        my_list_of_primes.append(6*n + 1)
    n = n + 1
    
def primes_under(j):
    my_primes_under = [2,3]
    n = 1
    while 6*n + 1 < j:
        if is_prime_aux(6*n - 1):
            my_primes_under.append(6*n - 1)
        if is_prime_aux(6*n + 1):
            my_primes_under.append(6*n + 1)
        n = n + 1
    return my_primes_under
    
def primes_between(j,k):
    if j > 3:
        primes_between_jk = []
    elif j == 3:
        primes_between_jk = [3]
    else:
        primes_between_jk = [2,3]
    n = 1
    while 6*n + 1 < k:
        if 6*n + 1 > j:
            if is_prime_aux(6*n - 1):
                primes_between_jk.append(6*n - 1)
            if is_prime_aux(6*n + 1):
                primes_between_jk.append(6*n + 1)
        n = n + 1
    return primes_between_jk

#Factors
def find_first_prime_factor(n):
    for j in my_list_of_primes:
        if j**2 > n:
            return n
        elif n % j == 0:
            return j
        
def factor_integer(n):
    factors = []
    aux = find_first_prime_factor(n)
    factors.append(aux)
    if aux == n:
        return factors
    else:
        return factors + factor_integer(n // aux)
    
def all_divisors(n):
    divisors = [1]
    for i in all_subsets(factor_integer(n)):
        divisors.append(total_product_list(i))
    divisors = list(set(divisors))
    divisors.sort()
    return divisors

def proper_divisors(n):
    my_proper_divisors = all_divisors(n)
    my_proper_divisors.remove(n)
    return my_proper_divisors


#Operations on numbers
def to_digits(n):
    my_digits=[]
    aux = n
    while aux >= 10:
        my_digits.append(aux % 10)
        aux = (aux - (aux % 10)) // 10
    my_digits.append(aux)
    my_digits.reverse()
    return my_digits

def digits_to_integer(my_list):
    total=0
    for j in range(len(my_list)):
        total += my_list[-j-1]*10**j
    return total

def factorial(n):
    my_factorial=1
    if n==0:
        return 1
    elif n==1:
        return my_factorial
    else:
        return n*factorial(n-1)
    
def binomial(n,i):
    return factorial(n)//(factorial(n-i)*factorial(i))

def is_palyndrome(n):
    my_digits = to_digits(n)
    j = 1
    while j <= len(my_digits)/2:
        if my_digits[-j]!= my_digits[j-1]:
            return False
        j +=1
    return True


#Operations on lists
def total_sum_list(my_list):
    my_sum=0
    for i in my_list:
        my_sum += i
    return my_sum

def total_product_list(my_list):
    my_product=1
    for i in my_list:
        my_product *= i
    return my_product

def take_one(my_list):
    singles=[]
    for i in my_list:
        singles.append([i])
    return singles

def omit_position(my_list,pos):
    new_list=[]
    for j in range(len(my_list)):
        if j != pos:
            new_list.append(my_list[j])
    return new_list

def omit_after_position(my_list,pos):
    new_list=[]
    for j in range(pos+1,len(my_list)):
        new_list.append(my_list[j])
    return new_list

def subsets(my_list,n):
    out_subsets=[]
    if n == 1:
        for i in take_one(my_list):
            out_subsets.append(i)
    else:
        for j in range(len(my_list)):
            for k in subsets(omit_after_position(my_list,j),n-1):
                out_subsets.append([my_list[j]]+k)
    return out_subsets

def all_subsets(my_list):
    all_subsets_out=[]
    for i in range (len(my_list)):
        all_subsets_out += subsets(my_list,i+1)
    return all_subsets_out

def permutations(my_list,n):
    out_permutations=[]
    if n == 1:
        for i in take_one(my_list):
            out_permutations.append(i)
    else:
        for j in range(len(my_list)):
            for k in permutations(omit_position(my_list,j),n-1):
                out_permutations.append([my_list[j]]+k)
    return out_permutations