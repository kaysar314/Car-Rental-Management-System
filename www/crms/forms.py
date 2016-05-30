
from django import forms
from .models import BRAND_CHOICES, GEAR_BOX_CHOICES, get_model_choices, Car, get_free_car_choices
import datetime

class RegisterCarForm(forms.Form):
    car_name = forms.CharField(
        label=u'Car name',
        max_length=50,
    )
    brand = forms.ChoiceField(
        label=u'Brand',
        choices=BRAND_CHOICES,
    )
    model = forms.ChoiceField(
        label=u'Model',
        choices=get_model_choices(),
    )
    gear_box = forms.ChoiceField(
        label=u'Gear box',
        choices=GEAR_BOX_CHOICES,
    )
    image = forms.ImageField(
        label=u'Image',
    )
    displacement = forms.DecimalField(
        label=u'Dispalcement',
        max_digits=3,
        decimal_places=1,
    )
    description = forms.CharField(
        label=u'Description',
        widget=forms.Textarea(attrs={'placeholder': 'Please enter the  description'}),
    )

    def is_valid(self):
        print("-----is_valid begin------")
        if super(RegisterCarForm, self).is_valid():
            print("Valid")
        else:
            print("Invalid")
        print("-----is_valid end------")
        return super(RegisterCarForm, self).is_valid()

    def clean_image(self):
        image = self.cleaned_data['image']
        if image == None:
            raise forms.ValidationError(u'No Image')
        return image

    def clean(self):
        cleaned_data = super(RegisterCarForm, self).clean()
        print("------Car Register clean-------")
        print(cleaned_data['car_name'])
        print(cleaned_data['brand'])
        print(cleaned_data['model'])
        print(cleaned_data['gear_box'])

        print(cleaned_data['displacement'])
        print(cleaned_data['description'])
        print("------Car Register clean ends-------")

    def save(self):
        print("------Car Register Save-------")
        car_name = self.cleaned_data.get('car_name')
        brand = self.cleaned_data.get('brand')
        model = self.cleaned_data.get('model')
        gear_box = self.cleaned_data.get('gear_box')
        img = self.cleaned_data.get('image')
        displacement = self.cleaned_data.get('displacement')
        description = self.cleaned_data.get('description')
        user = self.user
        car = Car(owner=user, name=car_name, brand=brand, model=model, gear_box=gear_box, image=img, displacement=displacement, description=description)
        car.save()

class RegisterOfferForm(forms.Form):
    car = forms.ChoiceField(
        label=u'Car',
        choices=get_free_car_choices(),
    )
    daily_rental = forms.IntegerField(
        label=u'Daily rental',
        min_value = 0,
    )
    fetch_date = forms.DateTimeField(
        label=u'Fetch date',
        initial=datetime.date.today,
    )
    return_date = forms.DateTimeField(
        label=u'Return date',
        initial=datetime.date.today,
    )

    def clean(self):
        super(RegisterOfferForm, self).clean()
        print("------Offer Register clean-------")

class RegisterDealForm(forms.Form):

    fetch_date = forms.DateTimeField(
        label=u'Fetch date',
        initial=datetime.date.today,
    )
    return_date = forms.DateTimeField(
        label=u'Return date',
        initial=datetime.date.today,
    )
