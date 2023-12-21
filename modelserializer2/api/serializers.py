from rest_framework import serializers
from .models import Record

class RecordSerializer(serializers.ModelSerializer):
    def start_with_r(value):
        if value[0].lower()!='r':
            raise serializers.ValidationError('Name should start with R')
    name = serializers.CharField(validators=[start_with_r])
    #name = serializers.CharField(read_only=True)
    class Meta:
        model = Record
        #fields = '__all__'
        # exclude = ['roll']
        fields = ['name','roll','city']
        #read_only = ['name','roll']
        #extra_kwargs = {'name':{'read_only':True}}
        
    # field level validator
    # def validate_roll(self, value):
    #     if value>=200:
    #         raise serializers.ValidationError('Seat full, sorry')
    #     return value
    
    # object level validation
    # def validate(self, data):
    #     nm = data.get('name')
    #     ct = data.get('city')
        
    #     if nm.lower()=='nabha' and ct.lower()!='bangalore':
    #         raise serializers.ValidationError('City must be Bangalore')
    #     return data