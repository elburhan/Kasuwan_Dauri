from django.apps import apps
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from KasuwanDauriInventory.permission import IsSuperAdmin
from KasuwanDauriInventory.helpers import getExcludedFields, getSuperAdminDynamicFormModels, renderResponse
from rest_framework import status
from django.core.serializers import serialize
from django.db import IntegrityError
import json

class SuperAdminDynamicFormController(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsSuperAdmin]

    def post(self, request, modelName):
        if modelName not in getSuperAdminDynamicFormModels():
            return renderResponse(data='Model Does Not Exist', message='Model Does Not Exist', status=404)
          
        model = getSuperAdminDynamicFormModels()[modelName]
        model_class = apps.get_model(model)

        if model_class is None:
            return renderResponse(data='Model not found', message='Model not found', status=404)

        fields_info = model_class._meta.fields
        model_fields = {field.name for field in fields_info}
        exclude_fields = getExcludedFields()
    
        required_fields = [field.name for field in fields_info if not field.null and field.default is not None and field.name not in exclude_fields]

        missing_fields = [field for field in required_fields if field not in request.data]
        if missing_fields:
            return renderResponse(data=[f'The following field is required: {field}' for field in missing_fields], message='Validation Error', status=400)
        
        fields = request.data.copy()
        fieldsdata = {key: value for key, value in fields.items() if key in model_fields}

        for field in fields_info:
            if field.is_relation and field.name in fieldsdata and isinstance(fieldsdata[field.name], int):
                related_model = field.related_model
                try:
                    fieldsdata[field.name] = related_model.objects.get(id=fieldsdata[field.name])
                except related_model.DoesNotExist:
                    return renderResponse(data=f'{field.name} Relation Not Found', message=f'{field.name} Relation Not Found', status=404)

        # Check if module_name already exists
        if 'module_name' in fieldsdata:
            existing_module = model_class.objects.filter(module_name=fieldsdata['module_name']).first()
            if existing_module:
                return renderResponse(data='Module with this name already exists', message='Module with this name already exists', status=400)

        try:
            model_instance = model_class.objects.create(**fieldsdata)
        except IntegrityError as e:
            return renderResponse(data=str(e), message='Error creating module', status=500)

        serialized_data = serialize('json', [model_instance])
        model_json = json.loads(serialized_data)
        response_json = model_json[0]['fields']
        response_json['id'] = model_json[0]['pk']
        return renderResponse(data=response_json, message='Data saved Successfully', status=200)
