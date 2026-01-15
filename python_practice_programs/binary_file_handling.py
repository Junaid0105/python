import pickle
#binary file 
li = ["junaid",25,"Amroha"]

file_object = open("bi_practice.dat","wb")

pickle.dump(li,file_object)
file_object.close()

file =open("bi_practice.dat","rb")
data = file.read()
print(data)