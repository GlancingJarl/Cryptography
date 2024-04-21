
p = 1091224913782100097176494561909751586255346040316
a = 1
b = 6
def add_points(P, Q, p):
    x1, y1 = P
    x2, y2 = Q
     
    if x1 == x2 and y1 == y2:
        m = (3*x1*x2 + a) * pow(2*y1, -1, p)
    else:
        m = (y2 - y1) * pow(x2 - x1, -1, p)
     
    x3 = (m*m - x1 - x2) % p
    y3 = (m * (x1 - x3) - y1) % p
     
    pointOnCurve((x3, y3), p)
         
    return x3, y3

def pointOnCurve(P, p):
    x, y = P
    return (y*y) % p == ( pow(x, 3, p) + a*x + b ) % p


def main():
    G=(950527233102840974417933448272333430645477194832
       ,760761184556487161112905193530635390921278666117)
    n = 1091224913782100097176494561909751586255318276045

    print("point on curve:",pointOnCurve((1,2),p))

  


main()