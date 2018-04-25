import os
import subprocess

path = os.getcwd()+'/test_set/'
current_path = os.getcwd()

for filename in os.listdir(path):
    print("Imagem: %s\n" % filename)
    cmd="python -m scripts.label_image --graph="+current_path+"/tf_files/retrained_graph.pb --image="+path+filename
    subprocess.call(cmd, shell=True)
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")