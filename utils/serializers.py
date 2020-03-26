from django.db.models import Model
from rest_framework import serializers


class RecursiveField(serializers.Serializer):
    """
    Поле для рекурсивного вывода дерева
    """

    def to_internal_value(self, data):
        return data

    def to_representation(self, value):
        return self.parent.parent.__class__(value, context=self.context).data


def update_nested(serializer_class, nested):
    """
    Обновление связаных объектов
    """
    for object_dict in nested:
        for key, value in object_dict.items():
            if isinstance(value, Model):
                object_dict[key] = value.pk
    serializer = serializer_class(many=True, data=nested, partial=True)
    serializer.is_valid(raise_exception=True)
    return serializer.save()
