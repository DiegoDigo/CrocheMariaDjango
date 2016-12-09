# from  rest_framework import generics
# from cliente.models import ClienteModel
#
# class PostBase(object):
#     model = ClienteModel
#     queryset = ClienteModel.objects.all()
#     serializer_class = serializers.MotoristaSerializer
#
#     def perform_create(self, serializer):
#         serializer.save(auth=self.request.user)
