"""
Core models - Base models and utilities
"""
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class TimeStampedModel(models.Model):
    """
    Abstract base class with created_at and updated_at fields
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class SoftDeleteModel(models.Model):
    """
    Abstract base class for soft delete functionality
    """
    is_active = models.BooleanField(default=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    def delete(self, using=None, keep_parents=False):
        """Soft delete - marca como inativo ao invés de deletar"""
        self.is_active = False
        self.deleted_at = timezone.now()
        self.save()
    
    def hard_delete(self):
        """Delete permanente do banco de dados"""
        super().delete()
    
    class Meta:
        abstract = True


class AuditModel(TimeStampedModel):
    """
    Abstract base class with audit fields
    """
    created_by = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='%(class)s_created'
    )
    updated_by = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='%(class)s_updated'
    )
    
    class Meta:
        abstract = True
