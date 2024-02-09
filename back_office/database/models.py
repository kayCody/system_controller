from django.db import models
from datetime import date
from django.db import models

import random, string

# Create your models here.
'''
DISTRICT = [   
    ('Atwima-Mponua-District','Atwima-Mponua District'),
    ('Adansi South District','Adansi South District'),
    ('Afigya-Kwabre District','Afigya-Kwabre District'),
    ('Ahafo-Ano North District','Ahafo-Ano North District'),
    ('Ahafo-Ano South District','Ahafo-Ano South District'),
    ('Amansie Central District','Amansie Central District'),
    ('Amansie West District','Amansie West District'),
    ('Asante-Akim Central Municipal District','Asante-Akim Central Municipal District'),
    ('Asante-Akim North District','Asante-Akim North District'),
    ('Asante-Akim South District','Asante-Akim South District'),
    ('Asokore-Mampong Municipal District','Asokore-Mampong Municipal District'),
    ('Atwima-Kwanwoma District','Atwima-Kwanwoma District'),
    ('Atwima-Nwabiagya District','Atwima-Nwabiagya District'),
    ('Bekwai Municipal District','Bekwai Municipal District'),
    ('Bosome-Freho District','Bosome-Freho District'),
    ('Bosomtwe District','Bosomtwe District'),
    ('Ejisu-Juaben Municipal District','Ejisu-Juaben Municipal District'),
    ('Ejura-Sekyedumase District','Ejura-Sekyedumase District'),
    ('Kumasi Metropolitan District','Kumasi Metropolitan District'),
    ('Kumawu District','Kumawu District'),
    ('Kwabre East District','Kwabre East District'),
    ('Mampong Municipal District','Mampong Municipal District'),
    ('Obuasi Municipal District','Obuasi Municipal District'),
    ('Offinso Municipal District','Offinso Municipal District'),
    ('Offinso North District','Offinso North District'),
    ('Sekyere-Afram Plains District (map)','Sekyere-Afram Plains District (map)'),
    ('Sekyere East District','Sekyere East District'),
    ('Sekyere South District (map)','Sekyere South District (map)'),
    ('Adansi North District (map)','Adansi North District (map)'),
    ('Berekum East Municipal District','Berekum Wast Municipal District'),
    ('Berekum West Municipal District','Berekum West Municipal District'),
    ('Dormaa East District','Dormaa East District'),
    ('Dormaa Central Municipal District','Dormaa Central Municipal District'),
    ('Dormaa West District','Dormaa West District'),
    ('Jaman North District','Jaman North District'),
    ('Jaman South District','Jaman South District'),
    ('Sunyani Municipal District','Sunyani Municipal District'),
    ('Sunyani West District','Sunyani West District'),
    ('Tain District','Tain District'),
    ('Banda District','Banda District'),
    ('Asunafo South District','Asunafo South District'), # // Ahafo District //
    ('Asutifi District','Asutifi District'),
    ('Asutifi South District','Asutifi South District'),
    ('Atebubu-Amantin District','Atebubu-Amantin District'),
    ('Kintampo North Municipal District','Kintampo North Municipal District'),
    ('Kintampo South District','Kintampo South District'),
    ('Nkoranza North District','Nkoranza North District'),
    ('Nkoranza South Municipal District','Nkoranza South Municipal District'),
    ('Pru District','Pru District'),
    ('Sene East District','Sene East District'),
    ('Sene West District','Sene West District'),
    ('Tano North District','Tano North District'),
    ('Tano South District','Tano South District'),
    ('Techiman Municipal District','Techiman Municipal District'),
    ('Techiman North District','Techiman North District'),
    ('Asunafo North Municipal District','Asunafo North Municipal District'),
    ('Atebubu Amantin Municipal','Atebubu Amantin Municipal'), # // Bono East Region
    ('Kintampo South','Kintampo South'),
    ('Nkoranza North','Nkoranza North'),
    ('Nkoranza South Municipal','Nkoranza South Municipal'),
    ('Pru','Pru'),
    ('Sene East','Sene East'),
    ('Sene West','Sene West'),
    ('Techiman Municipal','Techiman Municipal'),
    ('Techiman North','Techiman North'),
    ('Kintampo Municipal','Kintampo Municipal'),
    ('Abura - Asebu - Kwamankese District','Abura - Asebu - Kwamankese District'), # // Central District //
    ('Agona West Municipal District','Agona West Municipal District'),
    ('Ajumako-Enyan-Essiam District','Ajumako-Enyan-Essiam District'),
    ('Asikuma - Odoben - Brakwa District','Asikuma - Odoben - Brakwa District'),
    ('Assin North Municipal District','Assin North Municipal District'),
    ('Assin South District','Assin South District'),
    ('Awutu-Senya District','Awutu-Senya District'),
    ('Awutu Senya East Municipal District','Awutu Senya East Municipal District'),
    ('Cape Coast Metropolitan District','Cape Coast Metropolitan District'),
    ('Effutu Municipal District','Effutu Municipal District'),
    ('Ekumfi District','Ekumfi District'),
    ('Gomoa East District','Gomoa East District'),
    ('Gomoa West District','Gomoa West District'),
    ('Komenda-Edina','Komenda-Edina'),
    ('Eguafo-Abrem Municipal District','Eguafo-Abrem Municipal District'),
    ('Mfantseman Municipal District','Mfantseman Municipal District'),
    ('Twifo Atti - Mokwa District','Twifo Atti - Mokwa District'),
    ('Twifo Hemang - Lower Denkyira District','Twifo Hemang - Lower Denkyira District'),
    ('Upper Denkyira East Municipal District','Upper Denkyira East Municipal District'),
    ('Upper Denkyira West District','Upper Denkyira West District'),
    ('Agona East District','Agona East District'),
    ('Aowin District','Aowin District'), # // Western North
    ('Bia District','Bia District'),
    ('Bia East District','Bia East District'),
    ('Bibiani-Anhwiaso-Bekwai District','Bibiani-Anhwiaso-Bekwai District'),
    ('Bodi District','Bodi District'),
    ('Sefwi-Wiawso District','Sefwi-Wiawso District'),
    ('Yilo Krobo Municipal District','Yilo Krobo Municipal District'),
    ('Suaman District','Suaman District'),
    ('Juaboso District','Juaboso District'),
    ('Sefwi-Akontombra District','Sefwi-Akontombra District'),
    ('Keta','Keta'), # // Volta Region //
    ('Kpando','Kpando'),
    ('Ho','Ho'),
    ('Kadjebi','Kadjebi'),
    ('South Tongu','South Tongu'),
    ('South Dayi','South Dayi'),
    ('Krachi East','Krachi East'),
    ('Ketu North','Ketu North'),
    ('Nkwanta North','Nkwanta North'),
    ('Biakoye','Biakoye'),
    ('Nkwanta South','Nkwanta South'),
    ('Jasikan','Jasikan'),
    ('North Dayi','North Dayi'),
    ('Central Tongu','Central Tongu'),
    ('Krachi West','Krachi West'),
    ('Afadzato - South','Afadzato - South'),
    ('Agortime Ziope','Agortime Ziope'),
    ('North Tongu','North Tongu'),
    ('Akatsi North','Akatsi North'),
    ('Ho West','Ho West'),
    ('Krachi Ntsumuru','Krachi Ntsumuru'),
    ('Adaklu','Adaklu'),
    ('Akatsi South','Akatsi South'),
    ('>Ketu South','>Ketu South'),
    ('Hohoe','Hohoe'),
    ('JASIKAN DISTRICT','JASIKAN DISTRICT'), # // Oti Region
    ('KRACHI EAST MUNICIPAL','KRACHI EAST MUNICIPAL'),
    ('BIAKOYE DISTRICT','BIAKOYE DISTRICT'),
    ('KADJEBI DISTRICT','KADJEBI DISTRICT'),
    ('KRACHI NCHUMURU DISTRICT','KRACHI NCHUMURU DISTRICT'),
    ('KRACHI WEST DISTRICT','KRACHI WEST DISTRICT'),
    ('NKWANTA NORTH DISTRICT','NKWANTA NORTH DISTRICT'),
    ('NKWANTA SOUTH MUNICIPAL','NKWANTA SOUTH MUNICIPAL'),
    ('Akwapim North Municipal District','Akwapim North Municipal District'), # // Eastern Region
    ('Akyemansa District','Akyemansa District'),
    ('Asuogyaman District','Asuogyaman District'),
    ('Atiwa District','Atiwa District'),
    ('Ayensuano District','Ayensuano District'),
    ('Birim Central Municipal District','Birim Central Municipal District'),
    ('Birim North District','Birim North District'),
    ('Birim South District','Birim South District'),
    ('Denkyembour District','Denkyembour District'),
    ('East Akim Municipal District','East Akim Municipal District'),
    ('Fanteakwa District','Fanteakwa District'),
    ('Kwaebibirem District','Kwaebibirem District'),
    ('Kwahu Afram Plains North District','Kwahu Afram Plains North District'),
    ('Kwahu Afram Plains South District','Kwahu Afram Plains South District'),
    ('Kwahu East District','Kwahu East District'),
    ('Kwahu South District','Kwahu South District'),
    ('Kwahu West Municipal District','Kwahu West Municipal District'),
    ('Lower Manya Krobo Municipal District','Lower Manya Krobo Municipal District'),
    ('New Juaben Municipal District','New Juaben Municipal District'),
    ('Nsawam - Adoagyire Municipal District','Nsawam - Adoagyire Municipal District'),
    ('Suhum Municipal District','Suhum Municipal District'),
    ('Upper Manya Krobo District','Upper Manya Krobo District'),
    ('Upper West Akim District','Upper West Akim District'),
    ('West Akim Municipal','West Akim Municipal'),
    ('Akwapim South District','Akwapim South District'),    
]
'''
# // Members forms model //
class FormToken(models.Model):
    pass

class Member(models.Model):
    memberId = models.CharField(max_length=10, blank=True,unique=True)
    gfxNumber = models.CharField(max_length=10, blank=False, null=False)
    region = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    zoneNumber = models.CharField(max_length=100,blank=True, null=True)
    society = models.CharField(max_length=100,blank=True, null=True)
    image = models.ImageField(default="image.png",blank=True, null=True,upload_to="members_id/")
    title = models.CharField(max_length=100,blank=True, null=True)
    surname = models.CharField(max_length=100,blank=True, null=True)
    givenName = models.CharField(max_length=100,blank=True, null=True)
    middleName = models.CharField(max_length=100,blank=True, null=True)
    dateOfBirth = models.CharField(max_length=100,blank=True, null=True)
    gender = models.CharField(max_length=100,blank=True, null=True)
    address = models.CharField(max_length=100,blank=True, null=True)
    hometown = models.CharField(max_length=100,blank=True, null=True)
    hometownRegion = models.CharField(max_length=100,blank=True, null=True)
    idNumber = models.CharField(max_length=100,blank=True, null=True)
    levelOfEducation = models.CharField(max_length=100,blank=True, null=True)
    contact = models.CharField(max_length=100,blank=True, null=True)
    altContact = models.CharField(max_length=100,blank=True, null=True)
    maritalStatus = models.CharField(max_length=100,blank=True, null=True)
    familySize = models.CharField(max_length=100,blank=True, null=True)
    nextOfKingFullname = models.CharField(max_length=100,blank=True, null=True)
    relationshipWithNOK = models.CharField(max_length=100,blank=True, null=True)
    nokContact = models.CharField(max_length=100,blank=True, null=True)
    farmOwner = models.CharField(max_length=100,blank=True, null=True)
    farmSize = models.CharField(max_length=100,blank=True, null=True)
    numberOfLabourers = models.CharField(max_length=100,blank=True, null=True)
    farmLocation = models.CharField(max_length=100,blank=True, null=True)
    averageCropYield = models.CharField(max_length=100,blank=True, null=True)
    supportingBusiness = models.CharField(max_length=100,blank=True, null=True)
    buyerOfProduce = models.CharField(max_length=100,blank=True, null=True)
    reasonForChoosingBuyer = models.CharField(max_length=100,blank=True, null=True)
    fundInterest = models.CharField(max_length=100,blank=True, null=True)
    interestSpecify = models.CharField(max_length=100,blank=True, null=True)
    bankTransactingWith = models.CharField(max_length=100,blank=True, null=True)
    numberOfYears = models.CharField(max_length=100,blank=True, null=True)
    partOfAssociation = models.CharField(max_length=100,blank=True, null=True)
    associationSpecify = models.CharField(max_length=100,blank=True, null=True)
    created_at = models.DateTimeField(blank=True, auto_now_add=True, editable=True)
    updated = models.DateTimeField(blank=True, auto_now=True)
    
    def save(self, *args, **kwargs):
        prefix = 'GFX#'
        rand = random.randint(0, 10000000)
        member_generated_id=str(prefix).replace('#',str(rand).zfill(7))
        self.memberId = str(member_generated_id)
        super().save(*args,**kwargs)

    def __str__(self):
        return str(self.memberId)
    