import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .services import ask_ai


@csrf_exempt
def chat_api(request):

    if request.method != "POST":
        return JsonResponse(
            {
                "error": "POST request required"
            },
            status=405
        )

    body = json.loads(request.body)

    message = body.get("message", "")

    history = request.session.get("chat_history", [])

    answer, history = ask_ai(history, message)

    request.session["chat_history"] = history

    return JsonResponse(
        {
            "reply": answer
        }
    )
