# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import ArrayField

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Leagues(models.Model):
    league_id = models.BigIntegerField(primary_key=True)
    league_name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'leagues'


class LearningVectors(models.Model):
    match_id = models.BigIntegerField(primary_key=True)
    league_id = models.BigIntegerField(blank=True, null=True)
    season = models.TextField(blank=True, null=True)
    stage = models.BigIntegerField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    h_team = models.TextField(blank=True, null=True)
    a_team = models.TextField(blank=True, null=True)
    result = models.BigIntegerField(blank=True, null=True)
    b365h = models.FloatField(blank=True, null=True)
    b365d = models.FloatField(blank=True, null=True)
    b365a = models.FloatField(blank=True, null=True)
    h_speed = models.BigIntegerField(blank=True, null=True)
    h_pass = models.BigIntegerField(blank=True, null=True)
    h_shoot = models.BigIntegerField(blank=True, null=True)
    h_pressure = models.BigIntegerField(blank=True, null=True)
    h_chpass = models.BigIntegerField(blank=True, null=True)
    h_chcross = models.BigIntegerField(blank=True, null=True)
    h_daggr = models.BigIntegerField(blank=True, null=True)
    h_dwidth = models.BigIntegerField(blank=True, null=True)
    a_speed = models.BigIntegerField(blank=True, null=True)
    a_pass = models.BigIntegerField(blank=True, null=True)
    a_shoot = models.BigIntegerField(blank=True, null=True)
    a_pressure = models.BigIntegerField(blank=True, null=True)
    a_chpass = models.BigIntegerField(blank=True, null=True)
    a_chcross = models.BigIntegerField(blank=True, null=True)
    a_daggr = models.BigIntegerField(blank=True, null=True)
    a_dwidth = models.BigIntegerField(blank=True, null=True)
    h_age = models.FloatField(blank=True, null=True)
    a_age = models.FloatField(blank=True, null=True)
    h_tmv = models.FloatField(blank=True, null=True)
    a_tmv = models.FloatField(blank=True, null=True)
    h_form05 = models.BigIntegerField(blank=True, null=True)
    a_form05 = models.BigIntegerField(blank=True, null=True)
    h_form03 = models.BigIntegerField(blank=True, null=True)
    a_form03 = models.BigIntegerField(blank=True, null=True)
    fthg = models.FloatField(blank=True, null=True)
    ftag = models.FloatField(blank=True, null=True)
    hs = models.FloatField(blank=True, null=True)
    as_field = models.FloatField(db_column='as', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    hst = models.FloatField(blank=True, null=True)
    ast = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'learning_vectors'


class Matches(models.Model):
    match_id = models.BigAutoField(primary_key=True)
    league_id = models.BigIntegerField(blank=True, null=True)
    season = models.TextField(blank=True, null=True)
    stage = models.BigIntegerField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    h_team = models.TextField(blank=True, null=True)
    a_team = models.TextField(blank=True, null=True)
    result = models.BigIntegerField(blank=True, null=True)
    h_age = models.FloatField(blank=True, null=True)
    a_age = models.FloatField(blank=True, null=True)
    h_tmv = models.FloatField(blank=True, null=True)
    a_tmv = models.FloatField(blank=True, null=True)
    h_form05 = models.BigIntegerField(blank=True, null=True)
    a_form05 = models.BigIntegerField(blank=True, null=True)
    h_form03 = models.BigIntegerField(blank=True, null=True)
    a_form03 = models.BigIntegerField(blank=True, null=True)
    h_meanshotsontarget05 = models.FloatField(blank=True, null=True)
    a_meanshotsontarget05 = models.FloatField(blank=True, null=True)
    h_meanfulltimegoals05 = models.FloatField(blank=True, null=True)
    a_meanfulltimegoals05 = models.FloatField(blank=True, null=True)
    cart_res = models.IntegerField(blank=True, null=True)
    nb_res = models.IntegerField(blank=True, null=True)
    svm_res = models.IntegerField(blank=True, null=True)
    cart_proba = ArrayField(models.FloatField(blank=True, null=True),
                            size = 3)
    nb_proba = ArrayField(models.FloatField(blank=True, null=True),
                         size = 3)
    svm_proba = ArrayField(models.FloatField(blank=True, null=True),
                           size = 3)

    class Meta:
        managed = False
        db_table = 'matches'


class SocialAuthAssociation(models.Model):
    server_url = models.CharField(max_length=255)
    handle = models.CharField(max_length=255)
    secret = models.CharField(max_length=255)
    issued = models.IntegerField()
    lifetime = models.IntegerField()
    assoc_type = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'social_auth_association'
        unique_together = (('server_url', 'handle'),)


class SocialAuthCode(models.Model):
    email = models.CharField(max_length=254)
    code = models.CharField(max_length=32)
    verified = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'social_auth_code'
        unique_together = (('email', 'code'),)


class SocialAuthNonce(models.Model):
    server_url = models.CharField(max_length=255)
    timestamp = models.IntegerField()
    salt = models.CharField(max_length=65)

    class Meta:
        managed = False
        db_table = 'social_auth_nonce'
        unique_together = (('server_url', 'timestamp', 'salt'),)


class SocialAuthPartial(models.Model):
    token = models.CharField(max_length=32)
    next_step = models.SmallIntegerField()
    backend = models.CharField(max_length=32)
    data = models.TextField()

    class Meta:
        managed = False
        db_table = 'social_auth_partial'


class SocialAuthUsersocialauth(models.Model):
    provider = models.CharField(max_length=32)
    uid = models.CharField(max_length=255)
    extra_data = models.TextField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'social_auth_usersocialauth'
        unique_together = (('provider', 'uid'),)


class Teams(models.Model):
    team_id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teams'


class TeamsNamesMapping(models.Model):
    team = models.ForeignKey(Teams, models.DO_NOTHING, blank=True, null=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teams_names_mapping'
