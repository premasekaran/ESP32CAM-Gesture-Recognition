#include <WiFi.h>
#include <WebServer.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

const char* ssid = "hotspot";
const char* password = "redchocos";

WebServer server(80);

LiquidCrystal_I2C lcd(0x27,16,2);

void handleDisplay()
{
    if(server.hasArg("text"))
    {
        String txt = server.arg("text");

        Serial.print("Received: ");
        Serial.println(txt);

        lcd.clear();
        lcd.setCursor(0,0);
        lcd.print(txt);

        server.send(200,"text/plain","Displayed");
    }
}

void setup()
{
    Serial.begin(115200);

    lcd.init();
    lcd.backlight();

    WiFi.begin(ssid,password);

    while(WiFi.status()!=WL_CONNECTED)
    {
        delay(500);
        Serial.print(".");
    }

    Serial.println();
    Serial.println(WiFi.localIP());

    server.on("/display",handleDisplay);

    server.begin();

    lcd.print("Ready");
}

void loop()
{
    server.handleClient();
}