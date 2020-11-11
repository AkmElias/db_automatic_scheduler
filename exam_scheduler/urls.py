from django.urls import path
from . import views
from django.conf.urls import url, include
from django.shortcuts import redirect

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#url(r'^', include(router.urls)),
#url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#url(r'customview', CustomView.as_view()),
# ]
#urlpatterns += router.urls

urlpatterns = [

    # path('course_list/', views.course_list),
    # path('course_detail/<int:pk>/', views.course_detail),

]
