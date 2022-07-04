from django.forms import EmailField, EmailInput, ModelForm, TextInput, Textarea
from . models import Comment


class CommentForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
    
    class Meta:
        model = Comment
        fields = ["fullname", "email", "body"] 
        
        widgets = {
            'fullname': TextInput(attrs={'placeholder': 'Fullname',
                'class': 'block w-full border shadow rounded-lg outline-none mb-2 px-4 py-3',}),
            
            'email': EmailInput(attrs={'placeholder': 'Email', 
                'class': 'block w-full border shadow rounded-lg outline-none mb-2 px-4 py-3'}),
            
            'body': Textarea(attrs={'placeholder': 'Comment', 
                'class': 'block w-full border shadow rounded-lg outline-none appearance-none mb-2 px-4 py-3'})
        }
        