from django.contrib import admin
from refugee.models import refugge, hotspot, citizenships, sex, skills, marital_status, destination_country


@admin.register(refugge)
class refuggeAdmin(admin.ModelAdmin):
    """
    """
    list_display = (
        'id', 'case_number', 'first_name', 'last_name', 'father_name', 'mother_name', 'date_of_birth',
        'asylum_request', 'email_address', 'last_updated', 'created',
    )
    search_fields = (
        'first_name', 'last_name', 'father_name', 'mother_name', 'asylum_request', 'email_address',
    )
    autocomplete_fields = (
        'hotspot_code', 'citizenship_code', 'sex_code', 'skills', 'marital_status_code', 'destination_country_code',
    )

@admin.register(hotspot)
class hotspotAdmin(admin.ModelAdmin):
    """
    """
    list_display = (
        'id', 'hotspot_code', 'hotspot_location', 'hotspot_capacity',
    )
    search_fields = (
        'hotspot_location',
    )
    

@admin.register(citizenships)
class citizenshipsAdmin(admin.ModelAdmin):
    """
    """
    list_display = (
        'id', 'citizenship_code', 'citizenship_country',
    )
    search_fields = (
        'citizenship_country',
    )
    

@admin.register(sex)
class sexAdmin(admin.ModelAdmin):
    """
    """
    list_display = (
        'id', 'sex_code',
    )
    search_fields = (
        'sex_code',
    )
    

@admin.register(skills)
class skillsAdmin(admin.ModelAdmin):
    """
    """
    list_display = (
        'id', 'skill_code', 'skill_description',
    )
    search_fields = (
        'skill_description',
    )
    

@admin.register(marital_status)
class marital_statusAdmin(admin.ModelAdmin):
    """
    """
    list_display = (
        'id', 'marital_status_code', 'no_of_children', 'marital_status_description',
    )
    search_fields = (
        'marital_status_description',
    )
    

@admin.register(destination_country)
class destination_countryAdmin(admin.ModelAdmin):
    """
    """
    list_display = (
        'id', 'destination_country_code', 'destination_country_description',
    )
    search_fields = (
        'destination_country_description',
    )
    
