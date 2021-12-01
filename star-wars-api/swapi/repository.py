import logging
import requests
from .schema import PersonSchema

log = logging.getLogger(__name__)

class SwapiRepository:
    base_url: str = 'https://swapi.dev/api/'

    def _get(self, url):
        response = requests.get(url)
        if response.status_code != 200:
            raise IOError(f"{response.status_code}: {response.text}")
        return response.json()

    def _get_all(self, url):
        next_url = url
        while next_url:
            this_page = self._get(next_url)
            next_url = this_page['next']
            for result in this_page['results']:
                yield result

    def all(self):
        raise NotImplemented()

    def find(self, **filter):
        for item in self.all():
            is_match = True
            for field, value in filter.items():
                if getattr(item, field) != value:
                    is_match = False
                    # We do not want to compare other fields if at least one field is not equal.
                    break
            if is_match:
                yield item


class SwapiPeopleRepository(SwapiRepository):
    
    def all(self):
        url = f"{self.base_url}people/"
        schema = PersonSchema()
        for person_data in self._get_all(url):
            try:
                person = schema.load(person_data)
                yield person
            except Exception as error:
                print(person_data)
                log.error(person_data, exc_info=error)
                raise error

