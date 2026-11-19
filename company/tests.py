from django.test import TestCase

from .models import Client, Contract, Department, Employee, Project


class CompanyModelsTestCase(TestCase):
    def test_five_entity_tables_exist_and_are_empty(self):
        self.assertEqual(Department.objects.count(), 0)
        self.assertEqual(Employee.objects.count(), 0)
        self.assertEqual(Project.objects.count(), 0)
        self.assertEqual(Client.objects.count(), 0)
        self.assertEqual(Contract.objects.count(), 0)

    def test_models_have_four_to_five_fields(self):
        expected = {
            Department: 5,
            Employee: 5,
            Project: 5,
            Client: 5,
            Contract: 5,
        }
        for model, field_count in expected.items():
            concrete_fields = [
                f.name
                for f in model._meta.local_fields
                if f.name != 'id'
            ]
            self.assertEqual(len(concrete_fields), field_count, model.__name__)
