from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        name = kwargs.get("name", "")
        age = kwargs.get("age")
        gender = kwargs.get("gender")
        introduction = kwargs.get("introduction")
        if not email:
            raise ValueError("Users must have an email address")
        if name is None or not name.strip():
            raise ValueError("Users must have an valid name")
        if not age:
            raise ValueError("Users must have an age")
        if not gender or gender not in ("M", "F"):
            raise ValueError("Users must have an valid gender")
        user = self.model(
            email=self.normalize_email(email),
            name=name,
            age=age,
            gender=gender,
            introduction=introduction,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **kwargs):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email, password=password, **kwargs)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=30)
    age = models.PositiveIntegerField()
    GENDERS = (
        ("M", "Male"),
        ("F", "Female"),
    )
    gender = models.CharField(choices=GENDERS, max_length=1)
    introduction = models.TextField(default="-", null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "name",
        "age",
        "gender",
    ]

    def __str__(self):
        return f"{self.name} ({self.email})"

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
