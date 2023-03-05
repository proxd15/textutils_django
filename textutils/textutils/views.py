from django.http import HttpResponse # For sending response
from django.shortcuts import render

def index(request):
     
    return render(request,'index.html')   # teen parameters leta hai response , page name and parameters to be passed

def analysedtext(request):
    # text takn from the user in variable
    djtext = request.POST.get('text','default')

    # checkbox values checked here
    removepunc =  request.POST.get('removepunc','off')
    alluppercase =  request.POST.get('alluppercase','off')
    newlineremover =  request.POST.get('newlineremover','off')
    extraspaceremover =  request.POST.get('extraspaceremover','off')
    countchar =  request.POST.get('countchar','off')

    # for removing puntuations
    if removepunc == "on":
        analysed =""
        puntuations = '''.[](),?:;_-/''"\!&^%$#@*<>'''

        for char in djtext:             # Saare text ko iterate kar rahe hai
            if char not in puntuations:
                analysed = analysed + char
        params = {'purpose':'Removed Puntuations','analysedtext':analysed}
        djtext = analysed
         
    
    # to capatalise of letters
    if alluppercase == "on":
       upperanalysed = djtext.upper()
       params = {'purpose':'All to Upper','analysedtext':upperanalysed}
       djtext= upperanalysed
    
    # to remove the new line
    if newlineremover == "on":
        analysed =""
       
        for char in djtext:             # Saare text ko iterate kar rahe hai
            if char != "\n" and char != "\r":
                analysed = analysed + char

        params = {'purpose':'New line Removed','analysedtext':analysed}
        djtext = analysed
    
    # to remove a extraspace
    if extraspaceremover =="on":
       analysed =""
       
       for index,char in enumerate(djtext):             # Saare text ko iterate kar rahe hai
           if not(djtext[index]==" " and djtext[index+1]==" "):
               analysed = analysed + char
    
       params = {'purpose':'Space Removed','analysedtext':analysed}
       djtext = analysed
    
    # counting the character
    if countchar == "on":
        count = 0;
        for char in djtext:
            if char != " ":
               count = count + 1
        params = {'purpose':'Characters Counted','analysedtext':count}
        # return render(request,'analysed.html',params) 

    # throw a error if nothing is checked 
    
    return render(request,'analysed.html',params)

