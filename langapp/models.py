from django.db import models

# Create your models

from django.db import models

CLASS = [
    ('SS1', 'ss1'),
    ('ss2', 'SS2'),
    ('SS3', 'ss3')
]


# Create your models here.
class ContactForm(models.Model):
    subject = models.CharField(max_length=250, default='user')
    message = models.TextField(max_length=300)
    sender = models.EmailField()
    cc_myself = models.BooleanField()

    def __str__(self):
        return '%s' % self.subject


class FormMasters(models.Model):
    form_master_name = models.CharField(max_length=250)
    class_for = models.CharField(max_length=250)

    def __str__(self):
        return '%s' % self.form_master_name
