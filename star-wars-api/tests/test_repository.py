import pytest
from swapi import repository

pytestmark = [pytest.mark.default_cassette("swapi.yaml"), pytest.mark.vcr()]

@pytest.fixture(scope="session")
def vcr_config():
    return {
        "filter_headers": ["authorization"],
        "ignore_localhost": True,
        "record_mode": "once",
    }


@pytest.fixture
def people_repo():
    return repository.SwapiPeopleRepository()

def test_swapi_people_repo_all_returns_expected_number_of_people(people_repo):
    people = people_repo.all()
    assert len(list(people)) == 82

def test_swapi_people_repo_find_returns_expectd_person(people_repo):
    results = list(people_repo.find(hair_color='blond', mass=None))
    assert len(results) == 1
    assert results.pop().name == 'Finis Valorum'
