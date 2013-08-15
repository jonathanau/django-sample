from django.db import models

from south.modelsinspector import add_introspection_rules


class TagField(models.TextField):
  description = "Stores tags in a single database column."

  __metaclass__ = models.SubfieldBase


  def __init__(self, delimeter="|", *args, **kwargs):
    self.delimeter = delimeter
    super(TagField, self).__init__(*args, **kwargs)


  def to_python(self, value):
    # If it's already in a list, leave it
    if isinstance(value, list):
      return value

    # Otherwise, split by delimeter
    return value.split(self.delimeter)


  def get_prep_value(self, value):
    return self.delimeter.join(value)


add_introspection_rules([
  (
    [TagField],  # Class(es) these apply to
    [],          # Positional arguments
    {
      "delimeter": ["delimeter", {"default": "|"}],
    },
  ),
], ["^southtut3\.fields\.TagField"])


class UpperCaseField(models.TextField):
  "Makes sure its content is always upper-case."

  def to_python(self, value):
    return value.upper()

  def get_prep_value(self, value):
    return value.upper()


add_introspection_rules([], ["^southtut3\.fields\.UpperCaseField"])
