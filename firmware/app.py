

# Get prerequisites
from RPi import GPIO                         # GPIO library
from RPLCD import CharLCD                    # LCD library

import time
from datetime import datetime
import schedule

from darkSkyAPI import get_current_weather   #get_current_weather for getting latest weather info

# Get the icons for weather summary
from icons import make_list
icon_names = make_list()[0]
icon_bytes = make_list()[1]

# Declare LCD: cols and rows for your lcd, pin_rs = reset pin, pin_e = enable pin, pins_data for 4 bits communication, set pin numeriotation
lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23], numbering_mode=GPIO.BOARD)

# Turn off gpio warnings while in dev
GPIO.setwarnings(False)

# Declare the buffer to write on lcd (the buffer must be 16x2 - same as lcd)
framebuffer = [
    '',
    '',
]
long_string = str(framebuffer[1])  # save in long_string string to write on lcd

# Make icons for lcd
for index,val in enumerate(icon_bytes):
    lcd.create_char(index, val)


# Function to write the buffer on the screen ( scroll animation of second row is made by deleting and drawing the text each .4s )
def write_to_lcd(lcd, framebuffer, num_cols):
    lcd.home()
    for row in framebuffer:
        lcd.write_string(row.ljust(num_cols)[:num_cols])
        lcd.write_string('\r\n')


# Function which makes scroll effect
def loop_string(string, lcd, framebuffer, row, num_cols, delay=0.4): #DELAY= CONTROLS THE SPEED OF SCROLL
    padding = ' ' * num_cols
    s = padding + string + padding
    for i in range(len(s) - num_cols + 1):
        framebuffer[row] = s[i:i+num_cols]
        write_to_lcd(lcd, framebuffer, num_cols)
        time.sleep(delay)


# Function to update the framebuffer which is printed on the lcd
def update_buffer():
    weather_obj = get_current_weather()
    global framebuffer, long_string

    temperatureCelsius = round((weather_obj.temperature - 32) * .556, 1)                       # temperature in celcius
    measurement_time = datetime.fromtimestamp(weather_obj.time).strftime('%a,%H:%M')          # measurement time in day, hour, minutes
    summary = weather_obj.summary                                                              # brief summary
    precipProbability = int(weather_obj.precipProbability * 100 )                              # precipitation probability (%)
    humidity = int(weather_obj.humidity * 100)                                                 # humidity probability (%)
    icon_index = int(icon_names.index(weather_obj.icon))                                       # index of the icon

    # Pading for icon
    padding = ' ' * int(16 - (len( str(temperatureCelsius) ) + 2) - 2)

    framebuffer = [
        str( temperatureCelsius ) + unichr(0) + str('C') + padding + unichr(icon_index),
        str(measurement_time) + str('  ') + str(summary) +  str('  ') + str('Precip ') + str(precipProbability) + '%' + str(' ') + str("Humidity ") + str(humidity) + '%',
    ]

    long_string = str(framebuffer[1])


# Main function
def run():
    update_buffer()

    schedule.every(2).minutes.do(update_buffer)

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
            loop_string(long_string, lcd, framebuffer, 1, 16)


    except KeyboardInterrupt:
        print('lcd will be clear')
        lcd.close(clear=True)


# if this script is called, then execute 'run' method
if(__name__ == "__main__"):
    run()
