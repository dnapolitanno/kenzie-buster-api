from rest_framework.views import APIView, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication


from users.models import User
from users.serializers import UserSerializer


class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)
