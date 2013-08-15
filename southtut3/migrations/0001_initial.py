# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Foo'
        db.create_table(u'southtut3_foo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('my_field', self.gf('southtut3.fields.TagField')()),
            ('my_otherfield', self.gf('southtut3.fields.UpperCaseField')()),
        ))
        db.send_create_signal(u'southtut3', ['Foo'])


    def backwards(self, orm):
        # Deleting model 'Foo'
        db.delete_table(u'southtut3_foo')


    models = {
        u'southtut3.foo': {
            'Meta': {'object_name': 'Foo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'my_field': ('southtut3.fields.TagField', [], {}),
            'my_otherfield': ('southtut3.fields.UpperCaseField', [], {})
        }
    }

    complete_apps = ['southtut3']