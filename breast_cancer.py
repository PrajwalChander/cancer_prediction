import numpy as np
import pickle
loaded_model=pickle.load(open('C:/Users/PRAJWAL CHANDEER/Dropbox/PC/Desktop/ML to API/python/breast_cancer_classification.sav','rb'))
input1=(11.89,18.35,77.32,432.2,0.09363,0.1154,0.06636,0.03142,0.1967,0.06314,0.2963,1.563,2.087,21.46,0.008872,0.04192,0.05946,0.01785,0.02793,0.004775,13.25,27.1,86.2,531.2,0.1405,0.3046,0.2806,0.1138,0.3397,0.08365)
input_to_array=np.asarray(input1)
reshaped=input_to_array.reshape(1,-1)
predict=loaded_model.predict(reshaped)
if predict[0]=='B':
  print("This is B type cancer")
else:
  print("This is M type cancer")
