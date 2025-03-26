
def setKthDigitToComplement(n, k):
    isNegative = (n < 0)
    n = abs(n)
    
    if k > 0 and (n // (10**k) == 0):
        print("Index out of range")
        return False

    digit_at_kth_pos = (n // 10**k) % 10
    tens_complement = 10 - digit_at_kth_pos
    
    if tens_complement != 10:
        n -= digit_at_kth_pos * 10**k

        n += tens_complement * 10**k

    else: # this is assumed to happen only for k==0, e.g. 220 -> 2210
        n += 1
        n *= 10
        
    if (isNegative):
        n = -n
    return n

def canGetA(pts, graded, total):
    missing = total - graded
    remaining = missing + pts 
    threshold = total * 0.9
    hope = total * 0.85
    if remaining >= threshold:
        return True
    elif remaining > hope:
        return "Talk to professor!"
    else:
        return False

def calculateAge(bd, bm, by, d, m, y):
    age = y - by
    if bm > m or (bm == m and bd > d):
        age = age - 1
    if bd == d and bm == m: 
        return -age
    else:
        return age
    
print(calculateAge(1, 1, 1990, 5, 2, 2021) == 31)
calculateAge(12, 6, 2000, 25, 1, 2020) == 19
calculateAge(12, 6, 2000, 12, 6, 2020) == 20
calculateAge(29, 2, 2021, 31, 7, 2050) == 29
calculateAge(29, 2, 2021, 28, 2, 2022) == 0
calculateAge(29, 2, 2021, 31, 3, 2022) == 1

def cubicBoxes(n1, n2):
    v1 = n1 * (0.75 ** 3)
    v2 = n2 * (1.5 ** 3)
    return int(2 * (v1 + v2))

'''
Implement the function \lstinline{isEvenPositiveInt(n)} which, given a value \lstinline{n}, returns
\lstinline{True} if it is even, positive, and an integer, or it is equal to -1. Otherwise the
function must return \lstinline{False} and print out the message \lstinline{``No match!''}.

For instance:

\begin{itemize}

\item \lstinline{isEvenPositiveInt(6)} must return \lstinline{True};
\item \lstinline{isEvenPositiveInt(10)} must return \lstinline{True};
\item \lstinline{isEvenPositiveInt(0)} must return \lstinline{False} and print the message;
\item \lstinline{isEvenPositiveInt(-1)} must return \lstinline{True};
\item \lstinline{isEvenPositiveInt(6.0)} must return \lstinline{False} and print the message;
\item \lstinline{isEvenPositiveInt(1.1)} must return \lstinline{False} and print the message;
\item \lstinline{isEvenPositiveInt(-2)} must return \lstinline{False} and print the message;
\item \lstinline{isEvenPositiveInt(3)} must return \lstinline{False} and print the message;
\end{itemize}

\begin{solution}
  \lstinputlisting{../isEvenPositiveInt/sol.py}
\end{solution}
'''

def isEvenPositiveInt(n):
    if ((n % 2 == 0) and (n > 0) and (type(n)  == int)) or n == -1:
        return True
    else:
        print("No match!")
        return False
    
    
def mystery(a,b,c,d,e,f):
  if (c > f) or (c != f and b == e and a < d) or (c == f and b < e):
    return True
  else:
    return False

#print(mystery(1,2,3,4,5,6))

#print(mystery(5,3,8,5,4,8))

#print(mystery(59,44,85,56,44,85))

def isTriangle(a, b, c, is_right):
    if is_right == False:
        if (a + b < c and
            b + c < a and
            a + c < b):
            return True
        else:
            return False
    else:
        if (a**2 + b**2) == c**2:
            return True
        else:
            return False
