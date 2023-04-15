from django.shortcuts import render

# Create your views here.
def Deep_learning(request):
    course = "Deep learning"
    course_fee = 5000
    course_duration = "3 months"
    course_hr = 54
    course_type="online"
    course_time="8 pm"
    course_details={'c':course,'cf':course_fee,'cd':course_duration,'ch':course_hr,'ct':course_type,'ctm':course_time,'hlf':2500}

    return render(request,'deep_learning/dl_page.html',course_details)
