from django.db import models


class Pessoa(models.Model):
    """ Representa uma pessoa com nome e sobrenome. """
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=250)
    
    #def __str__(self):
        #return "{0} {1}".format(self.nome, self.sobrenome)
