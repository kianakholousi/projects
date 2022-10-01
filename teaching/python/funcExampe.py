# birthday song
def birthday():
    print("happy birthday to you")
    
def song(name):
    birthday()
    birthday()
    print("happy birthday, dear "+name)   
    birthday()
    
song("Amy")
song("bob")    

# score  Grade
# >=0.9  A
# >=0.8  B
# >=0.7  C
# >=0.6  D
# <0.6   F

def gradeCal(grade):
    if grade>=0.9:
        print("A")
    elif grade>=0.8:
        print("B")
    elif grade>=0.7:
        print("C")
    elif grade>=0.6:
        print("D")
    else: #else is for the last if #grade<0.6
        print("F")     
                   
gradeCal(float(input()))    