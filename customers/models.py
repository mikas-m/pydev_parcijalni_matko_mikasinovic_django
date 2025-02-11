from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=100)
    vat_id = models.IntegerField()
    street = models.TextField()
    city = models.TextField()
    country = models.TextField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """
        Overrides the save method to include any custom logic.
        Django automatically handles insert/update based on whether the instance has a primary key.
        """
        super().save(*args, **kwargs)

    @classmethod
    def from_tuple(cls, data):
        """
        Creates a Customer instance from a tuple.
        Args:
            data (tuple): A tuple containing (name, vat_id, street, city and country).
        Returns:
            Customer: An instance of Customer.
        """
        return cls(name=data[0], vat_id=data[1], street=data[2], city=data[3], country=data[4])

    @classmethod
    def get_all(cls):
        """
        Retrieves all Customer instances from the database.
        Returns:
            QuerySet: A QuerySet containing all Customer objects.
        """
        return cls.objects.all()
    