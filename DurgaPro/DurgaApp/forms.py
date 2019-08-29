from django import forms
from multiselectfield import MultiSelectFormField

class FeedbackForm(forms.Form):
    name=forms.CharField(
        label='Enter Your Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Name',
            }
        )
    )

    rating=forms.IntegerField(
        label="Enter Your Rating",
        widget=forms.NumberInput(
            {
                'class':'form-control',
                'placeholder':'Your Rating'
            }
        )
    )

    feedback=forms.CharField(
        label='Enter Your Feedback',
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Your Feedback'
            }
        )
    )


class EnquiryForm(forms.Form):
    name=forms.CharField(
        label='Enter Your Name',
        widget=forms.TextInput(

            attrs={
                'class':'form-control',
                'placeholder':'Your Name'
            }
        )
    )

    email=forms.EmailField(
        label='Enter Your Email',
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Email'
            }
        )
    )

    mobile=forms.IntegerField(
        label='Enter Your Mobile Number',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Mobile Number'
            }
        )
    )

    Gender_Choices=(
        ('F','Feamle'),
        ('M','Male')
    )


    gender=forms.ChoiceField(
        widget=forms.RadioSelect,choices=Gender_Choices
    )

    COURSES_CHOICES = (
        ('Py', 'Python'),
        ('Dj', 'Django'),
        ('RA', 'Rest-API'),
        ('Fl', 'Flask'),
        ('UI', 'UI')
    )


    courses=MultiSelectFormField(choices=COURSES_CHOICES)

    SHIFTS_CHOICES = (
        ('Mor', 'Morning Shift'),
        ('Afternoon', 'Afternoon Shift'),
        ('Evening', 'Evening Shift'),
        ('Night', 'Night Shift')
    )

    shifts=MultiSelectFormField(choices=SHIFTS_CHOICES)

    start_date=forms.DateField(
        widget=forms.SelectDateWidget()
    )