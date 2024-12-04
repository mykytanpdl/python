from django.core.validators import MinValueValidator
from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class PublishingHouse(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=13, unique=True, null=True, blank=True)
    email = models.EmailField(unique=True)
    country = models.ForeignKey(Country, on_delete=models.RESTRICT)
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=30)
    house_number = models.CharField(max_length=5)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    year_of_birth = models.IntegerField(null=True, blank=True)
    year_of_death = models.IntegerField(null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.RESTRICT)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(year_of_death__isnull=True) | models.Q(year_of_death__gte=models.F('year_of_birth')),
                name='chk_year_of_death'
            )
        ]


class Book(models.Model):
    TYPE_OF_COVER_CHOICES = [
        ('hardcover', 'Hardcover'),
        ('softcover', 'Softcover'),
        ('paperback', 'Paperback'),
    ]
    AGE_CATEGORY_CHOICES = [
        ('0-3', '0-3'),
        ('4-6', '4-6'),
        ('7-9', '7-9'),
        ('10-12', '10-12'),
        ('12+', '12+'),
        ('16+', '16+'),
        ('18+', '18+'),
        ('any', 'Any'),
    ]

    title = models.CharField(max_length=150)
    publishing_house = models.ForeignKey(PublishingHouse, on_delete=models.RESTRICT)
    publishing_year = models.PositiveIntegerField()
    ISBN = models.CharField(max_length=13, unique=True)
    number_of_pages = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    type_of_cover = models.CharField(max_length=10, choices=TYPE_OF_COVER_CHOICES, default='hardcover')
    language = models.CharField(max_length=20)
    age_category = models.CharField(max_length=5, choices=AGE_CATEGORY_CHOICES, default='any')
    total_copies = models.PositiveIntegerField(default=0)

    genres = models.ManyToManyField(Genre, through='BookGenre', related_name='books')
    authors = models.ManyToManyField(Author, through='BookAuthor', related_name='books')

    def __str__(self):
        return self.title

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(number_of_pages__gt=0), name='chk_number_of_pages'),
            models.CheckConstraint(check=models.Q(total_copies__gte=0), name='chk_total_copies'),
        ]


class BookGenre(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('book', 'genre')




class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('book', 'author')


class Reader(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=13, unique=True)
    email = models.EmailField(unique=True)
    passport_series = models.CharField(max_length=2, null=True, blank=True)
    passport_number = models.CharField(max_length=9)
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=30)
    house_number = models.CharField(max_length=5)
    apartment_number = models.CharField(max_length=10, null=True, blank=True)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        unique_together = ('passport_series', 'passport_number')


class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reader = models.ForeignKey(Reader, related_name='loans', on_delete=models.CASCADE)
    loan_date = models.DateField(auto_now=True)
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(return_date__isnull=True) | models.Q(return_date__gte=models.F('loan_date')),
                name='chk_loan_return_date'
            )
        ]

    def __str__(self):
        return f"Loan {self.id}: {self.book.title} to {self.reader.first_name} {self.reader.last_name}"
