from django.conf import settings

def title(request):
    return{
        "title": getattr(request, "title", "My Website Title"),
        "current_url": "{}:{}".format(request.resolver_match.app_name,
                                      request.resolver_match.url_name),
        "languages":settings.LANGUAGES
    }
