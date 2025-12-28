def reverse(x):
        if x>0:
            sign=1
        else:
           sign=-1
        x=abs(x)
        rev=0
        while x>0:
            rem=x%10
            rev=rev*rev*10+rem
            x=x//10
        if rev>2*31-1:
            return 0
        return sign*rev
print(reverse(654654))