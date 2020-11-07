from django.db import models

# Create your models here.
class Dreamreal(models.Model):

    website = models.CharField(max_length = 50)
    mail = models.CharField(max_length = 50)
    name = models.CharField(max_length = 50)
    phonenumber = models.IntegerField()
    online = models.ForeignKey('Online', on_delete = models.SET_DEFAULT, default = 1)

    def __str__(self):
        return "%s %s %s %s" % (self.website, self.mail, self.name, self.phonenumber)

    class Meta:
        db_table = "dreamreal"

class Online(models.Model):
    domain = models.CharField(max_length = 30)

    def __str__(self):
        return "%s" % (self.domain)

    class Meta:
        db_table = "online"