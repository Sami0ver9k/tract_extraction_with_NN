# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 18:32:26 2018

@author: majaa
"""

from tkinter import *
from tkinter import filedialog
import numpy as np
from nibabel import trackvis
from dipy.tracking.utils import length
from dipy.viz import fvtk
import vtk.util.colors as colors
import pickle


class Window(Frame):
   
   def show_tract(self,segmented_tract,segmented_tract2, color,color2):
          """Visualization of the segmented tract.
          """ 
          ren = fvtk.ren()           
          fvtk.add(ren, fvtk.line(segmented_tract.tolist(),
                                    colors=color,
                                    linewidth=2,
                                    opacity=0.3))
          
          fvtk.show(ren)
          ren2 = fvtk.ren()           
          fvtk.add(ren2, fvtk.line(segmented_tract2.tolist(),
                                    colors=color2,
                                    linewidth=2,
                                    opacity=0.3))
          
          fvtk.show(ren2)
          fvtk.clear(ren)
          fvtk.clear(ren2)

   def load(self,T_filename, threshold_short_streamlines=10.0):
          """Load tractogram from TRK file and remove short streamlines with
          length below threshold.
          """
          
          print("Loading %s" % T_filename)
          T, hdr = trackvis.read(T_filename, as_generator=False)
          T = np.array([s[0] for s in T], dtype=np.object)
          #T = np.array([s for s in T if if s in tr], dtype=np.object)
          
          
          print("Before")
          print("%s: %s streamlines" % (T_filename, len(T)))
          
          
          #f=0
          pickle_in = open("AFTract.pickle", "rb")
          st = pickle.load(pickle_in)
          print(st)
          tr=[]
          
          for l in range(len(st)):
              m,k=max((v,i) for i,v in enumerate(st[l]))
              #print("max")
              #print(st[l])
              #print(m)
              #print(k)
              if m>0 :
                  #tr[l]=f
                  #f=f+1
                  #print("################################################")
                  #print(tr)
                  tr.append(l)
              
          
          print(len(T))
          """for k in range(len(T),0,-1):
              #print("nai")
              if k in tr:
                  np.delete(T,T[k],0)
                  #print("Asi")
          """
          print(tr)
          tk=[]
          for o in range(len(T)):
              if o not in tr:
                  tk.append(o)
          print("length")
          print(len(tk))
          T2=np.delete(T,tk)
          print("After")
          print("%s: %s streamlines" % (T_filename, len(T2)))
          
          return T,T2, hdr
          #Removing short artifactual streamlines
          #print("Removing (presumably artifactual) streamlines shorter than %s" % threshold_short_streamlines)
          #T = np.array([s for s in T if length(s) >= threshold_short_streamlines], dtype=np.object)
          #print("%s: %s streamlines" % (T_filename, len(T)))
          #return T, hdr

    
   def Insert_work(self):
        self.fileName = filedialog.askopenfilename( filetypes= ( ("only trk files", ".trk"),("trk files","*.trk*")) )
        print(self.fileName)
        #np.random.seed(0)
        # test tractogram
   	    #test_tractogram = "100307"
        T_A_filename = self.fileName
        T_A,T_A2, hdr = self.load(T_A_filename, threshold_short_streamlines=10.0)
        print("Show the tract")
        color= colors.green
        color2= colors.sky_blue
        self.show_tract( T_A,T_A2,color,color2)
        
        #self.show_tract( color)
    

   def init_window(self):
          self.master.title("Tractogram")
          self.pack(fill=BOTH,expand=1)
          button1=Button(self,text='Insert',command=self.Insert_work)
          button1.place(x=0,y=0)

   def __init__(self, master=None):
         Frame.__init__(self, master,bg='black')

         self.master = master

         self.init_window()

if __name__ == '__main__':
    root=Tk() 
    root.geometry("800x600")
    app=Window(root)
    root.mainloop()
    