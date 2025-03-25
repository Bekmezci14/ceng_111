def area(d, u):

    d1, d2, d3, d4 = d
    u1, u2, u3     = u
    corners = []

    def dogru(p1,p2):
        #  0 = ay + bx + c  --->  [a, b, c]

        if p1[0] == p2[0]:
            c = p1[0]
            return [0, -1, c]
        if p1[1] == p2[1]:
            c = p2[1]
            return [-1, 0, c]

        m = (p2[1]-p1[1])/(p2[0]-p1[0])

        return [-1, m, p1[1]-(m*p1[0])]


    def kesisim(dogru1, dogru2):
        # kesistikleri noktanin koordinatlari  --->  [x, y]
        a, b, c = dogru1
        d, e, f = dogru2

        if b*d == a*e:
            return []
        
        x = ((a*f)-(c*d))/(b*d-a*e)
        if a ==0:
            return [-c/b, -(e*x+f)/d]
        if d ==0:
            return [-f/e, -(b*(-f/e)+c)/a]
        if b ==0:
            return [(((d*c)/a)-f)/e, -c/a]
        if e ==0:
            return [(((a*f)/d)-c)/b, -f/d]
        y = -(b*x+c)/a
        return [x, y]


    def ucgen_alan(a,b,c):
        # a b c koseli ucgenin alani  
        u = [a,b,c]
        return 0.5*abs(u[0][0]*u[1][1]+u[1][0]*u[2][1]+u[2][0]*u[0][1]-u[1][0]*u[0][1]-u[2][0]*u[1][1]-u[0][0]*u[2][1])
        #                (x1  *  y2)  + (x2   *  y3)  +  (x3  *  y1)  - (x2  *  y1)   -  (x3  *  y2)  -  (x1  *  y3)
        
        
    ucgenin_alan = ucgen_alan(u1,u2,u3)
    dortgenin_alan = ucgen_alan(d1,d2,d3) + ucgen_alan(d3,d4,d1)


    U = []
    D = []
    # ucgeni ve dortgeni olusturan dogrularin listesi

    U.append(dogru(u1, u2));U.append(dogru(u2, u3));U.append(dogru(u3,u1))
    D.append(dogru(d1,d2));D.append(dogru(d2,d3))
    D.append(dogru(d3,d4));D.append(dogru(d4,d1))

    points = []

    for dd in D:
        for uu in U:
            points.append(kesisim(uu, dd))
            
    # points[p11, p12, p13, p21, p22, p23, p31, p32, p33, p41, p42, p43]

    points1 = points[:3]   # [p11, p12, p13]
    points2 = points[3:6]  # [p21, p22, p23]
    points3 = points[6:9]  # [p31, p32, p33]
    points4 = points[9:]   # [p41, p42, p43]


    cur_d = d[1:] + [d[0]]   # cur_d = [d2, d3, d4, d1]
    cur_u = u[1:] + [u[0]]   # cur_u = [u2, u3, u1]


    def f(i, j, pp):
        # kesisim noktasi uzantisinin kesisimi ise listeye eklemiyor
        i-=1
        j-=1
        if (u[j][0]<=pp[0]<=cur_u[j][0] or cur_u[j][0]<=pp[0]<=u[j][0]):
            if (u[j][1]<=pp[1]<=cur_u[j][1] or cur_u[j][1]<=pp[1]<=u[j][1]):
                if (d[i][0]<=pp[0]<=cur_d[i][0] or cur_d[i][0]<=pp[0]<=d[i][0]):
                    if (d[i][1]<=pp[1]<=cur_d[i][1] or cur_d[i][1]<=pp[1]<=d[i][1]):
                        corners.append(pp)


    l = 0

    for p in points1:
        l+=1
        if len(p)!=0:
            f(1,l,p)

    l=0

    for p in points2:
        l+=1
        if len(p)!=0:
            f(2,l,p)

    l=0

    for p in points3:
        l+=1
        if len(p)!=0:
            f(3,l,p)

    l=0

    for p in points4:
        l+=1
        if len(p)!=0:
            f(4,l,p)

    
    for k in u:
        top=0
        for i, j in zip(d, cur_d):    
            top+=ucgen_alan(i, j, k)
        if abs(top-dortgenin_alan)<0.000001:
            corners.append(k)

    for k in d:
        top=0
        for i, j in zip(u, cur_u):
            top+=ucgen_alan(i, j, k)
        if abs(top-ucgenin_alan)<0.000001:
            corners.append(k)

    if len(corners)==0: return 0


    def komsu(l):
        # tum ikili kombinasyonlar
        temp_list=[]
        k=0
        for x in l:
            k+=1
            for i in range(k,len(l)):
                temp_list.append([x,l[i]])
        return temp_list
    
    ikili_komb = komsu(corners)
    
    komsular = []

    # tum noktalar, ikili nokta kombinasyonundan gecen dogrunun ayni tarafindaysa bu iki nokta komsudur.
    for x in ikili_komb:
        dogrumuz = dogru(x[0], x[1])
        n = 0
        m = 0
        for y in corners: 
            if  -0.000001<=((dogrumuz[0]*y[1])+(dogrumuz[1]*y[0])+dogrumuz[2]):
                n += 1
            if  0.000001>=((dogrumuz[0]*y[1])+(dogrumuz[1]*y[0])+dogrumuz[2]):
                m += 1
        if n == len(corners) or m == len(corners):
            komsular.append(x)
    
    if len(komsular)==0:
        return 0
    
    
    ordered = []
    ordered.append(komsular[0][0])
    ordered.append(komsular[0][1])
    del komsular[0]

    ctrl = 0
    changed = 1
    while changed:
        changed =0
        j = 0
        ctrl+=1
        for x in komsular:
            if ordered[-1] in x:
                i = x.index(ordered[-1])
                ordered.append(x[int(not i)])
                del komsular[j]
                changed = 1
            j+=1
        if ctrl>1000:
            return 0


    if len(corners)==3: return ucgen_alan(corners[0], corners[1], corners[2])

    elif len(corners)==4: 
        dortgen1 = ucgen_alan(ordered[0], ordered[1], ordered[3])
        dortgen2 = ucgen_alan(ordered[1], ordered[2], ordered[3])
        return dortgen1 + dortgen2

    elif len(corners)==5:
        besgen1 = ucgen_alan(ordered[0], ordered[1], ordered[4])
        besgen2 = ucgen_alan(ordered[1], ordered[2], ordered[3])
        besgen3 = ucgen_alan(ordered[1], ordered[3], ordered[4])
        return besgen1 + besgen2 + besgen3

    elif len(corners)==6:
        altigen1 = ucgen_alan(ordered[0], ordered[1], ordered[5])
        altigen2 = ucgen_alan(ordered[1], ordered[2], ordered[4])
        altigen3 = ucgen_alan(ordered[2], ordered[3], ordered[4])
        altigen4 = ucgen_alan(ordered[4], ordered[5], ordered[1])
        return altigen1 + altigen2 + altigen3 + altigen4

    elif len(corners)==7:
        yedigen1 = ucgen_alan(ordered[0], ordered[1], ordered[2])
        yedigen2 = ucgen_alan(ordered[2], ordered[3], ordered[4])
        yedigen3 = ucgen_alan(ordered[4], ordered[5], ordered[6])
        yedigen4 = ucgen_alan(ordered[6], ordered[0], ordered[2])
        yedigen5 = ucgen_alan(ordered[2], ordered[4], ordered[6])
        return yedigen1 + yedigen2 + yedigen3 + yedigen4 + yedigen5

    else: return 0

    