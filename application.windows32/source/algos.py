from math import *

def LSA(m,n,jobs):
    res = [[] for i in range(0,m)]
    while jobs :
        mSizes = [sum(x) for x in res]
        minM = mSizes.index(min(mSizes))
        res[minM].append(jobs[0])
        jobs.pop(0)
    return max([sum(x) for x in res])

def LPT(m,n,jobs) :
    jobs.sort(reverse=True)
    res = [[] for i in range(0,m)]
    while jobs :
        mSizes = [sum(x) for x in res]
        minM = mSizes.index(min(mSizes))
        res[minM].append(jobs[0])
        jobs.pop(0)
    return max([sum(x) for x in res])


def perso(m,n,jobs) :
    jobs.sort(reverse=True)
    minOpt = ceil(sum(jobs)/m)
    res = [[] for i in range(0,m)]
    i = 0
    while jobs :
        if i < m :
            cont = True
            while cont:
                candidats = [x for x in jobs if sum(res[i]) + x <= minOpt ]
                if candidats :
                    ind = jobs.index(candidats[0])
                    res[i].append(jobs[ind])
                    jobs.pop(ind)
                else :
                    cont = False
            i += 1
        else :
            mSizes = [sum(x) for x in res]
            minM = mSizes.index(min(mSizes))
            res[minM].append(jobs[0])
            jobs.pop(0)

    return max([sum(x) for x in res])