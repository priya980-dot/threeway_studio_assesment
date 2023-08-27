# threeway_studio_assesment
# Assessment

# Audio Uploader Django App

Welcome to the Audio Uploader Django App! This web application allows users to upload audio files, view them in a table, and calculate the total duration of uploaded audio files. Additionally, it checks if the total duration exceeds a specified limit.

## Approach 

* Language: Python
*  Framework: Django

* Database: SQLite (for simplicity)

# python manage.py migrate
* python manage.py migrate

# Run the development server:
* python manage.py runserver

# run and browse to
* http://127.0.0.1:8000/audio/upload/


# Features
 Users can upload audio files along with details such as user, name, and audio file.
 Uploaded audio files are stored in the database and displayed in a table.
 Total duration of uploaded audio files is calculated and displayed on the page.
 If the total duration of uploaded audio files exceeds 10 minutes, a warning is shown.
# How it works:

* The webpage is built using django framework.
# main code

*def upload_audio(request):
*    # If the request method is POST, process the form data
*    if request.method == 'POST':
*        form = AudioUploadForm(request.POST, request.FILES)
*        # Check if the form data is valid
*       if form.is_valid():
*           # Save the form data to the database
*            audio = form.save(commit=False)
*           audio.size = f"{audio.audio.size / 1024:.2f} KB"
*           audio.extension = audio.audio.name.split('.')[-1]
*           audio.save()
*           return redirect('upload_audio')  # Redirect to the same page after successful upload
*   else:
*       form = AudioUploadForm() # Create a form instance    
*   audios = UploadedAudio.objects.all() # Get all uploaded audio files
*    total_duration = sum(MP3(audio.audio.path).info.length for audio in audios) # Calculate total duration of uploaded audio files
*    duration_exceeds_limit = total_duration.total_seconds() > 600  # 10 minutes in seconds
*   return render(request, 'upload_audio.html', {'form': form, 'audios': audios})

## 
### I have add a following functionality ###
* link--http://127.0.0.1:8000/audio/upload/
* The form will take  detail of audio file and will give option to upload file  
* It will store in database and show on page

### **Assumption** ###
* There is only one user

