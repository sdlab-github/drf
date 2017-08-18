from django.db import models


class City(models.Model):
    c_id = models.AutoField(db_column='C_ID', primary_key=True)  # Field name made lowercase.
    cityname = models.CharField(db_column='CityName', max_length=10)  # Field name made lowercase.
    l = models.ForeignKey('Location', models.DO_NOTHING, db_column='L_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'City'


class Flowobservatory(models.Model):
    fo_id = models.AutoField(db_column='FO_ID', primary_key=True)  # Field name made lowercase.
    c = models.ForeignKey(City, models.DO_NOTHING, db_column='C_ID', blank=True, null=True)  # Field name made lowercase.
    basinidentifier = models.CharField(db_column='BasinIdentifier', max_length=10, blank=True, null=True)  # Field name made lowercase.
    observatoryname = models.CharField(db_column='ObservatoryName', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FlowObservatory'


class Forecast(models.Model):
    f_id = models.AutoField(db_column='F_ID', primary_key=True)  # Field name made lowercase.
    l = models.ForeignKey('Location', models.DO_NOTHING, db_column='L_ID', blank=True, null=True)  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='TimeStamp', blank=True, null=True)  # Field name made lowercase.
    elementvalue = models.CharField(db_column='ElementValue', max_length=10, blank=True, null=True)  # Field name made lowercase.
    forecastp = models.FloatField(db_column='ForecastP', blank=True, null=True)  # Field name made lowercase.
    forecastt = models.FloatField(db_column='ForecastT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Forecast'


class Forecastingtime(models.Model):
    ft_id = models.AutoField(db_column='FT_ID', primary_key=True)  # Field name made lowercase.
    forecastingtime = models.DateTimeField(db_column='ForecastingTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ForecastingTime'


class Irrigationarea(models.Model):
    irr_id = models.AutoField(db_column='IRR_ID', primary_key=True)  # Field name made lowercase.
    irrigationname = models.CharField(db_column='IrrigationName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    irrigationarea = models.FloatField(db_column='IrrigationArea', blank=True, null=True)  # Field name made lowercase.
    fallow = models.IntegerField(db_column='Fallow', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IrrigationArea'


class Irrigationwaterdemand(models.Model):
    iwd_id = models.AutoField(db_column='IWD_ID', primary_key=True)  # Field name made lowercase.
    r = models.ForeignKey('Reservoir', models.DO_NOTHING, db_column='R_ID', blank=True, null=True)  # Field name made lowercase.
    irrigationwaterdemand_1 = models.FloatField(db_column='IrrigationWaterDemand_1', blank=True, null=True)  # Field name made lowercase.
    irrigationwaterdemand_2 = models.FloatField(db_column='IrrigationWaterDemand_2', blank=True, null=True)  # Field name made lowercase.
    irrigationwaterdemand_3 = models.FloatField(db_column='IrrigationWaterDemand_3', blank=True, null=True)  # Field name made lowercase.
    irrigationwaterdemand_4 = models.FloatField(db_column='IrrigationWaterDemand_4', blank=True, null=True)  # Field name made lowercase.
    irrigationwaterdemand_5 = models.FloatField(db_column='IrrigationWaterDemand_5', blank=True, null=True)  # Field name made lowercase.
    irrigationwaterdemand_6 = models.FloatField(db_column='IrrigationWaterDemand_6', blank=True, null=True)  # Field name made lowercase.
    irrigationwaterdemand_7 = models.FloatField(db_column='IrrigationWaterDemand_7', blank=True, null=True)  # Field name made lowercase.
    irrigationwaterdemand_8 = models.FloatField(db_column='IrrigationWaterDemand_8', blank=True, null=True)  # Field name made lowercase.
    irrigationwaterdemand_9 = models.FloatField(db_column='IrrigationWaterDemand_9', blank=True, null=True)  # Field name made lowercase.
    irrigationwaterdemand_10 = models.FloatField(db_column='IrrigationWaterDemand_10', blank=True, null=True)  # Field name made lowercase.
    irrigationwaterdemand_11 = models.FloatField(db_column='IrrigationWaterDemand_11', blank=True, null=True)  # Field name made lowercase.
    irrigationwaterdemand_12 = models.FloatField(db_column='IrrigationWaterDemand_12', blank=True, null=True)  # Field name made lowercase.
    irrigationwaterdemand_13 = models.FloatField(db_column='IrrigationWaterDemand_13', blank=True, null=True)  # Field name made lowercase.
    irrigationwaterdemand_14 = models.FloatField(db_column='IrrigationWaterDemand_14', blank=True, null=True)  # Field name made lowercase.
    irrigationwaterdemand_15 = models.FloatField(db_column='IrrigationWaterDemand_15', blank=True, null=True)  # Field name made lowercase.
    irrigationwaterdemand_16 = models.FloatField(db_column='IrrigationWaterDemand_16', blank=True, null=True)  # Field name made lowercase.
    irrigationwaterdemand_17 = models.FloatField(db_column='IrrigationWaterDemand_17', blank=True, null=True)  # Field name made lowercase.
    irrigationwaterdemand_18 = models.FloatField(db_column='IrrigationWaterDemand_18', blank=True, null=True)  # Field name made lowercase.
    irrigationwaterdemand_19 = models.FloatField(db_column='IrrigationWaterDemand_19', blank=True, null=True)  # Field name made lowercase.
    irrigationwaterdemand_20 = models.FloatField(db_column='IrrigationWaterDemand_20', blank=True, null=True)  # Field name made lowercase.
    irrigationwaterdemand_21 = models.FloatField(db_column='IrrigationWaterDemand_21', blank=True, null=True)  # Field name made lowercase.
    irrigationwaterdemand_22 = models.FloatField(db_column='IrrigationWaterDemand_22', blank=True, null=True)  # Field name made lowercase.
    irrigationwaterdemand_23 = models.FloatField(db_column='IrrigationWaterDemand_23', blank=True, null=True)  # Field name made lowercase.
    irrigationwaterdemand_24 = models.FloatField(db_column='IrrigationWaterDemand_24', blank=True, null=True)  # Field name made lowercase.
    irrigationwaterdemand_25 = models.FloatField(db_column='IrrigationWaterDemand_25', blank=True, null=True)  # Field name made lowercase.
    irrigationwaterdemand_26 = models.FloatField(db_column='IrrigationWaterDemand_26', blank=True, null=True)  # Field name made lowercase.
    irrigationwaterdemand_27 = models.FloatField(db_column='IrrigationWaterDemand_27', blank=True, null=True)  # Field name made lowercase.
    irrigationwaterdemand_28 = models.FloatField(db_column='IrrigationWaterDemand_28', blank=True, null=True)  # Field name made lowercase.
    irrigationwaterdemand_29 = models.FloatField(db_column='IrrigationWaterDemand_29', blank=True, null=True)  # Field name made lowercase.
    irrigationwaterdemand_30 = models.FloatField(db_column='IrrigationWaterDemand_30', blank=True, null=True)  # Field name made lowercase.
    irrigationwaterdemand_31 = models.FloatField(db_column='IrrigationWaterDemand_31', blank=True, null=True)  # Field name made lowercase.
    irrigationwaterdemand_32 = models.FloatField(db_column='IrrigationWaterDemand_32', blank=True, null=True)  # Field name made lowercase.
    irrigationwaterdemand_33 = models.FloatField(db_column='IrrigationWaterDemand_33', blank=True, null=True)  # Field name made lowercase.
    irrigationwaterdemand_34 = models.FloatField(db_column='IrrigationWaterDemand_34', blank=True, null=True)  # Field name made lowercase.
    irrigationwaterdemand_35 = models.FloatField(db_column='IrrigationWaterDemand_35', blank=True, null=True)  # Field name made lowercase.
    irrigationwaterdemand_36 = models.FloatField(db_column='IrrigationWaterDemand_36', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IrrigationWaterDemand'


class Light(models.Model):
    light_id = models.AutoField(db_column='Light_ID', primary_key=True)  # Field name made lowercase.
    c = models.ForeignKey(City, models.DO_NOTHING, db_column='C_ID', blank=True, null=True)  # Field name made lowercase.
    ft = models.ForeignKey(Forecastingtime, models.DO_NOTHING, db_column='FT_ID', blank=True, null=True)  # Field name made lowercase.
    light_1 = models.CharField(db_column='Light_1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    light_2 = models.CharField(db_column='Light_2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    light_3 = models.CharField(db_column='Light_3', max_length=10, blank=True, null=True)  # Field name made lowercase.
    light_4 = models.CharField(db_column='Light_4', max_length=10, blank=True, null=True)  # Field name made lowercase.
    light_5 = models.CharField(db_column='Light_5', max_length=10, blank=True, null=True)  # Field name made lowercase.
    light_6 = models.CharField(db_column='Light_6', max_length=10, blank=True, null=True)  # Field name made lowercase.
    light_7 = models.CharField(db_column='Light_7', max_length=10, blank=True, null=True)  # Field name made lowercase.
    light_8 = models.CharField(db_column='Light_8', max_length=10, blank=True, null=True)  # Field name made lowercase.
    light_9 = models.CharField(db_column='Light_9', max_length=10, blank=True, null=True)  # Field name made lowercase.
    light_10 = models.CharField(db_column='Light_10', max_length=10, blank=True, null=True)  # Field name made lowercase.
    light_11 = models.CharField(db_column='Light_11', max_length=10, blank=True, null=True)  # Field name made lowercase.
    light_12 = models.CharField(db_column='Light_12', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Light'


class Location(models.Model):
    l_id = models.AutoField(db_column='L_ID', primary_key=True)  # Field name made lowercase.
    locationname = models.CharField(db_column='LocationName', max_length=3)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Location'


class Nextreservoirlights(models.Model):
    nrl_id = models.AutoField(db_column='NRL_ID', primary_key=True)  # Field name made lowercase.
    c = models.ForeignKey(City, models.DO_NOTHING, db_column='C_ID', blank=True, null=True)  # Field name made lowercase.
    nextreservoirlights = models.CharField(db_column='NextReservoirLights', max_length=10, blank=True, null=True)  # Field name made lowercase.
    releasetime = models.DateTimeField(db_column='ReleaseTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NextReservoirLights'


class Nextweekp(models.Model):
    nwp_id = models.AutoField(db_column='NWP_ID', primary_key=True)  # Field name made lowercase.
    c = models.ForeignKey(City, models.DO_NOTHING, db_column='C_ID', blank=True, null=True)  # Field name made lowercase.
    nextweekp = models.IntegerField(db_column='NextWeekP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NextWeekP'


class Peopleslivelihoodwater(models.Model):
    plw_id = models.AutoField(db_column='PLW_ID', primary_key=True)  # Field name made lowercase.
    r = models.ForeignKey('Reservoir', models.DO_NOTHING, db_column='R_ID', blank=True, null=True)  # Field name made lowercase.
    peopleslivelihoodwater_1 = models.FloatField(db_column='PeoplesLivelihoodWater_1', blank=True, null=True)  # Field name made lowercase.
    peopleslivelihoodwater_2 = models.FloatField(db_column='PeoplesLivelihoodWater_2', blank=True, null=True)  # Field name made lowercase.
    peopleslivelihoodwater_3 = models.FloatField(db_column='PeoplesLivelihoodWater_3', blank=True, null=True)  # Field name made lowercase.
    peopleslivelihoodwater_4 = models.FloatField(db_column='PeoplesLivelihoodWater_4', blank=True, null=True)  # Field name made lowercase.
    peopleslivelihoodwater_5 = models.FloatField(db_column='PeoplesLivelihoodWater_5', blank=True, null=True)  # Field name made lowercase.
    peopleslivelihoodwater_6 = models.FloatField(db_column='PeoplesLivelihoodWater_6', blank=True, null=True)  # Field name made lowercase.
    peopleslivelihoodwater_7 = models.FloatField(db_column='PeoplesLivelihoodWater_7', blank=True, null=True)  # Field name made lowercase.
    peopleslivelihoodwater_8 = models.FloatField(db_column='PeoplesLivelihoodWater_8', blank=True, null=True)  # Field name made lowercase.
    peopleslivelihoodwater_9 = models.FloatField(db_column='PeoplesLivelihoodWater_9', blank=True, null=True)  # Field name made lowercase.
    peopleslivelihoodwater_10 = models.FloatField(db_column='PeoplesLivelihoodWater_10', blank=True, null=True)  # Field name made lowercase.
    peopleslivelihoodwater_11 = models.FloatField(db_column='PeoplesLivelihoodWater_11', blank=True, null=True)  # Field name made lowercase.
    peopleslivelihoodwater_12 = models.FloatField(db_column='PeoplesLivelihoodWater_12', blank=True, null=True)  # Field name made lowercase.
    peopleslivelihoodwater_13 = models.FloatField(db_column='PeoplesLivelihoodWater_13', blank=True, null=True)  # Field name made lowercase.
    peopleslivelihoodwater_14 = models.FloatField(db_column='PeoplesLivelihoodWater_14', blank=True, null=True)  # Field name made lowercase.
    peopleslivelihoodwater_15 = models.FloatField(db_column='PeoplesLivelihoodWater_15', blank=True, null=True)  # Field name made lowercase.
    peopleslivelihoodwater_16 = models.FloatField(db_column='PeoplesLivelihoodWater_16', blank=True, null=True)  # Field name made lowercase.
    peopleslivelihoodwater_17 = models.FloatField(db_column='PeoplesLivelihoodWater_17', blank=True, null=True)  # Field name made lowercase.
    peopleslivelihoodwater_18 = models.FloatField(db_column='PeoplesLivelihoodWater_18', blank=True, null=True)  # Field name made lowercase.
    peopleslivelihoodwater_19 = models.FloatField(db_column='PeoplesLivelihoodWater_19', blank=True, null=True)  # Field name made lowercase.
    peopleslivelihoodwater_20 = models.FloatField(db_column='PeoplesLivelihoodWater_20', blank=True, null=True)  # Field name made lowercase.
    peopleslivelihoodwater_21 = models.FloatField(db_column='PeoplesLivelihoodWater_21', blank=True, null=True)  # Field name made lowercase.
    peopleslivelihoodwater_22 = models.FloatField(db_column='PeoplesLivelihoodWater_22', blank=True, null=True)  # Field name made lowercase.
    peopleslivelihoodwater_23 = models.FloatField(db_column='PeoplesLivelihoodWater_23', blank=True, null=True)  # Field name made lowercase.
    peopleslivelihoodwater_24 = models.FloatField(db_column='PeoplesLivelihoodWater_24', blank=True, null=True)  # Field name made lowercase.
    peopleslivelihoodwater_25 = models.FloatField(db_column='PeoplesLivelihoodWater_25', blank=True, null=True)  # Field name made lowercase.
    peopleslivelihoodwater_26 = models.FloatField(db_column='PeoplesLivelihoodWater_26', blank=True, null=True)  # Field name made lowercase.
    peopleslivelihoodwater_27 = models.FloatField(db_column='PeoplesLivelihoodWater_27', blank=True, null=True)  # Field name made lowercase.
    peopleslivelihoodwater_28 = models.FloatField(db_column='PeoplesLivelihoodWater_28', blank=True, null=True)  # Field name made lowercase.
    peopleslivelihoodwater_29 = models.FloatField(db_column='PeoplesLivelihoodWater_29', blank=True, null=True)  # Field name made lowercase.
    peopleslivelihoodwater_30 = models.FloatField(db_column='PeoplesLivelihoodWater_30', blank=True, null=True)  # Field name made lowercase.
    peopleslivelihoodwater_31 = models.FloatField(db_column='PeoplesLivelihoodWater_31', blank=True, null=True)  # Field name made lowercase.
    peopleslivelihoodwater_32 = models.FloatField(db_column='PeoplesLivelihoodWater_32', blank=True, null=True)  # Field name made lowercase.
    peopleslivelihoodwater_33 = models.FloatField(db_column='PeoplesLivelihoodWater_33', blank=True, null=True)  # Field name made lowercase.
    peopleslivelihoodwater_34 = models.FloatField(db_column='PeoplesLivelihoodWater_34', blank=True, null=True)  # Field name made lowercase.
    peopleslivelihoodwater_35 = models.FloatField(db_column='PeoplesLivelihoodWater_35', blank=True, null=True)  # Field name made lowercase.
    peopleslivelihoodwater_36 = models.FloatField(db_column='PeoplesLivelihoodWater_36', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PeoplesLivelihoodWater'


class Prewaterlevel(models.Model):
    pwl_id = models.AutoField(db_column='PWL_ID', primary_key=True)  # Field name made lowercase.
    r = models.ForeignKey('Reservoir', models.DO_NOTHING, db_column='R_ID', blank=True, null=True)  # Field name made lowercase.
    ft = models.ForeignKey(Forecastingtime, models.DO_NOTHING, db_column='FT_ID', blank=True, null=True)  # Field name made lowercase.
    predictionwaterlevel_1 = models.FloatField(db_column='PredictionWaterLevel_1', blank=True, null=True)  # Field name made lowercase.
    predictionwaterlevel_2 = models.FloatField(db_column='PredictionWaterLevel_2', blank=True, null=True)  # Field name made lowercase.
    predictionwaterlevel_3 = models.FloatField(db_column='PredictionWaterLevel_3', blank=True, null=True)  # Field name made lowercase.
    predictionwaterlevel_4 = models.FloatField(db_column='PredictionWaterLevel_4', blank=True, null=True)  # Field name made lowercase.
    predictionwaterlevel_5 = models.FloatField(db_column='PredictionWaterLevel_5', blank=True, null=True)  # Field name made lowercase.
    predictionwaterlevel_6 = models.FloatField(db_column='PredictionWaterLevel_6', blank=True, null=True)  # Field name made lowercase.
    predictionwaterlevel_7 = models.FloatField(db_column='PredictionWaterLevel_7', blank=True, null=True)  # Field name made lowercase.
    predictionwaterlevel_8 = models.FloatField(db_column='PredictionWaterLevel_8', blank=True, null=True)  # Field name made lowercase.
    predictionwaterlevel_9 = models.FloatField(db_column='PredictionWaterLevel_9', blank=True, null=True)  # Field name made lowercase.
    predictionwaterlevel_10 = models.FloatField(db_column='PredictionWaterLevel_10', blank=True, null=True)  # Field name made lowercase.
    predictionwaterlevel_11 = models.FloatField(db_column='PredictionWaterLevel_11', blank=True, null=True)  # Field name made lowercase.
    predictionwaterlevel_12 = models.FloatField(db_column='PredictionWaterLevel_12', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PreWaterLevel'


class Prewaterstoragecapacity(models.Model):
    pwsc_id = models.AutoField(db_column='PWSC_ID', primary_key=True)  # Field name made lowercase.
    r = models.ForeignKey('Reservoir', models.DO_NOTHING, db_column='R_ID', blank=True, null=True)  # Field name made lowercase.
    ft = models.ForeignKey(Forecastingtime, models.DO_NOTHING, db_column='FT_ID', blank=True, null=True)  # Field name made lowercase.
    predictionwaterstoragecapacity_1 = models.FloatField(db_column='PredictionWaterStorageCapacity_1', blank=True, null=True)  # Field name made lowercase.
    predictionwaterstoragecapacity_2 = models.FloatField(db_column='PredictionWaterStorageCapacity_2', blank=True, null=True)  # Field name made lowercase.
    predictionwaterstoragecapacity_3 = models.FloatField(db_column='PredictionWaterStorageCapacity_3', blank=True, null=True)  # Field name made lowercase.
    predictionwaterstoragecapacity_4 = models.FloatField(db_column='PredictionWaterStorageCapacity_4', blank=True, null=True)  # Field name made lowercase.
    predictionwaterstoragecapacity_5 = models.FloatField(db_column='PredictionWaterStorageCapacity_5', blank=True, null=True)  # Field name made lowercase.
    predictionwaterstoragecapacity_6 = models.FloatField(db_column='PredictionWaterStorageCapacity_6', blank=True, null=True)  # Field name made lowercase.
    predictionwaterstoragecapacity_7 = models.FloatField(db_column='PredictionWaterStorageCapacity_7', blank=True, null=True)  # Field name made lowercase.
    predictionwaterstoragecapacity_8 = models.FloatField(db_column='PredictionWaterStorageCapacity_8', blank=True, null=True)  # Field name made lowercase.
    predictionwaterstoragecapacity_9 = models.FloatField(db_column='PredictionWaterStorageCapacity_9', blank=True, null=True)  # Field name made lowercase.
    predictionwaterstoragecapacity_10 = models.FloatField(db_column='PredictionWaterStorageCapacity_10', blank=True, null=True)  # Field name made lowercase.
    predictionwaterstoragecapacity_11 = models.FloatField(db_column='PredictionWaterStorageCapacity_11', blank=True, null=True)  # Field name made lowercase.
    predictionwaterstoragecapacity_12 = models.FloatField(db_column='PredictionWaterStorageCapacity_12', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PreWaterStorageCapacity'


class Q90(models.Model):
    q90_id = models.AutoField(db_column='Q90_ID', primary_key=True)  # Field name made lowercase.
    fo = models.ForeignKey(Flowobservatory, models.DO_NOTHING, db_column='FO_ID', blank=True, null=True)  # Field name made lowercase.
    ten_1 = models.FloatField(db_column='Ten_1', blank=True, null=True)  # Field name made lowercase.
    ten_2 = models.FloatField(db_column='Ten_2', blank=True, null=True)  # Field name made lowercase.
    ten_3 = models.FloatField(db_column='Ten_3', blank=True, null=True)  # Field name made lowercase.
    ten_4 = models.FloatField(db_column='Ten_4', blank=True, null=True)  # Field name made lowercase.
    ten_5 = models.FloatField(db_column='Ten_5', blank=True, null=True)  # Field name made lowercase.
    ten_6 = models.FloatField(db_column='Ten_6', blank=True, null=True)  # Field name made lowercase.
    ten_7 = models.FloatField(db_column='Ten_7', blank=True, null=True)  # Field name made lowercase.
    ten_8 = models.FloatField(db_column='Ten_8', blank=True, null=True)  # Field name made lowercase.
    ten_9 = models.FloatField(db_column='Ten_9', blank=True, null=True)  # Field name made lowercase.
    ten_10 = models.FloatField(db_column='Ten_10', blank=True, null=True)  # Field name made lowercase.
    ten_11 = models.FloatField(db_column='Ten_11', blank=True, null=True)  # Field name made lowercase.
    ten_12 = models.FloatField(db_column='Ten_12', blank=True, null=True)  # Field name made lowercase.
    ten_13 = models.FloatField(db_column='Ten_13', blank=True, null=True)  # Field name made lowercase.
    ten_14 = models.FloatField(db_column='Ten_14', blank=True, null=True)  # Field name made lowercase.
    ten_15 = models.FloatField(db_column='Ten_15', blank=True, null=True)  # Field name made lowercase.
    ten_16 = models.FloatField(db_column='Ten_16', blank=True, null=True)  # Field name made lowercase.
    ten_17 = models.FloatField(db_column='Ten_17', blank=True, null=True)  # Field name made lowercase.
    ten_18 = models.FloatField(db_column='Ten_18', blank=True, null=True)  # Field name made lowercase.
    ten_19 = models.FloatField(db_column='Ten_19', blank=True, null=True)  # Field name made lowercase.
    ten_20 = models.FloatField(db_column='Ten_20', blank=True, null=True)  # Field name made lowercase.
    ten_21 = models.FloatField(db_column='Ten_21', blank=True, null=True)  # Field name made lowercase.
    ten_22 = models.FloatField(db_column='Ten_22', blank=True, null=True)  # Field name made lowercase.
    ten_23 = models.FloatField(db_column='Ten_23', blank=True, null=True)  # Field name made lowercase.
    ten_24 = models.FloatField(db_column='Ten_24', blank=True, null=True)  # Field name made lowercase.
    ten_25 = models.FloatField(db_column='Ten_25', blank=True, null=True)  # Field name made lowercase.
    ten_26 = models.FloatField(db_column='Ten_26', blank=True, null=True)  # Field name made lowercase.
    ten_27 = models.FloatField(db_column='Ten_27', blank=True, null=True)  # Field name made lowercase.
    ten_28 = models.FloatField(db_column='Ten_28', blank=True, null=True)  # Field name made lowercase.
    ten_29 = models.FloatField(db_column='Ten_29', blank=True, null=True)  # Field name made lowercase.
    ten_30 = models.FloatField(db_column='Ten_30', blank=True, null=True)  # Field name made lowercase.
    ten_31 = models.FloatField(db_column='Ten_31', blank=True, null=True)  # Field name made lowercase.
    ten_32 = models.FloatField(db_column='Ten_32', blank=True, null=True)  # Field name made lowercase.
    ten_33 = models.FloatField(db_column='Ten_33', blank=True, null=True)  # Field name made lowercase.
    ten_34 = models.FloatField(db_column='Ten_34', blank=True, null=True)  # Field name made lowercase.
    ten_35 = models.FloatField(db_column='Ten_35', blank=True, null=True)  # Field name made lowercase.
    ten_36 = models.FloatField(db_column='Ten_36', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Q90'


class Q95(models.Model):
    q95_id = models.AutoField(db_column='Q95_ID', primary_key=True)  # Field name made lowercase.
    fo = models.ForeignKey(Flowobservatory, models.DO_NOTHING, db_column='FO_ID', blank=True, null=True)  # Field name made lowercase.
    ten_1 = models.FloatField(db_column='Ten_1', blank=True, null=True)  # Field name made lowercase.
    ten_2 = models.FloatField(db_column='Ten_2', blank=True, null=True)  # Field name made lowercase.
    ten_3 = models.FloatField(db_column='Ten_3', blank=True, null=True)  # Field name made lowercase.
    ten_4 = models.FloatField(db_column='Ten_4', blank=True, null=True)  # Field name made lowercase.
    ten_5 = models.FloatField(db_column='Ten_5', blank=True, null=True)  # Field name made lowercase.
    ten_6 = models.FloatField(db_column='Ten_6', blank=True, null=True)  # Field name made lowercase.
    ten_7 = models.FloatField(db_column='Ten_7', blank=True, null=True)  # Field name made lowercase.
    ten_8 = models.FloatField(db_column='Ten_8', blank=True, null=True)  # Field name made lowercase.
    ten_9 = models.FloatField(db_column='Ten_9', blank=True, null=True)  # Field name made lowercase.
    ten_10 = models.FloatField(db_column='Ten_10', blank=True, null=True)  # Field name made lowercase.
    ten_11 = models.FloatField(db_column='Ten_11', blank=True, null=True)  # Field name made lowercase.
    ten_12 = models.FloatField(db_column='Ten_12', blank=True, null=True)  # Field name made lowercase.
    ten_13 = models.FloatField(db_column='Ten_13', blank=True, null=True)  # Field name made lowercase.
    ten_14 = models.FloatField(db_column='Ten_14', blank=True, null=True)  # Field name made lowercase.
    ten_15 = models.FloatField(db_column='Ten_15', blank=True, null=True)  # Field name made lowercase.
    ten_16 = models.FloatField(db_column='Ten_16', blank=True, null=True)  # Field name made lowercase.
    ten_17 = models.FloatField(db_column='Ten_17', blank=True, null=True)  # Field name made lowercase.
    ten_18 = models.FloatField(db_column='Ten_18', blank=True, null=True)  # Field name made lowercase.
    ten_19 = models.FloatField(db_column='Ten_19', blank=True, null=True)  # Field name made lowercase.
    ten_20 = models.FloatField(db_column='Ten_20', blank=True, null=True)  # Field name made lowercase.
    ten_21 = models.FloatField(db_column='Ten_21', blank=True, null=True)  # Field name made lowercase.
    ten_22 = models.FloatField(db_column='Ten_22', blank=True, null=True)  # Field name made lowercase.
    ten_23 = models.FloatField(db_column='Ten_23', blank=True, null=True)  # Field name made lowercase.
    ten_24 = models.FloatField(db_column='Ten_24', blank=True, null=True)  # Field name made lowercase.
    ten_25 = models.FloatField(db_column='Ten_25', blank=True, null=True)  # Field name made lowercase.
    ten_26 = models.FloatField(db_column='Ten_26', blank=True, null=True)  # Field name made lowercase.
    ten_27 = models.FloatField(db_column='Ten_27', blank=True, null=True)  # Field name made lowercase.
    ten_28 = models.FloatField(db_column='Ten_28', blank=True, null=True)  # Field name made lowercase.
    ten_29 = models.FloatField(db_column='Ten_29', blank=True, null=True)  # Field name made lowercase.
    ten_30 = models.FloatField(db_column='Ten_30', blank=True, null=True)  # Field name made lowercase.
    ten_31 = models.FloatField(db_column='Ten_31', blank=True, null=True)  # Field name made lowercase.
    ten_32 = models.FloatField(db_column='Ten_32', blank=True, null=True)  # Field name made lowercase.
    ten_33 = models.FloatField(db_column='Ten_33', blank=True, null=True)  # Field name made lowercase.
    ten_34 = models.FloatField(db_column='Ten_34', blank=True, null=True)  # Field name made lowercase.
    ten_35 = models.FloatField(db_column='Ten_35', blank=True, null=True)  # Field name made lowercase.
    ten_36 = models.FloatField(db_column='Ten_36', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Q95'


class Regionalwaterregime(models.Model):
    rwr_id = models.AutoField(db_column='RWR_ID', primary_key=True)  # Field name made lowercase.
    c = models.ForeignKey(City, models.DO_NOTHING, db_column='C_ID', blank=True, null=True)  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='TimeStamp')  # Field name made lowercase.
    reservoirlightsnow = models.CharField(db_column='ReservoirLightsNow', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RegionalWaterRegime'


class Reservedwater(models.Model):
    rw_id = models.AutoField(db_column='RW_ID', primary_key=True)  # Field name made lowercase.
    r = models.ForeignKey('Reservoir', models.DO_NOTHING, db_column='R_ID', blank=True, null=True)  # Field name made lowercase.
    reservedwater_1 = models.FloatField(db_column='ReservedWater_1', blank=True, null=True)  # Field name made lowercase.
    reservedwater_2 = models.FloatField(db_column='ReservedWater_2', blank=True, null=True)  # Field name made lowercase.
    reservedwater_3 = models.FloatField(db_column='ReservedWater_3', blank=True, null=True)  # Field name made lowercase.
    reservedwater_4 = models.FloatField(db_column='ReservedWater_4', blank=True, null=True)  # Field name made lowercase.
    reservedwater_5 = models.FloatField(db_column='ReservedWater_5', blank=True, null=True)  # Field name made lowercase.
    reservedwater_6 = models.FloatField(db_column='ReservedWater_6', blank=True, null=True)  # Field name made lowercase.
    reservedwater_7 = models.FloatField(db_column='ReservedWater_7', blank=True, null=True)  # Field name made lowercase.
    reservedwater_8 = models.FloatField(db_column='ReservedWater_8', blank=True, null=True)  # Field name made lowercase.
    reservedwater_9 = models.FloatField(db_column='ReservedWater_9', blank=True, null=True)  # Field name made lowercase.
    reservedwater_10 = models.FloatField(db_column='ReservedWater_10', blank=True, null=True)  # Field name made lowercase.
    reservedwater_11 = models.FloatField(db_column='ReservedWater_11', blank=True, null=True)  # Field name made lowercase.
    reservedwater_12 = models.FloatField(db_column='ReservedWater_12', blank=True, null=True)  # Field name made lowercase.
    reservedwater_13 = models.FloatField(db_column='ReservedWater_13', blank=True, null=True)  # Field name made lowercase.
    reservedwater_14 = models.FloatField(db_column='ReservedWater_14', blank=True, null=True)  # Field name made lowercase.
    reservedwater_15 = models.FloatField(db_column='ReservedWater_15', blank=True, null=True)  # Field name made lowercase.
    reservedwater_16 = models.FloatField(db_column='ReservedWater_16', blank=True, null=True)  # Field name made lowercase.
    reservedwater_17 = models.FloatField(db_column='ReservedWater_17', blank=True, null=True)  # Field name made lowercase.
    reservedwater_18 = models.FloatField(db_column='ReservedWater_18', blank=True, null=True)  # Field name made lowercase.
    reservedwater_19 = models.FloatField(db_column='ReservedWater_19', blank=True, null=True)  # Field name made lowercase.
    reservedwater_20 = models.FloatField(db_column='ReservedWater_20', blank=True, null=True)  # Field name made lowercase.
    reservedwater_21 = models.FloatField(db_column='ReservedWater_21', blank=True, null=True)  # Field name made lowercase.
    reservedwater_22 = models.FloatField(db_column='ReservedWater_22', blank=True, null=True)  # Field name made lowercase.
    reservedwater_23 = models.FloatField(db_column='ReservedWater_23', blank=True, null=True)  # Field name made lowercase.
    reservedwater_24 = models.FloatField(db_column='ReservedWater_24', blank=True, null=True)  # Field name made lowercase.
    reservedwater_25 = models.FloatField(db_column='ReservedWater_25', blank=True, null=True)  # Field name made lowercase.
    reservedwater_26 = models.FloatField(db_column='ReservedWater_26', blank=True, null=True)  # Field name made lowercase.
    reservedwater_27 = models.FloatField(db_column='ReservedWater_27', blank=True, null=True)  # Field name made lowercase.
    reservedwater_28 = models.FloatField(db_column='ReservedWater_28', blank=True, null=True)  # Field name made lowercase.
    reservedwater_29 = models.FloatField(db_column='ReservedWater_29', blank=True, null=True)  # Field name made lowercase.
    reservedwater_30 = models.FloatField(db_column='ReservedWater_30', blank=True, null=True)  # Field name made lowercase.
    reservedwater_31 = models.FloatField(db_column='ReservedWater_31', blank=True, null=True)  # Field name made lowercase.
    reservedwater_32 = models.FloatField(db_column='ReservedWater_32', blank=True, null=True)  # Field name made lowercase.
    reservedwater_33 = models.FloatField(db_column='ReservedWater_33', blank=True, null=True)  # Field name made lowercase.
    reservedwater_34 = models.FloatField(db_column='ReservedWater_34', blank=True, null=True)  # Field name made lowercase.
    reservedwater_35 = models.FloatField(db_column='ReservedWater_35', blank=True, null=True)  # Field name made lowercase.
    reservedwater_36 = models.FloatField(db_column='ReservedWater_36', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReservedWater'


class Reservoir(models.Model):
    r_id = models.AutoField(db_column='R_ID', primary_key=True)  # Field name made lowercase.
    reservoiridentifier = models.CharField(db_column='ReservoirIdentifier', max_length=8)  # Field name made lowercase.
    reservoirname = models.CharField(db_column='ReservoirName', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Reservoir'


class Reservoirstate(models.Model):
    rs_id = models.AutoField(db_column='RS_ID', primary_key=True)  # Field name made lowercase.
    r = models.ForeignKey(Reservoir, models.DO_NOTHING, db_column='R_ID', blank=True, null=True)  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='TimeStamp')  # Field name made lowercase.
    waterlevel = models.FloatField(db_column='WaterLevel', blank=True, null=True)  # Field name made lowercase.
    effectivewaterstoragecapacity = models.FloatField(db_column='EffectiveWaterStorageCapacity', blank=True, null=True)  # Field name made lowercase.
    percentageusedinreservoircapacity = models.FloatField(db_column='PercentageUsedInReservoirCapacity', blank=True, null=True)  # Field name made lowercase.
    maximumcapacity = models.FloatField(db_column='MaximumCapacity', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReservoirState'


class Rulecurve(models.Model):
    rc_id = models.AutoField(db_column='RC_ID', primary_key=True)  # Field name made lowercase.
    r = models.ForeignKey(Reservoir, models.DO_NOTHING, db_column='R_ID', blank=True, null=True)  # Field name made lowercase.
    tendays_no = models.FloatField(db_column='TenDays_No', blank=True, null=True)  # Field name made lowercase.
    upperlimit = models.FloatField(db_column='UpperLimit', blank=True, null=True)  # Field name made lowercase.
    midlimit = models.FloatField(db_column='MidLimit', blank=True, null=True)  # Field name made lowercase.
    lowerlimit = models.FloatField(db_column='LowerLimit', blank=True, null=True)  # Field name made lowercase.
    seriouslowerlimit = models.FloatField(db_column='SeriousLowerLimit', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RuleCurve'


class Simreservoirflow(models.Model):
    srf_id = models.AutoField(db_column='SRF_ID', primary_key=True)  # Field name made lowercase.
    r = models.ForeignKey(Reservoir, models.DO_NOTHING, db_column='R_ID', blank=True, null=True)  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='TimeStamp', blank=True, null=True)  # Field name made lowercase.
    streamflow = models.FloatField(db_column='StreamFlow', blank=True, null=True)  # Field name made lowercase.
    planwaterdemand = models.FloatField(db_column='PlanWaterDemand', blank=True, null=True)  # Field name made lowercase.
    irrigationrequirement = models.FloatField(db_column='IrrigationRequirement', blank=True, null=True)  # Field name made lowercase.
    waterright = models.FloatField(db_column='WaterRight', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SimReservoirFlow'


class Waterintakestructures(models.Model):
    wis_id = models.AutoField(db_column='WIS_ID', primary_key=True)  # Field name made lowercase.
    structuresname = models.CharField(db_column='StructuresName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    q_downstream = models.FloatField(db_column='Q_downstream', blank=True, null=True)  # Field name made lowercase.
    maxq = models.FloatField(db_column='MaxQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WaterIntakeStructures'


class Watersupply(models.Model):
    ws_id = models.AutoField(db_column='WS_ID', primary_key=True)  # Field name made lowercase.
    r = models.ForeignKey(Reservoir, models.DO_NOTHING, db_column='R_ID', blank=True, null=True)  # Field name made lowercase.
    c = models.ForeignKey(City, models.DO_NOTHING, db_column='C_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WaterSupply'