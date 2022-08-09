
from email.policy import default
from tokenize import PseudoExtras
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.CharField(default='Hola, twitter', max_length=100)
	image = models.ImageField(default='default.png')

	def __str__(self):
		return f'Perfil de {self.user.username}'

	def following(self):
		user_ids = Relationship.objects.filter(from_user=self.user)\
									.values_list('to_user_id', flat=True)
		return User.objects.filter(id__in=user_ids)

	def followers(self):
		user_ids = Relationship.objects.filter(to_user=self.user)\
									.values_list('from_user_id', flat=True)
		return User.objects.filter(id__in=user_ids)
    
class Post(models.Model):
	timestamp = models.DateTimeField(default=timezone.now)
	content = models.TextField()
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

	class Meta:
		ordering = ['-timestamp']

	def __str__(self):
		return self.content

class Relationship(models.Model):
	from_user = models.ForeignKey(User, related_name='relationships', on_delete=models.CASCADE)
	to_user = models.ForeignKey(User, related_name='related_to', on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.from_user} to {self.to_user}'

class Hijos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    nombre = models.CharField(max_length=50, default='nombre')
    sexo = models.BooleanField(default=True)
    tipo = models.CharField(max_length=30, default='nino')
    profile_pic = models.ImageField(default='default.png')
    
    def __str__(self):
        return f'{self.user} to {self.nombre}'
    
class Consultas(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, default=1)
    tipo = models.CharField(max_length=30, default='consulta')
    fecha = models.DateField(auto_now=True)
    talla = models.CharField(max_length=20, default='talla', blank=True)
    peso = models.CharField(max_length=20, default='peso', blank=True)
    nombre = models.ForeignKey(Hijos, on_delete=models.CASCADE, null=True, blank=True)
    recomendacion = models.CharField(max_length=200, default='Recomendacion')
    dato1 = models.CharField(max_length=100, default='dato1')
    dato2 = models.CharField(max_length=100, default='dato2')
    dato3 = models.CharField(max_length=100, default='dato3')
    pic = models.ImageField(default='default.png')
    
    def __str__(self):
        return f'{self.nombre} a {self.tipo}'
    
	
    
    
    

