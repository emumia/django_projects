from django.shortcuts import render

# Create your views here.
def sql_learning(request):
    return render(request,'sql_learning/sql_page.html',{'sql':'Sql learning'})

