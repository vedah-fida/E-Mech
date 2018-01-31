from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Mechanics
# Create your views here.

@login_required(login_url='login:login_user')
def all_mechanics(request):
    all_mechanics = "<h3>The listing for all the mechanics</h3>"
    return HttpResponse(all_mechanics)


def just_test(request, question_id):
    question = get_object_or_404(Mechanics, question_id)
    try:
        selected_question = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, "template_name", {"question": question,
                                                 "error_message": "You did not select a choice"})
    else:
        selected_question.votes += 1
        selected_question.save()
        return HttpResponseRedirect(reverse("app_name:url_name"), args="question_id")
