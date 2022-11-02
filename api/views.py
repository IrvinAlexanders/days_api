from rest_framework.views import APIView
from rest_framework.response import Response


# Star of class Holidays
class Holidays(APIView):

    def get(self, request):
        return Response('HELLO WORLD')

# End of class Holidays
