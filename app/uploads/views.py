from django.shortcuts import render
from django.core.files.storage import FileSystemStorage


def image_upload(request):
    if request.method == "POST" and request.FILES["image_file"]:


        try:
            image_file = request.FILES["image_file"]
            print('+++++++++++', image_file)



            fs = FileSystemStorage()
            filename = fs.save(image_file.name, image_file)
            image_url = fs.url(filename)
            print(image_url)
        except Exception as e:
            print(e)



        return render(request, "upload.html", {"image_url": image_url})
    return render(request, "upload.html")
