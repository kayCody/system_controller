# imports from the Django Forms module
from django import forms
from django.contrib.auth.forms import UserCreationForm

# imports from the various models ie(StaffApp, MembersApp, Admin, Users)
from django.contrib.auth.models import User
from.models import Member, Region, District, Society, Zone


# // class creatio for the form models of the various models //
# user form class model //
class UserCreateForm(UserCreationForm):
    #email = forms.EmailField()
    #first_name = forms.CharField(max_length=120,)
    #last_name = forms.CharField(max_length=120,)
    #user_permissions = forms.MultiValueField()
    #staff_id = forms.CharField()
    is_active = forms.BooleanField()
    is_staff = forms.BooleanField()
    #is_superuser = forms.BooleanField()
    class Meta:
        model = User
        fields = ['first_name','last_name','password1', 'password2','is_active','is_staff']
        labels = {
            'first_name':'Full Given names',
            'last_name':'surname name',
        }


# // Member Forms //
class MemberCreationForm(forms.ModelForm):
    class Meta:
        model = Member
        fields=['region','society','district','title','image','family_name','given_name','middle_name','sex','day','month','year','marital_status','family_size','address','address_city','address_region','level_of_education','type_of_id','id_card_no','hometown','hometown_region','personal_phone','alt_personal_phone','next_of_kin','relationship_with_kin','kins_address','kins_contact','number_of_farms','farmowner','crop','farmsize','farm_location','farm_image','location_lat','location_long','years_on_farm','farmowner2','crop2','farmsize2','farm_location2','farm_image2','location_lat2','location_long2','years_on_farm2','farmowner3','crop3','farmsize3','farm_location3','farm_image3','location_lat3','location_long3','years_on_farm3','farmowner4','crop4','farmsize4','farm_location4','farm_image4','location_lat4','location_long4','years_on_farm4','farmowner5','crop5','farmsize5','farm_location5','farm_image5','location_lat5','location_long5','years_on_farm5','overall_farming_years','business_before_farming','business_aside_farming','averageyield','previousyield','farmbenefit','buyerofproduce','numberoftimes','buyerbenefits','useoffund','any_bank_transacting_with','transactingbank','duration','part_of_any_farmers_association','farmers_association','declaration']
        labels = {
            'region':'',
            'society':'',
            'district':'',
            'title':'',
            'image':'',
            'family_name':'',
            'given_name':'',
            'middle_name':'',
            'sex':'',
            'day':'',
            'month':'',
            'year':'',
            'marital_status':'',
            'family_size':'',
            'address':'',
            'address_city':'',
            'address_region':'',
            'level_of_education':'',
            'type_of_id':'',
            'id_card_no':'',
            'hometown':'',
            'hometown_region':'',
            'personal_phone':'',
            'alt_personal_phone':'',
            'next_of_kin':'',
            'relationship_with_kin':'',
            'kins_address':'',
            'kins_contact':'',
            'number_of_farms':'',
            'farmowner':'',
            'crop':'',
            'farmsize':'',
            'farm_location':'',
            'farm_image':'',
            'location_lat':'',
            'location_long':'',
            'years_on_farm':'',
            'farmowner2':'',
            'crop2':'',
            'farmsize2':'',
            'farm_location2':'',
            'farm_image2':'',
            'location_lat2':'',
            'location_long2':'',
            'years_on_farm2':'',
            'farmowner3':'',
            'crop3':'',
            'farmsize3':'',
            'farm_location3':'',
            'farm_image3':'',
            'location_lat3':'',
            'location_long3':'',
            'years_on_farm3':'',
            'farmowner4':'',
            'crop4':'',
            'farmsize4':'',
            'farm_location4':'',
            'farm_image4':'',
            'location_lat4':'',
            'location_long4':'',
            'years_on_farm4':'',
            'farmowner5':'',
            'crop5':'',
            'farmsize5':'',
            'farm_location5':'',
            'farm_image5':'',
            'location_lat5':'',
            'location_long5':'',
            'years_on_farm5':'',
            'overall_farming_years':'',
            'business_before_farming':'',
            'business_aside_farming':'',
            'averageyield':'',
            'previousyield':'',
            'farmbenefit':'',
            'buyerofproduce':'',
            'numberoftimes':'',
            'buyerbenefits':'',
            'useoffund':'',
            'any_bank_transacting_with':'',
            'transactingbank':'',
            'duration':'',
            'part_of_any_farmers_association':'',
            'farmers_association':'',
            'declaration':'',
        }

'''
# // Staff Creation form column //
class StaffCreationForm(forms.ModelForm):
    class Meta:
        model = Staffs
        fields = ['title','image','family_name','given_name','middle_name','sex','day','month','year','marital_status','address','address_city','address_region','id_card_no','hometown','hometown_region','personal_phone','alt_personal_phone','next_of_kin','relationship_with_kin','kins_address','kins_contact','department', 'position','assigned_region','assigned_society']
        labels = {
            'title':'',
            'image':'',
            'family_name':'',
            'given_name':'',
            'middle_name':'',
            'sex':'',
            'day':'',
            'month':'',
            'year':'',
            'marital_status':'',
            'address':'',
            'address_city':'',
            'address_region':'',
            'id_card_no':'',
            'hometown':'',
            'hometown_region':'',
            'personal_phone':'',
            'alt_personal_phone':'',
            'next_of_kin':'',
            'relationship_with_kin':'',
            'kins_address':'',
            'kins_contact':'',
            'department':'',
            'position':'',
            'assigned_region':'',
            'assigned_society':'',
        }
'''
class ZonesForm(forms.ModelForm):
    class Meta:
        model = Zone
        fields = ['district', 'societies','zone_center', 'zone_coordinator']




