from django.shortcuts import render
from .models import *
# Create your views here.
def artistpost(request):
    return render(request, 'artistmodule/artistpost.html')

def add_artist_details(request):
    if request.method=='POST':
        song_name=request.POST.get('songtitle')
        artist_name=request.POST.get('Artistname')
        lyrics_by=request.POST.get('lyricsby')
        album=request.POST.get('album')
        genre_type=request.POST.get('Genretype')

        artist_details=ArtistDetails(
            song_name=song_name,
            artist_name=artist_name,
            lyrics_by=lyrics_by,
            album=album,
            genre_type=genre_type,
        )
        artist_details.save()
        return render(request,'artistmodule/datainserted.html')
    return render(request, 'artisthomepage.html')

def view_artist_details(request):
    artist_details_list= ArtistDetails.objects.all()
    return render(request,'artistmodule/view_artist_details.html',{'artist_details_list':artist_details_list})

