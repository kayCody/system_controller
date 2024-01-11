from rest_framework.serializers import ModelSerializer
from database.models import Member

class MemberSerializer(ModelSerializer):
  class Meta:
    model = Member
    fields = ('region','district','zoneNumber','society','image','title','surname','givenName','middleName','dateOfBirth','gender','address','hometown','hometownRegion','idNumber','levelOfEducation','contact','altContact','maritalStatus','familySize','nextOfKingFullname','relationshipWithNOK','nokContact','farmOwner','farmSize','numberOfLabourers','farmLocation','averageCropYield','supportingBusiness','buyerOfProduce','reasonForChoosingBuyer','fundInterest','interestSpecify','bankTransactingWith','numberOfYears','partOfAssociation','associationSpecify')