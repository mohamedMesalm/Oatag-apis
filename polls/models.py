from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  ,EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string

class favorite(models.Model):
    user_id = models.CharField(max_length=50 , blank=True, null=True)
    favoriteUser_id=models.CharField(max_length=50 , blank=True, null=True)

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    Image = models.ImageField(null=True, blank=True,
                              default='/placeholder.png')
    Name  = models.CharField(max_length=50 , blank=True, null=True)
    Job=models.CharField(max_length=50 , blank=True, null=True)
    Bio =models.CharField(max_length=50 , blank=True, null=True)
    Location =models.CharField(max_length=50 , blank=True, null=True)
    Isverified =models.BooleanField(default=False)
    isActive=models.BooleanField(default=True)
    isDirectOn=models.BooleanField(default=False)
    
# Create your models here.
    def __str__(self):
        return str(self.user)


       
@receiver(post_save , sender=User)
def create_user_profile(sender,instance,created , **kwargs):
    if created:
        Profile.objects.create(
            user = instance
        )

       


class Custom_button(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    title=models.CharField(max_length=50 , blank=True, null=True)
    icon=models.ImageField(null=True, blank=True,
                              default='/placeholder.png')
    color=models.CharField(max_length=50 , blank=True, null=True,default="#0000FF")
    isActive=models.BooleanField(default=False)
def __str__(self):
        return str(self.user)
@receiver(post_save , sender=User)
def create_user_custom_buttton(sender,instance,created , **kwargs):
    if created:
        Custom_button.objects.create(
            user = instance
        )
            

class Vcard(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    image=models.ImageField(null=True, blank=True,
                              default='/placeholder.png')
    first_name=models.CharField(max_length=50 , blank=True, null=True)
    last_name=models.CharField(max_length=50 , blank=True, null=True)

    email=models.CharField(max_length=50 , blank=True, null=True)
    phone=models.CharField(max_length=50 , blank=True, null=True)
    address=models.CharField(max_length=50 , blank=True, null=True)
    city=models.CharField(max_length=50 , blank=True, null=True)
    state=models.CharField(max_length=50 , blank=True, null=True)
    zip=models.CharField(max_length=50 , blank=True, null=True)
    country=models.CharField(max_length=50 , blank=True, null=True)
    company=models.CharField(max_length=50 , blank=True, null=True)
    title=models.CharField(max_length=50 , blank=True, null=True)
    website=models.CharField(max_length=50 , blank=True, null=True)
    notes=models.CharField(max_length=50 , blank=True, null=True)
    vcf_file=models.FileField(blank=True)
    isActive=models.BooleanField(default=False)

     

@receiver(post_save , sender=User)
def create_user_Vcard(sender,instance,created , **kwargs):
    if created:
        Vcard.objects.create(
            user = instance
        )   


                  

class config(models.Model):

    app_name=models.CharField(max_length=200, null=True, blank=True)
    App_icon=models.ImageField(null=True, blank=True,
                              default='/placeholder.png')
    app_email =models.EmailField(max_length=70,blank=True,unique=True)
    app_phone =models.CharField(max_length=200, null=True, blank=True)
    Maintaince_mode =models.BooleanField(default=True)
    App_account =models.CharField(max_length=200, null=True, blank=True)
    app_version =models.CharField(max_length=200, null=True, blank=True)
    Termes_conditions=models.TextField()
    About_us=models.TextField()
    privacy_policy=models.TextField()

class Playstore_config_class    (models.Model):
       status  =models.BooleanField(default=True)
       Link =models.CharField(max_length=200, null=True, blank=True)
       Playstore_config=models.ForeignKey(config, on_delete=models.SET_NULL, null=True,related_name="playstore")
class appstore_config_class    (models.Model):
       status  =models.BooleanField(default=True)
       Link =models.CharField(max_length=200, null=True, blank=True)
       appstore_config = models.ForeignKey(config, on_delete=models.SET_NULL, null=True,related_name="appstore")
             
SECTION_NUM = (
  ('1', 'Social media'),
  ('2','Contact info'),
  ('3','For Business'),
  ('4','Payments'),
  ('5','Content'),
  ('6','Music'),
  ('7','More'),

)

TYPE_OF_LINK=(
    ('1','username'),
    ('2','link'),
)

class platforms(models.Model):
    isActive=models.BooleanField(default=True)
    name =models.CharField(max_length=200, null=True, blank=True)
    domain=models.CharField(max_length=200, null=True, blank=True)
    dialog_title=models.CharField(max_length=200, null=True, blank=True)
    link_type=section=models.CharField(max_length=50,choices=TYPE_OF_LINK)
    error_message=models.CharField(max_length=200, null=True, blank=True)
    color1=models.CharField(max_length=50 , blank=True, null=True,default="#0000FF")
    color2=models.CharField(max_length=50 , blank=True, null=True,default="#0000FF")
    section=models.CharField(max_length=50,choices=SECTION_NUM)
    info=models.TextField()
    image=models.FileField(null=True, blank=True,
                              default='/placeholder.png')
    
    def __str__(self):
        return str(self.name)
        

                          

class data(models.Model):
    
    index_num=models.CharField(max_length=200, null=True, blank=True)
    user_id=models.CharField(max_length=200, null=True, blank=True)
    form_id=models.CharField(max_length=200, null=True, blank=True)
    name =models.CharField(max_length=200, null=True, blank=True)
    isActive=models.BooleanField(default=False)
    title=models.CharField(max_length=200, null=True, blank=True)
    domain=models.CharField(max_length=200, null=True, blank=True)
    username=models.CharField(max_length=200, null=True, blank=True)
    color1=models.CharField(max_length=50 , blank=True, null=True,default="#0000FF")
    color2=models.CharField(max_length=50 , blank=True, null=True,default="#0000FF")
    image=models.FileField(null=True, blank=True,
                              default='/placeholder.png')           

    def __str__(self):
        return str(self.user_id) + " " + str(self.name)

        




@receiver(reset_password_token_created)

def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    context = {
        'current_user': reset_password_token.user,
        'username': reset_password_token.user.username,
        'email': reset_password_token.user.email,
        'reset_password_url': "token={}".format( reset_password_token.key)
        }

    email_html_message = render_to_string('user_reset_password.html', context)
    # email_plaintext_message = render_to_string('user_reset_password.txt', context)    
    email_plaintext_message = "token={}".format( reset_password_token.key)

    # send_mail(
    #     # title:
    #     "Password Reset for {title}".format(title="Some website title"),
    #     # message:
    #     email_plaintext_message,
    #     # from:
    #     settings.EMAIL_HOST_USER,
    #     # to:
    #     [reset_password_token.user.email]
    # )        
    msg = EmailMultiAlternatives(
    # title:
    ("Password Reset for {title}".format(title="Some website title")),
    # message:
    email_plaintext_message,
    # from:
    settings.EMAIL_HOST_USER,
    # to:
    [reset_password_token.user.email]
    )
    msg.attach_alternative(email_html_message, "text/html")
    msg.send()




############################################ custom page #######################################################
class title(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    text=models.CharField(max_length=200, null=True, blank=True)
    fontSize=models.CharField(max_length=200, null=True, blank=True)
    fontName=models.CharField(max_length=200, null=True, blank=True)
    fontType=models.CharField(max_length=200, null=True, blank=True)
    fontColor=models.CharField(max_length=200, null=True, blank=True)


class header(models.Model):
    user = models.ForeignKey(User,unique=False , on_delete=models.CASCADE)
    text=models.TextField(blank=True)
    fontSize=models.CharField(max_length=200, null=True, blank=True)
    fontName=models.CharField(max_length=200, null=True, blank=True)
    fontType=models.CharField(max_length=200, null=True, blank=True)
    fontColor=models.CharField(max_length=200, null=True, blank=True)    


class product(models.Model):
    user=models.ForeignKey(User,unique=False , on_delete=models.CASCADE)
    name=models.CharField(max_length=200, null=True, blank=True)
    image1=models.ImageField(null=True, blank=True,
                              default='/placeholder.png')
    image2=models.ImageField(null=True, blank=True,
                              default='/placeholder.png')
    image3=models.ImageField(null=True, blank=True,
                              default='/placeholder.png')
    image4=models.ImageField(null=True, blank=True,
                              default='/placeholder.png')
    image5=models.ImageField(null=True, blank=True,
                              default='/placeholder.png')
    price=models.CharField(max_length=200, null=True, blank=True)
    description =models.TextField(blank=True)
    discount =models.CharField(max_length=200, null=True, blank=True)
    payment=models.CharField(max_length=200, null=True, blank=True)
    connection=models.CharField(max_length=200, null=True, blank=True)
    report=models.CharField(max_length=200, null=True, blank=True)
    info=models.CharField(max_length=200, null=True, blank=True)



class html(models.Model) :
    user=models.ForeignKey(User,unique=False , on_delete=models.CASCADE)
    body =   models.TextField(blank=True)
    info=models.CharField(max_length=200, null=True, blank=True)


class contact_form    (models.Model) :
    user=models.ForeignKey(User,unique=False , on_delete=models.CASCADE)
    subject=models.CharField(max_length=200, null=True, blank=True)
    content=models.TextField(blank=True)
    From=models.CharField(max_length=200, null=True, blank=True)
    to=models.CharField(max_length=200, null=True, blank=True)



class RSS_Feed(models.Model) :
    user=models.ForeignKey(User,unique=False , on_delete=models.CASCADE)
    rss_feed=models.CharField(max_length=200, null=True, blank=True)



class Link(models.Model )  :
    user=models.ForeignKey(User,unique=False , on_delete=models.CASCADE)
    image=models.ImageField(null=True, blank=True,
                              default='/placeholder.png')
    link=models.CharField(max_length=200, null=True, blank=True)
    color=models.CharField(max_length=200, null=True, blank=True)



class IMAGE(models.Model):
    user=models.ForeignKey(User,unique=False , on_delete=models.CASCADE)
    image=models.ImageField(null=True, blank=True,
                              default='/placeholder.png')

