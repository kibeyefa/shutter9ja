from django.shortcuts import get_object_or_404, render
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    ListCreateAPIView,
    UpdateAPIView,
)
from rest_framework.response import Response
from .serializers import (
    CompetitionListSerializer,
    EntryListSerializer,
    EntryVoteSerializer,
    VoteSubmissionSerializer,
)
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from django.core.mail import send_mail
from .serializers import ContactSerializer


# Create your views here.
class TwentyPerPagePagination(PageNumberPagination):
    page_size = 16  # 20 items per page


class CompetitionListView(ListAPIView):
    queryset = Competition.objects.all().order_by("-created")
    serializer_class = CompetitionListSerializer


class SingleCompetitionView(RetrieveAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionListSerializer
    lookup_field = "id"
    lookup_url_kwarg = "id"


class GetCurrentCompetitionView(ListAPIView):
    queryset = Competition.objects.filter(concluded=False).order_by("-created")
    serializer_class = CompetitionListSerializer


class EntryListView(ListCreateAPIView):
    parser_classes = [MultiPartParser, FormParser]
    queryset = Entry.objects.all()
    serializer_class = EntryListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["competition"]
    pagination_class = TwentyPerPagePagination

    def create(self, request, *args, **kwargs):
        images = request.FILES.getlist("images")

        if not images:
            return Response(
                {"images": "This field is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if len(images) > 3:
            return Response(
                {"images": "You can upload a maximum of 3 images."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        entry = serializer.save()

        for img in images:
            EntryImage.objects.create(entry=entry, image=img)

        return Response(self.get_serializer(entry).data, status=status.HTTP_201_CREATED)


class SingleEntryView(RetrieveAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntryListSerializer
    lookup_field = "id"
    lookup_url_kwarg = "id"


class EntryVoteView(APIView):
    def post(self, request, id):
        entry = get_object_or_404(Entry, id=id)
        serializer = VoteSubmissionSerializer(data=request.data)

        if serializer.is_valid():
            vote_count = serializer.validated_data["vote_count"]
            entry.vote_count += vote_count
            entry.save()

            updated_data = EntryListSerializer(entry)
            return Response(updated_data.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContactAPIView(APIView):
    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data

            # Optional: send confirmation or internal email
            send_mail(
                subject=f"Shutter9ja Message: {data.get('subject') or 'No Subject'}",
                message=(
                    f"Message from {data['fullName']} <{data['email']}>\n\n"
                    f"{data['message']}"
                ),
                from_email="noreply@shutter9ja.org",
                recipient_list=[
                    "support@shutter9ja.org",
                    "admin@shutter9ja.org",
                    "kibeyefa@gmail.com",
                    "patrickmagnum69@gmail.com"
                ],
                fail_silently=True,
            )

            return Response({"detail": "Message received."}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
