from django.http import HttpResponse
from django.shortcuts import render
from polls.models import PollQuestion


# Create your views here.
def all_polls(request, id = -1):
    question = PollQuestion.objects.all()
    context = {
        'pollquestion': question
    }
    if request.method == "POST":
        poll = PollQuestion.objects.get(id=id)
        print(request.POST)
        option = request.POST['poll']
        if option == 'option1':
            poll.option_one_votes += 1
        elif option == 'option2':
            poll.option_two_votes += 1
        elif option == 'option3':
            poll.option_three_votes += 1
        elif option == 'option4':
            poll.option_three_votes += 1
        else:
            return HttpResponse(400, 'Invalid form option')
        poll.save()
        return render(request, 'availablepolls.html', context)
    else:
        return render(request, "availablepolls.html", context)
