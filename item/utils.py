from django.utils.deconstruct import deconstructible
from urllib.parse import urlparse, urlsplit
import os.path
import uuid
from datetime import datetime

# for FileField. override the name of the file and repath
# @author: Charles A. Culaton 2018
class MimeTypeExtension(object):
    def get_ext(self,filename):
         file = os.path.splitext(os.path.basename(urlsplit(filename).path))
         return "%s" % file[1]
       
    def get_name(self,filename):
         file = os.path.splitext(os.path.basename(urlsplit(filename).path))
         return "%s" % file[0]
 
# create intance with sample PathAndRename("dir_location","image category","transaction number")   
@deconstructible
class PathAndRename(object):
    
    def __init__(self, sub_path,  img_cat=None, tr_number=None):
        dt = datetime.now()
        dt = dt.strftime('%m-%d-%Y_%I:%M_%p')
        self.sub_path  = sub_path
        self.img_cat = img_cat
        self.tr_number = dt
        
    def __call__(self, instance, filename):
         mime = MimeTypeExtension()
         ext = mime.get_ext(filename)
         path = self.sub_path
         added_path = (str(self.img_cat) ,str(self.tr_number),str(uuid.uuid4()))
         filename = "-".join(added_path)
         return "%s" %(path+"/"+filename+ext)