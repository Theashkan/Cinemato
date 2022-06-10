from django import forms
from posts.models import Comment

# Create your forms here.

class ShareForm(forms.Form):
	subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	email = forms.EmailField(max_length = 150, widget=forms.TextInput(attrs={'class': 'form-control'}))
	message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ("name" , "email", "body")
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'email': forms.EmailInput(attrs={'class':'form-control'}),
			'body': forms.Textarea(attrs={'class':'form-control'})
		}
