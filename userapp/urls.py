from django.urls import path
from userapp import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns=[
    path("Home",views. hom, name="home"),
    path("Aboutus",views.abt, name="about"),
    path("Booklist",views.boklst, name="booklist"),
    path("Contactus",views.cnt, name="contact"),
    path("UploadBook",views.upb, name="uploadbooks"),
    path("EditPage/<int:Book_id>",views.Epage,name="EDIT"),
    path("Delete/<int:book_id>",views.delete_book,name="DELETE"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
