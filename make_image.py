import os
import ui
def main():
    print("Main")
def make_image(self,image_name,base_name):
    if not os.path.exists('/images/'+ image_name):
        os.mkdir(str(os.getcwd())+'/images/'+ image_name)
    if base_name == "base":
        os.system('libcamera-jpeg -o '+' images/'+ image_name + '/'+ image_name +'_base'+'/'+image_name +'_base'+'.jpg')
    else:
        if not os.path.exists('images/'+ base_name+'/'+ image_name):
            os.mkdir(str(os.getcwd())+'images/'+ image_name)
        os.system('libcamera-jpeg -o '+' images/'+base_name+'/'+ image_name +'/'+image_name+(1+len(os.listdir('images/'+base_name+'/'+ image_name)))+'.jpg')
    self.comboBox_prod_update()



if __name__ == "__main__":
    main()
