import re
import argparse
import os




def matches_length_registration(length,registration,seq):
    canonical_list = ['A','T','T','T','A','T','T','T','A','T','T','T','A','T','T','T','A','T','T','T','A','A','T','T','T','A']
    full_list = canonical_list[registration%4:registration%4+length]
    full_string = ''.join(full_list)
    if len(re.findall('(?='+full_string+')',seq))>0:
        return True
    else:
        return False


def get_length_registration(length,registration,seqstring):
    while length+registration%4>=5: #stop if length is too small
#         print(length,registration%4)
        if matches_length_registration(length,registration%4,seqstring)&(length>5): #Then done
            return(length,registration%4)
            print("Length = "+repr(length)+", Registration = "+repr(registration%4), "Effective Length = "+repr(length+registration%4))
            length=0
        elif (length==5)&(registration%4==0):
            if matches_length_registration(5,0,seqstring): #Then done
                return(length,registration%4)
                print("Length = "+repr(length)+", Registration = "+repr(registration%4), "Effective Length = "+repr(length+registration%4))
            else:       
                return(0,0)
        else:
            registration+=1
            length-=1
            if (registration%4)==0:
                length+=3
    return(0,0) #if nothing else gets returned then effective length is too small
    
    
def matches_length_registration_1mismatch(length,registration,seq):
    canonical_list = ['A','T','T','T','A','T','T','T','A','T','T','T','A','T','T','T','A','T','T','T','A','A','T','T','T','A']
    full_list = canonical_list[registration%4:registration%4+length]
    for i in range(1,len(full_list)-1): #putting N at the end doesn't count!
        full_list = canonical_list[registration%4:registration%4+length]
        full_list[i]='.'
        full_string = ''.join(full_list)
        if len(re.findall('(?='+full_string+')',seq))>0:
            return True
    return False


def get_length_registration_1mismatch(length,registration,seqstring):
    while length+registration%4>=5: #stop if length is too small
#         print(length,registration%4)
        if matches_length_registration_1mismatch(length,registration%4,seqstring)&(length>5): #Then done
            return(length,registration%4)
            print("Length = "+repr(length)+", Registration = "+repr(registration%4), "Effective Length = "+repr(length+registration%4))
            length=0
        elif (length==5)&(registration%4==0):
            if matches_length_registration_1mismatch(5,0,seqstring): #Then done
                return(length,registration%4)
                print("Length = "+repr(length)+", Registration = "+repr(registration%4), "Effective Length = "+repr(length+registration%4))
            else:       
                return(0,0)
        else:
            registration+=1
            length-=1
            if (registration%4)==0:
                length+=3
    return(0,0) #if nothing else gets returned then effective length is too small


def matches_length_registration_end(length,registration,seq):
    canonical_list = ['A','T','T','T','A','T','T','T','A','T','T','T','A','T','T','T','A','T','T','T','A','A','T','T','T','A']
    full_list = canonical_list[(registration-length)%4:(registration-length)%4+length]
    full_string = ''.join(full_list)
    if len(re.findall('(?='+full_string+')',seq))>0:
        return True
    else:
        return False


def get_length_registration_end(length,registration,seqstring):
    while length+(registration)%4>=1: #stop if length is too small
#         print(length,registration%4)
        if matches_length_registration_end(length,registration%4,seqstring)&(length>5): #Then done
            return(length,registration%4)
#             print("Length = "+repr(length)+", Registration = "+repr(registration%4), "Effective Length = "+repr(length+registration%4))
            length=0
        elif (length==5)&(registration%4==1):
            if matches_length_registration_end(5,1,seqstring): #Then done
                return(length,registration%4)
            else:
                registration-=1
                length-=1
                if ((registration+2)%4)==0:
                    length+=3
        else:
            registration-=1
            length-=1
            if ((registration+2)%4)==0:
                length+=3
    return(0,0)




def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-seqstring", "--seqstring", type=str, help="Sequence String")
    parser.add_argument("-maxlength","--maxlength",type=int,default=26,help="Maximum ARE length we'll try")
    parser.add_argument("-mismatch","--mismatch",type=int,default=0,help="Number of mismatches allowed")
    parser.add_argument("-startreg","--startreg",type=int,default=1,help="Should we use end registration instead of start, 1 or 0")
    args = parser.parse_args()
    
    seqstring = args.seqstring
    maxlength = min(args.maxlength,len(seqstring)+4)
    mismatch = args.mismatch
    startreg = args.startreg
    #starting registration could be an option
    
    if maxlength<=4:
        print("Error: 'maxlength' parameter needs to be at least 5; 26 is default")
   
    seqstring = seqstring.replace("U","T") #Now either U or T will work

    if startreg!=1:
        length,registration = get_length_registration_end(maxlength,0,seqstring)
        effective_length = (registration+2)%4+length
    else:
        if (mismatch==0):
            length,registration = get_length_registration(maxlength,0,seqstring)
            effective_length = registration%4+length
        if (mismatch==1):
            length,registration = get_length_registration_1mismatch(maxlength,0,seqstring)
            effective_length = registration%4+length

    print("length = "+str(length)+", registration = "+str(registration)+", effective_length = "+str(effective_length))
        
if __name__ == '__main__':
     main()

