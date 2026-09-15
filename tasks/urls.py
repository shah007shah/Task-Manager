from rest_framework.routers import DefaultRouter
from .views import LoginView, SignupView, TaskViewSet,UserViewSet
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()

router.register("tasks", TaskViewSet, basename="tasks")
router.register("users", UserViewSet, basename="users")


urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh"
    ),
]
urlpatterns += router.urls
# urlpatterns = router.urls