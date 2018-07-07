from django import forms
from demo.constants.Master import MEAL_CHOICE, SERVICE_CHOICE, RANK_CHOICE


class ExEditForm(forms.Form):
  name = forms.CharField(
      label='ホテル名',
      max_length=20,
      widget=forms.TextInput(
          attrs={'class': 'form-control'}
      )
  )
  address = forms.CharField(
      label='アドレス',
      max_length=100,
      widget=forms.TextInput(
          attrs={'class': 'form-control'}
      )
  )
  stars = forms.ChoiceField(
      label='ランク',
      choices=RANK_CHOICE,
      widget=forms.Select(
          attrs={'class': 'form-control'}
      )
  )
  meal = forms.ChoiceField(
      label='食事',
      choices=MEAL_CHOICE,
      widget=forms.RadioSelect(
          attrs={'class': 'custom-control-input'}
      ),
      initial=0
  )
  service = forms.MultipleChoiceField(
      label='サービス',
      widget=forms.CheckboxSelectMultiple(
          attrs={'class': 'custom-control-input'}
      ),
      choices=SERVICE_CHOICE
  )
  comments = forms.CharField(
      label='コメント',
      max_length=100
      #   attrs={'size': 40}
  )
  # open_date
