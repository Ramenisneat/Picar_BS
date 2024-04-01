from RPLCD.i2c import CharLCD
from time import sleep
import subprocess

lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=20, rows=4, dotsize=8)


while True:
    try:
        out = subprocess.Popen(['hostname','-I'], stdout = subprocess.PIPE).stdout.read()
        ip = str(out).split(" ")[0][2:]
    except:
        ip = "NOIP"
        
    lcd.clear()

    lcd.write_string('KRAIG Here')
    lcd.crlf()
    lcd.write_string(f"My IP: {ip}")
    
    sleep(10)

    lcd.clear()
    lcd.write_string("     0    0     ")
    lcd.crlf()
    lcd.write_string("   =       =    ")
    lcd.crlf()
    lcd.write_string("    =======    ")
    sleep(2)

    lcd.clear()
    lcd.write_string("     V    V     ")
    lcd.crlf()
    lcd.write_string("   =       =    ")
    lcd.crlf()
    lcd.write_string("    =======    ")
    sleep(.75)

    lcd.clear()
    lcd.write_string("     0    0     ")
    lcd.crlf()
    lcd.write_string("   =       =    ")
    lcd.crlf()
    lcd.write_string("    =======    ")
    sleep(2)

