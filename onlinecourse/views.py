from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Enrollment, Question, Choice, Submission
from django.contrib.auth.decorators import login_required

@login_required
def submit(request, course_id):
    user = request.user
    course = get_object_or_404(Course, pk=course_id)
    enrollment = Enrollment.objects.get(user=user, course=course)

    submission = Submission.objects.create(enrollment=enrollment)

    selected_choice_ids = request.POST.getlist('choice')
    for choice_id in selected_choice_ids:
        choice = Choice.objects.get(pk=choice_id)
        submission.choices.add(choice)

    submission.save()

    return redirect('onlinecourse:show_exam_result', course_id=course.id, submission_id=submission.id)

@login_required
def show_exam_result(request, course_id, submission_id):
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)

    selected_choices = submission.choices.all()
    selected_choice_ids = selected_choices.values_list('id', flat=True)

    total_score = 0
    max_score = 0

    for question in course.question_set.all():
        max_score += question.grade_point
        if question.is_get_score(selected_choice_ids):
            total_score += question.grade_point

    context = {
        'course': course,
        'selected_choices': selected_choices,
        'total_score': total_score,
        'max_score': max_score,
    }

    return render(request, 'onlinecourse/exam_result_bootstrap.html', context)

from django.shortcuts import render, get_object_or_404
from .models import Course

def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    context = {
        'course': course,
    }
    return render(request, 'onlinecourse/course_details_bootstrap.html', context)
