# Nasıl Kurulur Ve Çalıştırılır?

**not: Başlamadan önce https://www.python.org/downloads/ sitesinden python 3 kurmanız gerekmektedir. Eğer GNU/Linux kullanıyorsanız uçbirimi açın ve aşağıdaki komutu yazınız;**

`$python --version`

**eğer python 3 ise kurmanıza gerek yoktur. Eğer python 3 değil ise Linux başlığına gidiniz.**

# Windows
- C:\Users\kullanıcıadı\Downloads klasörüne geliniz
- python-3.xx.x-amd64.exe programını kurunuz 

**not: kurulumu yaparken ADD PATH kutucuğunu işaretleyiniz**

![](https://miro.medium.com/max/720/0*7nOyowsPsGI19pZT.png)

- kurulum bittikten sonra ingilizce projem.py nin üzerine çift tıklayarak programı çalıştırabilirsiniz

# GNU/Linux 
- "Ingilice-Projem-main" zip dosyasını çıkarınız 

- uçbirimi açınız şu komutu yazınız;

 Debian tabanlı sistemler için : `$sudo apt update`
 /Pardus/Debian/Linux Mint/Ubuntu/Pop os vs.
 
 Arch tabanlı sistemler için: `$sudo pacman -Syu`
 /manjaro/arch linux/archman vs.
 
 Redhat tabanlı sistemler için `$sudo dnf upgrade`
 /Fedora/Centos vs.
 
- güncelleme bittikten sonra python 3 kurulumu için şu komutu yazınız;

 Debian tabanlılar:`$sudo apt-get install python3`
 
 Arch tabanlılar :`$sudo pacman -S python3`
 
 Redhat tabanlılar:`$sudo dnf install python3`
 
- python 3 kurulumunu bitirdikten isterseniz uçbirimi temizlemek için `$clear`komutunu kullanabilirsiniz

- şimdi çalıştırmak için uçbirime şu komutları yazınız;

`$cd İndirilenler`

`$cd Ingilice-Projem-main`

burada çalıştıracağınız programı yazınız `$python program.py` ve program çalıştı.
