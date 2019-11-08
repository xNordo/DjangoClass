from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
	title		= forms.CharField(label='',
					widget=forms.TextInput(attrs={"placeholder": "type your title here"}))
	#email		= forms.EmailField()
	description	= forms.CharField(
						required=False,
						widget=forms.Textarea(
								attrs={
									"class": "new-class-name two",
									"id": "my-id-for-textarea",
									"rows": 20,
									"cols": 70

								}
							)
						)
	price		= forms.DecimalField(initial=199.99)

	class Meta:
		model = Product
		fields = {
			'title',
			'price',
			'description'
		}
	def clean_title(self, *args, **kwargs):
		title = self.cleaned_data.get("title")
		if not 'CFE' in title:
			raise forms.ValidationError("There is no CFE in title")
		if not 'news' in title:
			raise forms.ValidationError("There is no news in title")
		else:
			return title

	def clean_email(self, *args, **kwargs):
		email = self.cleaned_data.get("email")
		if not email.endswith("edu"):
			raise forms.ValidationError("This is not a valid email")
		return email



class RawProductForm(forms.Form):
	title		= forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "type your title here"}))
	description	= forms.CharField(
						required=False,
						widget=forms.Textarea(
								attrs={
									"class": "new-class-name two",
									"id": "my-id-for-textarea",
									"rows": 20,
									"cols": 60

								}
							)
						)
	price		= forms.DecimalField(initial=199.99)
