from django.contrib import messages
from .models import Iletisim
from django.shortcuts import redirect, render
from django.core.mail import send_mail

def iletisim(request):
    if request.method == 'POST':
        ilan_id = request.POST['listing_id']
        ilan = request.POST['listing']
        isim = request.POST['name']
        email = request.POST['email']
        telefon = request.POST['phone']
        mesaj = request.POST['message']
        kullanici_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # Kullanıcının zaten bir talepte bulunup bulunmadığını kontrol etmek
        if request.user.is_authenticated:
            kullanici_id = request.user.id
            iletisim_yapmis = Iletisim.objects.all().filter(ilan_id=ilan_id, kullanici_id=kullanici_id)
            if iletisim_yapmis:
                messages.error(request, 'Bu ilan için zaten talepte bulundunuz!')
                return redirect('/listings/'+ilan_id)

        iletisim = Iletisim(ilan_id=ilan_id, ilan=ilan, isim=isim, email=email, telefon=telefon, mesaj=mesaj, kullanici_id=kullanici_id)
        iletisim.save()

        # Email gönderme
        send_mail(
            'Gayrimenkul Görüşme Talebi',
            'Görüşme: ' + ilan + 'hakkında görüşme talebi gerçekleşmiştir. Lütfen yönetim alanında oturum açarak talep hakkında bilgi alınız.',
            'bulent.yalazi@gmail.com',
            [realtor_email, 'bulent.yalazi@yahoo.com'],
            fail_silently=False
        )

        messages.success(request, 'Talebiniz iletilmiştir. Bir emlakçı sizinle iletişime geçecektir.')
        return redirect('/listings/'+ilan_id)