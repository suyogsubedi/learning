import pytest
from mathss import format_data_for_excel, format_data_for_display
# fixture chai kunai pani data dherai thau ma use huncha bhane ek thau ma lekhera chaina thau ma utilize garna.

# fixture auta file ma banayera arko ma use garna ko lagi chai import garna parcha, tara import nei nagari tyo data use garna mancha bhane chai conftest.py file ma fixture create garne

@pytest.fixture
def example_people_data():
    return [
        {
            "given_name": "Alfonsa",
            "family_name": "Ruiz",
            "title": "Senior Software Engineer",
        },
        {
            "given_name": "Sayid",
            "family_name": "Khan",
            "title": "Project Manager",
        },
    ]


# def test_format_data_for_display(example_people_data):
#     assert format_data_for_display(example_people_data) == [
#         "Alfonsa Ruiz: Senior Software Engineer",
#         "Sayid Khan: Project Manager",
#     ]


# def test_format_data_for_excel(example_people_data):
#     assert format_data_for_excel(example_people_data) == """given,family,title
# Alfonsa,Ruiz,Senior Software Engineer
# Sayid,Khan,Project Manager
# """

def test_conftest(example_people_data,dummyData):
    assert example_people_data == dummyData