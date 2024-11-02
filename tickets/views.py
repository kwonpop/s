from django.shortcuts import render, redirect
from django.http import JsonResponse
import requests
import os

def index(request):
    return render(request, 'index.html')

def download_image(request):
    if request.method == 'POST':
        image_url = request.POST.get('image_url')
        image_name = os.path.join('media', 'flight_ticket.jpg')

        try:
            response = requests.get(image_url)
            response.raise_for_status()  # 오류가 발생하면 예외를 발생시킴
            with open(image_name, 'wb') as f:
                f.write(response.content)
            return redirect('get_image')  # 다운로드 후 이미지 보기 페이지로 리다이렉트
        except Exception as e:
            return JsonResponse({'error': f'이미지 다운로드에 실패했습니다: {str(e)}'}, status=500)

def get_image(request):
    image_path = os.path.join('media', 'flight_ticket.jpg')
    if os.path.exists(image_path):
        return render(request, 'get_image.html', {'image_url': image_path})
    else:
        return JsonResponse({'error': '이미지가 존재하지 않습니다.'}, status=404)