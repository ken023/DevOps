import models
from rest_framework import serializers
from authority.models import ExtendUser

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    users = serializers.PrimaryKeyRelatedField(many=True,queryset=ExtendUser.objects.all())
    class Meta:
        model = models.Group
        fields = ('id', 'name', 'info', 'uuid', 'status','users','framework'
                )
        read_only_fields = ('id','framework'
                             )

class StorageSerializer(serializers.HyperlinkedModelSerializer):
    group_name = serializers.StringRelatedField(source="get_all_group_name",read_only=True)
    class Meta:
        model = models.Storage
        fields = ('id','disk_size','disk_path','info','group_name',
                  )

class SystemTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.System_Type
        fields = (
            'id','name'
        )
class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Position
        fields = (
            'id','name'
        )

class HostDetailSerializer(serializers.ModelSerializer):
    systemtype = serializers.PrimaryKeyRelatedField(queryset=models.System_Type.objects.all())
    position = serializers.PrimaryKeyRelatedField(queryset=models.Position.objects.all())
    class Meta:
        model = models.HostDetail
        fields = (
            'position','systemtype','info'
        )

class HostSerializer(serializers.ModelSerializer):
    label = serializers.CharField(source='__unicode__',read_only=True)
    detail = HostDetailSerializer(required=True)
    class Meta:
        model=models.Host
        fields = (
            'id','uuid','label','detail','connect_ip','service_ip','hostname','sshport','status'
        )
        read_only_fields = ('id','uuid','label')

    def create(self, validated_data):
        detail = validated_data.pop('detail')
        detail_instance = models.HostDetail.objects.create(**detail)
        return models.Host.objects.create(detail=detail_instance,**validated_data)

    def update(self, instance, validated_data):
        detail = validated_data.pop('detail')
        for v in detail:
            if hasattr(instance.detail,v):
                setattr(instance.detail,v,detail.get(v))
        instance.detail.save()
        return super(HostSerializer,self).update(instance,validated_data)

class HostPasswordSerializer(serializers.ModelSerializer):
    password = serializers.StringRelatedField(source='password_get',read_only=True)
    class Meta:
        model=models.Host
        fields = ('id','password')