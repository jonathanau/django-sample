from django.db import models

from southtut3.fields import TagField, UpperCaseField


class Foo(models.Model):
  my_field = TagField()
  my_otherfield = UpperCaseField()
