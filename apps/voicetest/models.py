from django.db import models

class Project_Number(models.Model):
    emoji = models.CharField(max_length=100, blank=True)
    client_number = models.IntegerField(null=True, blank=True)
    tag = models.CharField(max_length=100, blank=True)
    
class Resume(models.Model):
    education_sub = models.CharField(max_length=255, blank=True)
    education_institution = models.CharField(max_length=255, blank=True)
    education_degree = models.CharField(max_length=255, blank=True)
    education_year = models.CharField(max_length=255, blank=True)
    
class ProfessionalExperience(models.Model):
    job_title = models.CharField(max_length=255, blank=True)
    company_name = models.CharField(max_length=255, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    responsibilities = models.TextField(blank=True)
    
class Services(models.Model):
    service_name = models.CharField(max_length=255, blank=True)
    service_description = models.TextField(blank=True)
    service_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
class Testimonial(models.Model):
    client_name = models.CharField(max_length=255, blank=True)
    testimonial_text = models.TextField(blank=True)
    rating = models.IntegerField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)

class Profile(models.Model):
    name = models.CharField(max_length=100)
    social_links = models.JSONField(default=dict, blank=True)
    about_me = models.TextField(blank=True)
    about_me_intro = models.CharField(max_length=255, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    website = models.URLField(blank=True)
    phone_number = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    degree = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=254)
    about_me_description = models.TextField(blank=True)
    project_number = models.ForeignKey(Project_Number, on_delete=models.CASCADE, null=True, blank=True, related_name='profiles')
    skill_que = models.CharField(max_length=255, blank=True)
    skill_ans = models.CharField(max_length=255, blank=True)
    skill_progress = models.IntegerField(default=0, blank=True)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, null=True, blank=True, related_name='profiles')
    professional_experience = models.ForeignKey(ProfessionalExperience, on_delete=models.CASCADE, null=True, blank=True, related_name='profiles')
    portfolio_text = models.TextField(blank=True)
    services_text = models.TextField(blank=True)
    service = models.ForeignKey(Services, on_delete=models.CASCADE, null=True, blank=True, related_name='profiles')
    testimonial_text = models.TextField(blank=True)
    testimonial = models.ForeignKey(Testimonial, on_delete=models.CASCADE, null=True, blank=True, related_name='profiles')
    
    
