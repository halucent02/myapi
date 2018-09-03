from django.db import models
from .utils import PathAndRename

# S3 configurations and logic here:
# Since i dont have an Amazon account this is temporarily disabled

# import os
# import boto3
# from boto3.s3.transfer import S3Transfer

# local_directory = 'Local directory path'
# transfer = S3Transfer(boto3.client('s3', 'Bucket region', 
#                                    aws_access_key_id = '*********',
#                                    aws_secret_access_key='********'))
# client = boto3.client('s3')
# bucket = 'Bucket name'
# for root, dirs, files in os.walk(local_directory):
#     for filename in files:
#         local_path = os.path.join(root, filename)
#         relative_path = os.path.relpath(local_path, local_directory)
#         s3_path = os.path.join('S3 path',relative_path)
#         if filename.endswith('.pdf'):
#             aws = transfer.upload_file(local_path, bucket, s3_path,extra_args={'ACL': 'public-read'})
#         else:
#             aws = transfer.upload_file(local_path, bucket, s3_path)


# make a new instance for PathAndRename()
# pathandrename = PathAndRename(aws,file type, additional file extension)

class Item(models.Model):
    name    = models.CharField(max_length=100, blank=True, null=True, default='')
    file    = models.FileField(upload_to=PathAndRename("file","image","test"),max_length=100, blank=True, null=True)
    size    = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return self.name

    class Meta:
        ordering = ('created',)
