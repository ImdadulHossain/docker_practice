from django.shortcuts import render

def voice_test_view(request):
    return render(request, 'voicetest/index.html')
