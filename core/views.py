from django.shortcuts import render

from about.models import About
from business.models import Business
from gallery.models import Gallery
from contact.models import Contact
from cta_banner.models import CTABanner
from faq.models import FAQ
from hero.models import Hero
from reviews.models import Reviews
from social.models import Social
from standard.models import Standard
from videos.models import Videos
from vision_mission.models import VisionMissionCard


def home(request):
    videos_section = Videos.objects.prefetch_related('items').first()
    featured_video = None
    other_videos = []
    if videos_section:
        all_video_items = list(videos_section.items.all())
        featured_video = next((i for i in all_video_items if i.is_featured), all_video_items[0] if all_video_items else None)
        other_videos = [i for i in all_video_items if i != featured_video]

    gallery = Gallery.objects.prefetch_related('images').first()
    gallery_categories = []
    if gallery:
        for img in gallery.images.all():
            if img.category not in gallery_categories:
                gallery_categories.append(img.category)

    business = Business.objects.prefetch_related('items').first()
    business_names = []
    if business:
        for item in business.items.all():
            business_names.append(item.title.split('/')[0].strip())

    context = {
        'hero': Hero.objects.prefetch_related('slides').first(),
        'about': About.objects.prefetch_related('stats').first(),
        'vision_mission_cards': VisionMissionCard.objects.all(),
        'business': business,
        'business_names': business_names,
        'standard': Standard.objects.prefetch_related('items').first(),
        'videos_section': videos_section,
        'featured_video': featured_video,
        'other_videos': other_videos,
        'gallery': gallery,
        'gallery_categories': gallery_categories,
        'reviews_section': Reviews.objects.prefetch_related('items').first(),
        'social': Social.objects.prefetch_related('links', 'featured_cards').first(),
        'faq': FAQ.objects.prefetch_related('items').first(),
        'contact': Contact.objects.prefetch_related('methods').first(),
        'cta_banner': CTABanner.objects.first(),
    }
    return render(request, 'home.html', context)
