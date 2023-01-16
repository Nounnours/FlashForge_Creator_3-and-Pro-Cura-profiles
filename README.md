# FlashForge_Creator_3-and-Pro-Cura-profiles

First version of the profile that actually works on the latest Cura (5.2.1 as of today)
This should simply go into appdata/roaming/cura/"version number"/ path
so in my case : appdata/roaming/cura/5.2/

This is based off a profile created and published by someone else on Thingyverse I simply modified it and made all the extruders/ cooling fan etc controls work in Gcode directly
Original link there:
https://www.thingiverse.com/thing:4574596

Note that there's also a very usefull hack (I can't call this a fix) that gets rif of the decimal in temperature settigns ie: 230.0 deg to make it 230 deg
The issue with the decimal is that most FlashForge printers interpret this as a setpoint of 0deg..which has the effect of turning off your extruder while the printer will try to mover around and extrude filament...
Anyway this hack from the discussion over there on this cura issue: https://github.com/Ultimaker/Cura/issues/8657
This @danilocesar hack/fix works for now and is part of this profile so thanks to all the people before me

I reworked this entire profile to generate near enough the same Gcode as to what comes out of FlashPrint

This definitely supports independant printing on each extruders (anoyingly extruder 1 is Right and 2 is left on Cura but I might be able to flip this later on)
It should also work for dual material printing but I haven't tested this yet

note that mirrors and clone mode like in flashprint are not working for now since Cura doesn't support any of this yet (maybe in the future who knows?)

Anyway hope this can help people since I've seen amny struggling with this lately!