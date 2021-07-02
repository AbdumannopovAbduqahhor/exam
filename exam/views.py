from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView

from exam.forms import UserModelForm
from exam.models import UserModel


# def index(request):  # ListView
#     q = request.GET.get('q')
#     if q:
#         data = UserModel.objects.filter(brand_name__icontains=q)
#     else:
#         data = UserModel.objects.all()
#     context = {
#         'data': data
#     }
#
#     return render(request, 'index.html', context)
class ExamDetailView(LoginRequiredMixin, DetailView):
    template_name = 'index.html'
    model = UserModel


#
# def create_view(request):
#     if request.method == 'POST':
#         form = UserModelForm(request.POST, files=request.FILES)
#
#         if form.is_valid():
#             form.save()
#
#         return redirect('/exam/')
#     else:
#         form = UserModelForm()
#
#         context = {
#             'form': form
#         }
#         return render(request, 'create.html', context)


class ExamCreateView(LoginRequiredMixin, CreateView):
    template_name = 'create.html'
    form_class = UserModelForm
    success_url = '/exam/'
