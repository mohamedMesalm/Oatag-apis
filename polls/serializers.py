from rest_framework import serializers,viewsets
from .models import *
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.password_validation import validate_password

class appstore_configSerializer(serializers.ModelSerializer):
    class Meta:
        model = appstore_config_class
        fields = ('status','Link')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('Image','Name')        
class Playstore_configSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playstore_config_class
        fields = ('status','Link')       
class favoriteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = favorite
        fields = ('favoriteUser_id',)
     

class ConfigSerializer(serializers.ModelSerializer):

    playstore = Playstore_configSerializer(many=True)
    appstore=appstore_configSerializer(many=True)
    class Meta:
        model = config
        fields = ('app_name','App_icon','app_email','app_phone','Maintaince_mode','App_account','app_version','Termes_conditions','About_us', 'privacy_policy','playstore','appstore')
    
      

class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
   
    isAdmin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'name', 'isAdmin']

    def get__id(self, obj):
        return obj.id

    def get_isAdmin(self, obj):
        return obj.is_staff

    def get_name(self, obj):
        name = obj.first_name

        return name



class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'name', 'isAdmin', 'token']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)
class DataSerializer(serializers.ModelSerializer):
    color_list=serializers.SerializerMethodField()
    class Meta:
        model = data
        fields = ['form_id', 'name', 'isActive', 'title', 'domain', 'username','color_list','image']

    def get_color_list(self, obj):
        a=[]
        if obj.color1 != "":
            a.append(obj.color1)

        if obj.color2 != "":
            a.append(obj.color2)    

        return a    

class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = platforms
        fields='__all__'

class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"message": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"message": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):

        instance.set_password(validated_data['password'])
        instance.save()

        return instance








class pic (object)        :
    def __init__(self,image):
        self.image=image


class picSerializer(serializers.Serializer)        :

    image=serializers.ImageField()


class fi (object)        :
    def __init__(self,file):
        self.file=file
class fileSerializer(serializers.Serializer)        :

    file=serializers.FileField()

################################### custom page ###################################################

class titleSerializer(serializers.ModelSerializer):
    class Meta:
        model = title
        fields='__all__'

class headerSerializer(serializers.ModelSerializer):
    class Meta:
        model = header
        fields='__all__'  


class htmlSerializer(serializers.ModelSerializer):
    class Meta:
        model = html
        fields='__all__'  


class contact_formSerializer(serializers.ModelSerializer):
    class Meta:
        model = contact_form
        fields='__all__'


class RSS_FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = RSS_Feed 
        fields='__all__'


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link 
        fields='__all__'       

       

class IMAGESerializer(serializers.ModelSerializer):
    class Meta:
        model = IMAGE 
        fields='__all__'       

class productSerializer(serializers.ModelSerializer):
    images=serializers.SerializerMethodField()
    class Meta:
        model = product 
        fields=('id','user','name','images','price','description','discount','payment','connection','report','info')
      
        

    def get_images(self, obj):
        a=[]
        if obj.image1 != "":
            file=obj.image1
            new=pic(file)
            serializer=picSerializer(new)
            img=serializer.data
            JsonObject={}
            JsonObject['image1']=img['image']
            a.append(JsonObject)
       
        if obj.image2 != "":
            file=obj.image2
            print(pic(file))
            new=pic(file)
            serializer=picSerializer(new)
            img=serializer.data
            JsonObject={}
            JsonObject['image2']=img['image']
            a.append(JsonObject)
       

        if obj.image3 != "":
            file=obj.image3
            new=pic(file)
            serializer=picSerializer(new)
            img=serializer.data
            JsonObject={}
            JsonObject['image3']=img['image']
            a.append(JsonObject)
       

        if obj.image4 != "":
            file=obj.image4
            new=pic(file)
            serializer=picSerializer(new)
            img=serializer.data
            JsonObject={}
            JsonObject['image4']=img['image']
            a.append(JsonObject)
       

        if obj.image5 !="":
            file=obj.image5
            new=pic(file)
            serializer=picSerializer(new)
            img=serializer.data
            JsonObject={}
            JsonObject['image5']=img['image']
            a.append(JsonObject)

        return a
        

               


      