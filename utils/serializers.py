from rest_framework import serializers


class RecursiveField(serializers.Serializer):
    """
    Поле для рекурсивного вывода дерева
    """

    def to_representation(self, value):
        return self.parent.parent.__class__(value, context=self.context).data

def update_nested(serializer_class, nested):
    serializer = serializer_class(many=True, data=nested, partial=True)
    serializer.is_valid(raise_exception=True)
    return serializer.save()