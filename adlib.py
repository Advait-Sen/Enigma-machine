import time

class gates:
    def andgate(self,b):
        if self+b>2:
           print("You can only input a 0 or a 1")
        if self+b==2:
            return 1
        else:
            return 0
    def orgate(self,b):
        if self+b!=0:
            return 1
        else:
            return 0
    def nandgate(self,b):
        if self+b!=2:
            return 1
        else:
            return 0
    def xorgate(self,b):
        """Check whether two things equal one another, be they int, str, float, or whatever"""
        if self==b:
            return 0
        else:
            return 1
    def notgate(self):
        return (self+1)%2
    def norgate(self,b):
        if self+b==0:
            return 1
        else:
            return 0

class rand:
    """A set of useful random generators for ints,floats,strings,chars,etc."""
    def nextFloat(self=0,maximum=1,decs=3):
        """Gives a random float between the lowest and highest number
        It excludes the upper boundary. The decs is how many decimal places you want the number to go to
        Usage: rand.nextInt(lower_boundary,upper_boundary,decs)"""
        newfloat=rand.nextInt(self*pow(10,decs),maximum*pow(10,decs))/pow(10,decs)
        return float(newfloat)

    def nextInt(self=0,maximum=1000000):
        """Gives a random number between the lowest and highest number
        It excludes the upper boundary
        Usage: rand.nextInt(lower_boundary,upper_boundary)"""
        millisec=time.time()
        millisec-=int(millisec)
        millisec =millisec *10000000
        sec=round(millisec/10)
        minute=round(sec/60)
        hour=round(minute/60)
        day=round(hour/24)
        month=round(day/30)
        year=round(day/365)
        timeval=millisec+sec+minute+hour+day+month+year
        newrand=(((sec+year+hour)/3)*millisec+((minute+hour+month)/3))%maximum
        if newrand<self:
            if maximum>=(self*2):
                newrand+=self
            else:
                newrand=(self+maximum)/2
        return int(newrand)

    def nextStr(self=5):
        """Gives a random string, no numbers. For numbers see rand.nextChar. Default length is 5 characters
        Usage: rand.nextStr(length)"""
        alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        newstring=""
        sleep=0
        for i in range(self):
            x=rand.nextInt(26)
            newstring+=alphabet[x]
            sleep=rand.nextInt(300)/1000
            time.sleep(sleep)
        return str(newstring)
    
    def nextChar(self=5):
        """Gives a random string, with numbers. For no numbers see rand.nextStr. Default length is 5 characters
        Usage: rand.nextChar(length)"""
        alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]
        newchar=""
        sleep=0
        for i in range(self):
            x=rand.nextInt(36)
            newstring+=alphabet[x]
            sleep=rand.nextInt(300)/1000
            time.sleep(sleep)
        return str(newstring)


class maths:
    """A set of useful maths functions"""
    def isPrime(self):
        """Returns a boolean, if the number is prime"""
        f=0
        for i in range(2,self-1):
            if self%i==0:
                f=1
                return False
        yield True


    def hcf(self,b):
        """Returns the HCF of the two numbers using Euclid's Lemma"""
        q=1
        while q!=0:
            q=max(self,b)-min(self,b)
            if self>b:
                self=q
            else:
                b=q
        return(max(self,b))
    
    def hcflist(self):
        """Returns the HCF of a list of numbers using maths.hcf"""
        f=self[0]
        for i in range(len(self)-1):
            f=maths.hcf(self[i+1],f)
        return(f)
    
    def lcm(self,b):
        """Returns the LCM of the two numbers by dividing their product by HCF"""
        return(self*b/maths.hcf(self,b))

    def lcmlist(self):
        """Returns the LCM of a list of numbers using maths.lcm"""
        f=self[0]
        for i in range(len(self)-1):
            f=maths.lcm(self[i+1],f)
        return(f)

    def fact(self):
        """Gives factorial of argument, assuming int"""
        f=1
        for i in range(self):
            f*=(i+1)
        return(f)
    def fib(self,first=0,second=1):
        """Gives fibonacci number of that value.
        Running with second two params starts fib sequence from that number onwards, eg: 2,4,6,10 ..."""
        if self<0:
            return(maths.fib(self+2)-maths.fib(self+1))
        elif self>1:
            return(maths.fib(self-2)+maths.fib(self-1))
        else:
            if(self==0):
                return(first)
            else:
                return(second)