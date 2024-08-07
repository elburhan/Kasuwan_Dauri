import json
from KasuwanDauriInventory.helpers import renderResponse
from UserServices.models import Modules
from rest_framework.views import APIView
from django.core.serializers import serialize

class ModuleView(APIView):
    def get(self, request):
        menus = Modules.objects.filter(is_menu=True, parent_id=None, is_active=True).order_by('display_order')
        serialized_menus = serialize('json', menus)
        serialized_menus = json.loads(serialized_menus)

        cleaned_menus = []
        for menu in serialized_menus:
            menu['fields']['id'] = menu['pk']
            menu['fields']['submenu'] = list(Modules.objects.filter(
                parent_id=menu['pk'], is_active=True, is_menu=True
            ).order_by('display_order').values(
                'id', 'module_name', 'module_icon', 'is_menu', 'is_active', 'parent_id', 'display_order', 'module_url', 'module_description'
            ))
            cleaned_menus.append(menu['fields'])

        return renderResponse(data=cleaned_menus, message='All modules', status=200)
