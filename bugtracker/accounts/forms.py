from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    

    def clean_username(self):
        username = self.cleaned_data.get('username', '').strip()
        if not username:
            raise forms.ValidationError("Username cannot be empty.")
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password', '').strip()
        if not password:
            raise forms.ValidationError("Password cannot be empty.")
        return password
    
class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=False)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean_username(self):
        username = self.cleaned_data.get('username', '').strip()
        if not username:
            raise forms.ValidationError("Username cannot be empty.")
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password', '').strip()
        if not password:
            raise forms.ValidationError("Password cannot be empty.")
        return password