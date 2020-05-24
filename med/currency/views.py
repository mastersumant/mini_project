# howdy/views.py
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from currency.test import main
import os
from django.template import RequestContext
@csrf_exempt
def check_currency(request):
     if request.method != 'POST': 
        return HttpResponse(form_page)
     print("5")
     with open(os.path.join("currency\\test_images\\1.jpg"), 'wb+') as destination:
        for chunk in request.FILES['image'].chunks():
            destination.write(chunk)
     file_n = '100.mp3'
     print(file_n)
     return HttpResponse(display_page.format(file_n))
 
    
# Create your views here.
form_page="""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Currency Detection</title>
    <style>
        @charset "UTF-8";



/*******************choose***********************/
/* Hide original appearance */
.choose-file {
    height: 0.1px;
    opacity: 0;
    overflow: hidden;
    z-index: -1;
    position: absolute;
    width: 0.1px;
}

/* Style both input field and label */
.choose-file+.upload-file {
    background-color: #e2f8f9;
    box-sizing: border-box;
    color: #5A5541;
    display: block;
    font-family: Sans-serif;
    font-size: 16px;
    font-weight: 400;
    padding: 8.2rem 1rem 2rem;
    text-align: center;
    text-transform: uppercase;
    border: 2px dashed #27BEC5;
    border-radius: 16px;
    text-transform: initial;
    cursor: pointer;
}

.choose-file:focus+.upload-file,
.choose-file+.upload-file:hover {
    background-color: #d2f3f5;
}


label.upload-file::before {
    content: "Choose a image file or capture it using camera";
    text-decoration: underline;
    color: #27BEC5;
    font-size: 16px;
}

/* This appears after a file is chosen. */
.choose-file:valid+.upload-file::before {
    content: attr(data-text);
    color: #5A5541;
    font-size: 16px;
}

.upload {
    position: relative;
    min-height: 100%;
    min-width: 100%;
    
    
}

.upload img {
    width: 55px;
    position: relative;
    top: 130px;
    pointer-events: none;
    align-content: center;
}

.btn.btn-up {
    color: #fff;
    background-color: #27BEC5;
    border-color: #27BEC5;
    min-width: 72px;
    font-size: 16px;
    margin: 20px auto 0px;
    display: table;
    text-transform: initial;
}
    </style>
</head>
<body>
    <center><h2>Bring your currency in front of camera</h2>
    <br>
    <form  action="http://192.168.43.147:8000/currency/" id="mForm"  method="post"  enctype="multipart/form-data">
    
    <div class="upload" >
        <img src="https://www.thinkpower.com.tw/demo/tsmp-art/images/icon_cloud@2x.png" alt="">
    
    <input class="choose-file" type="file" id="choose-file"  name="image" required>
    
    <label for="choose-file" class="upload-file" data-text="name" >
        <div class="btn btn-up" type="button"></div>
    </label>
</div>
<center><br><input class="btn btn-up" type="submit" value="submit"></center>
</form>

    <script type="text/javascript">
        window.onload=function(){
            var auto = setTimeout(function(){ autoRefresh(); }, 100);
    
            function submitform(){
              document.forms["myForm"].submit();
            }
    
            function autoRefresh(){
               clearTimeout(auto);
               auto = setTimeout(function(){ submitform(); autoRefresh(); }, 10000);
            }
        }
    </script>
</body>
</html>"""

display_page="""
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Currency Detection</title>
</head>
<body>
    <br>
    <br>
        <h2>Bring your tablet in front of camera</h2>
    <br>

    <form  action="http://192.168.43.147:8000/currency/"  method="post"  enctype="multipart/form-data">
    
    <input type="file"  name="image" required>
    <input type="submit" value="submit">
    </form>
    <br>
     <audio controls autoplay>
    <source src="http://www.sitsark.in/proj/{}" type="audio/mp3">
    </audio>
</body>
</html>"""