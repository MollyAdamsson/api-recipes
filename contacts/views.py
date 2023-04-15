from rest_framework import generics, permissions
from blog_api.permissions import IsOwnerOrReadOnly
from .models import Contact
from .serializers import ContactSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


class ContactList(generics.ListCreateAPIView):
    """
    View for the contact model
    """
    serializer_class = ContactSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Contact.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    @api_view(['POST'])
    def submit_contact(request):
        if request.method == 'POST':
            serializer = ContactSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user) 
            return Response({'message': 'Contact form submitted successfully.'},
                            status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a contact, or update or delete it by id.
    """
    permission_classes = [permissions.IsAdminUser]
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()