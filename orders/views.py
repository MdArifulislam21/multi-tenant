from django.shortcuts import render
from .serializers import PollSerializer
from rest_framework import viewsets
from .models import Poll
from tenants.utils import tenant_from_request


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

    def get_queryset(self):
        tenant = tenant_from_request(self.request)
        return super().get_queryset().filter(tenant=tenant)