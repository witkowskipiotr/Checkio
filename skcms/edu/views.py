from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import redirect


def show_number(request, number):
    answer = """
    <html><body><p>
    The answer is %s!
    </p></body></html>
    """ % number
    return HttpResponse(answer)


def dispatch(request):
    if request.method == "GET":

        action = request.GET["action"]
        player_id = request.GET["player"]

        if action == "show-player":
            redirect("/show_player?id={}".format(player_id))

        elif action == "challenge":
            redirect("/challenge-player?id={}".format(player_id))
        else:
            raise Http404