# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 22:55:14 2018

@author: majaa
"""


from tkinter import *
from tkinter import filedialog
import numpy as np
from nibabel import trackvis
from dipy.tracking.utils import length
from dipy.viz import fvtk
from dipy.segment import *
import vtk.util.colors as colors
from dipy.tracking.distances import mam_distances, bundles_distances_mam
import pickle


#from dipy.tracking.distances import mam_distances, bundles_distances_mam

if __name__ == '__main__':
    
    subjectList =["100307"]
    tractList = [
                "_af.left.trk"
               
                 

                ]
    subTract={}
    subHdr={}
    #for i in range(0,len(tractList)):
        #T_filename=subjectList[0]+tractList[i]
        #print(T_filename)
        #subTract[i],subHdr[i] = trackvis.read(T_filename, as_generator=False)
        #subTract[i] = np.array([s[0] for s in subTract[i]], dtype=np.object)
    wholeTract, hdr = trackvis.read("target.trk", as_generator=False)
    wholeTract = np.array([s[0] for s in wholeTract], dtype=np.object)
    a=len(wholeTract)
    print(a)
    
    
    
    tractTrack=[[0 for x in range(100)] for y in range(len(wholeTract))]
        #print(tractTrack)
    k=0
    #for p in range(len(400)):
        #print(minVal[i][p])
        #tractTrack[minVal[i][p]][0]=0
    
    
    for i in range(0,len(subjectList)) :
        length1=0
        s=[]
        tractLen=[]
        for j in range(0,len(tractList)) :
            T_filename=subjectList[i]+tractList[j]
            print(T_filename)
            subTract[j],subHdr[j] = trackvis.read(T_filename, as_generator=False)
            subTract[j] = np.array([s[0] for s in subTract[j]], dtype=np.object)
            length1=length1+len(subTract[j])
            tractLen.append(len(subTract[j]))
           # print(length1)
            s=np.concatenate((s, subTract[j]),axis=0) 
            
        print(len(s))
        print("Tract Length")
        print(tractLen)
        #print(s[0:5])
        #DM = bundles_distances_mam(s , wholeTract )
        #print(DM[0:10])
        DM = bundles_distances_mam(s.tolist() , wholeTract.tolist() )
        print("Length of distance Matrix")
        print(len(DM))    
        #print(DM[0])
        minVal=[[0 for x in range(2)] for y in range(len(s))] 
        minVal[i].remove(0)
        minVal[i].remove(0)
        wholeTract=0 
        for l in range(0,len(s)) :
            
            m,k=min((v,i) for i,v in enumerate(DM[l]))
            print (m,k)
            minVal[i].append(k)
            #print("Minimum loop ")
            #print(minVal[i])
            
        print("Minimum distances ")
        #--print(minVal[i])
        #print(list.index(min(DM)))
        
        
        
        
        for t in range(len(minVal)):
            if(t<tractLen[0]):
                tractTrack[minVal[i][t]][0]=tractTrack[minVal[i][t]][0]+1
                
               # print(minVal[i][t])
                #print(tractTrack[minVal[i][t]])
        
        #tractTrack[269][0]=tractTrack[269][0]+1
        #print(tractTrack[269])
    """    
    voteVal = np.array([0 for x in range(len(wholeTract))],dtype=int) 
    minV= np.array(minVal[i-1],dtype=int)
    for i in range(1,len(subjectList)) :
        minV = np.concatenate((minV, minVal[i]))  
    """ 
     
    #print(minV)
    
    #for i in range(0,len(subjectList)) :
        #for j in range(0,len(minVal[i])):
            #print(voteVal[minVal[i][j]])
    try:

        print(tractTrack)    
        pickle_out = open("AFTract.pickle", "wb")
            
        pickle.dump(tractTrack, pickle_out)

        print("Insert after deletion ...")
        
        #pickle_in = open("KNNTract.pickle", "rb")
        #student = pickle.load(pickle_in)
        #print(student)
        
    except EOFError as error:
        print("File Empty")      
    
    
    
    
    