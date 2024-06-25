from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import AudioFile
from django.core.files import File

def schwa_home(request):
    if request.user.is_authenticated:
        sounds = AudioFile.objects.filter(user=request.user)
        context = {'username': request.user.username, 'sounds': sounds}
        return render(request, 'schwa_home.html', context=context)
    else:

        return redirect('/')

def save_recording(request):

    file_name = request.POST['file_name']
    audio = request.FILES['audioRecording']
    AudioFile.objects.create(audio_file=audio, file_name=file_name, user=request.user)
    # audio_file = AudioFile.objects.create(audio_file=audio, file_name=file_name, user=request.user)

    # path = audio_file.audio_file.path
    # flac_path = f'{path}.flac'
    # convert_cmd = f'ffmpeg -i {path} {wav_path}'
    #
    # subprocess.call(convert_cmd, shell=True)
    # f = open(flac_path, 'rb')
    # django_file = File(f)
    # audio_file.audio_file = django_file
    # audio_file.save()
    # f.close()
    # django_file.close()
    # os.remove(flac_path)

    return HttpResponse()
