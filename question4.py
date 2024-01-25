import random  
import numpy as np


def phi_R(n,C):
    res=1
    for j in range(1,n):
        res=res*min(j,C)
    return res

#  H0 R1 D2 

def compute_approx_1(lh, uh, ur, ud, C, p,N):
    n=100
    mu=[uh,ur,ud]
    gamma=[lh,lh/p,(1-p)*lh/p]
    rho=[g/u for g,u in zip(gamma,mu)]
    rr=rho[1]
    somme=sum([rr**(i)/phi_R(i,C) for i in range(1,n)])
    pr0=1/somme
    # print(pr0)
    
    req_nb_r=sum([i*pr0*rr**i/phi_R(i,C) for i in range(1,n)])
    debug=sum([pr0*rr**i/phi_R(i,C) for i in range(1,n)])
   # print(debug)
    #print(phi_R(n,C))
    requests_nb=[rho[0]/(1-rho[0]),req_nb_r,rho[2]/(1-rho[2])] 
    sojourns=[c/g for c,g in zip(requests_nb,gamma)]
    (sojourn_h,sojourn_r,sojourn_d)=tuple(sojourns)
    sojourn_r_d=(sojourn_r+(1-p)*sojourn_d)/p
    mean_sojourn=sojourn_h+sojourn_r_d
    return (requests_nb,mean_sojourn,sojourns)


def compute_approx_2(lh, uh, ur, ud, C, p,N):
    n=100
    mu_h_d=[uh,ud]
    gamma_h_d=[lh,(1-p)*lh/p]
    gamma=[lh,lh/p,(1-p)*lh/p]
    rho_h_d=[g/u for g,u in zip(gamma_h_d,mu_h_d)]
    rho_r=gamma[1]/(C*ur)
    r_nb_h_d=[r/(1-r) for r in rho_h_d]
    req_nb_r= sum([(1-rho_r)*rho_r**i*i for i in range(1,n)])
    requests_nb=[r_nb_h_d[0],req_nb_r,r_nb_h_d[1]]
    sojourns=[c/g for c,g in zip(requests_nb,gamma)]
    (sojourn_h,sojourn_r,sojourn_d)=tuple(sojourns)
    mean_sojourn=sojourn_h+(sojourn_r+(1-p)*sojourn_d)/p
    return (requests_nb,mean_sojourn,sojourns)





lh=1
uh=10
ur=1
ud=10
C=5
p=0.5
N=15

print("approximation 1:")
app1=compute_approx_1(lh,uh,ur,ud,C,p,N)
print("Mean number of requests: {}".format(app1[0]))
print("Mean sojourn time: {}".format(app1[1]))
print("Mean sojourn time in each node: {}".format(app1[2]))

print("approximation 2:")
app2=compute_approx_2(lh,uh,ur,ud,C,p,N)
print("Mean number of requests: {}".format(app2[0]))
print("Mean sojourn time: {}".format(app2[1]))
print("Mean sojourn time in each node: {}".format(app2[2]))