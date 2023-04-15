from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def machine_learning(request):
    ml_course_list={'m_courses':['Bashar vai','Md shakil vai','shohan vai','Muhammad vai']}
    return render(request,'machine_learning/ml_page.html',ml_course_list)
