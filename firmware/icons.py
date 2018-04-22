temp= (         # temp circle
	0b00111,
	0b00101,
	0b00111,
	0b00000,
	0b00000,
	0b00000,
	0b00000,
	0b00000
)
clear_day = (          #clear day
	0b00000,
	0b10001,
	0b00100,
	0b01010,
	0b00100,
	0b10001,
	0b00000,
	0b00000
)

clear_night = (
	0b00110,
	0b01001,
	0b10010,
	0b10100,
	0b10100,
	0b10010,
	0b01001,
	0b00110
)

partly_cloudy_day = (
    0b10011,
	0b00100,
	0b10100,
	0b00011,
	0b01110,
	0b10001,
	0b10001,
	0b01110
)

partly_cloudy_night = (
    0b01110,
	0b10001,
	0b10010,
	0b10010,
	0b10001,
	0b01110,
	0b10001,
	0b01110
)

cloudy = (
	0b00000,
	0b00000,
	0b01110,
	0b10001,
	0b10001,
	0b01110,
	0b00000,
	0b00000
)

rain = (    #raining and sleeti
	0b01110,
	0b10001,
	0b10001,
	0b01110,
	0b00000,
	0b00010,
	0b01010,
	0b01000
)

snow = (
	0b01110,
	0b10001,
	0b10001,
	0b01110,
	0b00100,
	0b01010,
	0b00100,
	0b00000
)


def make_list():
    icon_names = [
                 'temp',
                 'clear-day',
                 'clear-night',
                 'partly-cloudy-day',
                 'partly-cloudy-night',
                 'cloudy',
                 'rain',
                 'snow'
                 ]
    icon_bytes = [
                  temp,
                  clear_day,
                  clear_night,
                  partly_cloudy_day,
                  partly_cloudy_night,
                  cloudy,
                  rain,
                  snow
                  ]
    return [icon_names,icon_bytes]
