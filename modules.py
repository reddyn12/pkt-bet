import autoalert


def m1(ht,at,hs,ass,hp,ap,ha,aa,cl,per):
    if "1" in per:
        #8-11
        min=int(cl.split(":")[0])
        if min>=8 and min<12:
            if hs<-8.5 and hp>ap and ha>aa:
                autoalert.text()
            elif ass<-8.5 and ap>hp and aa>ha:
                autoalert.text()
    print("hi")

def lifes2short():
    pass

def lifs2long():
    pass

def minconv(t):
    m=float(t.split(":")[0])
    s=float(t.split(":")[1])
    comb=720-((m*60)+s)
    sans=str(comb/720.0)
    return sans.split(".")[1]

def getTime(c,t):
    try:
        time="100"
        if t=="0":
            if "time" in c:
                time="3.0"
            else:
                if "OT" in c:
                    if "-" in c:

                        s = c.split(" - ")[0]
                        x = s.split(".")[0]
                        if len(x) == 1:
                            temp = "0:0" + x
                        else:
                            temp = "0:" + x

                        time = "5."
                        time = time + minconv(temp)
                    else:

                        time = "5.0"
                else:
                    if "-" in c:
                        perc=c.split(" - ")[1]
                        per=perc[0]
                        s=c.split(" - ")[0]
                        x=s.split(".")[0]
                        if len(x)==1:
                            temp = "0:0"+x
                        else:
                            temp="0:"+x
                        time=per+"."
                        time=time+minconv(temp)
                    else:
                        per=int(c[-3])
                        per=per+1
                        time=str(per)+".0"
        else:
            if "OT" in c:
                time="5."
                time=time+minconv(t)
            else:
                time=c[0]+"."
                time=time+minconv(t)

        return float(time)
    except:
        print("error  "+c+"  "+t)