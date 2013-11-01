from django.db import models

# Create your models here.

class Poll(models.Model):
  # Creates a class that subclasses models.Model

  # Each of these variables is a field
  # Fields are stored as columns in a database
  # The columns are named after their variable names (e.g. question)


  question = models.CharField(max_length=200)
  
  # pub_date has the machine name pub_date
  # pub_date actually changed its variable name to 'date published'
  # its human-readable name
  pub_date = models.DateTimeField('date published')

class Choice(models.Model):
  # models.ForeignKey(Poll) creates a relationship between classes
  # django all common database relationships: many-to-ones, many-to-manys
  # one-to-ones
 
  # poll = models.ForeignKey(poll) shows that each choice is related
  # to a single poll
  poll = models.ForeignKey(Poll)
  choice_text = models.CharField(max_length=200)
  vote = models.IntegerField(default=0)


