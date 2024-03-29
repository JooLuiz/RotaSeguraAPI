from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import EMPTY_VALUES
from django.forms import ValidationError
from django.utils.translation import ugettext_lazy as _
import re

error_messages = {
    'invalid': _("Invalid CPF number."),
    'digits_only': _("This field requires only numbers."),
    'max_digits': _("This field requires exactly 11 digits."),
}

def DV_maker(v):
	if v >= 2:
	    return 11 - v
	return 0

class User(AbstractUser):
    pass

    def upload_to(instance, filename):
    	return 'uploads/{cpf}/{filename}'.format(
        	cpf=instance.cpf, filename=filename)

    def upload_to_background(instance, filename):
    	return 'uploads/{cpf}/background_{filename}'.format(
        	cpf=instance.cpf, filename=filename)

    def validate_CPF(value):
	    if value in EMPTY_VALUES:
	        return u''
	    if not value.isdigit():
	        value = re.sub("[-\.]", "", value)
	    orig_value = value[:]
	    try:
	        int(value)
	    except ValueError:
	        raise ValidationError(error_messages['digits_only'])
	    if len(value) != 11:
	        raise ValidationError(error_messages['max_digits'])
	    orig_dv = value[-2:]

	    new_1dv = sum([i * int(value[idx]) for idx, i in enumerate(range(10, 1, -1))])
	    new_1dv = DV_maker(new_1dv % 11)
	    value = value[:-2] + str(new_1dv) + value[-1]
	    new_2dv = sum([i * int(value[idx]) for idx, i in enumerate(range(11, 1, -1))])
	    new_2dv = DV_maker(new_2dv % 11)
	    value = value[:-1] + str(new_2dv)
	    if value[-2:] != orig_dv:
	        raise ValidationError(error_messages['invalid'])
	        return orig_value

    cpf = models.CharField(unique=True, max_length=14, validators=[validate_CPF])
    avatar = models.ImageField(upload_to=upload_to, null=True, blank=True, default='defaultAvatar.jpg')
    background = models.ImageField(upload_to=upload_to_background, null=True, blank=True, default='defaultBackground.jpg')
