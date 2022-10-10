# 1 вариант 

def calc_pi(eps=1.0e-5):
        s=0 #сумма накопления
        d=1 #начальное значение делителя  
        sgn=1 #знак 
        while True:
            a=4/d
            s=s+sgn*a
            if a<eps:
                return s
            sgn=-sgn
            d=d+2
print(calc_pi())
