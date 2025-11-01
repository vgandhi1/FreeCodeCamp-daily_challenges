def prime_check(n):
    if n <=0:
        raise ValueError("Input number must be a positive integer (n >= 1).")
    if n== 1:
        return False
    if n==2:
        return True

    if n%2 == 0:
        return False
    
    primt_list = [2]
    limit = int(n**0.5)

    for div in range(3,limit+1,2):
        if n % div == 0:
            return False
        #else:
    return True
            
            
#prime_check(293), prime_check(307), prime_check(309), prime_check(20)
prime_check(-15)
