#problem statment:
#any number from 1 to 40 can be described 
# as summation of 1,3,9,27 . you can use negative sign 
# i.e. 39 = -1 + 3 + 9 + 27
# how to find this out ? 
# it could be observed that all 1,3,... are power of 3
# so first any number in question will be converted in base 3.
# for 10 in decimal, 10 = 3^2 + 1 . so 101 in base 3. 
# so  10 = 9 + 1 
# but any of 1,3,9,27 could only be used one and only once
# so how 11 can be described? 
# 11 = 9 + 2 = 102 in base 3 which would give 9 + 2(1) 
# but only single 1 could be used. in such case, 
# follwing trick is used 
# any time digit 2 is observed on any place, that digit is 
# described as subtraction like this 
# in base 3, 102 = 110 - 1 , 120 = 210 - 10 = 1010 - 100 - 10
# How about 2222 ? simple ! 10000 - 1
# like this 2 is eliminated in from digits. 
# this looks like modular airthmatic with negative quotients.
# http://math.stackexchange.com/questions/730515/negative-quotients-and-their-remainders


def to_base3 ( num ):
    #creats a list which has multiple of 3's power 
    #in reverse order. ie 1 is represented [1]
    # 3 as [0, 1] 9 as [0,0,1] and 11 as [2,0,1]
    # additional 0 is padded to accomodate one more power 
    # so 3 is [ 0, 1, 0 ]. 
    digits = list();
    while (num > 0 ):
        digits.append( num % 3 );
        num = num /3;
    digits.append(0);
    return digits;
        
def eliminate_2 ( digits) :
    i = 0
    # i miss c style for loop 
    
    while ( i < len(digits)) :
        #print digits[i];
        if digits[i] == 2 : 
            #set carry to next digit and make it -1
            digits[i] = -1;
            digits[i + 1] += 1;
            
            k = i + 1;
            while ( digits[k] > 2 ) :
                digits[k] = 0;
                digits[k + 1] += 1;
                k = k + 1;
                
        i = i + 1;
    return digits   

def sum_print (digits) :
    i = 0
    while ( i < len(digits)) :
        if digits[i] != 0 :
            print 3**(i)*digits[i];
        i += 1;
            
for i in range(1,41):
    print "----";
    print i , "=";
    sum_print(eliminate_2(to_base3(i)));
    
