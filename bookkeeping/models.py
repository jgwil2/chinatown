from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):
    description = models.CharField(max_length=200)
    date_created = models.DateTimeField()

class Participant(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

class Expense(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    paid_by = models.ForeignKey(Participant, on_delete=models.CASCADE)

class Reimbursement(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    paid_by = models.ForeignKey(Participant, on_delete=models.CASCADE,
        related_name='reimbursement_paid_by')
    paid_to = models.ForeignKey(Participant, on_delete=models.CASCADE,
        related_name='reimbursement_paid_to')
