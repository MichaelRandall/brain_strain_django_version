from django import forms
from brain_strain.models import Player, Country
from django_countries.widgets import CountrySelectWidget

GENDER_SELECTION = (('M', 'Male', 'male'), ('F', 'Female', 'female'))


class PlayerForm(forms.ModelForm):
    first_name = forms.CharField(max_length=20, help_text="Enter your first name.")
    last_name = forms.CharField(max_length=20, help_text="Enter your last name.")
    user_name = forms.CharField(max_length=60, help_text="Enter your username.")
    email = forms.EmailField(max_length=254, help_text="Enter your email address.")
    player_gender = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices=GENDER_SELECTION)
    #widgets = {'country': CountrySelectWidget}
    player_location = forms.CharField(max_length=60, help_text="Please enter the country name.")

    class Meta:
        model = Player

    fields = ('first_name', 'last_name', 'user_name', 'email', 'player_gender', 'player_country')


class CountryForm(forms.ModelForm):
    country_name = forms.CharField(max_length=254, help_text="Please enter the country name.")

    model = Country

    fields = 'country_name'




# class Category(models.Model):
#     name = models.CharField(max_length=128, unique=True)
#
#     def __unicode__(self):
#         return self.name
#
# class Page(models.Model):
#     category = models.ForeignKey(Category)
#     title = models.CharField(max_length=128)
#     url = models.URLField()
#     views = models.IntegerField(default=0)
#
#     def __unicode__(self):
#         return self.title
#
# class CategoryForm(forms.ModelForm):
#     name = forms.CharField(max_length=128, help_text="Please enter the category name.")
#     views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
#     likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
#
#     # An inline class to provide additional information on the form.
#     class Meta:
#         # Provide an association between the ModelForm and a model
#         model = Category
#
# class PageForm(forms.ModelForm):
#     title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
#     url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
#     views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
#
#     class Meta:
#         # Provide an association between the ModelForm and a model
#         model = Page
#
#         # What fields do we want to include in our form?
#         # This way we don't need every field in the model present.
#         # Some fields may allow NULL values, so we may not want to include them...
#         # Here, we are hiding the foreign key.
#         fields = ('title', 'url', 'views')