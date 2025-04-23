from django import forms
from .models import Employee

class UserCreateForm(forms.ModelForm):
    template_name = 'userdoc/form_snippet.html'
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'user_name', 'domain', 'password', 'extension', 'cell_phone', 'slug']

    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    user_name = forms.CharField(label="Username", max_length=100)
    domain = forms.ChoiceField(label="Domain", choices=[("cjmoyna.com", "cjmoyna.com"), ("mobiletracksolutions.com", "mobiletracksolutions.com")])
    password = forms.CharField(label="Password")
    extension = forms.CharField(label="Extension", required=False)
    cell_phone = forms.CharField(label="Cell Phone", required=False, max_length=15)
    slug = forms.CharField(label="Slug", required=False, widget=forms.HiddenInput())

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("user_name")
        if username:
            cleaned_data["slug"] = username.lower().replace(" ", "-")
        else:
            raise forms.ValidationError("Username is required.")
        return cleaned_data

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if not username:
            raise forms.ValidationError("Username is required.")
        return username
    def clean_domain(self):
        domain = self.cleaned_data.get("domain")
        if not domain:
            raise forms.ValidationError("Domain is required.")
        return domain
    def clean_password(self):
        password = self.cleaned_data.get("password")
        if not password:
            raise forms.ValidationError("Password is required.")
        return password
    