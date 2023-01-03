import os


def main():
    print("Main")


def make_image(self, image_name, base_name):
    if not os.path.exists('/images/' + image_name):
        try:
            os.mkdir(str(os.getcwd())+'/images/' + image_name)
        except:
            "This folder exists"
    try:
        if not os.path.exists('/images/' + image_name+'/'+image_name+'_operating'):
            os.mkdir(str(os.getcwd())+'/images/' +
                     image_name+'/'+image_name+'_operating')
    except:
        print("This folder exists")
    if base_name == "base":
        try:
            if not os.path.exists('/images/' + image_name+'/'+image_name+'_base'):
                os.mkdir(str(os.getcwd())+'/images/' +
                         image_name+'/'+image_name+'_base')
        except:
            print("This folder exists")
        os.system('libcamera-jpeg -o '+' images/' + image_name +
                  '/' + image_name + '_base'+'/'+image_name + '_base'+'.jpg')
    else:
        try:
            os.mkdir(str(os.getcwd())+'/images/' + image_name+"/"+image_name)
        except:
            print("This folder exists")
        os.system('libcamera-jpeg -o '+' images/'+image_name+'/' + image_name + '/' +
                  image_name+str(1+len(os.listdir('images/'+image_name+'/' + image_name)))+'.jpg')
    self.comboBox_prod_update()


if __name__ == "__main__":
    main()
