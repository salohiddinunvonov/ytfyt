from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Book)
admin.site.register(AudioBook)
admin.site.register(Language)
admin.site.register(Historyaudio)
admin.site.register(HistoryAudioBook)
admin.site.register(Rating)
admin.site.register(RatingAudioBook)
admin.site.register(RatingBook)