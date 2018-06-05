from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=550, null=False, default="1")
    author = models.CharField(max_length=550, null=False, default="2")
    img_url = models.CharField(max_length=550, null=False, default="3")

	
    def __str__(self):
        """A string representation of the model."""
        return self.name
    #修改表名字
    class Meta():
        db_table = 'books'
