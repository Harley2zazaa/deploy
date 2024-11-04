from django.shortcuts import render  # สำคัญ ไอนี้ไว้ใช้เรียกไฟล์
from django.http import HttpResponse  # สำคัญ อันนี้ตอบสนอง
from django.conf import settings# นำเข้า settings สำหรับดึง API key
import requests  # ใช้สำหรับเรียก API ภายนอก

# Create your views here.
# ฟังก์ชัน ให้มันทำ
def index(request):
    return render(request,"index.html") #ใส่ tag html ได้

def about(request):
    return render(request,"about.html")

# ฟังก์ชันค้นหา recipes จาก API
def search_recipes(request):
    query = request.GET.get('query')  # ดึงคีย์เวิร์ดที่ผู้ใช้ค้นหาจาก query parameter
    api_key = settings.SPOONACULAR_API_KEY  # ดึง API key จาก settings

    # เรียก API ของ Spoonacular ด้วย query
    url = f"https://api.spoonacular.com/recipes/complexSearch?query={query}&number=6&apiKey={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        recipes = response.json().get('results', [])  # ดึงผลลัพธ์การค้นหาจาก response
    else:
        recipes = []  # กรณีเกิดข้อผิดพลาด

    # ส่งผลลัพธ์ไปที่ search_results.html
    return render(request, "search_results.html", {'recipes': recipes})
