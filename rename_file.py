import os

def rename_files():
    files_list = os.listdir(r'C:/Machine Learning\Python\prank')
    #print files_list
    
    os.chdir(r'C:/Machine Learning\Python\prank')
    for i in files_list:
        os.rename(i,i.translate(None, '0123456789'))
        


rename_files()
    
