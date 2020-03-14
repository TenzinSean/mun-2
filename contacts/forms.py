from django import forms


class Contact(forms.Form):
    Email = forms.Emailfield()


    def __str__(self):
        return self.Email