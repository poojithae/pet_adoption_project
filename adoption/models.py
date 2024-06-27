from django.db import models

# Create your models here.
class pet(models.Model):
    SPECIES_CHOICES = [
        ('DOG', 'Dog'),
        ('CAT', 'Cat'),
        ('BIRD', 'Bird'),
        ('RABBIT', 'Rabbit'),
    ]

    name = models.CharField(max_length=100)
    species = models.CharField(max_length=10, choices=SPECIES_CHOICES)
    breed = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    available_for_adoption = models.BooleanField(default=True)


#defines instances of pet class and returns the name of the pet
    def __str__(self):
        return self.name
    





#class AdoptedPet(models.Model):
 #   pet = models.OneToOneField(Pet, on_delete=models.CASCADE)
  #  adopted_by = models.CharField(max_length=100)
   # adoption_date = models.DateField(auto_now_add=True)
    #special_requirements = models.TextField(blank=True)

    #def __str__(self):
     #   return f"{self.pet.name} - Adopted by {self.adopted_by}"



