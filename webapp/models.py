from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager

class CustomUserManager(BaseUserManager):
   def create_user(self, email=None, password=None,*args, **extra_fields):
        """
        Create and return a regular user with the given email and password.
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
   def create_superuser(self, email, password=None,*args, **extra_fields):
        """
        Create and return a superuser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password,*args, **extra_fields)
   def get_by_natural_key(self, email):
        """
        Retrieve a user using their natural key (email in this case).
        """
        return self.get(email=email)
class User(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(db_index=True,unique=True)

    is_staff =models.BooleanField(default=True)
    is_active =models.BooleanField(default=True)
    is_superuser =models.BooleanField(default=True)
    username=None
    objects= CustomUserManager()

    USERNAME_FIELD ='email'
    REQUIRED_FEILDS =[]

    class Meta:
        verbose_name='User'
        verbose_name_plural='User'


    def __str__(self) :
        return self.email

class Prediction(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=30)
    sex = models.IntegerField(choices=[(0, 'Female'), (1, 'Male')])
    chest_pain_type = models.IntegerField(choices=[(0, 'ATA'), (1, 'NAP'), (2, 'ASY'), (3, 'TA')])
    resting_ecg = models.IntegerField(choices=[(0, 'Normal'), (1, 'ST'), (2, 'LVH')])
    exercise_angina = models.IntegerField(choices=[(0, 'Yes'), (1, 'No')])
    st_slope = models.IntegerField(choices=[(0, 'Up'), (1, 'Flat'), (2, 'Down')])
    fasting_bs = models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], default=0)
    oldpeak = models.FloatField(
        validators=[
            MinValueValidator(-2.6),
            MaxValueValidator(6.2)
        ]
    )

    # Max heart rate with range validation
    max_heart_rate = models.IntegerField(
        validators=[
            MinValueValidator(60),
            MaxValueValidator(202)
        ]
    )
    prediction_result = models.IntegerField(choices=[(0, 'No Heart Disease'), (1, 'Heart Disease')], null=True)

   
    created_at= models.DateTimeField(auto_now_add=True)
    
    

    def _str_(self):
        return f"{self.name} - Prediction: {'Heart Disease' if self.prediction_result else 'No Heart Disease'}"


class Feedback(models.Model):
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField()
    desc = models.TextField(null=True, blank=True)
    def __str__(self) :
        return self.name
    
class Login(models.Model):
    email = models.CharField(max_length=50,null=True)
    password = models.CharField(max_length=50,null=True)
    def __str__(self) :
        return self.email

class Registration(models.Model):
    first_name = models.CharField(max_length=122)
    last_name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    password = models.CharField(max_length=122)
    confirm_password = models.CharField(max_length=122)
    def __str__(self) :
        return self.first_name
   