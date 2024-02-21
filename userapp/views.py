from django.shortcuts import render,redirect
from .forms import upbook
from .models import book
from django.http import HttpResponse
# Create your views here.
def hom(request):
    return render(request,"Home.html")
def abt(request):
    return render(request,"About.html")
def boklst(request):
    shelf=book.objects.all()
    return render(request,"BookList.html",{"data":shelf})
def upb(request):
    uploads=upbook()
    if request.method=="POST":
        uploads=upbook(request.POST,request.FILES)
        if uploads.is_valid():
          uploads.save()
          return redirect('booklist')
        else:
          return HttpResponse("""something went wrong.please reload webpage by clicking <a href="{{url:'uploadbooks'}}"> reload</a>""") 
    return render(request,"UploadBooks.html",{'upbk':upload})
def cnt(request):
    return render(request,"Contact.html")
def Epage(request,Book_id):
    Book_id=int(Book_id)
    try:
        Book_Shelf=book.objects.get(id=Book_id)
    except book.DoesNotExist:
        return redirect('booklist')
    BK_form=upbook(request.POST or None,instance=Book_Shelf)
    if BK_form.is_valid():
       BK_form.save()
       return redirect('booklist')
    return render(request,"UploadBooks.html",{'upbk':BK_form})
def delete_book(request,book_id):
    book_id=int(book_id)
    try:
        book_shelf=book.objects.get(id=book_id)
    except book.DoesNotExist:
        return redirect('booklist')
    book_shelf.delete()
    return redirect('booklist')