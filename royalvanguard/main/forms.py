from django import forms

class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': "form-control", "placeholder":"Your nnName"}))
    email = forms.EmailField(required=False, widget=forms.Textarea(attrs={'class': "form-control", "placeholder":"Your Email"}))
    phone = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': "form-control", "placeholder":"Your phone"}))
    subject = forms.CharField(max_length=100, required=False,  widget=forms.Textarea(attrs={'class': "form-control", "placeholder":"Subject"}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control send-message-form", 'cols': 80, 'rows': 40, "placeholder":"Leave a message here"}))

