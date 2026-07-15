import json
from cipher.rules import get_separator_length , ELIGIBLE_SYMBOLS

with open("alphabet.json", "r",  encoding="utf-8") as f:
    alphabet = json.load(f)

##FUNCTIONS
def get_letter(alphabet,value):
    for key, val in alphabet.items():
        if val == value:
            return key
    return None

## """MAIN"""
while True:
    
    msg = input("escribi puto:")
    if msg == "":
        break
    #separator_count = get_separator_length(msg)
    #print(separator_count)
    i=0
    while i < len(msg):
        if msg[i] in ELIGIBLE_SYMBOLS:
            separator_count = get_separator_length(msg[i:i+3])
            #print(separator_count)
            print(get_letter(alphabet,msg[i:i+3]))
            i = i + 3 + separator_count
        else:
            print(msg[i])
            i += 1


# &><-$$$<->&<-$&><-$&>-$>&< &<&>-$-$>&<&-&>$<<-$>&&>$<- (hello world)
# &>< = h
# $$< = e
# <-$ = l
# <-$ = l
# -$> = o
#  
# &<& = w
# -$> = o
# &-& = r
# <-$ = l
# &>$ = d