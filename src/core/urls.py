from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.views import View


class RedirectSocialGitHub(View):

    def get(self, request, *args, **kwargs):
        code, state = str(request.GET['code']), str(request.GET['state'])
        json_obj = {'code': code, 'state': state}
        print(json_obj)
        return JsonResponse(json_obj)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context


class RedirectSocialTwitter(View):

    def get(self, request, *args, **kwargs):
        code, state = str(request.GET['code']), str(request.GET['state'])
        json_obj = {'code': code, 'state': state}
        print(json_obj)
        return JsonResponse(json_obj)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/v1/', include('djoser.urls')),
    path('api/auth/v1/', include('djoser.urls.jwt')),
    path('api/auth/v1/', include('djoser.social.urls')),

    path('api/auth/v1/', include('social_django.urls', namespace='social')),

    path('complete/github/', RedirectSocialGitHub.as_view()),
    path('', RedirectSocialTwitter.as_view()),
]
