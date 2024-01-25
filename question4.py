import random  
import numpy as np


def phi_R(n,C):
    return np.prod([min(j,C) for j in range(1,n)])
#  H0 R1 D2 

def compute_approx_1(lh, uh, ur, ud, C, p,N):
    n=100
    mu=[uh,ur,ud]
    gamma=[lh,lh/p,(1-p)*lh/p]
    rho=[g/u for g,u in zip(gamma,mu)]
    phir=phi_R(n,C)
    somme=sum([rho[1]**i/phir for i in range(1,n)])
    pr0=1/somme
    # print(pr0)
    
    req_nb_r=sum([(pr0*rho[1]**i/phir)*i for i in range(1,n)])
    debug=sum([pr0*rho[1]**i/phir for i in range(1,n)])
    # print(debug)

    requests_nb=[rho[0]/(1-rho[0]),req_nb_r,rho[2]/(1-rho[2])] 
    sojourns=[c/g for c,g in zip(requests_nb,gamma)]
    (sojourn_h,sojourn_r,sojourn_d)=(sojourns[0],sojourns[1],sojourns[2])
    sojourn_r_d=(sojourn_r+(1-p)*sojourn_d)/p
    mean_sojourn=sojourn_h+sojourn_r_d
    return (mean_sojourn,requests_nb)


lh=1
uh=10
ur=1
ud=10
C=5
p=0.5
N=15


(mean,reque)=compute_approx_1(lh,uh,ur,ud,C,p,N)
print(mean)
print(reque)