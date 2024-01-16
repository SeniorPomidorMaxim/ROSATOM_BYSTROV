from django.contrib import admin

from .models import Company, Question, Division


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('company',  'email', 'content','time_create')
    list_filter = ('company', )
    search_fields = ('company',)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name','division', )
    list_filter = ('division', )
    search_fields = ('name',)


@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ('name', )
