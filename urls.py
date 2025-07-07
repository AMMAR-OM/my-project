
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Task.views import ( CustomUserViewSet , CourseViewSet,ProfileViewSet,EnrollmentViewSet,AssignmentViewSet ,     GradeViewSet, PaymentViewSet, MessageViewSet,
    ComplaintViewSet, ReportViewSet, QuizViewSet
)
from django.contrib import admin

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'enrollments', EnrollmentViewSet)
router.register(r'grades', GradeViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'complaints', ComplaintViewSet)
router.register(r'reports', ReportViewSet)
router.register(r'quizes', QuizViewSet)
router.register(r'assignments', AssignmentViewSet)


urlpatterns = [
    path('', include(router.urls)),
        path('admin/', admin.site.urls),
        path('api/', include(router.urls)),

]
