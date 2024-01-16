from django import forms

from .models import Question,Company,Division


class QuestionForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)

        self.fields['division'] = forms.TypedChoiceField(
            choices=[(division.id, division.name) for division in Division.objects.all()],
            coerce=int,
            label='Выберите ваш дивизион',
            widget=forms.Select(attrs={
                'class': 'custom-select-class',
                'style': 'width: 400px; height: 30px;'
            }),
        )
        self.fields['company'] = forms.TypedChoiceField(
            choices=[(0, 'другое')] + [(company.id, company.name) for company in Company.objects.all()],
            coerce=int,
            required=False,
            label='Выберите ваше предприятие',
            widget=forms.Select(
                attrs={
                    'class': 'custom-select-class',
                    'style': 'width: 400px; height: 30px;'
                }
            ),
        )

    custom_name_company = forms.CharField(
        max_length=35,
          required=False,
          label='Название предприятия',
        widget=forms.TextInput(
            attrs={
            'class': 'custom-text-input',
            'style': 'width: 400px; height: 30px;'
                    }
            ),
    )
    email = forms.EmailField(
        required=False,
        label='Если вы хотите лично получить ответ на ваш вопрос, оставьте электронную почту,на которую необходимо отправить ответ(можно не корпаративную).',
        widget=forms.EmailInput(
            attrs={
            'class': 'custom-email-input',
            'style': 'width: 400px; height: 30px;'
                    }
            ),
        )

    content = forms.CharField(
        max_length= 1000,
        label='Задайте ваш вопрос генеральному директору Госкорпорации «Росатом» А.Е.Лихачев',
        widget=forms.Textarea(
            attrs={
            'class': 'custom-textarea',
            'style': 'width: 1300px; height: 180px;'
                    }
            ),
        )
    
    



    def clean(self):
        
        cleaned_data = self.cleaned_data
        company_id = cleaned_data.get('company')
        custom_name_company = cleaned_data.get('custom_name_company')

        # Проверяем, если выбрана компания "Другое", то custom_name_company должно быть заполнено
        if company_id == default_company_name_and_id['default_choice_id'] and custom_name_company == '':
            self.add_error('custom_name_company','Поле "Название предприятия" обязательно, если выбрано "другое"')
        if company_id != default_company_name_and_id['default_choice_id'] and custom_name_company !='':
            self.add_error('company',"Если вы указали ваше предприятие, то оставьте поле 'Название предприятия' пустым ")
        
        return cleaned_data


    def save(self, commit=True):
        custom_name_company = self.cleaned_data['custom_name_company']
        division_id = self.cleaned_data['division']
        company_id = self.cleaned_data['company']

        if custom_name_company != '' and company_id == default_company_name_and_id['default_choice_id']:
            company = Company.objects.create(name=custom_name_company, division=Division.objects.get(id=division_id))
        else:
            company = Company.objects.get(id=company_id)
            company.save()
            
    
        Question.objects.create(
            company=company,
            email = self.cleaned_data['email'] if self.cleaned_data['email']!="" else "",
            content=self.cleaned_data['content']
        )


default_company_name_and_id={
        'default_choice_id':
        0,
        'default_choice_name' :
        'другое'
        }