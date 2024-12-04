from library.models import Country
from library.repositories.base_repository import BaseRepository


class CountryRepository(BaseRepository):
    model = Country

    @classmethod
    def find_by_name(cls, name):
        return cls.model.objects.filter(name__iexact=name).first()
