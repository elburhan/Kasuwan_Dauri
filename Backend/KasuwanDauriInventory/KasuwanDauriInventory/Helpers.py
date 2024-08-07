from django.db.models import ForeignKey
from rest_framework.response import Response
from rest_framework.views import exception_handler
from rest_framework.exceptions import AuthenticationFailed,NotAuthenticated,PermissionDenied

def getDynamicFormModels():
    return {
        'product': 'ProductServices.Products',
        'category': 'ProductServices.Categories',
        'warehouse': 'InventoryServices.Warehouse',
    }

def getSuperAdminDynamicFormModels():
    return {
        'modules': 'UserServices.Modules',
    }

def checkisFileField(field):
    return field in ['image', 'file', 'path', 'video', 'audio']

def getExcludedFields():
    return ['id', 'domain_user_id', 'added_by_user_id', 'created_at', 'updated_at', 'created_by_user_id', 'updated_by_user_id']

def getDynamicFormFields(model_instance, domain_user_id):
    fields = {'text': [], 'select': [], 'radio': [], 'checkbox': [], 'textarea': [], 'json': [], 'file': []}
    
    for field in model_instance._meta.fields:
        if field.name in getExcludedFields():
            continue

        label = field.name.replace('_', ' ').title()
        fielddata = {
            'name': field.name,
            'label': label,
            'placeholder': 'Enter ' + label,
            'default': model_instance.__dict__.get(field.name, ''),
            'required': not field.null,
        }
        
        if checkisFileField(field.name):
            fielddata['type'] = 'file'
        elif field.get_internal_type() == 'JSONField':
            fielddata['type'] = 'json'
        elif field.choices:
            fielddata['type'] = 'select'
            fielddata['options'] = [{'id': choice[0], 'value': choice[1]} for choice in field.choices]
        elif field.get_internal_type() in ['CharField', 'IntegerField', 'DecimalField', 'FloatField']:
            fielddata['type'] = 'text'
        elif field.get_internal_type() in ['BooleanField', 'NullBooleanField']:
            fielddata['type'] = 'checkbox'
        elif isinstance(field, ForeignKey):
            related_model = field.related_model
            related_key_name = related_model._meta.pk.name
            
            # Attempt to use default key if specified
            if hasattr(related_model, 'defaultkey'):
                related_key_name = related_model.defaultkey()
                options = related_model.objects.filter(domain_user_id=domain_user_id).values_list('id', related_key_name,related_model.defaultkey())
            else:
                options = related_model.objects.filter(domain_user_id=domain_user_id).values_list('id', related_key_name)
            
            fielddata['options'] = [{'id': option[0], 'value': option[1]} for option in options]
            fielddata['type'] = 'select'
        else:
            fielddata['type'] = 'text'

        fields[fielddata['type']].append(fielddata)
    
    return fields

def parseDictToList(data):
    values = []
    for key, value in data.items():
        values.extend(value)
    return values
def renderResponse(data, message, status=200):
    if status >= 200 and status < 300:
        if isinstance(data, dict):
            data = parseDictToList(data)
        return Response({'data': data, 'message': message}, status=status)
    else:
        if isinstance(data, dict):
            return Response({'error': data, 'message': message}, status=status)
        elif isinstance(data, list):
            return Response({'error': {'message': data}, 'message': message}, status=status)
        else:
            return Response({'error': {'message': data}, 'message': message}, status=status)


def custom_exception_handler(exc, context):
    response=exception_handler(exc,context)

    if isinstance(exc,AuthenticationFailed):
        response_data={
            'message':exc.detail,
            'errors':exc.detail.get('message',[]),
        }
        return renderResponse(data=response_data['errors'],message=response_data['message']['detail'],status=response.status_code)
    elif isinstance(exc,NotAuthenticated):
        return renderResponse(data='User is not authenticated',message='User is not authenticated',status=exc.status_code)
    elif isinstance(exc,PermissionDenied):
        return renderResponse(data="You don't have permission to access this page",message='Permission Denied',status=exc.status_code)
    return response