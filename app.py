from algos import *
from random import *

def generateInstances(m,n,k,mini,maxi) :
    instances = []
    for i in range(k):
        newInst = str(m)+":"+str(n)
        jobs = list(map(str,[randint(mini,maxi) for x in range(n)]))
        for job in jobs:
            newInst += ":" + job
        instances.append(newInst)
    return instances


def fromString(args):
    tmp = list(map(int,args.split(":")))
    m = tmp[0]
    n = tmp[1]
    jobs = tmp[2:]
    bInfMax = max(jobs)
    bInfMoy = sum(jobs)/m
    jobsParam = list(jobs)
    resLSA = LSA(m,n,jobsParam)
    jobsParam = list(jobs)
    resLPT = LPT(m,n,jobsParam)
    jobsParam = list(jobs)
    resPerso = perso(m,n,jobsParam)
    ret = "Borne inferieure ‘‘maximum’’ = " + str(bInfMax) + "\nBorne inferieure ‘‘moyenne’’ = " + str(bInfMoy)
    ret += "\nResultat LSA = " + str(resLSA) + "\nResultat LPT = " + str(resLPT) + "\nResultat MyAlgo = " + str(resPerso)
    return ret

def fromFile(fileName):
    f = open(fileName, 'r')
    args = f.readline()
    f.close()
    return fromString(args)

def fromGeneration(m,n,k,mini,maxi,output) :
    f = open(output, 'w')
    ratiosLSA = []
    ratiosLPT = []
    ratiosPerso = []
    instances = generateInstances(m,n,k,mini,maxi)
    for i in instances :
        tmp = list(map(int,i.split(":")))
        m = tmp[0]
        n = tmp[1]
        jobs = tmp[2:]
        bInfMax = max(jobs)
        bInfMoy = sum(jobs)/m

        jobsParam = list(jobs)
        resLSA = LSA(m,n,jobsParam)
        jobsParam = list(jobs)
        resLPT = LPT(m,n,jobsParam)
        jobsParam = list(jobs)
        resPerso = perso(m,n,jobsParam)

        ret = "Borne inferieure ‘‘maximum’’ = " + str(bInfMax) + "\nBorne inferieure ‘‘moyenne’’ = " + str(bInfMoy)
        ret += "\nResultat LSA = " + str(resLSA) + "\nResultat LPT = " + str(resLPT) + "\nResultat MyAlgo = " + str(resPerso)
        f.write(ret + "\n")
        f.write(50*"=" + "\n")

        ratiosLSA.append(resLSA / max(bInfMax,bInfMoy))
        ratiosLPT.append(resLPT / max(bInfMax,bInfMoy))
        ratiosPerso.append(resPerso / max(bInfMax,bInfMoy))
    avgLSA = sum(ratiosLSA) / len(ratiosLSA)
    avgLPT = sum(ratiosLPT) / len(ratiosLPT)
    avgPerso = sum(ratiosPerso) / len(ratiosPerso)
    f.write("Ratio d’approximation moyen LSA = " + str(avgLSA) + "\n")
    f.write("Ratio d’approximation moyen LPT = " + str(avgLPT) + "\n")
    f.write("Ratio d’approximation moyen MyAlgo = " + str(avgPerso) + "\n")
    f.close()
