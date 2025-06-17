from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializer import ContactMessageSerializer,NewsletterSubscriberSerializer
from rest_framework import status


# Create your views here.



@api_view(['POST'])
@permission_classes([])
def contact_message_create(request):
    serializer = ContactMessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Your message has been sent successfully.'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([])
def subscribe_newsletter(request):
    serializer = NewsletterSubscriberSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Successfully subscribed to newsletter.'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)