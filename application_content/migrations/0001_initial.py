# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-25 19:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Leagues',
            fields=[
                ('league_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('league_name', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'leagues',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LearningVectors',
            fields=[
                ('match_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('league_id', models.BigIntegerField(blank=True, null=True)),
                ('season', models.TextField(blank=True, null=True)),
                ('stage', models.BigIntegerField(blank=True, null=True)),
                ('date', models.TextField(blank=True, null=True)),
                ('h_team', models.TextField(blank=True, null=True)),
                ('a_team', models.TextField(blank=True, null=True)),
                ('result', models.BigIntegerField(blank=True, null=True)),
                ('b365h', models.FloatField(blank=True, null=True)),
                ('b365d', models.FloatField(blank=True, null=True)),
                ('b365a', models.FloatField(blank=True, null=True)),
                ('h_speed', models.BigIntegerField(blank=True, null=True)),
                ('h_pass', models.BigIntegerField(blank=True, null=True)),
                ('h_shoot', models.BigIntegerField(blank=True, null=True)),
                ('h_pressure', models.BigIntegerField(blank=True, null=True)),
                ('h_chpass', models.BigIntegerField(blank=True, null=True)),
                ('h_chcross', models.BigIntegerField(blank=True, null=True)),
                ('h_daggr', models.BigIntegerField(blank=True, null=True)),
                ('h_dwidth', models.BigIntegerField(blank=True, null=True)),
                ('a_speed', models.BigIntegerField(blank=True, null=True)),
                ('a_pass', models.BigIntegerField(blank=True, null=True)),
                ('a_shoot', models.BigIntegerField(blank=True, null=True)),
                ('a_pressure', models.BigIntegerField(blank=True, null=True)),
                ('a_chpass', models.BigIntegerField(blank=True, null=True)),
                ('a_chcross', models.BigIntegerField(blank=True, null=True)),
                ('a_daggr', models.BigIntegerField(blank=True, null=True)),
                ('a_dwidth', models.BigIntegerField(blank=True, null=True)),
                ('h_age', models.FloatField(blank=True, null=True)),
                ('a_age', models.FloatField(blank=True, null=True)),
                ('h_tmv', models.FloatField(blank=True, null=True)),
                ('a_tmv', models.FloatField(blank=True, null=True)),
                ('h_form05', models.BigIntegerField(blank=True, null=True)),
                ('a_form05', models.BigIntegerField(blank=True, null=True)),
                ('h_form03', models.BigIntegerField(blank=True, null=True)),
                ('a_form03', models.BigIntegerField(blank=True, null=True)),
                ('fthg', models.FloatField(blank=True, null=True)),
                ('ftag', models.FloatField(blank=True, null=True)),
                ('hs', models.FloatField(blank=True, null=True)),
                ('as_field', models.FloatField(blank=True, db_column='as', null=True)),
                ('hst', models.FloatField(blank=True, null=True)),
                ('ast', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'learning_vectors',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Matches',
            fields=[
                ('match_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('league_id', models.BigIntegerField(blank=True, null=True)),
                ('season', models.TextField(blank=True, null=True)),
                ('stage', models.BigIntegerField(blank=True, null=True)),
                ('date', models.TextField(blank=True, null=True)),
                ('h_team', models.TextField(blank=True, null=True)),
                ('a_team', models.TextField(blank=True, null=True)),
                ('result', models.BigIntegerField(blank=True, null=True)),
                ('h_age', models.FloatField(blank=True, null=True)),
                ('a_age', models.FloatField(blank=True, null=True)),
                ('h_tmv', models.FloatField(blank=True, null=True)),
                ('a_tmv', models.FloatField(blank=True, null=True)),
                ('h_form05', models.BigIntegerField(blank=True, null=True)),
                ('a_form05', models.BigIntegerField(blank=True, null=True)),
                ('h_form03', models.BigIntegerField(blank=True, null=True)),
                ('a_form03', models.BigIntegerField(blank=True, null=True)),
                ('h_meanshotsontarget05', models.FloatField(blank=True, null=True)),
                ('a_meanshotsontarget05', models.FloatField(blank=True, null=True)),
                ('h_meanfulltimegoals05', models.FloatField(blank=True, null=True)),
                ('a_meanfulltimegoals05', models.FloatField(blank=True, null=True)),
                ('cart_res', models.IntegerField(blank=True, null=True)),
                ('nb_res', models.IntegerField(blank=True, null=True)),
                ('svm_res', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'matches',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SocialAuthAssociation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server_url', models.CharField(max_length=255)),
                ('handle', models.CharField(max_length=255)),
                ('secret', models.CharField(max_length=255)),
                ('issued', models.IntegerField()),
                ('lifetime', models.IntegerField()),
                ('assoc_type', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'social_auth_association',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SocialAuthCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=254)),
                ('code', models.CharField(max_length=32)),
                ('verified', models.BooleanField()),
            ],
            options={
                'db_table': 'social_auth_code',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SocialAuthNonce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server_url', models.CharField(max_length=255)),
                ('timestamp', models.IntegerField()),
                ('salt', models.CharField(max_length=65)),
            ],
            options={
                'db_table': 'social_auth_nonce',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SocialAuthPartial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=32)),
                ('next_step', models.SmallIntegerField()),
                ('backend', models.CharField(max_length=32)),
                ('data', models.TextField()),
            ],
            options={
                'db_table': 'social_auth_partial',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SocialAuthUsersocialauth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider', models.CharField(max_length=32)),
                ('uid', models.CharField(max_length=255)),
                ('extra_data', models.TextField()),
            ],
            options={
                'db_table': 'social_auth_usersocialauth',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('team_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'teams',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TeamsNamesMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'teams_names_mapping',
                'managed': False,
            },
        ),
    ]
