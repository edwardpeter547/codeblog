from django.forms import EmailInput, ModelForm, TextInput, Textarea
from . models import Contact


class ContactForm(ModelForm):
    
    class Meta:
        model = Contact
        fields = ["fullname", "email", "message"]
        
        widgets = {
            'fullname': TextInput(attrs={'placeholder': 'Fullname',
                    'class': 'block w-full border shadow rounded-lg outline-none mb-2 px-4 py-3'}),
            
            'email': EmailInput(attrs={'placeholder': 'Email', 
                    'class': 'block w-full border shadow rounded-lg outline-none mb-2 px-4 py-3'}), 
            
            'message': Textarea(attrs={'placeholer': 'Message', 
                    'class': 'block w-full border shadow rounded-lg outline-none appearance-none mb-2 px-4 py-3'})
        }