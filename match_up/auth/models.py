# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Rank(models.Model):
	id = models.IntegerField(primary_key=True)
	user_id = models.IntegerField()
	score_total = models.IntegerField()
	score_nhl = models.IntegerField()
	score_nba = models.IntegerField()
	class Meta:
		db_table = u'Rank'

class Schedule(models.Model):
	id = models.IntegerField(primary_key=True)
	game_id = models.IntegerField(unique=True)
	league = models.CharField(unique=True, max_length=30)
	time = models.CharField(max_length=90)
	status = models.CharField(max_length=90)
	home_team = models.CharField(unique=True, max_length=150)
	home_score = models.IntegerField()
	away_team = models.CharField(unique=True, max_length=150)
	away_score = models.IntegerField()
	winner = models.CharField(max_length=90)
	class Meta:
		db_table = u'Schedule'

class UserPicks(models.Model):
	id = models.IntegerField(primary_key=True)
	user_id = models.IntegerField()
	game_id = models.IntegerField()
	league = models.CharField(max_length=90)
	user_pick = models.CharField(max_length=90)
	home_team = models.CharField(max_length=90)
	away_team = models.CharField(max_length=90)
	winner = models.CharField(max_length=90)
	points = models.IntegerField()
	class Meta:
		db_table = u'User_picks'

class Users(models.Model):
	id = models.IntegerField(primary_key=True)
	user_id = models.IntegerField()
	username = models.CharField(max_length=60)
	email = models.CharField(max_length=90)
	password = models.CharField(max_length=255)
	score_total = models.IntegerField()
	score_nhl = models.IntegerField()
	score_nba = models.IntegerField()
	class Meta:
		db_table = u'Users'

# class AuthGroup(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(unique=True, max_length=240)
#     class Meta:
#         db_table = u'auth_group'

# class AuthGroupPermissions(models.Model):
#     id = models.IntegerField(primary_key=True)
#     group_id = models.IntegerField()
#     permission_id = models.IntegerField()
#     class Meta:
#         db_table = u'auth_group_permissions'

# class AuthMessage(models.Model):
#     id = models.IntegerField(primary_key=True)
#     user_id = models.IntegerField()
#     message = models.TextField()
#     class Meta:
#         db_table = u'auth_message'

# class AuthPermission(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=150)
#     content_type_id = models.IntegerField()
#     codename = models.CharField(unique=True, max_length=255)
#     class Meta:
#         db_table = u'auth_permission'

# class AuthUser(models.Model):
#     id = models.IntegerField(primary_key=True)
#     username = models.CharField(unique=True, max_length=90)
#     first_name = models.CharField(max_length=90)
#     last_name = models.CharField(max_length=90)
#     email = models.CharField(max_length=225)
#     password = models.CharField(max_length=384)
#     is_staff = models.IntegerField()
#     is_active = models.IntegerField()
#     is_superuser = models.IntegerField()
#     last_login = models.DateTimeField()
#     date_joined = models.DateTimeField()
#     class Meta:
#         db_table = u'auth_user'

# class AuthUserGroups(models.Model):
#     id = models.IntegerField(primary_key=True)
#     user_id = models.IntegerField()
#     group_id = models.IntegerField()
#     class Meta:
#         db_table = u'auth_user_groups'

# class AuthUserUserPermissions(models.Model):
#     id = models.IntegerField(primary_key=True)
#     user_id = models.IntegerField()
#     permission_id = models.IntegerField()
#     class Meta:
#         db_table = u'auth_user_user_permissions'

# class DjangoAdminLog(models.Model):
#     id = models.IntegerField(primary_key=True)
#     action_time = models.DateTimeField()
#     user_id = models.IntegerField()
#     content_type_id = models.IntegerField(null=True, blank=True)
#     object_id = models.TextField(blank=True)
#     object_repr = models.CharField(max_length=255)
#     action_flag = models.IntegerField()
#     change_message = models.TextField()
#     class Meta:
#         db_table = u'django_admin_log'

# class DjangoContentType(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=255)
#     app_label = models.CharField(unique=True, max_length=255)
#     model = models.CharField(unique=True, max_length=255)
#     class Meta:
#         db_table = u'django_content_type'

# class DjangoSession(models.Model):
#     session_key = models.CharField(max_length=120, primary_key=True)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()
#     class Meta:
#         db_table = u'django_session'

# class HomeUsers(models.Model):
#     id = models.IntegerField(primary_key=True)
#     username = models.CharField(max_length=60)
#     class Meta:
#         db_table = u'home_users'

