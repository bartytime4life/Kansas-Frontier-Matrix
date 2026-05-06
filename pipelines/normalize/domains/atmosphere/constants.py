AQI_CATEGORIES = {
    1: ("Good", 0, 50, "0-50"),
    2: ("Moderate", 51, 100, "51-100"),
    3: ("Unhealthy for Sensitive Groups", 101, 150, "101-150"),
    4: ("Unhealthy", 151, 200, "151-200"),
    5: ("Very Unhealthy", 201, 300, "201-300"),
    6: ("Hazardous", 301, 500, "301-500"),
}

CATEGORY_ALIASES = {
    "USG": "Unhealthy for Sensitive Groups",
    "Unhealthy for Sensitive": "Unhealthy for Sensitive Groups",
}

POLLUTANT_MAP = {
    "OZONE": ("O3", "Ozone", "ppb"),
    "O3": ("O3", "Ozone", "ppb"),
    "PM2.5": ("PM25", "Fine particulate matter", "ug/m3"),
    "PM25": ("PM25", "Fine particulate matter", "ug/m3"),
    "PM_2_5": ("PM25", "Fine particulate matter", "ug/m3"),
    "PM 2.5": ("PM25", "Fine particulate matter", "ug/m3"),
    "PM10": ("PM10", "Coarse particulate matter", "ug/m3"),
    "PM 10": ("PM10", "Coarse particulate matter", "ug/m3"),
    "NO2": ("NO2", "Nitrogen dioxide", "ppb"),
    "NITROGEN DIOXIDE": ("NO2", "Nitrogen dioxide", "ppb"),
    "SO2": ("SO2", "Sulfur dioxide", "ppb"),
    "SULFUR DIOXIDE": ("SO2", "Sulfur dioxide", "ppb"),
    "CO": ("CO", "Carbon monoxide", "ppm"),
    "CARBON MONOXIDE": ("CO", "Carbon monoxide", "ppm"),
}
SOURCE_DOC_REFS = [
    "https://docs.airnowapi.org/",
    "https://docs.airnowapi.org/webservices",
    "https://docs.airnowapi.org/faq",
]
