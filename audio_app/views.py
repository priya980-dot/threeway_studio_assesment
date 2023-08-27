from django.shortcuts import render, redirect
from .forms import AudioUploadForm
from .models import UploadedAudio
from mutagen.mp3 import MP3
def upload_audio(request):
    # If the request method is POST, process the form data
    if request.method == 'POST':
        form = AudioUploadForm(request.POST, request.FILES)
        # Check if the form data is valid
        if form.is_valid():
            # Save the form data to the database
            audio = form.save(commit=False)
            audio.size = f"{audio.audio.size / 1024:.2f} KB"
            audio.extension = audio.audio.name.split('.')[-1]
            audio.save()
            return redirect('upload_audio')  # Redirect to the same page after successful upload
    else:
        form = AudioUploadForm() # Create a form instance

    
    audios = UploadedAudio.objects.all() # Get all uploaded audio files
    total_duration = sum(MP3(audio.audio.path).info.length for audio in audios) # Calculate total duration of uploaded audio files
    duration_exceeds_limit = total_duration.total_seconds() > 600  # 10 minutes in seconds
    return render(request, 'upload_audio.html', {'form': form, 'audios': audios})

