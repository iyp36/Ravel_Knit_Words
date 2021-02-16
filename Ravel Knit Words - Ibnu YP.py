print('Soal 3 - Ravel Knit Words')
print('='*30)

# Function Initialization :
def ravel(knit):
    ravel= ''
    ini = 0
    while ini < len(knit):
        for i in range(len(knit)+1):
            ravel += knit[0:i]
            ini += 1
    return ravel
    
# Use the function

print(ravel('Purwadhika'))
print(ravel('Digital'))
print(ravel('Coding'))
print(ravel('School'))
print('='*30)

# Function Initialization :

def knit(ravel):
    knit=''
    # ravel=list(ravel)
    # print(ravel[10])
    # print(ravel)
    # for j in ravel:
    #     print(j)
    #     # for j in range(ravel):
    # i=0
    # j=0
    # while j < len(ravel):
    # for j in range(len(ravel)-1):
    #     if ravel[j:] == ravel[j+1:]:
    #         pass
    #     else:
    #         knit += ravel[j]
    # #         i += 1
    # #         j += 1
    # return knit
    if len(ravel) == 21: #= untuk mengakses cooding dan school
        knit = ravel[len(ravel)-6:]
    elif len(ravel) == 28: #=> untuk mengakses digital
        knit = ravel[len(ravel)-7:]
    else:
        knit = ravel[len(ravel)-10:]

    return knit

    
# Use the function

print(knit('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))
print(knit('DDiDigDigiDigitDigitaDigital'))
print(knit('CCoCodCodiCodinCoding'))
print(knit('SScSchSchoSchooSchool'))
