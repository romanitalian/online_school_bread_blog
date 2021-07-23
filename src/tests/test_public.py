import pytest
from django.urls import reverse

# from main.models import ContactUs


def test_view(client):
   res = client.get("/")
   assert res.status_code == 200

# @pytest.mark.django_db
# def test_home_page(client):
#     response = client.get(reverse("home_page"))
#     assert response.status_code == 200

#
# def test_contacts_us_show(client):
#     response = client.get(reverse("contact-us-create"))
#     assert response.status_code == 200
#
#
# def test_contacts_us_post_empty_form(client):
#     response = client.post(reverse("contact-us-create"))
#     assert response.status_code == 200
#     assert response.context_data['form'].errors == {
#         'email': ['Обязательное поле.'],
#         'subject': ['Обязательное поле.'],
#         'message': ['Обязательное поле.']
#     }
#
#
# def test_contacts_us_wrong_email(client):
#     response = client.post(reverse("contact-us-create"), data={
#         'email': 'not-valid-email'
#     })
#     assert response.status_code == 200
#     assert response.context_data['form'].errors == {
#         'email': ['Введите правильный адрес электронной почты.'],
#         'subject': ['Обязательное поле.'],
#         'message': ['Обязательное поле.']
#     }
#
#
# def test_contacts_us_correct_form(client):
#     response = client.post(reverse("contact-us-create"), data={
#         'email': 'test@mail.com',
#         'subject': 'subj',
#         'message': 'msg',
#     })
#     assert response.status_code == 302
#
#
# def test_contacts_us_correct_form_check_count(client):
#     count_before = ContactUs.objects.count()
#     response = client.post(reverse("contact-us-create"), data={
#         'email': 'test@mail.com',
#         'subject': 'subj',
#         'message': 'msg',
#     })
#     assert response.status_code == 302
#     assert ContactUs.objects.count() == count_before + 1
#
#     response = client.post(reverse("contact-us-create"), data={
#         'email': 'test@mail.com',
#         'subject': 'subj',
#         'message': 'msg',
#     })
#     assert response.status_code == 302
#     assert ContactUs.objects.count() == count_before + 2
#
#
# def test_tutu(client, tt):
#     print(f"in test fixture: {tt}")
#
#
# def test_tutu2(client, tt):
#     print(f"in test2 fixture: {tt}")
#
#
# def test_acc(acc_fixt):
#     print(acc_fixt)
#
# def test_acc(author_fixt):
#     print(acc_fixt)
#
#
# def test_contacts_us_correct_form_check_count(client, fake_fixt):
#     count_before = ContactUs.objects.count()
#     response = client.post(reverse("contact-us-create"), data={
#         'email': fake_fixt.email(),
#         'subject': fake_fixt.word(),
#         'message': fake_fixt.word(),
#     })
#     assert response.status_code == 302
#     assert ContactUs.objects.count() == count_before + 1
