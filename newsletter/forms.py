from django import forms
from .models import SignUp


class ContactForm(forms.Form):
    full_name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField()


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name', 'email', 'donation', 'doner_kebab']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split("@")
        _, extension = provider.split(".")
        if not extension == "is":
            raise forms.ValidationError(
                "Please go duck urself its Juden site.")
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        return full_name

    def clean_donation(self):
        donation = self.cleaned_data.get('donation')
        if not donation.endswith(("€", "$")):
            raise forms.ValidationError("Ojj wajj gib € or $ !!")
        return donation

    def clean_doner_kebab(self):
        dk = self.cleaned_data.get('doner_kebab')
        if dk not in ("yes", "no"):
            raise forms.ValidationError("Just anwser you wanna kebab!! (yes/no)")
        return dk
