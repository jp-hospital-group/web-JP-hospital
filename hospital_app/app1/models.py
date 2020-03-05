# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class App1Hospitalinfo(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    serial_id = models.CharField(max_length=5)
    serial_id_last = models.CharField(max_length=5)
    public_year = models.IntegerField()
    city_id = models.CharField(max_length=5)
    hospital_name = models.CharField(max_length=500)
    hospital_type = models.CharField(max_length=50)
    dpc_bed_calcu = models.IntegerField()
    hospital_charge_type = models.CharField(max_length=50)
    dpc_bed_rate = models.FloatField()
    recovery_bed_num = models.IntegerField()
    regional_care_bed_num = models.IntegerField()
    mental_bed_num = models.IntegerField()
    recuperation_bed_num = models.IntegerField()
    tuberculosis_bed_num = models.IntegerField()
    bed_number = models.IntegerField()
    public_month = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'app1_hospitalinfo'


class App1Postalcode(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    city_cd = models.CharField(max_length=5)
    postal_cd_old = models.CharField(max_length=5)
    postal_cd = models.CharField(max_length=7)
    prefecture_name_kana = models.CharField(max_length=50)
    city_name_kana = models.CharField(max_length=50)
    cyo_name_kana = models.CharField(max_length=50)
    prefecture_name = models.CharField(max_length=50)
    city_name = models.CharField(max_length=50)
    cyo_name = models.CharField(max_length=50)
    multi_postal_per_cyo = models.IntegerField()
    have_small_ban = models.IntegerField()
    have_cyome = models.IntegerField()
    multi_cyo_per_postal = models.IntegerField()
    update_flg = models.IntegerField()
    reason_flg = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'app1_postalcode'

# ---------------------------------------
# Create Database View Model
#
# ---------------------------------------


class ViewHospitalInfo(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    serial_id = models.CharField(max_length=5)
    serial_id_last = models.CharField(max_length=5)
    public_year = models.IntegerField()
    city_id = models.CharField(max_length=5)
    hospital_name = models.CharField(max_length=500)
    hospital_type = models.CharField(max_length=50)
    dpc_bed_calcu = models.IntegerField()
    hospital_charge_type = models.CharField(max_length=50)
    dpc_bed_rate = models.FloatField()
    recovery_bed_num = models.IntegerField()
    regional_care_bed_num = models.IntegerField()
    mental_bed_num = models.IntegerField()
    recuperation_bed_num = models.IntegerField()
    tuberculosis_bed_num = models.IntegerField()
    bed_number = models.IntegerField()
    public_month = models.IntegerField()
    prefecture_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'v_hospital_info'


# ---------------------------------------
# Admin Table Model
#
# ---------------------------------------

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    last_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
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



