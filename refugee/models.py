from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator


class refugge(models.Model):
    case_number = models.IntegerField(validators=[MaxValueValidator(9999999999)])
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    father_name = models.CharField(max_length=25)
    mother_name = models.CharField(max_length=25)
    hotspot_code = models.ForeignKey("hotspot", to_field='hotspot_code', on_delete=models.CASCADE)
    citizenship_code = models.ForeignKey("citizenships", to_field='citizenship_code', on_delete=models.CASCADE)
    sex_code = models.ForeignKey("sex", to_field='sex_code', on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    skills = models.ForeignKey("skills", to_field='skill_code', on_delete=models.CASCADE)
    marital_status_code = models.ForeignKey("marital_status", to_field='marital_status_code', on_delete=models.CASCADE)
    destination_country_code = models.ForeignKey(
        "destination_country", to_field='destination_country_code', on_delete=models.CASCADE)
    asylum_request = models.CharField(max_length=5)
    email_address = models.EmailField(max_length=30)
    photo_picture = models.ImageField()
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    # class Meta:
    #     verbose_name = _('Πρόσφυγας')
    #     verbose_name_plural = _('Πρόσφυγες')

    def __str__(self):
        return f'{self.first_name}  {self.last_name}'


class hotspot(models.Model):
    hotspot_code = models.IntegerField(validators=[MaxValueValidator(99999)], unique=True)
    hotspot_location = models.CharField(max_length=20)
    hotspot_capacity = models.IntegerField(validators=[MaxValueValidator(9999999999)])

    def __str__(self):
        return f'{self.hotspot_code}'


class citizenships(models.Model):
    citizenship_code = models.IntegerField(validators=[MaxValueValidator(99999)], unique=True)
    citizenship_country = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.citizenship_code} {self.citizenship_country}'


class sex(models.Model):
    sex_code = models.IntegerField(validators=[MaxValueValidator(99999)], unique=True)

    def __str__(self):
        return self.sex_code


class skills(models.Model):
    skill_code = models.IntegerField(validators=[MaxValueValidator(99999)], unique=True)
    skill_description = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.skill_code} {self.skill_description}'


class marital_status(models.Model):
    marital_status_code = models.IntegerField(validators=[MaxValueValidator(99999)], unique=True)
    no_of_children = models.IntegerField(validators=[MaxValueValidator(999)])
    marital_status_description = models.CharField(max_length=10)

    def __str__(self):
        return self.marital_status_code


class destination_country(models.Model):
    destination_country_code = models.IntegerField(validators=[MaxValueValidator(99999)], unique=True)
    destination_country_description = models.CharField(max_length=25)

    def __str__(self):
        return self.destination_country_code
