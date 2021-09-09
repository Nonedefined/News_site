from rest_framework.generics import RetrieveAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response


from .serializers import MessageSerializer
from ..models import *


@api_view()
def list_messages(request, pk):
    """ Get all messages with pagination by 10 messages per request"""
    number = 10*pk
    messages = Message.objects.all()[number: number+10]

    result = []
    for mes in messages:
        result.append({"id": mes.id, "text": mes.text, "email": mes.email})

    return Response(result)


class MessageAPIView(CreateAPIView):
    """Create a new message"""
    serializer_class = MessageSerializer


class MessageDetailAPIView(RetrieveAPIView):
    """Get single message by id"""
    serializer_class = MessageSerializer
    queryset = Message.objects.all()






