def pd2(listarg):#不能计算出绝对正确的值:4/(1-5/6),9*(7-13/3),估计还有...
    count=0
    allcount=0
    def pd(listarg2):
        nonlocal count,allcount
        for numi,i in enumerate(listarg2):
            for numj,j in enumerate(listarg2):
                if numj!=numi:       
                    for k in range(4):
                        if k==0:
                            new=j+i
                        if k==1:
                            new=j-i
                        if k==2:
                            new=j*i
                        if k==3:
                            if i!=0:
                                new=j/i
                            else:
                                continue
                        newlist=[]
                        for numm,m in enumerate(listarg2):
                            if numm!=numi and numm!=numj:
                                newlist.append(m)
                        newlist.append(new)
                        if abs(newlist[0]-24)<0.0000000001 and len(newlist)==1:
                        #if newlist==[24]:
                            count+=1
                        if len(newlist)==1:
                            allcount+=1
                        pd(newlist)
    pd(listarg)
    return allcount,count

def pd3(listarg):#请给我一个列表或元组
    listarg=sorted(listarg)
    count=0
    stringlist=[]
    string=''
    sum=0
    for index in range(54):
#三个共用一个(index35,index53),两个共用一个(index38,包含index40的一部分)
        if index==0:#a+b+c+d
            for i in listarg:
                sum+=i
            if sum==24:
                count+=1
                for numi,i in enumerate(listarg):
                    string+=str(i)+'+'
                string=string[:-1]
                stringlist.append(string)
            sum=0
            string=''
        if index==1:#a*b*c*d
            sum=1
            for i in listarg:
                sum*=i
            if sum==24:
                count+=1
                for numi,i in enumerate(listarg):
                    string+=str(i)+'*'
                string=string[:-1]
                stringlist.append(string)
            sum=0
            string=''
        if index==2:#a+b+c-d
            for numj,j in enumerate(listarg):
                if j in listarg[:numj]:
                    continue
                for numk,k in enumerate(listarg):
                    if numk==numj:
                        sum-=k
                    else:
                        sum+=k
                if sum==24:
                    count+=1
                    newlist=listarg[:numj]+listarg[numj+1:]
                    newlist.append(j)
                    for numi,i in enumerate(newlist):
                        if numi==3:
                            string=string[:-1]
                            string+='-'+str(i)
                        else:
                            string+=str(i)+'+'
                    stringlist.append(string)
                newlist=[]
                sum=0
                string=''
        if index==3:#a*b+c+d
            recordlist=[]
            for numj,j in enumerate(listarg):
                for numk,k in enumerate(listarg):
                    if numk <=numj:
                        continue
                    for numm,m in enumerate(listarg):
                        if numm!=numj and numm!=numk:
                            sum+=m
                    sum+=j*k
                    if sum==24:
                        if [j,k] not in recordlist:
                            recordlist.append([j,k])
                            count+=1
                            for numi,i in enumerate(listarg):
                                if numi!=numj and numi!=numk:
                                    string+=str(i)+'+'
                            string+=str(j)+'*'+str(k)
                            stringlist.append(string)
                    sum=0
                    string=''
        if index==4:#(a+b)*c+d
            recordlist=[]
            for numj,j in enumerate(listarg):
                for numk,k in enumerate(listarg):
                    if numk<=numj:
                        continue
                    for numm,m in enumerate(listarg):
                        if numm==numj or numm==numk:
                            continue
                        for numx,x in enumerate(listarg):
                            if numx not in [numj,numk,numm]:
                                sum+=x
                                d=x
                        sum+=(j+k)*m
                        if sum==24:
                            if [j,k] not in recordlist:
                                recordlist.append([j,k])
                                count+=1
                                string='(%s+%s)*%s+%s'%(j,k,m,d)
                                stringlist.append(string)
                        sum=0
                        string=''
                        d=0
        if index==5:#(a+b+c)*d
            for numj,j in enumerate(listarg):
                for numk,k in enumerate(listarg):
                    if numk!=numj and j not in listarg[:numj]:
                        sum+=k
                sum*=j
                if sum==24:
                    count+=1
                    string+='('
                    for numi,i in enumerate(listarg):
                        if numi!=numj:
                            string+=str(i)+'+'
                    string=string[:-1]+")*"+str(j)
                    stringlist.append(string)
                sum=0
                string=''
        if index==6:#(a+b)*(c+d)
            recordlist=[]
            for numj,j in enumerate(listarg):
                for numk,k in enumerate(listarg):
                    if numk<=numj:
                        continue
                    list_for_cd=[]
                    for numx,x in enumerate(listarg):
                        if numx!=numj and numx!=numk:
                            list_for_cd.append(x)
                    c,d=list_for_cd
                    sum=(j+k)*(c+d)
                    if sum==24:
                        if [j,k] not in recordlist and [c,d] not in recordlist:
                            recordlist.append([j,k])
                            count+=1
                            string='(%s+%s)*(%s+%s)'%(j,k,c,d)
                            stringlist.append(string)
                    c,d=0,0
                    sum=0
                    string=''
        if index==7:#a/b+c+d
            recordlist=[]
            for numj,j in enumerate(listarg):
                for numk,k in enumerate(listarg):
                    if numk<=numj:
                        continue
                    list_for_cd=[]
                    for numx,x in enumerate(listarg):
                        if numx!=numj and numx!=numk:
                            list_for_cd.append(x)
                    c,d=list_for_cd
                    sum=k/j+c+d
                    if sum==24:
                        if [k,j] not in recordlist:
                            recordlist.append([k,j])
                            count+=1
                            string='%s/%s+%s+%s'%(k,j,c,d)
                            stringlist.append(string)
                    c,d=0,0
                    sum=0
                    string=''
        if index==8:#(a+b)/c+d
            recordlist=[]
            for numj,j in enumerate(listarg):
                for numk,k in enumerate(listarg):
                    if numk>numj:
                        for numm,m in enumerate(listarg):
                            if numm!=numj and numm!=numk:
                                for numx,x in enumerate(listarg):
                                    if numx not in [numj,numk,numm]:
                                        sum=(j+k)/m+x
                                        if sum==24:
                                            if [j,k] not in recordlist:
                                                recordlist.append([j,k])
                                                count+=1
                                                string='(%s+%s)/%s+%s'%(j,k,m,x)
                                                stringlist.append(string)
                                        sum=0
                                        string=''
        if index==9:#(a+b+c)/d
            for numi,i in enumerate(listarg):
                if i in listarg[:numi]:
                    continue
                for numj,j in enumerate(listarg):
                    if numj!=numi:
                        sum+=j
                sum/=i
                if sum==24:
                    count+=1
                    string+='('
                    for numk,k in enumerate(listarg):
                        if numk!=numi:
                            string+=str(k)+'+'
                    string=string[:-1]
                    string+=')/%s'%i
                    stringlist.append(string)
                sum=0
                string=''
        if index==10:#a+b-c-d
            if listarg==[1,1,13,13]:
                count+=1
                stringlist.append('13+13-1-1')
        if index==11:#a*b-c-d
            recordlist=[]
            for numi,i in enumerate(listarg):
                for numj,j in enumerate(listarg):
                    if numj>numi:
                        list_for_cd=[]
                        for numk,k in enumerate(listarg):
                            if numk!=numi and numk!=numj:
                                list_for_cd.append(k)
                        c,d=list_for_cd
                        sum=i*j-c-d
                        if sum==24:
                            if [i,j] not in recordlist:
                                recordlist.append([i,j])
                                count+=1
                                string='%s*%s-%s-%s'%(i,j,c,d)
                                stringlist.append(string)
                        c,d=0,0
                        sum=0
                        string=''
        if index==12:#(a-b-c)*d
            recordlist=[]
            for numi,i in enumerate(listarg):
                if numi!=2 and numi!=3:
                    continue
                for numj,j in enumerate(listarg):
                    if numj!=numi:
                        list_for_bc=[]
                        for numk,k in enumerate(listarg):
                            if numk not in [numi,numj]:
                                list_for_bc.append(k)
                        b,c=list_for_bc
                        sum=(i-b-c)*j
                        if sum==24:
                            if [i,j] not in recordlist:
                                recordlist.append([i,j])
                                count+=1
                                string='(%s-%s-%s)*%s'%(i,b,c,j)
                                stringlist.append(string)
                        b,c=0,0
                        sum=0
                        string=''
        if index==13:#a*(b-c)-d
            recordlist=[]
            for numi,i in enumerate(listarg):
                for numj,j in enumerate(listarg):
                    if numj>numi:
                        for numk,k in enumerate(listarg):
                            if numk not in [numi,numj]:                                
                                for numm,m in enumerate(listarg):
                                    if numm not in [numi,numj,numk]:
                                        d=m
                                sum=k*(j-i)-d
                                if sum==24:
                                    if [i,j] not in recordlist:
                                        recordlist.append([i,j])
                                        count+=1
                                        string='%s*(%s-%s)-%s'%(k,j,i,d)
                                        stringlist.append(string)
                                d=0
                                sum=0
                                string=''
        if index==14:#a*b*c+d
            for numi,i in enumerate(listarg):
                if i not in listarg[:numi]:
                    newlist=list(listarg)
                    newlist.pop(numi)
                    a,b,c=newlist
                    sum=a*b*c+i
                    if sum==24:
                        count+=1
                        string='%s*%s*%s+%s'%(a,b,c,i)
                        stringlist.append(string)
                    a,b,c=0,0,0
                    sum=0
                    string=''
        if index==15:#a*(b+c)*d
            recordlist=[]
            for numi,i in enumerate(listarg):
                for numj,j in enumerate(listarg):
                    if numj>numi:
                        list_for_ad=[]
                        for numk,k in enumerate(listarg):
                            if numk not in [numi,numj]:
                                list_for_ad.append(k)
                        a,d=list_for_ad
                        sum=a*(i+j)*d
                        if sum==24:
                            if [i,j] not in recordlist:
                                recordlist.append([i,j])
                                count+=1
                                string='%s*(%s+%s)*%s'%(a,i,j,d)
                                stringlist.append(string)
                        a,d=0,0
                        string=''
                        sum=0
        if index==16:#a*b*c-d
            for numi,i in enumerate(listarg):
                if i not in listarg[:numi]:
                    newlist=list(listarg)
                    newlist.pop(numi)
                    a,b,c=newlist
                    sum=a*b*c-i
                    if sum==24:
                        count+=1
                        string='%s*%s*%s-%s'%(a,b,c,i)
                        stringlist.append(string)
                    a,b,c=0,0,0
                    sum=0
                    string=''
        if index==17:#a*(b-c)*d
            recordlist=[]
            for numi,i in enumerate(listarg):
                for numj,j in enumerate(listarg):
                    if numj>numi:
                        list_for_ad=[]
                        for numk,k in enumerate(listarg):
                            if numk not in [numi,numj]:
                                list_for_ad.append(k)
                        a,d=list_for_ad
                        sum=a*(j-i)*d
                        if sum==24:
                            if [i,j] not in recordlist:
                                recordlist.append([i,j])
                                count+=1
                                string='%s*(%s-%s)*%s'%(a,j,i,d)
                                stringlist.append(string)
                        a,d=0,0
                        sum=0
                        string=''
        if index==18:#a*b*c/d
            for numi,i in enumerate(listarg):
                if i not in listarg[:numi]:
                    newlist=list(listarg)
                    newlist.pop(numi)
                    a,b,c=newlist
                    sum=a*b*c/i
                    if sum==24:
                        count+=1
                        string='%s*%s*%s/%s'%(a,b,c,i)
                        stringlist.append(string)
                    a,b,c=0,0,0
                    sum=0
                    string=''
        if index==19:#a+b/c/d
            recordlist=[]
            for numi,i in enumerate(listarg):
                if numi==2 or numi==3:
                    for numj,j in enumerate(listarg):
                        if numj!=numi:
                            list_for_cd=[]
                            for numk,k in enumerate(listarg):
                                if numk not in [numi,numj]:
                                    list_for_cd.append(k)
                            c,d=list_for_cd
                            sum=j+i/c/d
                            if sum==24:
                                if [i,j] not in recordlist:
                                    recordlist.append([i,j])
                                    count+=1
                                    string='%s+%s/%s/%s'%(j,i,c,d)
                                    stringlist.append(string)
                            c,d=0,0
                            sum=0
                            string=''
        if index==20:#a*b/c/d
            recordlist=[]
            for numi,i in enumerate(listarg):
                for numj,j in enumerate(listarg):
                    if numj>numi and numj>1:
                        list_for_cd=[]
                        for numk,k in enumerate(listarg):
                            if numk not in [numi,numj]:
                                list_for_cd.append(k)
                        c,d=list_for_cd
                        sum=i*j/c/d
                        if sum==24:
                            if [i,j] not in recordlist:
                                recordlist.append([i,j])
                                count+=1
                                string='%s*%s/%s/%s'%(i,j,c,d)
                                stringlist.append(string)
                        c,d=0,0
                        sum=0
                        string=''
        if index==21:#(a-b)*c/d
            recordlist=[]
            for numi,i in enumerate(listarg):
                for numj,j in enumerate(listarg):
                    if numj>numi:
                        for numk,k in enumerate(listarg):
                            if numk not in [numi,numj]:
                                for numm,m in enumerate(listarg):
                                    if numm not in [numi,numj,numk]:
                                        d=m
                                sum=(j-i)*k/d
                                if sum==24:
                                    if [i,j] not in recordlist:
                                        recordlist.append([i,j])
                                        count+=1
                                        string='(%s-%s)*%s/%s'%(j,i,k,d)
                                        stringlist.append(string)
                                d=0
                                sum=0
                                string=''
        if index==22:#(a*b-c)/d
            recordlist=[]
            for numi,i in enumerate(listarg):
                for numj,j in enumerate(listarg):
                    if numj>numi:
                        for numk,k in enumerate(listarg):
                            if numk not in [numi,numj]:
                                for numm,m in enumerate(listarg):
                                    if numm not in [numi,numj,numk]:
                                        d=m
                                sum=(i*j-k)/d
                                if sum==24:
                                    if [i,j] not in recordlist:
                                        recordlist.append([i,j])
                                        count+=1
                                        string='(%s*%s-%s)/%s'%(i,j,k,d)
                                        stringlist.append(string)
                                d=0
                                sum=0
                                string=''
        if index==23:#a*(b-c/d)
            recordlist=[]
            for numi,i in enumerate(listarg):
                for numj,j in enumerate(listarg):
                    if numj!=numi:
                        for numk,k in enumerate(listarg):
                            if numk not in [numi,numj]:
                                for numm,m in enumerate(listarg):
                                    if numm not in [numi,numj,numk]:
                                        b=m
                                sum=k*(b-i/j)
                                if abs(sum-24)<0.0000000001:
                                    if [i,j] not in recordlist:
                                        recordlist.append([i,j])
                                        count+=1
                                        string='%s*(%s-%s/%s)'%(k,b,i,j)
                                        stringlist.append(string)
                                b=0
                                sum=0
                                string=''
        if index==24:#a*b-c/d
            recordlist=[]
            for numi,i in enumerate(listarg):
                for numj,j in enumerate(listarg):
                    if numj>numi:
                        list_for_dc=[]
                        for numk,k in enumerate(listarg):
                            if numk not in [numi,numj]:
                                list_for_dc.append(k)
                        d,c=list_for_dc
                        sum=i*j-c/d
                        if sum==24:
                            if [i,j] not in recordlist:
                                recordlist.append([i,j])
                                count+=1
                                string='%s*%s-%s/%s'%(i,j,c,d)
                                stringlist.append(string)
                        d,c=0,0
                        sum=0
                        string=''
        if index==25:#a*b/c-d
            recordlist=[]
            for numi,i in enumerate(listarg):
                for numj,j in enumerate(listarg):
                    if numj>numi:
                        for numk,k in enumerate(listarg):
                            if numk not in [numi,numj]:
                                for numm,m in enumerate(listarg):
                                    if numm not in [numi,numj,numk]:
                                        d=m
                                sum=i*j/k-d
                                if sum==24:
                                    if [i,j] not in recordlist:
                                        recordlist.append([i,j])
                                        count+=1
                                        string='%s*%s/%s-%s'%(i,j,k,d)
                                        stringlist.append(string)
                                d=0
                                sum=0
                                string=''
        if index==26:#a*(b/c-d)
            recordlist=[]
            for numi,i in enumerate(listarg):
                for numj,j in enumerate(listarg):
                    if numj>numi:
                        for numk,k in enumerate(listarg):
                            if numk not in [numi,numj]:
                                for numm,m in enumerate(listarg):
                                    if numm not in [numi,numj,numk]:
                                        d=m
                                sum=k*(j/i-d)
                                if abs(sum-24)<0.0000000001:
                                    if [i,j] not in recordlist:
                                        recordlist.append([i,j])
                                        count+=1
                                        string='%s*(%s/%s-%s)'%(k,j,i,d)
                                        stringlist.append(string)
                                d=0
                                sum=0
                                string=''
        if index==27:#a*b/(c-d)
            recordlist=[]
            for numi,i in enumerate(listarg):
                for numj,j in enumerate(listarg):
                    if numj>numi:
                        list_for_ab=[]
                        for numk,k in enumerate(listarg):
                            if numk not in [numi,numj]:
                                list_for_ab.append(k)
                        a,b=list_for_ab
                        if j==i:
                            continue
                        sum=a*b/(j-i)
                        if sum==24:
                            if [i,j] not in recordlist:
                                recordlist.append([i,j])
                                count+=1
                                string='%s*%s/(%s-%s)'%(a,b,j,i)
                                stringlist.append(string)
                        a,b=0,0
                        sum=0
                        string=''
        if index==28:#(a+b)*c/d
            recordlist=[]
            for numi,i in enumerate(listarg):
                for numj,j in enumerate(listarg):
                    if numj>numi:
                        for numk,k in enumerate(listarg):
                            if numk not in [numi,numj]:
                                for numm,m in enumerate(listarg):
                                    if numm not in [numi,numj,numk]:
                                        d=m
                                sum=(i+j)*k/d
                                if sum==24:
                                    if [i,j] not in recordlist:
                                        recordlist.append([i,j])
                                        count+=1
                                        string='(%s+%s)*%s/%s'%(i,j,k,d)
                                        stringlist.append(string)
                                d=0
                                sum=0
                                string=''
        if index==29:#a+b*c/d
            recordlist=[]
            for numi,i in enumerate(listarg):
                for numj,j in enumerate(listarg):
                    if numj>numi:
                        for numk,k in enumerate(listarg):
                            if numk not in [numi,numj]:
                                for numm,m in enumerate(listarg):
                                    if numm not in [numi,numj,numk]:
                                        d=m
                                sum=k+i*j/d
                                if sum==24:
                                    if [i,j] not in recordlist:
                                        recordlist.append([i,j])
                                        count+=1
                                        string='%s+%s*%s/%s'%(k,i,j,d)
                                        stringlist.append(string)
                                d=0
                                sum=0
                                string=''
        if index==30:#(a+b*c)/d
            recordlist=[]
            for numi,i in enumerate(listarg):
                for numj,j in enumerate(listarg):
                    if numj>numi:
                        for numk,k in enumerate(listarg):
                            if numk not in [numi,numj]:
                                for numm,m in enumerate(listarg):
                                    if numm not in [numi,numj,numk]:
                                        d=m
                                sum=(k+i*j)/d
                                if sum==24:
                                    if [i,j] not in recordlist:
                                        recordlist.append([i,j])
                                        count+=1
                                        string='(%s+%s*%s)/%s'%(k,i,j,d)
                                        stringlist.append(string)
                                d=0
                                sum=0
                                string=''
        if index==32:#(a+b/c)*d
            recordlist=[]
            for numi,i in enumerate(listarg):
                for numj,j in enumerate(listarg):
                    if numj!=numi:
                        for numk,k in enumerate(listarg):
                            if numk not in [numi,numj]:
                                for numm,m in enumerate(listarg):
                                    if numm not in [numi,numj,numk]:
                                        d=m
                                sum=(k+i/j)*d
                                if sum==24:
                                    if [i,j] not in recordlist:
                                        recordlist.append([i,j])
                                        count+=1
                                        string='(%s+%s/%s)*%s'%(k,i,j,d)
                                        stringlist.append(string)
                                d=0
                                sum=0
                                string=''
        if index==33:#a*b+c/d
            recordlist=[]
            for numi,i in enumerate(listarg):
                for numj,j in enumerate(listarg):
                    if numj>numi:
                        list_for_dc=[]
                        for numk,k in enumerate(listarg):
                            if numk not in [numi,numj]:
                                list_for_dc.append(k)
                        d,c=list_for_dc
                        sum=i*j+c/d
                        if sum==24:
                            if [i,j] not in recordlist:
                                recordlist.append([i,j])
                                count+=1
                                string='%s*%s+%s/%s'%(i,j,c,d)
                                stringlist.append(string)
                        d,c=0,0
                        sum=0
                        string=''
        if index==34:#a*b/(c+d)
            recordlist=[]
            for numi,i in enumerate(listarg):
                for numj,j in enumerate(listarg):
                    if numj>numi:
                        list_for_cd=[]
                        for numk,k in enumerate(listarg):
                            if numk not in [numi,numj]:
                                list_for_cd.append(k)
                        c,d=list_for_cd
                        sum=i*j/(c+d)
                        if sum==24:
                            if [i,j] not in recordlist:
                                recordlist.append([i,j])
                                count+=1
                                string='%s*%s/(%s+%s)'%(i,j,c,d)
                                stringlist.append(string)
                        c,d=0,0
                        sum=0
                        string=''
        if index==35:#(a+b-c)/d,a+(b-c)/d,a+b/c-d
            if 1 not in listarg:
                continue
            recordlist=[]
            newlist=listarg[1:]
            for numi,i in enumerate(newlist):
                for numj,j in enumerate(newlist):
                    if numj>numi:
                        for numk,k in enumerate(newlist):
                            if numk not in [numi,numj]:
                                sum=i+j-k
                                if sum==24:
                                    if [i,j] not in recordlist:
                                        recordlist.append([i,j])
                                        count+=3
                                        string='(%s+%s-%s)/1'%(i,j,k)
                                        stringlist.append(string)
                                        string='%s+(%s-%s)/1'%(i,j,k)#surprise
                                        stringlist.append(string)
                                        string='%s+%s/1-%s'%(i,j,k)#surprise*2
                                        stringlist.append(string)
                                sum=0
                                string=''
        if index==36:#a+b-c/d
            if 13 in listarg:
                newlist=listarg[:-1]
                if 13 in newlist:
                    d,c=newlist[:-1]
                    if c/d==2:
                        count+=1
                        stringlist.append('13+13-%s/%s'%(c,d))
                elif 12 in newlist:
                    c,d=newlist[:-1]
                    if c==d:
                        count+=1
                        stringlist.append('13+12-%s/%s'%(c,d))
        if index==37:#(a+b)/c-d
            if listarg==[1,2,13,13]:
                count+=1
                stringlist.append('(13+13)/1-2')
            if listarg==[1,1,12,13]:
                count+=1
                stringlist.append('(12+13)/1-1')
        if index==38:#a+b/(c-d),(a+b)/(c-d),a+(b-c)*d的一部分
            if listarg==[12,12,12,13]:
                count+=3
                stringlist.append('12+12/(13-12)')
                stringlist.append('(12+12)/(13-12)')
                stringlist.append('12+(13-12)*12')
            if 12 in listarg and 13 not in listarg and 12 in listarg[:-1]:
                d,c=listarg[:-2]
                if c-d==1:
                    count+=3
                    stringlist.append('12+12/(%s-%s)'%(c,d))
                    stringlist.append('(12+12)/(%s-%s)'%(c,d))
                    stringlist.append('12+(%s-%s)*12'%(c,d))
            if 11 in listarg and 13 in listarg:
                newlist=list(listarg)
                flag1,flag2=1,1
                for numi,i in enumerate(listarg):
                    if i==11 and flag1:
                        newlist.pop(numi)
                        flag1=0
                    if i==13 and flag2:
                        newlist.pop(numi-1)
                        flag2=0
                d,c=newlist
                if c-d==1:
                    count+=5
                    stringlist.append('13+11/(%s-%s)'%(c,d))
                    stringlist.append('11+13/(%s-%s)'%(c,d))
                    stringlist.append('11+(%s-%s)*13'%(c,d))
                    stringlist.append('13+(%s-%s)*11'%(c,d))
                    stringlist.append('(13+11)/(%s-%s)'%(c,d))
        if index==39:#(a+b-c)*d
            recordlist=[]
            for numi,i in enumerate(listarg):
                for numj,j in enumerate(listarg):
                    if numj>numi:
                        for numk,k in enumerate(listarg):
                            if numk not in [numi,numj]:
                                for numm,m in enumerate(listarg):
                                    if numm not in [numi,numj,numk]:
                                        sum=(i+j-k)*m
                                        d=m
                                if sum==24:
                                    if [i,j] not in recordlist:
                                        recordlist.append([i,j])
                                        count+=1
                                        string='(%s+%s-%s)*%s'%(i,j,k,d)
                                        stringlist.append(string)
                                d=0
                                sum=0
                                string=''
        if index==40:#a+(b-c)*d,一部分在index38
            recordlist=[]
            for numi,i in enumerate(listarg):
                for numj,j in enumerate(listarg):
                    if numj>numi:
                        for numk,k in enumerate(listarg):
                            if numk not in [numi,numj]:
                                for numm,m in enumerate(listarg):
                                    if numm not in [numi,numj,numk]:
                                        sum=k+(j-i)*m
                                        d=m
                                if sum==24:
                                    if [i,j] not in recordlist:
                                        recordlist.append([i,j])
                                        count+=1
                                        string='%s+(%s-%s)*%s'%(k,j,i,d)
                                        stringlist.append(string)
                                d=0
                                sum=0
                                string=''
        if index==41:#a+b-c*d
            if listarg==[1,2,13,13]:
                count+=1
                stringlist.append('13+13-2*1')
            if listarg==[1,1,12,13]:
                count+=1
                stringlist.append('12+13-1*1')
        if index==42:#(a+b)*c-d
            recordlist=[]
            for numi,i in enumerate(listarg):
                for numj,j in enumerate(listarg):
                    if numj>numi:
                        for numk,k in enumerate(listarg):
                            if numk not in [numi,numj]:
                                for numm,m in enumerate(listarg):
                                    if numm not in [numi,numj,numk]:
                                        d=m
                                sum=(i+j)*k-d
                                if sum==24:
                                    if [i,j] not in recordlist:
                                        count+=1
                                        recordlist.append([i,j])
                                        string='(%s+%s)*%s-%s'%(i,j,k,d)
                                        stringlist.append(string)
                                d=0
                                sum=0
                                string=''
        if index==43:#a+b*c-d
            recordlist=[]
            for numi,i in enumerate(listarg):
                for numj,j in enumerate(listarg):
                    if numj>numi:
                        for numk,k in enumerate(listarg):
                            if numk not in [numi,numj]:
                                for numm,m in enumerate(listarg):
                                    if numm not in [numi,numj,numk]:
                                        d=m
                                sum=k+i*j-d
                                if sum==24:
                                    if [i,j] not in recordlist:
                                        recordlist.append([i,j])
                                        count+=1
                                        string='%s+%s*%s-%s'%(k,i,j,d)
                                        stringlist.append(string)
                                d=0
                                sum=0
                                string=''
        if index==44:#(a+b)*(c-d)
            recordlist=[]
            for numi,i in enumerate(listarg):
                for numj,j in enumerate(listarg):
                    if numj>numi:
                        list_for_ab=[]
                        for numk,k in enumerate(listarg):
                            if numk not in [numi,numj]:
                                list_for_ab.append(k)
                        a,b=list_for_ab
                        sum=(a+b)*(j-i)
                        if sum==24:
                            if [i,j] not in recordlist:
                                recordlist.append([i,j])
                                count+=1
                                string='(%s+%s)*(%s-%s)'%(a,b,j,i)
                                stringlist.append(string)
                        a,b=0,0
                        sum=0
                        string=''
        if index==45:#(a-b)*(c-d)
            recordlist=[]
            for numi,i in enumerate(listarg):
                for numj,j in enumerate(listarg):
                    if numj>numi:
                        list_for_dc=[]
                        for numk,k in enumerate(listarg):
                            if numk not in [numi,numj]:
                                list_for_dc.append(k)
                        d,c=list_for_dc
                        sum=(j-i)*(c-d)
                        if sum==24:
                            if [i,j] not in recordlist:
                                recordlist.append([i,j])
                                count+=1
                                string='(%s-%s)*(%s-%s)'%(j,i,c,d)
                                stringlist.append(string)
                        d,c=0,0
                        sum=0
                        string=''
        if index==46:#a/(b-c/d)
            recordlist=[]
            for numi,i in enumerate(listarg):
                for numj,j in enumerate(listarg):
                    if numj!=numi:
                        for numk,k in enumerate(listarg):
                            if numk not in [numi,numj]:
                                for numm,m in enumerate(listarg):
                                    if numm not in [numi,numj,numk]:
                                        b=m
                                if b-i/j!=0:
                                    sum=k/(b-i/j)
                                if abs(sum-24)<0.0000000001:
                                    if [i,j] not in recordlist:
                                        recordlist.append([i,j])
                                        count+=1
                                        string='%s/(%s-%s/%s)'%(k,b,i,j)
                                        stringlist.append(string)
                                b=0
                                sum=0
                                string=''
        if index==47:#a/(b/c-d)
            recordlist=[]
            for numi,i in enumerate(listarg):
                for numj,j in enumerate(listarg):
                    if numj>numi:
                        for numk,k in enumerate(listarg):
                            if numk not in [numi,numj]:
                                for numm,m in enumerate(listarg):
                                    if numm not in [numi,numj,numk]:
                                        d=m
                                if j/i-d!=0:
                                    sum=k/(j/i-d)
                                if abs(sum-24)<0.0000000001:
                                    if [i,j] not in recordlist:
                                        recordlist.append([i,j])
                                        count+=1
                                        string='%s/(%s/%s-%s)'%(k,j,i,d)
                                        stringlist.append(string)
                                d=0
                                sum=0
                                string=''
        if index==48:#(a*b-c)*d
            recordlist=[]
            for numi,i in enumerate(listarg):
                for numj,j in enumerate(listarg):
                    if numj>numi:
                        for numk,k in enumerate(listarg):
                            if numk not in [numi,numj]:
                                for numm,m in enumerate(listarg):
                                    if numm not in [numi,numj,numk]:
                                        d=m
                                sum=(i*j-k)*d
                                if sum==24:
                                    if [i,j] not in recordlist:
                                        recordlist.append([i,j])
                                        count+=1
                                        string='(%s*%s-%s)*%s'%(i,j,k,d)
                                        stringlist.append(string)
                                d=0
                                sum=0
                                string=''
        if index==49:#(a+b*c)*d
            recordlist=[]
            for numi,i in enumerate(listarg):
                for numj,j in enumerate(listarg):
                    if numj>numi:
                        for numk,k in enumerate(listarg):
                            if numk not in [numi,numj]:
                                for numm,m in enumerate(listarg):
                                    if numm not in [numi,numj,numk]:
                                        d=m
                                sum=(k+i*j)*d
                                if sum==24:
                                    if [i,j] not in recordlist:
                                        recordlist.append([i,j])
                                        count+=1
                                        string='(%s+%s*%s)*%s'%(k,i,j,d)
                                        stringlist.append(string)
                                d=0
                                sum=0
                                string=''
        if index==50:#a*b+c*d
            recordlist=[]
            for numi,i in enumerate(listarg):
                for numj,j in enumerate(listarg):
                    if numj>numi:
                        list_for_cd=[]
                        for numk,k in enumerate(listarg):
                            if numk not in [numi,numj]:
                                list_for_cd.append(k)
                        c,d=list_for_cd
                        sum=i*j+c*d
                        if sum==24:
                            if [i,j] not in recordlist and [c,d] not in recordlist:
                                recordlist.append([i,j])
                                count+=1
                                string='%s*%s+%s*%s'%(i,j,c,d)
                                stringlist.append(string)
                        c,d=0,0
                        sum=0
                        string=''
        if index==51:#a*b-c*d
            recordlist=[]
            for numi,i in enumerate(listarg):
                for numj,j in enumerate(listarg):
                    if numj>numi and numj!=1:
                        list_for_cd=[]
                        for numk,k in enumerate(listarg):
                            if numk not in [numi,numj]:
                                list_for_cd.append(k)
                        c,d=list_for_cd
                        sum=i*j-c*d
                        if sum==24:
                            if [i,j] not in recordlist:
                                recordlist.append([i,j])
                                count+=1
                                string='%s*%s-%s*%s'%(i,j,c,d)
                                stringlist.append(string)
                        c,d=0,0
                        sum=0
                        string=''
        if index==52:#(a-b*c)*d
            recordlist=[]
            for numi,i in enumerate(listarg):
                for numj,j in enumerate(listarg):
                    if numj>numi:
                        for numk,k in enumerate(listarg):
                            if numk>0 and numk not in [numi,numj]:
                                for numm,m in enumerate(listarg):
                                    if numm not in [numi,numj,numk]:
                                        d=m
                                sum=(k-i*j)*d
                                if sum==24:
                                    if [i,j] not in recordlist:
                                        recordlist.append([i,j])
                                        count+=1
                                        string='(%s-%s*%s)*%s'%(k,i,j,d)
                                        stringlist.append(string)
                                d=0
                                sum=0
                                string=''
        if index==53:#(a+b)/c/d,(a+b/c)/d,a/b+c/d
            if listarg==[1,1,11,13]:
                count+=4
                stringlist.append('(13+11)/1/1')
                stringlist.append('(13+11/1)/1')
                stringlist.append('(11+13/1)/1')
                stringlist.append('13/1+11/1')
            if listarg==[1,1,12,12]:
                count+=3
                stringlist.append('(12+12)/1/1')
                stringlist.append('(12+12/1)/1')
                stringlist.append('12/1+12/1')
    return(stringlist,count)

def test():
    testlist=[]
    for i in range(1,14):
        for j in range(1,14):
            for k in range(1,14):
                for m in range(1,14):
                    testr=sorted([i,j,k,m])
                    if testr not in testlist:
                        testlist.append(testr)
    return testlist

def tg():
    from random import randint
    return [randint(1,13),randint(1,13),randint(1,13),randint(1,13)]

def problem():
    left=[]
    for i in test():
        if pd3(i)[1]==0 and pd2(i)[1]>0:
            left.append(i)
    return left

print(len(problem()),problem())
            

      # all right                  
                           
