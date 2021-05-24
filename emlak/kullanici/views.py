from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.contrib.auth.models import User
from iletisim.models import Iletisim

def kayit(request):
    if request.method == 'POST':
        # Formdan değer al
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # Şifreleri eşleştir
        if password == password2:
            # Kullanıcı adını kontrol et
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Bu kullanıcı adı önceden kullanılmış!')
                return redirect('kayit')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Bu mail adresi önceden kullanılmış!')
                    return redirect('kayit')
                else:
                    # Şartlar uygun kullanıcıyı kaydet
                    user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
                    # Kayittan sonra oturum aç
                    # auth.login(request, user)
                    # messages.success(request, 'Oturumunuz açılmıştır.')
                    # return redirect('index')
                    user.save()
                    messages.success(request, 'Kaydınız gerçekleştirilmiştir. Oturum açabilirsiniz.')
                    return redirect('oturum')
        else:
            messages.error(request, 'Şifreler uyuşmuyor!')
            return redirect('kayit')
    else:
        return render(request, 'kullanici/kayit.html')

def oturum(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Oturumunuz açılmıştır.')
            return redirect('panel')
        else:
            messages.error(request, 'Geçersiz kullanıcı')
            return redirect('oturum')
    else:
        return render(request, 'kullanici/oturum.html')

def panel(request):
    kullanıcı_iletisim = Iletisim.objects.order_by('-iletisim_tarihi').filter(kullanici_id=request.user.id)
    context = {
        'iletisimler': kullanıcı_iletisim
    }
    return render(request, 'kullanici/panel.html', context)

def ayrilma(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Oturumunuzdan ayrıldınız')
        return redirect('index')