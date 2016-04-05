from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator
from datetime import datetime


class Form(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='homeschool_site/static/uploaded_forms')
    is_visible_by_unreg = models.BooleanField(verbose_name='Seen By Unapproved Users?')

    def __str__(self):
        return self.title


class HomeSchoolUser(AbstractUser):
    STUDENT, ALUMNI, CHAPERONE = 'student', 'alumni', 'chaperone'
    STATUS_CHOICES = (
        (STUDENT, 'Student'),
        (ALUMNI, 'Alumni'),
        (CHAPERONE, 'Chaperone'),
    )

    status = models.CharField(
        choices=STATUS_CHOICES,
        max_length=255,
        help_text='The status of the user.',
        default=STUDENT,
    )

    is_approved = models.BooleanField(default=False)

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        if self.get_full_name() is not " ":
            return self.get_full_name()
        else:
            return self.username


class News(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    time_of_news = models.DateTimeField(default=datetime.now, editable=False)

    class Meta:
        verbose_name_plural = "News"


class RSVP(models.Model):
    user = models.ForeignKey('homeschool_site.HomeSchoolUser')
    response = models.BooleanField()
    note = models.TextField()
    event = models.ForeignKey('homeschool_site.Event', null=True)
    num_guests = models.IntegerField()
    time_rsvpd = models.DateTimeField(default=datetime.now, editable=False)

    def get_user_status(self):
        return self.user.status

    get_user_status.short_description = 'User Status'
    get_user_status.admin_order_field = 'user__status'

    def get_start_of_note(self):
        if len(self.note) > 50:
            return self.note[:50] + '...'
        else:
            return self.note

    def __str__(self):
        return str(self.user) + ": " + str(self.event)

    get_start_of_note.short_description = 'Note'

    class Meta:
        verbose_name = "RSVP"
        verbose_name_plural = "RSVPs"


class Event(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255, null=True)
    date = models.DateField()
    price = models.DecimalField(decimal_places=2, max_digits=6, default=0.00)
    description = models.TextField(null=True)
    other_info = models.TextField(null=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    contact_message = models.TextField(help_text="This will be your greeting message on the Contact Us page.")
    contact_name = models.CharField(max_length=255)
    contact_email = models.EmailField(null=True)
    phone_regex = RegexValidator(regex=r'^\d{10}$', message="Phone number must be 10 digits")
    contact_phone = models.CharField(validators=[phone_regex], null=True, max_length=12)
    active = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.active:
            try:
                temp = Contact.objects.get(active=True)
                if self != temp:
                    temp.active = False
                    temp.save()
            except Contact.DoesNotExist:
                pass
        super().save()


class AboutUs(models.Model):
    message = models.TextField()
    active = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.active:
            try:
                temp = AboutUs.objects.get(active=True)
                if self != temp:
                    temp.active = False
                    temp.save()
            except AboutUs.DoesNotExist:
                pass
        super().save()

    def get_message(self):
        return self.message[:150]

    class Meta:
        verbose_name = "About Us"
        verbose_name_plural = "About Us"
