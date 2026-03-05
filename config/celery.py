"""
Celery configuration for OdontoInsight project.
"""
import os
from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('odontoinsight')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

# Periodic tasks schedule
app.conf.beat_schedule = {
    # Análise diária de desperdício de materiais
    'analyze-material-waste-daily': {
        'task': 'apps.analytics.tasks.analyze_material_waste',
        'schedule': crontab(hour=1, minute=0),  # 1:00 AM diariamente
    },
    # Previsão de déficit mensal (toda segunda-feira)
    'predict-monthly-deficit': {
        'task': 'apps.analytics.tasks.predict_monthly_deficit',
        'schedule': crontab(day_of_week=1, hour=6, minute=0),  # Segundas às 6:00 AM
    },
    # Análise de risco de churn de pacientes (toda semana)
    'analyze-patient-churn': {
        'task': 'apps.analytics.tasks.analyze_patient_churn',
        'schedule': crontab(day_of_week=0, hour=7, minute=0),  # Domingos às 7:00 AM
    },
    # Automação de recuperação de pacientes inativos (toda terça e quinta)
    'recover-inactive-patients': {
        'task': 'apps.automation.tasks.recover_inactive_patients',
        'schedule': crontab(day_of_week='2,4', hour=9, minute=0),  # Terças e quintas às 9:00 AM
    },
}

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
