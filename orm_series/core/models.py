from django.db import models

'''class Courts(models.Model):
    Court_Name = models.TextField()
    Court_Link = models.TextField()
    Scrap_Type = models.PositiveIntegerField()
    Site_Status = models.TextField()
    Response_Code = models.TextField()
    Date_and_Time = models.DateTimeField()
'''

class Court(models.Model):
    Court_Name = models.TextField()
    Court_Link = models.TextField()
    Scrap_Type = models.PositiveIntegerField()
    Site_Status = models.TextField()
    Response_Code = models.TextField()
    Date_and_Time = models.TextField()