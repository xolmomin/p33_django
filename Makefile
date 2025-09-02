celery:
	celery -A root worker -l INFO

celery-beat:
	celery -A root beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler