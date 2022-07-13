from .models import *
from django.forms import ModelForm

class CandidateForm(ModelForm):
    class Meta:
        model=Candidate
        fields='__all__'
        exclude=['total_vote']

class VotersForm(ModelForm):
    class Meta:
        model=Voters
        fields='__all__'
