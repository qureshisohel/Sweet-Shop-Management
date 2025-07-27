from rest_framework import viewsets, generics, status, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Sweet
from .serializers import SweetSerializer, SweetSearchSerializer

class SweetViewSet(viewsets.ModelViewSet):
    queryset = Sweet.objects.all()
    serializer_class = SweetSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy', 'restock']:
            self.permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
        return super().get_permissions()
    
    @action(detail=True, methods=['post'])
    def purchase(self, request, pk=None):
        sweet = self.get_object()
        if sweet.quantity <= 0:
            return Response(
                {'error': 'This sweet is out of stock'},
                status=status.HTTP_400_BAD_REQUEST
            )
        sweet.quantity -= 1
        sweet.save()
        return Response({'message': 'Purchase successful', 'quantity': sweet.quantity})
    
    @action(detail=True, methods=['post'])
    def restock(self, request, pk=None):
        sweet = self.get_object()
        quantity = request.data.get('quantity', 1)
        try:
            quantity = int(quantity)
            if quantity <= 0:
                raise ValueError
        except (ValueError, TypeError):
            return Response(
                {'error': 'Quantity must be a positive integer'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        sweet.quantity += quantity
        sweet.save()
        return Response({'message': 'Restock successful', 'quantity': sweet.quantity})

class SweetSearchView(generics.ListAPIView):
    serializer_class = SweetSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        queryset = Sweet.objects.all()
        serializer = SweetSearchSerializer(data=self.request.query_params)
        serializer.is_valid(raise_exception=True)
        
        data = serializer.validated_data
        
        if name := data.get('name'):
            queryset = queryset.filter(name__icontains=name)
        if category := data.get('category'):
            queryset = queryset.filter(category=category)
        if min_price := data.get('min_price'):
            queryset = queryset.filter(price__gte=min_price)
        if max_price := data.get('max_price'):
            queryset = queryset.filter(price__lte=max_price)
        
        return queryset