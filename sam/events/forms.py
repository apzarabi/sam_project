# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User

from .models import Event

persian_default_errors = {
    'required': u"این فیلد الزامی است.",
}
class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        exclude = ['condition', 'condition_description', 'subcategory', 'id_of_subcategory', 'dealer']

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'type': "text",
                                                     'class': "form-control",
                                                     'id': "name",
                                                     'placeholder': u"نام",
                                                     })
        self.fields['address'].widget.attrs.update({'type': "text",
                                                     'class': "form-control",
                                                     'id': "address",
                                                     'placeholder': u"نشانی",
                                                     })
        self.fields['neighborhood'].widget.attrs.update({'type': "text",
                                                     'class': "form-control",
                                                     'id': "neighborhood",
                                                     'placeholder': u"محله",
                                                     })
        self.fields['description'].widget.attrs.update({'type': "text",
                                                     'class': "form-control",
                                                     'id': "description",
                                                     'placeholder': u"توضیحات",
                                                     })
        self.fields['latitude'].widget.attrs.update({'type': "float",
                                                     'class': "form-control",
                                                     'id': "latitude",
                                                     'placeholder': u"عرض جغرافیایی",
                                                     })
        self.fields['longitude'].widget.attrs.update({'type': "float",
                                                     'class': "form-control",
                                                     'id': "longitude",
                                                     'placeholder': u"طول جغرافیایی",
                                                     })
        self.fields['phone_number'].widget.attrs.update({'type': "text",
                                                     'class': "form-control",
                                                     'id': "phone_number",
                                                     'placeholder': u"شماره تلفن",
                                                     })
