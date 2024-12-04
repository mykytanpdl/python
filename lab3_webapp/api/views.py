
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.serializers import *
from library.models import *
from library.repositories.author_repository import AuthorRepository
from library.repositories.book_repository import BookRepository
from library.repositories.country_repository import CountryRepository
from library.repositories.genre_repository import GenreRepository
from library.repositories.loan_repository import LoanRepository
from library.repositories.pub_house_repository import PublishingHouseRepository
from library.repositories.reader_repository import ReaderRepository


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_book(request, book_id):
    book = BookRepository.get(pk=book_id)
    serializer = BookSerializer(book)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_books(request):
    books = BookRepository.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_book(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        try:
            BookRepository.create(**serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_book(request, book_id):
    try:
        book = BookRepository.get(book_id)
    except Book.DoesNotExist:
        return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = BookSerializer(book, data=request.data)
    if serializer.is_valid():
        try:
            BookRepository.update(book_id, **serializer.validated_data)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_book(request, book_id):
    try:
        BookRepository.delete(book_id)
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Book.DoesNotExist:
        return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_reader(request, reader_id):
    reader = ReaderRepository.get(pk=reader_id)
    serializer = ReaderSerializer(reader)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_readers(request):
    readers = ReaderRepository.all()
    serializer = ReaderSerializer(readers, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_reader(request):
    serializer = ReaderSerializer(data=request.data)
    if serializer.is_valid():
        try:
            ReaderRepository.create(**serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_reader(request, reader_id):
    try:
        reader = ReaderRepository.get(reader_id)
    except Reader.DoesNotExist:
        return Response({'error': 'Reader not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ReaderSerializer(reader, data=request.data)
    if serializer.is_valid():
        try:
            ReaderRepository.update(reader_id, **serializer.validated_data)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_reader(request, reader_id):
    try:
        ReaderRepository.delete(reader_id)
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Reader.DoesNotExist:
        return Response({'error': 'Reader not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_author(request, author_id):
    try:
        author = AuthorRepository.get(author_id)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)
    except Author.DoesNotExist:
        return Response({'error': 'Author not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_authors(request):
    authors = AuthorRepository.all()
    serializer = AuthorSerializer(authors, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_author(request):
    serializer = AuthorSerializer(data=request.data)
    if serializer.is_valid():
        try:
            AuthorRepository.create(**serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_author(request, author_id):
    try:
        author = AuthorRepository.get(author_id)
    except Author.DoesNotExist:
        return Response({'error': 'Author not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = AuthorSerializer(author, data=request.data)
    if serializer.is_valid():
        try:
            AuthorRepository.update(author_id, **serializer.validated_data)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_author(request, author_id):
    try:
        AuthorRepository.delete(author_id)
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Author.DoesNotExist:
        return Response({'error': 'Author not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_genre(request, genre_id):
    try:
        genre = GenreRepository.get(genre_id)
        serializer = GenreSerializer(genre)
        return Response(serializer.data)
    except Genre.DoesNotExist:
        return Response({'error': 'Genre not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_genres(request):
    genres = GenreRepository.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_genre(request):
    serializer = GenreSerializer(data=request.data)
    if serializer.is_valid():
        try:
            GenreRepository.create(**serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_genre(request, genre_id):
    try:
        genre = GenreRepository.get(genre_id)
    except Genre.DoesNotExist:
        return Response({'error': 'Genre not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = GenreSerializer(genre, data=request.data)
    if serializer.is_valid():
        try:
            GenreRepository.update(genre_id, **serializer.validated_data)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_genre(request, genre_id):
    try:
        GenreRepository.delete(genre_id)
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Genre.DoesNotExist:
        return Response({'error': 'Genre not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_loan(request, loan_id):
    try:
        loan = LoanRepository.get(loan_id)
        serializer = LoanSerializer(loan)
        return Response(serializer.data)
    except Loan.DoesNotExist:
        return Response({'error': 'Loan not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_loans(request):
    loans = LoanRepository.all()
    serializer = LoanSerializer(loans, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_loan(request):
    serializer = LoanSerializer(data=request.data)
    if serializer.is_valid():
        try:
            LoanRepository.create(**serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_loan(request, loan_id):
    try:
        loan = LoanRepository.get(loan_id)
    except Loan.DoesNotExist:
        return Response({'error': 'Loan not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = LoanSerializer(loan, data=request.data)
    if serializer.is_valid():
        try:
            LoanRepository.update(loan_id, **serializer.validated_data)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_loan(request, loan_id):
    try:
        LoanRepository.delete(loan_id)
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Loan.DoesNotExist:
        return Response({'error': 'Loan not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_country(request, country_id):
    try:
        country = CountryRepository.get(country_id)
        serializer = CountrySerializer(country)
        return Response(serializer.data)
    except Country.DoesNotExist:
        return Response({'error': 'Country not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_countries(request):
    countries = CountryRepository.all()
    serializer = CountrySerializer(countries, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_country(request):
    serializer = CountrySerializer(data=request.data)
    if serializer.is_valid():
        try:
            CountryRepository.create(**serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_country(request, country_id):
    try:
        country = CountryRepository.get(country_id)
    except Country.DoesNotExist:
        return Response({'error': 'Country not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = CountrySerializer(country, data=request.data)
    if serializer.is_valid():
        try:
            CountryRepository.update(country_id, **serializer.validated_data)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_country(request, country_id):
    try:
        CountryRepository.delete(country_id)
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Country.DoesNotExist:
        return Response({'error': 'Country not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_publishing_house(request, publishing_house_id):
    try:
        publishing_house = PublishingHouseRepository.get(publishing_house_id)
        serializer = PublishingHouseSerializer(publishing_house)
        return Response(serializer.data)
    except PublishingHouse.DoesNotExist:
        return Response({'error': 'Publishing House not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_publishing_houses(request):
    publishing_houses = PublishingHouseRepository.all()
    serializer = PublishingHouseSerializer(publishing_houses, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_publishing_house(request):
    serializer = PublishingHouseSerializer(data=request.data)
    if serializer.is_valid():
        try:
            PublishingHouseRepository.create(**serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_publishing_house(request, publishing_house_id):
    try:
        publishing_house = PublishingHouseRepository.get(publishing_house_id)
    except PublishingHouse.DoesNotExist:
        return Response({'error': 'Publishing House not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = PublishingHouseSerializer(publishing_house, data=request.data)
    if serializer.is_valid():
        try:
            PublishingHouseRepository.update(publishing_house_id, **serializer.validated_data)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_publishing_house(request, publishing_house_id):
    try:
        PublishingHouseRepository.delete(publishing_house_id)
        return Response(status=status.HTTP_204_NO_CONTENT)
    except PublishingHouse.DoesNotExist:
        return Response({'error': 'Publishing House not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def total_books_per_genre(request):
    genres = GenreRepository.total_books_per_genre()
    return Response(genres)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def avg_pages_per_genre(request):
    genres = GenreRepository.avg_pages_per_genre()
    return Response(genres)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def total_loans_per_genre(request):
    genres = GenreRepository.total_loans_per_genre()
    return Response(genres)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def total_books_per_publishing_house(request):
    publishing_houses = PublishingHouseRepository.total_books_per_publishing_house()
    return Response(publishing_houses)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def total_loans_per_book(request):
    books = BookRepository.total_loans_per_book()
    return Response(books)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def total_loans_per_age_category(request):
    books = BookRepository.total_loans_per_age_category()
    return Response(books)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def total_books_per_year(request):
    books = BookRepository.total_books_per_year()
    return Response(books)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def total_loans_per_reader(request):
    readers = ReaderRepository.total_loans_per_reader()
    return Response(readers)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def count_books_by_author(request):
    authors = AuthorRepository.count_books_by_author()
    return Response(authors)


