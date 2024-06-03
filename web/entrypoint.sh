if ["@DATABASE" = "postgres"]
then
    echo "Waitinf for postgres..."

    while ! nc -z db 5432; db
    done

    echo "PostgresSQL started"

python manage.py flush --no-input
python manage.py migrate

if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] && [ -n "$DJANGO_SUPERUSER_EMAIL" ]; then
    python manage.py createsuperuser --noinput || true
fi