from django.template import Context, Template
from django.test import Client, TestCase
from django.urls import reverse

from .entities import LeaderProfile, MetricCard
from .models import ContactInquiry, ContactOffice


class CoreViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertEqual(response.context['title'], 'Головна сторінка')
        self.assertIn('services', response.context)
        self.assertIn('stats', response.context)
        self.assertIn('portal_data', response.context)
        self.assertGreaterEqual(len(response.context['stats']), 1)
        metrics = response.context['portal_data']['dashboard']['metrics']
        self.assertTrue(metrics)
        self.assertIsInstance(metrics[0], MetricCard)
        self.assertContains(response, 'Усього показників:')

    def test_news_view(self):
        response = self.client.get(reverse('news'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news.html')
        self.assertEqual(response.context['title'], 'Новини компанії')
        self.assertIn('articles', response.context)
        self.assertIn('news_payload', response.context)

    def test_news_nested_redirect(self):
        response = self.client.get('/news/latest-updates/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.headers['Location'], '/news/')

    def test_management_view(self):
        response = self.client.get(reverse('management'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'management.html')
        self.assertEqual(response.context['title'], 'Керівництво компанії')
        self.assertIn('team', response.context)
        self.assertIn('board_data', response.context)
        profiles = response.context['board_data']['leaders']['profiles']
        self.assertTrue(profiles)
        self.assertIsInstance(profiles[0], LeaderProfile)
        self.assertContains(response, 'Гаряча лінія:')

    def test_custom_format_phone_filter(self):
        rendered = Template('{% load company_extras %}{{ phone|format_phone }}').render(
            Context({'phone': '+380441234567'})
        )
        self.assertEqual(rendered, '+380 44 123 45 67')

    def test_management_nested_redirect(self):
        response = self.client.get('/management/board/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.headers['Location'], '/management/')

    def test_about_view(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')
        self.assertEqual(response.context['title'], 'Про компанію')

    def test_about_nested_redirect(self):
        response = self.client.get('/about/team/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.headers['Location'], '/about/')

    def test_contacts_main_view(self):
        response = self.client.get(reverse('contacts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contacts.html')
        self.assertEqual(response.context['title'], 'Контакти представництв')
        self.assertIn('countries', response.context)
        self.assertIn('form', response.context)

    def test_contacts_form_submit(self):
        response = self.client.post(
            reverse('contacts'),
            {
                'name': 'Тест',
                'email': 'test@example.com',
                'subject': 'Питання',
                'message': 'Текст звернення для перевірки форми.',
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.headers['Location'], reverse('contacts'))
        self.assertEqual(ContactInquiry.objects.count(), 1)

    def test_contacts_country_views(self):
        countries = [
            ('france', 'Контакти: Франція (Париж)'),
            ('ukraine', 'Контакти: Україна (Київ / Одеса)'),
            ('austria', 'Контакти: Австрія (Відень)'),
            ('germany', 'Контакти: Німеччина (Берлін)'),
        ]
        for country, expected_title in countries:
            with self.subTest(country=country):
                self.assertTrue(ContactOffice.objects.filter(code=country).exists())
                url = reverse('contacts_country', kwargs={'country': country})
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)
                self.assertTemplateUsed(response, 'contact_country.html')
                self.assertEqual(response.context['title'], expected_title)

    def test_contacts_case_insensitivity(self):
        response = self.client.get('/contacts/FRANCE/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact_country.html')

    def test_contacts_unknown_country_404(self):
        url = reverse('contacts_country', kwargs={'country': 'unknown-country'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_custom_404_page(self):
        response = self.client.get('/non-existing-page-url-12345/')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')
        self.assertContains(response, '404', status_code=404)
        self.assertContains(response, 'Розділ не знайдено', status_code=404)

    def test_redirect_shortcuts(self):
        res_branch = self.client.get('/branch/')
        self.assertEqual(res_branch.status_code, 302)
        self.assertEqual(res_branch.headers['Location'], '/branches/')

        res_contact = self.client.get('/contact/')
        self.assertEqual(res_contact.status_code, 302)
        self.assertEqual(res_contact.headers['Location'], '/contacts/')

        res_history = self.client.get('/history/')
        self.assertEqual(res_history.status_code, 302)
        self.assertEqual(res_history.headers['Location'], '/branches/history/')

    def test_custom_middleware_headers(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.headers.get('X-Company-Name'), 'ZemNyux Inc.')
        self.assertEqual(response.headers.get('X-Powered-By'), 'ZemNyux 26/02/2026')

    def test_static_css_file_exists(self):
        import os

        from django.conf import settings

        css_path = os.path.join(settings.STATICFILES_DIRS[0], 'css', 'style.css')
        self.assertTrue(os.path.exists(css_path))
        with open(css_path, 'r', encoding='utf-8') as f:
            content = f.read()
        self.assertIn('.site-header', content)
        self.assertIn('.hero-banner', content)
