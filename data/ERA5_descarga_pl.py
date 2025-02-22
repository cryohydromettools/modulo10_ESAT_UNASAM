import cdsapi

c = cdsapi.Client()

c.retrieve(
    'reanalysis-era5-pressure-levels',
    {
        'product_type': 'reanalysis',
        'format': 'netcdf',
        'time': [
            '00:00', '06:00', '12:00',
            '18:00',
        ],        'variable': ['specific_humidity', 'temperature',],
        'pressure_level': [
            '200', '500', '1000',
        ],
        'day': [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
            '13', '14', '15',
            '16', '17', '18',
            '19', '20', '21',
            '22', '23', '24',
            '25', '26', '27',
            '28', '29', '30',
            '31',
        ],
        'month': [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
        ],
        'year': '2017',
        'area': [
            -7, -79, -11,
            -76.5,
        ],
    },
    'ERA5_2017_CRS_pl.nc')