from django.shortcuts import render, redirect, get_object_or_404
from .forms import CourseInfo
from .models import Course
from django.views.generic import TemplateView, ListView
from django.db.models import Q

# Create your views here.


class Homepage(TemplateView):
    template_name = 'posts/homepage.html'


class SearchResults(ListView):
    model = Course
    template_name = 'posts/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Course.objects.filter(
            Q(title__icontains=query) | Q(SubjectField__icontains=query) | Q(teacher__icontains=query)
        )

        return object_list
        #return Course.objects.filter(title__icontains='abc')


def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'posts/course_detail.html', {'course': course})


def upload_course(request):
    if request.method == 'POST':
        form = CourseInfo(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.save()
            return redirect('course_detail', pk=course.pk)
    else:
        form = CourseInfo
    return render(request, 'posts/new_course.html', {'form': form})
