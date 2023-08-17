from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView
from account.views import RegisterView, LoginView, UserListView, RegistrationPhoneView, VerifyEmail, UserViewSet, ResetPasswordConfirmView, ResetPasswordView
from hotel.views import BookingViewSet, HotelViewSet, CommentViewSet
from restourant.views import ProductViewSet, CategoryViewSet, LikeCreateView
from services_pr.views import ServicesViewSet, SelectViewSet, BookingUnderServicesViewSet

# router = routers.DefaultRouter()
# router.register('', UserViewSet)
# router.register('booking-services', BookingUnderServicesViewSet)
# router.register('bookings', BookingViewSet)
# router.register('category_restourant', CategoryViewSet)
# router.register('comments', CommentViewSet)
# router.register('hotels', HotelViewSet)
# router.register('likes', LikeCreateView)
# router.register('product', ProductViewSet)
# router.register('select_services', SelectViewSet)
# router.register('services', ServicesViewSet)

r = routers.DefaultRouter()
r.register('users', UserViewSet)
r.register('booking-services', BookingUnderServicesViewSet)
r.register('bookings', BookingViewSet)
r.register('category_restourant', CategoryViewSet)
r.register('comments', CommentViewSet)
r.register('hotels', HotelViewSet)
r.register('likes', LikeCreateView)
r.register('product', ProductViewSet)
r.register('select_services', SelectViewSet)
r.register('services', ServicesViewSet)



urlpatterns = [
    path('reset-password/', ResetPasswordView.as_view()),
    path('reset-password/confirm/', ResetPasswordConfirmView.as_view()),
    path('registration/', RegisterView.as_view()),
    path('register-phone/', RegistrationPhoneView.as_view()),
    path('login/', LoginView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('email-verify/', VerifyEmail.as_view(), name='email-verify'),
    path('bookings/', UserListView.as_view()),
    path('', include(r.urls)),
]






