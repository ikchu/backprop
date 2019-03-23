# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Problem(models.Model): # default Django tutorial implementation
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    # binary_expression_tree = 
    # hints = # reach feature, would need to put in a separate class and cross reference
    # comments = # reach feature, would need to put in a separate class and cross reference

    def __str__(self):
        return self.question_text

    # create new Problem, add to Problems db
    # should take care of adding it into the db
    def new():
        return 'Problem.new() not yet implemented'
    
#class Progress(models.Model): # cross reference a user and a problem to get their current progress on the problem

#class User(models.Model): # is this one necessary? Does Django have a built-in user class?

# class Choice(models.Model):
#     problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)