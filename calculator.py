
def dm(grade):
    total=0
    if grade=='O':
        total=40
    elif grade=='A+':
        total=36
    elif grade=='A':
        total=32
    elif grade=='B+':
        total=28
    elif grade=='B':
        total=24
    elif grade=='C':
        total=20
    elif grade=='C+':
        total=16
    else:
        total=0

    return total
    
def digilogic(grade):
    total=0
    if grade=='O':
        total=30
    elif grade=='A+':
        total=27
    elif grade=='A':
        total=24
    elif grade=='B+':
        total=21
    elif grade=='B':
        total=18
    elif grade=='C':
        total=15
    elif grade=='C+':
        total=12
    else:
        total=0

    return total

def dc(grade):
    total=0
    if grade=='O':
        total=30
    elif grade=='A+':
        total=27
    elif grade=='A':
        total=24
    elif grade=='B+':
        total=21
    elif grade=='B':
        total=18
    elif grade=='C':
        total=15
    elif grade=='C+':
        total=12
    else:
        total=0

    return total

def pdp(grade):
    total=0
    if grade=='O':
        total=30
    elif grade=='A+':
        total=27
    elif grade=='A':
        total=24
    elif grade=='B+':
        total=21
    elif grade=='B':
        total=18
    elif grade=='C':
        total=15
    elif grade=='C+':
        total=12
    else:
        total=0

    return total

def dbms(grade):
    total=0
    if grade=='O':
        total=30
    elif grade=='A+':
        total=27
    elif grade=='A':
        total=24
    elif grade=='B+':
        total=21
    elif grade=='B':
        total=18
    elif grade=='C':
        total=15
    elif grade=='C+':
        total=12
    else:
        total=0

    return total

def uhv(grade):
    total=0
    if grade=='O':
        total=30
    elif grade=='A+':
        total=27
    elif grade=='A':
        total=24
    elif grade=='B+':
        total=21
    elif grade=='B':
        total=18
    elif grade=='C':
        total=15
    elif grade=='C+':
        total=12
    else:
        total=0

    return total

def tamil(grade):
    total=0
    if grade=='O':
        total=10
    elif grade=='A+':
        total=9
    elif grade=='A':
        total=8
    elif grade=='B+':
        total=7
    elif grade=='B':
        total=6
    elif grade=='C':
        total=5
    elif grade=='C+':
        total=4
    else:
        total=0

    return total

def pdp_lab(grade):

    total=0
    if grade=='O':
        total=15
    elif grade=='A+':
        total=13.5
    elif grade=='A':
        total=12
    elif grade=='B+':
        total=10.5
    elif grade=='B':
        total=9
    elif grade=='C':
        total=7.5
    elif grade=='C+':
        total=6
    else:
        total=0

    return total

def dbms_lab(grade):

    total=0
    if grade=='O':
        total=15
    elif grade=='A+':
        total=13.5
    elif grade=='A':
        total=12
    elif grade=='B+':
        total=10.5
    elif grade=='B':
        total=9
    elif grade=='C':
        total=7.5
    elif grade=='C+':
        total=6
    else:
        total=0

    return total

def cgpa_calculator(maths,logic,com,pdp,db,u,tam,lab1,lab2):
    x=dm(maths)+digilogic(logic)+dc(com)+pdp(pdp)+dbms(db)+uhv(u)+tamil(tam)+pdp_lab(lab1)+dbms_lab(lab2)
    return x/23







