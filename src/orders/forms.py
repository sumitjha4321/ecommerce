from django import forms
from .models import UserCheckOut, UserAddress


#TUTORIAL WAS USING USER MODEL TO RAISE "A USER WITH THAT EMAIL ALREADY EXISTS..". 
# FIGURE OUT LATER THAT WHAT MODEL TO USE (USER OR USERCHECKOUT), AS OF NOW, I AM USING USERCHECKOUT MODEL.
#from django.contrib.auth import get_user_model
#User = get_user_model() 

class GuestCheckOutForm(forms.Form):
	email = forms.EmailField()
	email2 = forms.EmailField(label = "Email Again")

	def clean_email2(self): #VVI --> MUST DO CLEAN_EMAIL2
		print self.cleaned_data
		email = self.cleaned_data["email"]
		email2 = self.cleaned_data["email2"]

		if email == email2:
			
			if UserCheckOut.objects.filter(email=email).count() != 0:
				raise forms.ValidationError("User already exists. Please login instead.")
				
			return email
		else:
			raise forms.ValidationError("Please make sure the emails in both field matches.")
		return email

class AddressForm(forms.Form):
	shipping_address = forms.ModelChoiceField(
		queryset = UserAddress.objects.all(),
		empty_label = None,
		widget=forms.RadioSelect,
		)
	billing_address = forms.ModelChoiceField(
		queryset = UserAddress.objects.all(),
		empty_label = None,
		widget=forms.RadioSelect,
		

		)

class UserAddressForm(forms.ModelForm):
	class Meta:
		model = UserAddress
		fields = [
			'name',
			'mobile',
			'address1',
			'address2',
			'pin',
			'state',
			'type',

		]