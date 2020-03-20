from django.db import models
from django.urls import reverse

# Create your models here.

TIMES = (
  ('M', 'Morning'),
  ('A', 'Afternoon'),
  ('E', 'Evening')
)


class Dog(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField() 
  def __str__(self):
    return self.name    
  def get_absolute_url(self):
    return reverse('dogs_detail', kwargs={'dog_id': self.id})


class Walks(models.Model):
  date = models.DateField('Date Walked')
  time = models.CharField(
    max_length=1,
    choices=TIMES,
    default=TIMES[0][0]
  )
  dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_meal_display()} on {self.date}"
