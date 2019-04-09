from django import forms

class NameForm(forms.Form):
    firstName = forms.CharField(label='First Name', max_length=100)
    lastName = forms.CharField(label='Last Name', max_length=100)

class treeSize(forms.Form):
    size = forms.IntegerField(label='Create new tree of size', min_value = 1, max_value = 5, required = False)

class visibility(forms.Form):
    showAll = forms.BooleanField(label='Toggle Answers', required = False)

# class forwardprop(forms.Form):
    
