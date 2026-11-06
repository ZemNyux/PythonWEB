from django.test import Client, TestCase
from django.urls import reverse


class BranchesViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_branches_list_view(self):
        response = self.client.get(reverse('branches_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'branches_list.html')
        self.assertEqual(response.context['title'], 'Міжнародні філії компанії')
        self.assertIn('branches', response.context)
        self.assertEqual(len(response.context['branches']), 3)

    def test_london_view(self):
        response = self.client.get(reverse('london'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'london.html')
        self.assertEqual(response.context['title'], 'Філія в Лондоні')

        # Перевірка альтернативного шляху з великої літери
        alt_response = self.client.get('/branches/London/')
        self.assertEqual(alt_response.status_code, 200)

    def test_paris_view(self):
        response = self.client.get(reverse('paris'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'paris.html')
        self.assertEqual(response.context['title'], 'Філія в Парижі')

        # Перевірка альтернативного шляху з великої літери
        alt_response = self.client.get('/branches/Paris/')
        self.assertEqual(alt_response.status_code, 200)

    def test_berlin_view(self):
        response = self.client.get(reverse('berlin'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'berlin.html')
        self.assertEqual(response.context['title'], 'Філія в Берліні')

        # Перевірка альтернативного шляху з великої літери
        alt_response = self.client.get('/branches/Berlin/')
        self.assertEqual(alt_response.status_code, 200)

    def test_history_views(self):
        history_pages = [
            ('history_main', 'history.html', 'Історія компанії та філій'),
            ('history_dates', 'dates.html', 'Хронологія розвитку та дати'),
            ('history_facts', 'facts.html', 'Значущі факти про нас'),
        ]
        for url_name, template, expected_title in history_pages:
            with self.subTest(url_name=url_name):
                response = self.client.get(reverse(url_name))
                self.assertEqual(response.status_code, 200)
                self.assertTemplateUsed(response, template)
                self.assertEqual(response.context['title'], expected_title)
