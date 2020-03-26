from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response


class CustomUpdateAPIView(UpdateAPIView):
    update_serializer = None

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_update_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        response_data = self.get_serializer(instance=instance).data
        return Response(response_data)

    def get_update_serializer(self, *args, **kwargs):
        update_serializer_class = self.get_update_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return update_serializer_class(*args, **kwargs)

    def get_update_serializer_class(self):
        if not self.update_serializer:
            raise AttributeError('Поле update_serializer обязательно')
        return self.update_serializer
