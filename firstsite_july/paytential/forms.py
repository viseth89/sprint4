from django.forms import ModelForm
from paytential.models import Evaluation


class EvaluationForm(ModelForm):
    class Meta:
        model = Evaluation
        fields = ['performance', 'potential', 'feedback', 'user']
