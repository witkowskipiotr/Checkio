from datetime import datetime


def my_cp(request):
    ctx = {
        "now": datetime.now(),
        "version": "1.0",
        "user": request.user
    }
    return ctx
