__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os, shutil
import zipfile

# Pathing variables
cwd = os.getcwd()
path = os.path.join(cwd, "cache") 

# Make or clean directory "cache"
def clean_cache():   
    if os.path.exists(path):
        shutil.rmtree(path) 
        os.mkdir(path)
    else:
        os.mkdir(path)      

def cache_zip(file, path):
    with zipfile.ZipFile(file,"r") as zip_ref:
        zip_ref.extractall(path)

#takes a zip file path (str) and a cache dir path (str) as arguments
#cache_zip("C:/Users/kvanw/Documents/Winc/files/data.zip", path)

# returns list include path
def cached_files():
    files_list = [os.path.abspath("cache/" + files) for files in os.listdir(path)]
    return files_list

# find hiden password
def find_password(cachedfiles):

    for file in cachedfiles:
        
        with open(file, "r") as txt:
            text = txt.read()         
            
            if "password" in text:

                find_space = text.find(" ")
                password_begin = text[find_space +1:]            
                find_n = password_begin.find("\n")
                password = password_begin[:find_n]                  
                return password             
            else:
                continue
            
    

