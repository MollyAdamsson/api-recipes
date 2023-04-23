from django.urls import path
from profilereviews import views

urlpatterns = [
    path('profilereviews/', views.ProfileReviewList.as_view()),
    path('profilereviews/<int:pk>/', views.ProfileReviewDetail.as_view())
]
