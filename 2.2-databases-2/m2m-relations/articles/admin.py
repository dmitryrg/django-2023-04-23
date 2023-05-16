# from django.contrib import admin
#
# from .models import Article, Scope
#
#
# class ScopeInline(admin.TabularInline):
#     model = Scope
#     extra = 0
#
#
# @admin.register(Article)
# class ArticleAdmin(admin.ModelAdmin):
#     inlines = [ScopeInline]

from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        is_main_true_counter = 0 if len(self.forms) else None
        for form in self.forms:
            if form.cleaned_data['is_main']:
                is_main_true_counter += 1
                if is_main_true_counter > 1:
                    raise ValidationError('Главный тэг может быть только один')
        if is_main_true_counter == 0:
            raise ValidationError('Главный тэг должен быть выбран')
        return super().clean()  # вызываем базовый код переопределяемого метода


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]
