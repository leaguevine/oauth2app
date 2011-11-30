# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Client.status'
        db.add_column('oauth2app_client', 'status', self.gf('django.db.models.fields.IntegerField')(default=1), keep_default=False)

        # Adding field 'Client.submitted_by'
        db.add_column('oauth2app_client', 'submitted_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='client_submitted_by', null=True, to=orm['auth.User']), keep_default=False)

        # Adding field 'Client.approved_by'
        db.add_column('oauth2app_client', 'approved_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='client_approved_by', null=True, to=orm['auth.User']), keep_default=False)

        # Adding field 'Client.removed_by'
        db.add_column('oauth2app_client', 'removed_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='client_removed_by', null=True, to=orm['auth.User']), keep_default=False)

        # Adding field 'Client.submitted_time'
        db.add_column('oauth2app_client', 'submitted_time', self.gf('django.db.models.fields.DateTimeField')(db_index=True, null=True, blank=True), keep_default=False)

        # Adding field 'Client.approved_time'
        db.add_column('oauth2app_client', 'approved_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True), keep_default=False)

        # Adding field 'Client.removed_time'
        db.add_column('oauth2app_client', 'removed_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True), keep_default=False)

        # Adding field 'Client.submission_message'
        db.add_column('oauth2app_client', 'submission_message', self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True), keep_default=False)

        # Adding field 'Client.removal_message'
        db.add_column('oauth2app_client', 'removal_message', self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True), keep_default=False)

        # Adding field 'Client.auto_approve'
        db.add_column('oauth2app_client', 'auto_approve', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Client.counts_towards_contributions'
        db.add_column('oauth2app_client', 'counts_towards_contributions', self.gf('django.db.models.fields.BooleanField')(default=True), keep_default=False)

        # Adding field 'Client.real_type'
        db.add_column('oauth2app_client', 'real_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='client_real_type', null=True, to=orm['contenttypes.ContentType']), keep_default=False)

        # Adding index on 'Client', fields ['id']
        db.create_index('oauth2app_client', ['id'])


    def backwards(self, orm):
        
        # Removing index on 'Client', fields ['id']
        db.delete_index('oauth2app_client', ['id'])

        # Deleting field 'Client.status'
        db.delete_column('oauth2app_client', 'status')

        # Deleting field 'Client.submitted_by'
        db.delete_column('oauth2app_client', 'submitted_by_id')

        # Deleting field 'Client.approved_by'
        db.delete_column('oauth2app_client', 'approved_by_id')

        # Deleting field 'Client.removed_by'
        db.delete_column('oauth2app_client', 'removed_by_id')

        # Deleting field 'Client.submitted_time'
        db.delete_column('oauth2app_client', 'submitted_time')

        # Deleting field 'Client.approved_time'
        db.delete_column('oauth2app_client', 'approved_time')

        # Deleting field 'Client.removed_time'
        db.delete_column('oauth2app_client', 'removed_time')

        # Deleting field 'Client.submission_message'
        db.delete_column('oauth2app_client', 'submission_message')

        # Deleting field 'Client.removal_message'
        db.delete_column('oauth2app_client', 'removal_message')

        # Deleting field 'Client.auto_approve'
        db.delete_column('oauth2app_client', 'auto_approve')

        # Deleting field 'Client.counts_towards_contributions'
        db.delete_column('oauth2app_client', 'counts_towards_contributions')

        # Deleting field 'Client.real_type'
        db.delete_column('oauth2app_client', 'real_type_id')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'oauth2app.accessrange': {
            'Meta': {'object_name': 'AccessRange'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'})
        },
        'oauth2app.accesstoken': {
            'Meta': {'object_name': 'AccessToken'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['oauth2app.Client']"}),
            'expire': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1322622769'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1322619169'}),
            'mac_key': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '20', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'refresh_token': ('django.db.models.fields.CharField', [], {'null': 'True', 'default': "'fcd1dbc53d'", 'max_length': '10', 'blank': 'True', 'unique': 'True', 'db_index': 'True'}),
            'refreshable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'scope': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['oauth2app.AccessRange']", 'symmetrical': 'False'}),
            'token': ('django.db.models.fields.CharField', [], {'default': "'514e98eeca'", 'unique': 'True', 'max_length': '10', 'db_index': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'oauth2app.client': {
            'Meta': {'object_name': 'Client'},
            'approved_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'client_approved_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'approved_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'auto_approve': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'counts_towards_contributions': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_index': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'default': "'23ddf19183c63844a0c4a52f3b7ebe'", 'unique': 'True', 'max_length': '30', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'real_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'client_real_type'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'redirect_uri': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'removal_message': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'removed_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'client_removed_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'removed_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'secret': ('django.db.models.fields.CharField', [], {'default': "'4597ce5e6420a3fc9b8901146ab4a9'", 'unique': 'True', 'max_length': '30'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'submission_message': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'submitted_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'client_submitted_by'", 'null': 'True', 'to': "orm['auth.User']"}),
            'submitted_time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'oauth2app.code': {
            'Meta': {'object_name': 'Code'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['oauth2app.Client']"}),
            'expire': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1322619289'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1322619169'}),
            'key': ('django.db.models.fields.CharField', [], {'default': "'da641f127f0f8089bf4c4895409d60'", 'unique': 'True', 'max_length': '30', 'db_index': 'True'}),
            'redirect_uri': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'scope': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['oauth2app.AccessRange']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'oauth2app.macnonce': {
            'Meta': {'object_name': 'MACNonce'},
            'access_token': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['oauth2app.AccessToken']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nonce': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_index': 'True'})
        },
        'trackable_object.editlog': {
            'Meta': {'object_name': 'EditLog'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'edit_message': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'edit_time': ('django.db.models.fields.DateTimeField', [], {}),
            'editted_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {})
        }
    }

    complete_apps = ['oauth2app']
