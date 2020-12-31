from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core import validators

# Create your models here.
# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.is_admin = True
        user.is_customer = False
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    id = models.BigAutoField(
        primary_key=True,
    )

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        validators=[
            validators.EmailValidator("Invalid Email")
        ]
    )
    
    first_name = models.CharField(
        max_length=50, 
        verbose_name='First Name',
        blank=False,
        null=False,
        validators=[
            validators.MinLengthValidator(3, message="First name is too short"),
            validators.MaxLengthValidator(15, message="First name is too long"),
        ]
    )

    last_name = models.CharField(
        max_length=50, 
        verbose_name='Last Name',
        blank=False,
        null=False,
        validators=[
            validators.MinLengthValidator(3, message="Last name is too short"),
            validators.MaxLengthValidator(15, message="Last name is too long"),
        ]
    )

    date_joined = models.DateTimeField(
        auto_now_add=True
    )

    last_updated = models.DateTimeField(
        auto_now=True
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) # a admin user; non super-user
    is_admin = models.BooleanField(default=False) # a superuser
    is_merchant=models.BooleanField(default=False)
    is_customer = models.BooleanField(default=True)
    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password are required by default.

    objects = UserManager()

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

class CustomerDetails(models.Model):

    STATES = (
        ('Kerala', 'Kerala'),
        ('Karnataka', 'Karnataka')
    )

    id = models.BigAutoField(
        primary_key=True
    )

    phone = models.CharField(
        max_length=10,
        verbose_name='Phone Number',
        unique=True,
        validators=[
            validators.MinLengthValidator(10),
        ]
    )

    address = models.TextField(
        max_length=300,
        verbose_name='Address'
    )

    pin = models.CharField(
        verbose_name="Postal Code",
        max_length=6,
        validators=[
            validators.RegexValidator('^[1-9]{1}[0-9]{2}\\s{0,1}[0-9]{3}$', "Invalid Pin Number")
        ]
    )

    city = models.CharField(
        verbose_name="City",
        max_length=50,
        validators=[
            validators.MinLengthValidator(3, "Invalid city name")
        ]
    )

    state = models.CharField(
        max_length=50,
        choices=STATES,
        default='Kerala'
    )

    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE
    )