''' We will either find a way , or make one , Hannibal Barqa '''

import numpy as np
import random
import time
result=open('results.txt','a')
def RemplirAleatoirementReelLong(matrice):
    nbr_lignes=matrice.shape[0]
    nbr_colonnes=matrice.shape[1]
    for i in range(nbr_lignes):
        for j in range(nbr_colonnes):
            matrice[i][j]=random.uniform(0,10000)
def RemplirAleatoirementReelSimple(matrice):
    nbr_lignes=matrice.shape[0]
    nbr_colonnes=matrice.shape[1]
    for i in range(nbr_lignes):
        for j in range(nbr_colonnes):
            matrice[i][j]=np.float16(random.uniform(0,100))
def ADMAT_IJ(matrice1,matrice2):
    if matrice1.shape==matrice2.shape:
        matrice_somme=np.ones(matrice1.shape)
        for i in range(matrice1.shape[0]):
            for j in range(matrice1.shape[1]):
                matrice_somme[i][j]=matrice1[i][j]+matrice2[i][j]
        return matrice_somme
    else:
        print 'Erreur : matrices de dimensions incompatibles'
def ADMAT_JI(matrice1,matrice2):
    if matrice1.shape==matrice2.shape:
        matrice_somme=np.ones(matrice1.shape)
        for i in range(matrice1.shape[1]):
            for j in range(matrice1.shape[0]):
                matrice_somme[j][i]=matrice1[j][i]+matrice2[j][i]
        return matrice_somme
    else:
        print 'Erreur : matrices de dimensions incompatibles'
def PRODMAT_IJK(matrice1,matrice2):
    if matrice1.shape[1]==matrice2.shape[0]:
        matrice_produit=np.ones((matrice1.shape[0],matrice2.shape[1]))
        for i in range(matrice1.shape[0]):
            for j in range(matrice2.shape[1]):
                for k in range(matrice1.shape[0]):
                    matrice_produit[i][j]=matrice1[i,k]*matrice2[k,j]
    else :
        print 'Erreur : matrice non compatibles'
def PRODMAT_IKJ(matrice1,matrice2):
    if matrice1.shape[1]==matrice2.shape[0]:
        matrice_produit=np.ones((matrice1.shape[0],matrice2.shape[1]))
        for i in range(matrice1.shape[0]):
            for k in range(matrice1.shape[1]):
                for j in range(matrice2.shape[0]):
                    matrice_produit[i][j]=matrice1[i,k]*matrice2[k,j]
    else :
        print 'Erreur : matrice non compatibles'
def PRODMAT_JIK(matrice1,matrice2):
    if matrice1.shape[1]==matrice2.shape[0]:
        matrice_produit=np.ones((matrice1.shape[0],matrice2.shape[1]))
        for j in range(matrice2.shape[1]):
            for i in range(matrice1.shape[0]):
                for k in range(matrice1.shape[1]):
                    matrice_produit[i][j]=matrice1[i,k]*matrice2[k,j]
    else :
        print 'Erreur : matrice non compatibles'
def PRODMAT_JKI(matrice1,matrice2):
    if matrice1.shape[1]==matrice2.shape[0]:
        matrice_produit=np.ones((matrice1.shape[0],matrice2.shape[1]))
        for j in range(matrice2.shape[1]):
            for k in range(matrice1.shape[0]):
                for i in range(matrice1.shape[1]):
                    matrice_produit[i][j]=matrice1[i,k]*matrice2[k,j]
    else :
        print 'Erreur : matrice non compatibles'
def PRODMAT_KIJ(matrice1,matrice2):
    if matrice1.shape[1]==matrice2.shape[0]:
        matrice_produit=np.ones((matrice1.shape[0],matrice2.shape[1]))
        for k in range(matrice1.shape[1]):
            for i in range(matrice1.shape[0]):
                for j in range(matrice2.shape[0]):
                    matrice_produit[i][j]=matrice1[i,k]*matrice2[k,j]
    else :
        print 'Erreur : matrice non compatibles'
def PRODMAT_KJI(matrice1,matrice2):
    if matrice1.shape[1]==matrice2.shape[0]:
        matrice_produit=np.ones((matrice1.shape[0],matrice2.shape[1]))
        for k in range(matrice1.shape[1]):
            for j in range(matrice2.shape[0]):
                for i in range(matrice1.shape[0]):
                    matrice_produit[i][j]=matrice1[i,k]*matrice2[k,j]
    else :
        print 'Erreur : matrice non compatibles'
def evaluationDuTempsExecutionADMAT_IJ(matrice1,matrice2,specification):
    temps_debut_ADMAT_IJ=time.time()
    matrice_test=ADMAT_IJ(matrice1,matrice2)
    temps_fin_ADMAT_IJ=time.time()
    temps_ADMAT_IJ=temps_fin_ADMAT_IJ-temps_debut_ADMAT_IJ
    #print 'ADMAT IJ ',specification,' prend :',temps_ADMAT_IJ,' secondes'
    ch= 'ADMAT IJ '+specification+' prend :'+str(temps_ADMAT_IJ)+' secondes'+'\n'
    return ch
def evaluationDuTempsExecutionADMAT_JI(matrice1,matrice2,specification):
    temps_debut_ADMAT_JI=time.time()
    matrice_test=ADMAT_JI(matrice1,matrice2)
    temps_fin_ADMAT_JI=time.time()
    temps_ADMAT_JI=temps_fin_ADMAT_JI-temps_debut_ADMAT_JI
    #print 'ADMAT JI ',specification,' prend :',temps_ADMAT_JI,' secondes'
    ch= 'ADMAT JI '+specification+' prend :'+str(temps_ADMAT_JI)+' secondes'+'\n'
    return ch

def evaluationDuTempsExecutionPRODMAT_IJK(matrice1,matrice2,specification):
    temps_debut_PRODMAT_IJK=time.time()
    matrice_test=PRODMAT_IJK(matrice1,matrice2)
    temps_fin_PRODDMAT_IJK=time.time()
    temps_PRODDMAT_IJK=temps_fin_PRODDMAT_IJK-temps_debut_PRODMAT_IJK
    #print 'PRODMAT IJK ',specification,' prend :',temps_PRODDMAT_IJK,' secondes'
    ch= 'PRODMAT IJK '+specification+' prend :'+str(temps_PRODDMAT_IJK)+' secondes'+'\n'
    return ch
def evaluationDuTempsExecutionPRODMAT_IKJ(matrice1,matrice2,specification):
    temps_debut_PRODMAT_IKJ=time.time()
    matrice_test=PRODMAT_IKJ(matrice1,matrice2)
    temps_fin_PRODDMAT_IKJ=time.time()
    temps_PRODDMAT_IKJ=temps_fin_PRODDMAT_IKJ-temps_debut_PRODMAT_IKJ
    #print 'PRODMAT IKJ ',specification,' prend :',temps_PRODDMAT_IKJ,' secondes'
    ch= 'PRODMAT IKJ '+specification+' prend :'+str(temps_PRODDMAT_IKJ)+' secondes'+'\n'
    return ch
def evaluationDuTempsExecutionPRODMAT_JIK(matrice1,matrice2,specification):
    temps_debut_PRODMAT_JIK=time.time()
    matrice_test=PRODMAT_JIK(matrice1,matrice2)
    temps_fin_PRODDMAT_JIK=time.time()
    temps_PRODDMAT_JIK=temps_fin_PRODDMAT_JIK-temps_debut_PRODMAT_JIK
    #print 'PRODMAT JIK ',specification,' prend :',temps_PRODDMAT_JIK,' secondes'
    ch= 'PRODMAT JIK '+specification+' prend :'+str(temps_PRODDMAT_JIK)+' secondes'+'\n'
    return ch
def evaluationDuTempsExecutionPRODMAT_JKI(matrice1,matrice2,specification):
    temps_debut_PRODMAT_JKI=time.time()
    matrice_test=PRODMAT_JKI(matrice1,matrice2)
    temps_fin_PRODDMAT_JKI=time.time()
    temps_PRODDMAT_JKI=temps_fin_PRODDMAT_JKI-temps_debut_PRODMAT_JKI
    #print 'PRODMAT JKI ',specification,' prend :',temps_PRODDMAT_JKI,' secondes'
    ch= 'PRODMAT JKI '+specification+' prend :'+str(temps_PRODDMAT_JKI)+' secondes'+'\n'
    return ch
def evaluationDuTempsExecutionPRODMAT_KIJ(matrice1,matrice2,specification):
    temps_debut_PRODMAT_KIJ=time.time()
    matrice_test=PRODMAT_KIJ(matrice1,matrice2)
    temps_fin_PRODDMAT_KIJ=time.time()
    temps_PRODDMAT_KIJ=temps_fin_PRODDMAT_KIJ-temps_debut_PRODMAT_KIJ
    #print 'PRODMAT KIJ ',specification,' prend :',temps_PRODDMAT_KIJ,' secondes'
    ch= 'PRODMAT KIJ '+specification+' prend :'+str(temps_PRODDMAT_KIJ)+' secondes'+'\n'
    return ch

def evaluationDuTempsExecutionPRODMAT_KJI(matrice1,matrice2,specification):
    temps_debut_PRODMAT_KJI=time.time()
    matrice_test=PRODMAT_KJI(matrice1,matrice2)
    temps_fin_PRODDMAT_KJI=time.time()
    temps_PRODDMAT_KJI=temps_fin_PRODDMAT_KJI-temps_debut_PRODMAT_KJI
    #print 'PRODMAT KJI ',specification,' prend :',temps_PRODDMAT_KJI,' secondes'
    ch= 'PRODMAT KJI '+specification+' prend :'+str(temps_PRODDMAT_KJI)+' secondes'+'\n'
    return ch

MS100_1,ML100_1=np.ones((100,100)),np.ones((100,100))
MS100_2,ML100_2=np.ones((100,100)),np.ones((100,100))
MS200_1,ML200_1=np.ones((200,200)),np.ones((200,200))
MS200_2,ML200_2=np.ones((200,200)),np.ones((200,200))
MS500_1,ML500_1=np.ones((500,500)),np.ones((500,500))
MS500_2,ML500_2=np.ones((500,500)),np.ones((500,500))
MS1000_1,ML1000_1=np.ones((1000,1000)),np.ones((1000,1000))
MS1000_2,ML1000_2=np.ones((1000,1000)),np.ones((1000,1000))
MS1500_1,ML1500_1=np.ones((1500,1500)),np.ones((1500,1500))
MS1500_2,ML1500_2=np.ones((1500,1500)),np.ones((1500,1500))
MS2000_1,ML2000_1=np.ones((2000,2000)),np.ones((2000,2000))
MS2000_2,ML2000_2=np.ones((2000,2000)),np.ones((2000,2000))
temps_debut_remplissage=time.time()
RemplirAleatoirementReelLong(ML100_1)
RemplirAleatoirementReelLong(ML200_1)
RemplirAleatoirementReelLong(ML500_1)
RemplirAleatoirementReelLong(ML1000_1)
RemplirAleatoirementReelLong(ML1500_1)
RemplirAleatoirementReelLong(ML2000_1)
RemplirAleatoirementReelSimple(MS100_1)
RemplirAleatoirementReelSimple(MS200_1)
RemplirAleatoirementReelSimple(MS500_1)
RemplirAleatoirementReelSimple(MS1000_1)
RemplirAleatoirementReelSimple(MS1500_1)
RemplirAleatoirementReelSimple(MS2000_1)
RemplirAleatoirementReelLong(ML100_2)
RemplirAleatoirementReelLong(ML200_2)
RemplirAleatoirementReelLong(ML500_2)
RemplirAleatoirementReelLong(ML1000_2)
RemplirAleatoirementReelLong(ML1500_2)
RemplirAleatoirementReelLong(ML2000_2)
RemplirAleatoirementReelSimple(MS100_2)
RemplirAleatoirementReelSimple(MS200_2)
RemplirAleatoirementReelSimple(MS500_2)
RemplirAleatoirementReelSimple(MS1000_2)
RemplirAleatoirementReelSimple(MS1500_2)
RemplirAleatoirementReelSimple(MS2000_2)
temps_fin_remplissage=time.time()
temps_remplissage=temps_fin_remplissage-temps_debut_remplissage
#print 'le temps de remplissage des matrices  est : ',temps_remplissage,' secondes.'
ch='le temps de remplissage des matrices  est : '+str(temps_remplissage)+' secondes.'+'\n'
result.write(ch)

result.write(evaluationDuTempsExecutionADMAT_IJ(MS100_1,MS100_2,'  100x100 Simple'))
result.write(evaluationDuTempsExecutionADMAT_IJ(MS200_1,MS200_2,'  200x200 Simple'))
result.write(evaluationDuTempsExecutionADMAT_IJ(MS500_1,MS500_2,'  500x500 Simple'))
result.write(evaluationDuTempsExecutionADMAT_IJ(MS1000_1,MS1000_2,'1000x1000 Simple'))
result.write(evaluationDuTempsExecutionADMAT_IJ(MS1500_1,MS1500_2,'1500x1500 Simple'))
result.write(evaluationDuTempsExecutionADMAT_IJ(MS2000_1,MS2000_2,'2000x2000 Simple'))

result.write(evaluationDuTempsExecutionADMAT_JI(MS100_1,MS100_2,'  100x100 Simple'))
result.write(evaluationDuTempsExecutionADMAT_JI(MS200_1,MS200_2,'  200x200 Simple'))
result.write(evaluationDuTempsExecutionADMAT_JI(MS500_1,MS500_2,'  500x500 Simple'))
result.write(evaluationDuTempsExecutionADMAT_JI(MS1000_1,MS1000_2,'1000x1000 Simple'))
result.write(evaluationDuTempsExecutionADMAT_JI(MS1500_1,MS1500_2,'1500x1500 Simple'))
result.write(evaluationDuTempsExecutionADMAT_JI(MS2000_1,MS2000_2,'2000x2000 Simple'))

result.write(evaluationDuTempsExecutionADMAT_IJ(ML100_1,ML100_2,'  100x100 Long'))
result.write(evaluationDuTempsExecutionADMAT_IJ(ML200_1,ML200_2,'  200x200 Long'))
result.write(evaluationDuTempsExecutionADMAT_IJ(ML500_1,ML500_2,'  500x500 Long'))
result.write(evaluationDuTempsExecutionADMAT_IJ(ML1000_1,ML1000_2,'1000x1000 Long'))
result.write(evaluationDuTempsExecutionADMAT_IJ(ML1500_1,ML1500_2,'1500x1500 Long'))
result.write(evaluationDuTempsExecutionADMAT_IJ(ML2000_1,ML2000_2,'2000x2000 Long'))

result.write(evaluationDuTempsExecutionADMAT_JI(ML100_1,ML100_2,'  100x100 Long'))
result.write(evaluationDuTempsExecutionADMAT_JI(ML200_1,ML200_2,'  200x200 Long'))
result.write(evaluationDuTempsExecutionADMAT_JI(ML500_1,ML500_2,'  500x500 Long'))
result.write(evaluationDuTempsExecutionADMAT_JI(ML1000_1,ML1000_2,'1000x1000 Long'))
result.write(evaluationDuTempsExecutionADMAT_JI(ML1500_1,ML1500_2,'1500x1500 Long'))
result.write(evaluationDuTempsExecutionADMAT_JI(ML2000_1,ML2000_2,'2000x2000 Long'))

result.write(evaluationDuTempsExecutionPRODMAT_IJK(MS100_1,MS100_2,'  100x100 Simple'))
result.write(evaluationDuTempsExecutionPRODMAT_IJK(MS500_1,MS500_2,'  500x500 Simple'))
result.write(evaluationDuTempsExecutionPRODMAT_IJK(MS1000_1,MS1000_2,'1000x1000 Simple'))
result.write(evaluationDuTempsExecutionPRODMAT_IJK(MS1500_1,MS1500_2,'1500x1500 Simple'))
result.write(evaluationDuTempsExecutionPRODMAT_IJK(MS2000_1,MS2000_2,'2000x2000 Simple'))
result.write(evaluationDuTempsExecutionPRODMAT_IJK(ML100_1,ML100_2,'  100x100 Long'))
result.write(evaluationDuTempsExecutionPRODMAT_IJK(ML500_1,ML500_2,'  500x500 Long'))
result.write(evaluationDuTempsExecutionPRODMAT_IJK(ML1000_1,ML1000_2,'1000x1000 Long'))
result.write(evaluationDuTempsExecutionPRODMAT_IJK(ML1500_1,ML1500_2,'1500x1500 Long'))
result.write(evaluationDuTempsExecutionPRODMAT_IJK(ML2000_1,ML2000_2,'2000x2000 Long'))

result.write(evaluationDuTempsExecutionPRODMAT_IKJ(MS100_1,MS100_2,'  100x100 Simple'))
result.write(evaluationDuTempsExecutionPRODMAT_IKJ(MS500_1,MS500_2,'  500x500 Simple'))
result.write(evaluationDuTempsExecutionPRODMAT_IKJ(MS1000_1,MS1000_2,'1000x1000 Simple'))
result.write(evaluationDuTempsExecutionPRODMAT_IKJ(MS1500_1,MS1500_2,'1500x1500 Simple'))
result.write(evaluationDuTempsExecutionPRODMAT_IKJ(MS2000_1,MS2000_2,'2000x2000 Simple'))
result.write(evaluationDuTempsExecutionPRODMAT_IKJ(ML100_1,ML100_2,'  100x100 Long'))
result.write(evaluationDuTempsExecutionPRODMAT_IKJ(ML500_1,ML500_2,'  500x500 Long'))
result.write(evaluationDuTempsExecutionPRODMAT_IKJ(ML1000_1,ML1000_2,'1000x1000 Long'))
result.write(evaluationDuTempsExecutionPRODMAT_IKJ(ML1500_1,ML1500_2,'1500x1500 Long'))
result.write(evaluationDuTempsExecutionPRODMAT_IKJ(ML2000_1,ML2000_2,'2000x2000 Long'))

result.write(evaluationDuTempsExecutionPRODMAT_JIK(MS100_1,MS100_2,'  100x100 Simple'))
result.write(evaluationDuTempsExecutionPRODMAT_JIK(MS500_1,MS500_2,'  500x500 Simple'))
result.write(evaluationDuTempsExecutionPRODMAT_JIK(MS1000_1,MS1000_2,'1000x1000 Simple'))
result.write(evaluationDuTempsExecutionPRODMAT_JIK(MS1500_1,MS1500_2,'1500x1500 Simple'))
result.write(evaluationDuTempsExecutionPRODMAT_JIK(MS2000_1,MS2000_2,'2000x2000 Simple'))
result.write(evaluationDuTempsExecutionPRODMAT_JIK(ML100_1,ML100_2,'  100x100 Long'))
result.write(evaluationDuTempsExecutionPRODMAT_JIK(ML500_1,ML500_2,'  500x500 Long'))
result.write(evaluationDuTempsExecutionPRODMAT_JIK(ML1000_1,ML1000_2,'1000x1000 Long'))
result.write(evaluationDuTempsExecutionPRODMAT_JIK(ML1500_1,ML1500_2,'1500x1500 Long'))
result.write(evaluationDuTempsExecutionPRODMAT_JIK(ML2000_1,ML2000_2,'2000x2000 Long'))

result.write(evaluationDuTempsExecutionPRODMAT_JKI(MS100_1,MS100_2,'  100x100 Simple'))
result.write(evaluationDuTempsExecutionPRODMAT_JKI(MS500_1,MS500_2,'  500x500 Simple'))
result.write(evaluationDuTempsExecutionPRODMAT_JKI(MS1000_1,MS1000_2,'1000x1000 Simple'))
result.write(evaluationDuTempsExecutionPRODMAT_JKI(MS1500_1,MS1500_2,'1500x1500 Simple'))
result.write(evaluationDuTempsExecutionPRODMAT_JKI(MS2000_1,MS2000_2,'2000x2000 Simple'))
result.write(evaluationDuTempsExecutionPRODMAT_JKI(ML100_1,ML100_2,'  100x100 Long'))
result.write(evaluationDuTempsExecutionPRODMAT_JKI(ML500_1,ML500_2,'  500x500 Long'))
result.write(evaluationDuTempsExecutionPRODMAT_JKI(ML1000_1,ML1000_2,'1000x1000 Long'))
result.write(evaluationDuTempsExecutionPRODMAT_JKI(ML1500_1,ML1500_2,'1500x1500 Long'))
result.write(evaluationDuTempsExecutionPRODMAT_JKI(ML2000_1,ML2000_2,'2000x2000 Long'))

result.write(evaluationDuTempsExecutionPRODMAT_KIJ(MS100_1,MS100_2,'  100x100 Simple'))
result.write(evaluationDuTempsExecutionPRODMAT_KIJ(MS500_1,MS500_2,'  500x500 Simple'))
result.write(evaluationDuTempsExecutionPRODMAT_KIJ(MS1000_1,MS1000_2,'1000x1000 Simple'))
result.write(evaluationDuTempsExecutionPRODMAT_KIJ(MS1500_1,MS1500_2,'1500x1500 Simple'))
result.write(evaluationDuTempsExecutionPRODMAT_KIJ(MS2000_1,MS2000_2,'2000x2000 Simple'))
result.write(evaluationDuTempsExecutionPRODMAT_KIJ(ML100_1,ML100_2,'  100x100 Long'))
result.write(evaluationDuTempsExecutionPRODMAT_KIJ(ML500_1,ML500_2,'  500x500 Long'))
result.write(evaluationDuTempsExecutionPRODMAT_KIJ(ML1000_1,ML1000_2,'1000x1000 Long'))
result.write(evaluationDuTempsExecutionPRODMAT_KIJ(ML1500_1,ML1500_2,'1500x1500 Long'))
result.write(evaluationDuTempsExecutionPRODMAT_KIJ(ML2000_1,ML2000_2,'2000x2000 Long'))

result.write(evaluationDuTempsExecutionPRODMAT_KJI(MS100_1,MS100_2,'  100x100 Simple'))
result.write(evaluationDuTempsExecutionPRODMAT_KJI(MS500_1,MS500_2,'  500x500 Simple'))
result.write(evaluationDuTempsExecutionPRODMAT_KJI(MS1000_1,MS1000_2,'1000x1000 Simple'))
result.write(evaluationDuTempsExecutionPRODMAT_KJI(MS1500_1,MS1500_2,'1500x1500 Simple'))
result.write(evaluationDuTempsExecutionPRODMAT_KJI(MS2000_1,MS2000_2,'2000x2000 Simple'))
result.write(evaluationDuTempsExecutionPRODMAT_KJI(ML100_1,ML100_2,'  100x100 Long'))
result.write(evaluationDuTempsExecutionPRODMAT_KJI(ML500_1,ML500_2,'  500x500 Long'))
result.write(evaluationDuTempsExecutionPRODMAT_KJI(ML1000_1,ML1000_2,'1000x1000 Long'))
result.write(evaluationDuTempsExecutionPRODMAT_KJI(ML1500_1,ML1500_2,'1500x1500 Long'))
result.write(evaluationDuTempsExecutionPRODMAT_KJI(ML2000_1,ML2000_2,'2000x2000 Long'))

result.close()
#the commented section is to be activated when needed
'''
if PRODMAT_KJI(MS100_1,MS100_2)==PRODMAT_IJK(MS100_1,MS100_2):
    print 'okay!'
if PRODMAT_KIJ(MS100_1,MS100_2)==PRODMAT_IJK(MS100_1,MS100_2):
    print 'okay!'
if PRODMAT_JIK(MS100_1,MS100_2)==PRODMAT_IJK(MS100_1,MS100_2):
    print 'okay!'
if PRODMAT_JKI(MS100_1,MS100_2)==PRODMAT_IJK(MS100_1,MS100_2):
    print 'okay!'
if PRODMAT_IKJ(MS100_1,MS100_2)==PRODMAT_IJK(MS100_1,MS100_2):
    print 'okay!'
evaluationDuTempsExecutionPRODMAT_IJK(MS100_1,MS100_2,'  100x100 Simple')
evaluationDuTempsExecutionPRODMAT_IKJ(MS100_1,MS100_2,'  100x100 Simple')
evaluationDuTempsExecutionPRODMAT_JIK(MS100_1,MS100_2,'  100x100 Simple')
evaluationDuTempsExecutionPRODMAT_JKI(MS100_1,MS100_2,'  100x100 Simple')
evaluationDuTempsExecutionPRODMAT_KJI(MS100_1,MS100_2,'  100x100 Simple')
evaluationDuTempsExecutionPRODMAT_KIJ(MS100_1,MS100_2,'  100x100 Simple')


RemplirAleatoirementReelLong(ML100_1)
RemplirAleatoirementReelSimple(MS100_1)
RemplirAleatoirementReelLong(ML100_2)
RemplirAleatoirementReelSimple(MS100_2)
result.write(evaluationDuTempsExecutionPRODMAT_KIJ(MS100_1,MS100_2,'  100x100 Simple'))
result.write(evaluationDuTempsExecutionPRODMAT_KIJ(ML100_1,ML100_2,'  100x100 Long'))
'''
