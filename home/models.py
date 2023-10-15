from django.db import models



class H1BApplicant(models.Model):
    CASE_NUMBER = models.CharField(max_length=255)
    PREVAILING_WAGE = models.DecimalField(max_digits=10, decimal_places=2)
    PW_UNIT_OF_PAY = models.CharField(max_length = 255)

    def __str__(self):
        return self.
