from django.db import models

#Model for black cards which are prompts.
class BlackCard(models.Model):
	text = models.CharField(max_length=225)

	def __str__(self):
		return self.text

#Model for white cards which are supposed to be funny I think??
class WhiteCard(models.Model):
        text = models.CharField(max_length=225)

        def __str__(self):
                return self.text

#Model for users at lib
class usersatlib(models.Model):
        name = models.CharField(max_length=225)

        def __str__(self):
                return self.text

#Model for book
class Book(models.Model):
        title = models.CharField(max_length=225)
	 

        def __str__(self):
                return self.text




