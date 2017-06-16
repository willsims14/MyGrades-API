from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
import json


@csrf_exempt
def register_user(request):
    # Load the JSON string of the request body into a dict
    req_body = json.loads(request.body.decode())

    # Create a new user by invoking the `create_user` helper method on Django's built-in User model
    new_user = User.objects.create_user(
                    username=req_body['username'],
                    password=req_body['password'])

    # Commit the user to the database by saving it
    new_user.save()
    token = Token.objects.create(user=new_user)
    data = json.dumps({'token':token.key, 'pk':new_user.id})

    return HttpResponse(data, content_type='application/json')

