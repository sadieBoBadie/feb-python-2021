from django.db import models

# Create your models here.

class State(models.Model):
    name = models.CharField(max_length=45)
    abbrev = models.CharField(max_length=2)
    population = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # cities

    def __repr__(self):
        return f"State: {self.abbrev}"

class City(models.Model):
    name = models.CharField(max_length=45)
    population = models.IntegerField()
    state = models.ForeignKey(State, related_name="cities", on_delete=models.)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

california = State.objects.create(name="California", abbrev="CA", population=20)
sd = City.objects.create(name="San Diego", population=12, state=california)

print(sd.state.name)

california.cities.all()