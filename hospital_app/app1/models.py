from django.db import models

# Create your models here.


class HospitalInfo(models.Model):
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
    recovery_bed_num = models.IntegerField()
    regional_care_bed_num = models.IntegerField()
    mental_bed_num = models.IntegerField()
    recuperation_bed_num = models.IntegerField()
    tuberculosis_bed_num = models.IntegerField()
    bed_number = models.IntegerField()
    public_month = models.IntegerField()


class PostalCode(models.Model):
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

