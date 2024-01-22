from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

class Profile(models.Model):
    USER_TYPE_CHOICES = [
        ('individual', 'Физическое лицо'),
        ('business', 'Юридическое лицо'),
    ]

    STATUS_CHOICES = [
        ('seller', 'Продавец'),
        ('buyer', 'Покупатель'),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    full_name = models.CharField(max_length=80)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',
                              blank=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона', 
                                    validators=[RegexValidator(r'^\+?\d{9,15}$', 
                                    'Введите правильный номер телефона.')])

    email = models.EmailField()

    def __str__(self):
        return f'Profile of {self.user.username}'
    
class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    text = models.TextField()
    link = models.URLField(blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f'Message from {self.sender.username} to {self.recipient.username}'
