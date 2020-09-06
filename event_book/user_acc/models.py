from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from rest_framework_simplejwt.tokens import RefreshToken

# Create your models here.


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, username, first_name, last_name, address, phone, city, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        if not username:
            raise ValueError(_('The Username must be set'))
        if not first_name:
            raise ValueError(_('The First name must be set'))
        if not last_name:
            raise ValueError(_('The Last name must be set'))
        if not address:
            raise ValueError(_('The Address must be set'))
        if not phone:
            raise ValueError(_('The Phone must be set'))
        if not city:
            raise ValueError(_('The City must be set'))

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            address=address,
            phone=phone,
            city=city,
        )

        # user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, last_name, address, phone, city, password, **extra_fields):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            first_name=first_name,
            last_name=last_name,
            address=address,
            phone=phone,
            city=city,
        )

        """
      Create and save a SuperUser with the given email and password.
      """
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
        # extra_fields.setdefault('is_staff', True)
        # extra_fields.setdefault('is_superuser', True)
        # extra_fields.setdefault('is_active', True)

        # if extra_fields.get('is_staff') is not True:
        #     raise ValueError(_('Superuser must have is_staff=True.'))
        # if extra_fields.get('is_superuser') is not True:
        #     raise ValueError(_('Superuser must have is_superuser=True.'))
        # return self.create_user(email, password, **extra_fields)


class Account(AbstractBaseUser):

    email = models.EmailField(
        verbose_name='email address', max_length=255, unique=True
    )
    username = models.CharField(
        verbose_name='username', max_length=255, unique=True)
    first_name = models.CharField(
        verbose_name='first name', max_length=30, blank=True)
    last_name = models.CharField(
        verbose_name='last name', max_length=150, blank=True)
    address = models.TextField(
        verbose_name='address', max_length=500, blank=True)
    phone = models.TextField(verbose_name='phone', max_length=50, blank=True)

    # password field supplied by AbstractBaseUser
    # last_login field supplied by AbstractBaseUser
    cities = (
        ('Accra', 'Accra'),
        ('Kumasi', 'Kumasi'),
        ('Tamale', 'Tamale'),
        ('Takoradi', 'Takoradi'),
        ('Sunyani', 'Sunyani'),
        ('Cape_Coast', 'Cape Coast'),
        ('Obuasi', 'Obuasi'),
        ('Teshie', 'Teshie'),
        ('Koforidua', 'Koforidua'),
        ('Wa', 'Wa'),
        ('Bolgatanga', 'Bolgatanga'),
    )

    city = models.CharField(verbose_name='city', max_length=50,
                            choices=cities, default='')

    # Designates whether this user should be treated as active.
    # Unselect this instead of deleting accounts.
    is_active = models.BooleanField(default=True)

    # Designates whether the user can log into this admin site.
    is_staff = models.BooleanField(default=False)

    # is_superuser field provided by PermissionsMixin
    # groups field provided by PermissionsMixin
    # user_permissions field provided by PermissionsMixin

    date_joined = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name',
                       'last_name', 'address', 'phone', 'city']

    objects = CustomUserManager()

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def __str__(self):
        return '{} <{}>'.format(self.get_full_name(), self.email)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)

        }