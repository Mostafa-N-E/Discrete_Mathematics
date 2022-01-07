from django.http import HttpResponse
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins

from .main import Permutation, catalan
from .serializers import ContactUsSerializer


class CalculateApi(APIView):
    def post(self, request, *args, **kwargs):
        data = self.change_maping(request.data)
        print("-----------------------------------------------------")
        print(data)
        question = Permutation(**data)
        return Response(
            {'message':str(question.get_resulte())},
            status=status.HTTP_200_OK,
        )

    def change_maping(self, data):
        return {
            'boxes':int(data['k']),
            'bullets':int(data['n']),
            'being_different_bullets':eval(data['o1'].capitalize()),
            'being_different_boxes':eval(data['o2'].capitalize()),
            'being_empty_boxes':eval(data['o3'].capitalize())
        }


class CatalanApi(APIView):
    def post(self, request, *args, **kwargs):
        res = catalan(int(request.data['n']))
        return Response(
            {'message':str(res)},
            status=status.HTTP_200_OK,
        )




class Contact_us(mixins.CreateModelMixin, GenericAPIView):
    """
        Record messages sent by users through the contact form
    """
    serializer_class = ContactUsSerializer

    def post(self, request, *args, **kwargs):
        self.create(request, *args, **kwargs)
        return Response({"message": "Your message has been sent. Thank you", "title": "Success", "button": "Aww yiss"})