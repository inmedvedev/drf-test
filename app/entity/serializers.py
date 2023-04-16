from rest_framework import serializers
from .models import Property, Entity


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = (
            "key",
            "value",
        )


class EntityListSerializer(serializers.ModelSerializer):
    properties = serializers.SerializerMethodField()

    class Meta:
        model = Entity
        fields = (
            "modified_by",
            "value",
            "properties",
        )

    def get_properties(self, entity):
        properties = PropertySerializer(entity.properties.all(), many=True).data
        entity_properties = {
            entity_property["key"]: entity_property["value"]
            for entity_property in properties
        }
        return entity_properties


class EntityCreateSerializer(serializers.ModelSerializer):
    properties = PropertySerializer(many=True)
    modified_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    value = serializers.IntegerField()

    class Meta:
        model = Entity
        fields = (
            "properties",
            "modified_by",
            "value",
        )

    def create(self, validated_data):
        properties = validated_data.pop("properties")
        entity = Entity.objects.create(**validated_data)

        for entity_property in properties:
            entity.properties.create(
                key=list(entity_property.items())[0][1],
                value=list(entity_property.items())[1][1],
            )
        return entity
