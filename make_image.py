import os
import ui
def main():
    print("Main")
def make_image(self,image_name,base_name):
    if not os.path.exists('/images/'+ image_name):
        try: 
            os.mkdir(str(os.getcwd())+'/images/'+ image_name)
        except:
            "Folder problem"
    if base_name == "base":
        if not os.path.exists('/images/'+ image_name):
            os.mkdir(str(os.getcwd())+'/images/'+ image_name+'/'+image_name+'_base')
        os.system('libcamera-jpeg -o '+' images/'+ image_name + '/'+ image_name +'_base'+'/'+image_name +'_base'+'.jpeg')
    else:
        try:
            os.mkdir(str(os.getcwd())+'images/'+ image_name+"/"+image_name)
        except:
            print("Folder już istnieje")
        os.system('libcamera-jpeg -o '+' images/'+image_name+'/'+ image_name +'/'+image_name+str(1+len(os.listdir('images/'+image_name+'/'+ image_name)))+'.jpeg')
    self.comboBox_prod_update()



if __name__ == "__main__":
    main()
