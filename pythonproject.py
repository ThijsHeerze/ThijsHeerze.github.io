from m5stack import lcd
# 320 x 240
lcd.setRotation(1)
lcd.text(lcd.CENTER, 25, 'My name is?')
# Deze code print: "My name is?".
time.sleep(1)
# Deze code zorgt ervoor dat hij 1 seconde wacht.
lcd.text(lcd.CENTER, 45, 'Printing...')
# Deze code print: "Printing."
rijen = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
# Dit is een array voor het aantal rijen horizontaal.
xAs = [[], [1, 2, 3, 4, 5, 6, 8, 9, 11, 12, 14, 15, 18, 19, 21, 22, 23, 24], [1, 2, 3, 4, 5, 6, 8, 9, 11, 12, 14, 15, 18, 19, 21, 22, 23, 24], [3, 4, 8, 9, 11, 12, 14, 15, 18, 19, 21, 22], [3, 4, 8, 9, 11, 12, 14, 15, 18, 19, 21, 22], [3, 4, 8, 9, 10, 11, 12, 14, 15, 18, 19, 21, 22, 23, 24], [3, 4, 8, 9, 10, 11, 12, 14, 15, 18, 19, 21, 22, 23, 24], [3, 4, 8, 9, 11, 12, 14, 15, 18, 19, 23, 24], [3, 4, 8, 9, 11, 12, 14, 15, 18, 19, 23, 24], [3, 4, 8, 9, 11, 12, 14, 15, 17, 18, 19, 21, 22, 23, 24], [3, 4, 8, 9, 11, 12, 14, 15, 17, 18, 19, 21, 22, 23, 24]];
# multidimentional array voor elke coördinaat voor elke letter in horizontale rijen.
kleuren = [lcd.WHITE, lcd.WHITE, lcd.WHITE, lcd.WHITE, lcd.WHITE, lcd.WHITE]
# Dit zijn de kleuren voor elke horizontale rij.

for y in rijen:
    # Elke keer als Y deelbaar is door 2, dan wacht hij 1 seconden.
    if y % 2:
        time.sleep(1)
    for x in xAs[y]:
        lcd.drawPixel(50+x, 75+y, lcd.WHITE)
        # Deze code zorgt ervoor op welke pixels de letters getyped worden.