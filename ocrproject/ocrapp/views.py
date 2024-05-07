from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.http import JsonResponse
from .models import OcrModel
from PIL import Image
import os
from django.conf import settings
import pytesseract
from django.core.serializers import serialize
import json

# Create your views here.
def home_page(request):
    context = {
        "activeLink": "Home"
    }
    return render(request, "homepage.html", context)

def about_us(request):
    context = {
        "activeLink": "AboutUs",
        "array": [i for i in range(4)]
    }
    return render(request, "aboutus.html", context)

def contact_us(request):
    context = {
        "activeLink": "ContactUs"
    }
    return render(request, "contactus.html", context)

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("home_page")




def extract(request):
    try:
        if request.method == "POST":
            uploaded_image = request.FILES.get('uploaded_image')
            print("uploaded_image",uploaded_image.name)
            if uploaded_image.name.split(".")[1] in ["jpg", "png", "svg", "gif"]:

                new_data = OcrModel(image=uploaded_image)
                new_data.save()
                # Example usage
                # Save the uploaded image to the server
                upload_path = os.path.join(settings.BASE_DIR, 'uploads\\images\\', uploaded_image.name)
                with open(upload_path, 'wb') as destination:
                    for chunk in uploaded_image.chunks():
                        destination.write(chunk)
                
                # Extract text from the uploaded image
                # print("path of image - ",upload_path)
                image = Image.open(upload_path)
                text = pytesseract.image_to_string(image)
                # print("sdsdsdsdsdsds-",text)
                # Construct the image URL
                
                
                # Serialize all instances of OcrModel
                serialized_data = serialize('json', OcrModel.objects.filter(id=new_data.id))
                json_data = json.loads(serialized_data)[0]['fields']
                json_data['extracted_text'] = text
                image_url = settings.MEDIA_URL + 'images/' + json_data['image'].split("/")[1]
                json_data['image_url'] = image_url

                return JsonResponse({'message': 'success', 'status': 200, 
                                    'data': json_data}, 
                                    status=200)
            else:
                return JsonResponse({'message': 'wrong image extension', 'status': 400}, 
                                    status=400)

    except Exception as e:
        print(e)
        return JsonResponse({'message': 'exception occured!', 'status':400}, status=400)