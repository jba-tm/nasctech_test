from rest_framework import views, response, status, exceptions
from ..functions import functions
from django.utils.translation import gettext_lazy as _


class DataAPIView(views.APIView):
    http_method_names = ['get', ]

    def get(self, request, *args, **kwargs):
        try:
            data = list(map(int, request.query_params.get('data', '').split(',')))

        except ValueError as e:
            raise exceptions.ValidationError(e)
        rules = request.query_params.get('rule', '').split(',')
        if '' in rules:
            rules.remove('')
        if len(rules) != 6:
            raise exceptions.ValidationError(_('Rules count must be equal to 6'))
        result = []
        for rule in rules:
            try:
                # print(rule)
                # print(functions['sum'](data))
                result.append(functions[rule](data))
            except KeyError as e:
                raise exceptions.ValidationError(e)
        return response.Response(data={'result': result}, status=status.HTTP_200_OK)
