from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    user = models.CharField(max_length=100)
    portfolio_title = models.CharField(max_length=200)
    portfolio_description = models.TextField(blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='portfolio')

    def __str__(self):
        return self.portfolio