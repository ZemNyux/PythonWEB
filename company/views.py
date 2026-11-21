from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from .models import Client, Contract, Department, Employee, Project


@require_http_methods(['GET', 'OPTIONS'])
def api_company(request):
    """Return the company dashboard data for the separate local React client."""
    if request.method == 'OPTIONS':
        response = JsonResponse({}, status=204)
    else:
        departments = list(Department.objects.values(
            'id', 'name', 'code', 'description', 'head_name', 'is_active'
        ))
        employees = list(Employee.objects.select_related('department').values(
            'id', 'full_name', 'position', 'email', 'phone',
            'department__name', 'department_id'
        ))
        projects = list(Project.objects.values(
            'id', 'title', 'code', 'status', 'budget', 'start_date'
        ))
        clients = list(Client.objects.values(
            'id', 'name', 'industry', 'contact_email', 'country', 'is_active'
        ))
        contracts = list(Contract.objects.select_related('client').values(
            'id', 'number', 'title', 'amount', 'signed_on', 'client__name', 'client_id'
        ))
        response = JsonResponse({
            'company': {'name': 'ZemNyux Inc.', 'tagline': 'Корпоративний портал'},
            'departments': departments,
            'employees': employees,
            'projects': projects,
            'clients': clients,
            'contracts': contracts,
            'meta': {'total': sum(map(len, (departments, employees, projects, clients, contracts)))},
        })

    origin = request.headers.get('Origin', '')
    if origin in ('http://localhost:5173', 'http://127.0.0.1:5173'):
        response['Access-Control-Allow-Origin'] = origin
        response['Vary'] = 'Origin'
        response['Access-Control-Allow-Methods'] = 'GET, OPTIONS'
        response['Access-Control-Allow-Headers'] = 'Content-Type'
    return response
