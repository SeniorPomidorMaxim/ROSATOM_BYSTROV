from django.shortcuts import render,redirect
from django.views import View
from django.http import JsonResponse
from django.views.generic import TemplateView

from myapp.forms import QuestionForm, default_company_name_and_id
from myapp.models import Division, Question, Company
        


class AddQuestions(View):
    form_class = QuestionForm

    def get(self, request):
        return render(
            request, 
            'form_post.html', {
                'form': self.form_class()
            }
        )

    def post(self, request):
        form = self.form_class(request.POST)    
        if form.is_valid():
            form.save()
            return redirect('home')
        
        return render(request, 'form_post.html', {'form': form})


class GetCompanies(View):
    def get(self, request):
        division = Division.objects.get(id=request.GET.get('division_id')) 
        companies = division.companies.all()
        data = [
            {'id': company.id,
            'name': company.name}
            for company in companies
            ]+[
                {'id': default_company_name_and_id['default_choice_id'],
                'name': default_company_name_and_id['default_choice_name']}
                ]
        
        return JsonResponse(data, safe=False)


class IndexView(TemplateView):
    template_name = 'index.html'



def list(request):
    context = {
        'questions': Question.objects.all(),
        'companys': Company.objects.all()
    }
    return render(request, 'form_get.html',context)


