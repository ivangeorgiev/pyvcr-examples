import pytest
from swapi.schema import PersonSchema
from swapi import model

@pytest.fixture(scope="session")
def person_schema():
    schema = PersonSchema()
    return schema

@pytest.fixture
def person_data():
    data =  {
        "name": "Luke Skywalker",
        "height": "172",
        "mass": "77",
        "hair_color": "blond",
        "skin_color": "fair",
        "eye_color": "blue",
        "birth_year": "19BBY",
        "gender": "male",
        "homeworld": "https://swapi.dev/api/planets/1/",
        "films": [
            "https://swapi.dev/api/films/1/",
            "https://swapi.dev/api/films/2/",
            "https://swapi.dev/api/films/3/",
            "https://swapi.dev/api/films/6/"
        ],
        "species": [],
        "vehicles": [
            "https://swapi.dev/api/vehicles/14/",
            "https://swapi.dev/api/vehicles/30/"
        ],
        "starships": [
            "https://swapi.dev/api/starships/12/",
            "https://swapi.dev/api/starships/22/"
        ],
        "created": "2014-12-09T13:50:51.644000Z",
        "edited": "2014-12-20T21:17:56.891000Z",
        "url": "https://swapi.dev/api/people/1/"
    }

    return data

@pytest.fixture
def deserialized_person_data():
    return {
        "name": "Luke Skywalker",
        "height": 172,
        "mass": 77,
        "hair_color": "blond",
        "skin_color": "fair",
        "eye_color": "blue",
        "birth_year": "19BBY",
        "gender": "male",        
    }

def test_person_schema_deserializes_to_person_object_with_attributes_set(person_schema, person_data, deserialized_person_data):
    result = person_schema.load(person_data)
    assert isinstance(result, model.Person)
    assert result.asdict() == deserialized_person_data
    

def test_person_with_unknown_mass_is_set_to_none(person_schema, person_data, deserialized_person_data):
    person_data['mass'] = 'unknown'
    deserialized_person_data['mass'] = None
    result = person_schema.load(person_data)
    assert result.asdict() == deserialized_person_data

def test_person_with_big_float_mass_is_correctly_parsed(person_schema, person_data, deserialized_person_data):
    person_data['mass'] = '1,569.2'
    deserialized_person_data['mass'] = 1569.2
    result = person_schema.load(person_data)
    assert result.asdict() == deserialized_person_data


def test_person_with_unknown_height_is_set_to_none(person_schema, person_data, deserialized_person_data):
    person_data['height'] = 'unknown'
    deserialized_person_data['height'] = None
    result = person_schema.load(person_data)
    assert result.asdict() == deserialized_person_data
