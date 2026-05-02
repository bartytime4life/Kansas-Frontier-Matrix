SUPPORTED_PRODUCT_TYPES={"hourly_aq_obs","hourly_data_values","daily_data_v2","monitoring_site_locations","cityzipcodes_lookup","reportingarea_candidate"}
FORBIDDEN_SCHEMES=("http://","https://","ftp://","s3://","gs://")
SECRET_KEYS=("api_key","token","secret","password","bearer","credential","authorization")
POLLUTANT_MAP={"OZONE":"O3","O3":"O3","PM2.5":"PM25","PM25":"PM25","PM_2_5":"PM25","PM 2.5":"PM25","PM10":"PM10","PM 10":"PM10","NO2":"NO2","NITROGEN DIOXIDE":"NO2","SO2":"SO2","SULFUR DIOXIDE":"SO2","CO":"CO","CARBON MONOXIDE":"CO","OZONE-8HR":"O3_8HR","OZONE-1HR":"O3_1HR","PM2.5-24HR":"PM25_24HR","PM25-24HR":"PM25_24HR","PM10-24HR":"PM10_24HR","SO2-24HR":"SO2_24HR","CO-8HR":"CO_8HR"}
AQI_CATEGORY={0:"Good",1:"Moderate",2:"Unhealthy for Sensitive Groups",3:"Unhealthy",4:"Very Unhealthy",5:"Hazardous"}
