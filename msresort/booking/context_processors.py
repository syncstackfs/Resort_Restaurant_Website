from django.conf import settings


def site_media(request):
    return {
        'HERO_VIDEO_URL': settings.HERO_VIDEO_URL,
    }
