import math

def check_triangle(pointa,pointb,pointc):
    
    len_ab=math.sqrt((pointa[0]-pointb[0])**2+(pointa[1]-pointb[1])**2)
    len_ac=math.sqrt((pointa[0]-pointc[0])**2+(pointa[1]-pointc[1])**2)
    len_cb=math.sqrt((pointc[0]-pointb[0])**2+(pointc[1]-pointb[1])**2)
    
    if len_ab+len_ac>len_cb:
        print("It is a Trinagle")
        print("And It's Area : ",cal_area(len_ab, len_ac, len_cb))
    else:
        print("It is not a Trinagle")
    
def cal_area(len_ab,len_ac,len_cb):
    s=(len_ab+len_ac+len_cb)/2
    area=math.sqrt(s*(s-len_ab)*(s-len_ac)*(s-len_cb))
    return area
    

def main():
    p = []
    for k in range(1,4):
        x =[]
        for i in range(2):
            x.append(int(input("enter point's X&Y Coordinates:")))
        p.append(x)
    
    check_triangle(p[0],p[1],p[2])
        
    
main()
