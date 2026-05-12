from django.db import models

# Create your models here.


class Question(models.Model):
    text = models.TextField()           
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:60]   


class Option(models.Model):
    question = models.ForeignKey(
        Question,
        related_name='options',         
        on_delete=models.CASCADE        
    )
    text = models.CharField(max_length=300) 
    is_correct = models.BooleanField(default=False)  

    def __str__(self):
        return f"{self.question.text[:30]} → {self.text[:30]}"