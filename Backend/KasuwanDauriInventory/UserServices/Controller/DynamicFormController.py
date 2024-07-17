from KasuwanDauriInventory.helpers import getDynamicFormFields, getDynamicFormModels, getExcludedFields, renderResponse
from UserServices.models import Users
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.core.serializers import serialize
from django.apps import apps


class DynamicFormController(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, modelName):
        if modelName not in getDynamicFormModels():
            return renderResponse (data='Model Does Not Exist', message='Model Does Not Exist', status=404)
          

        model = getDynamicFormModels()[modelName]
        model_class=apps.get_model(model)

        if model_class is None:
            return renderResponse(data='Model not found', message='Model not found', status=404)


        fields_info=model_class._meta.fields
        model_fields={field.name for field in fields_info}
        exclude_fields=getExcludedFields()
    
        required_fields=[field.name for field in fields_info if not field.null and field.default is not None and field.name not in exclude_fields]

        missing_fields=[field for field in required_fields if field not in request.data]
        if missing_fields:
            return renderResponse(data=[f'The Following field is required :{field}' for field in missing_fields], message='Validation Error', status=400)

        
        
        fields=request.data.copy()
        fields['domain_user_id']=request.user.domain_user_id
        fields['added_by_user_id']=Users.objects.get(id=request.user.id)

        fieldsdata={key:value for key, value in fields.items() if key in model_fields}
        print(model_fields)
        print(fields.items())
        print(fieldsdata.items()) 

        for field in fields_info:
            if field.is_relation and field.name in fieldsdata and isinstance(fieldsdata[field.name],int):
                related_model=field.related_model
                try:
                    fieldsdata[field.name]=related_model.objects.get(id=fieldsdata[field.name])
                except related_model.DoesNotExist:
                    return renderResponse(data=f'{field.name} Relation Not Exist found', message=f'{field.name} Relation Not Exist found', status=404)




        model_instance=model_class.objects.create(**fieldsdata)

        serialized_data=serialize('json',[model_instance])
        model_json=json.loads(serialized_data)
        response_json=model_json[0]['fields']
        response_json['id']=model_json[0]['pk']
        return renderResponse(data=response_json, message='Data saved Successfully', status=200)

    def get(self, request, modelName):
        if modelName not in getDynamicFormModels():
            return renderResponse(data='Model not found', message='Model not found', status=404)

        model = getDynamicFormModels()[modelName]
        model_class=apps.get_model(model)

        if model_class is None:
            return renderResponse(data='Model not found', message='Model not found', status=404)
            

        fields_info=model_class._meta.fields
        model_fields={field.name for field in fields_info}
        exclude_fields=getExcludedFields()
    
        required_fields=[field.name for field in fields_info if not field.null and field.default is not None and field.name not in exclude_fields]

        missing_fields=[field for field in required_fields if field not in request.data]
        if missing_fields:
            return renderResponse(data=[f'The Following field is required :{field}' for field in missing_fields], message='Validation Error', status=400)
        
        fields=request.data.copy()
        fields['domain_user_id']=request.user.domain_user_id
        fields['added_by_user_id']=request.user.id

        model_instance=model_class.objects.create(**fields)

        serialized_data=serialize('json',[model_instance])
        model_json=json.loads(serialized_data)
        return renderResponse(data=model_json, message='Data saved Successfully', status=200)

        
    def get(self, request, modelName): 
        if modelName not in getDynamicFormModels():
            return renderResponse(data='Model not found', message='Model not found', status=404)
        
        model = getDynamicFormModels()[modelName]
        model_class=apps.get_model(model)

        if model_class is None:
            return renderResponse(data='Model not found', message='Model not found', status=404)

        model_instance = model_class()
        fields=getDynamicFormFields(model_instance,request.user.domain_user_id)
        return renderResponse(data=fields, message='Form fields fetched successfully', status=200)
