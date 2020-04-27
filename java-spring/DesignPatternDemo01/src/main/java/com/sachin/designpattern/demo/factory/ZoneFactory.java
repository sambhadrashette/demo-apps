package com.sachin.designpattern.demo.factory;

public class ZoneFactory {
    public Zone createZone(String zoneId) {
        Zone zone = null;
        if (zoneId.equalsIgnoreCase("USE")) {
            zone = new ZoneUSEastern();
        } else if (zoneId.equalsIgnoreCase("USC")) {
            zone = new ZoneUSCentral();
        } else if (zoneId.equalsIgnoreCase("USM")) {
            zone = new ZoneUSMountains();
        } else if (zoneId.equalsIgnoreCase("USP")) {
            zone = new ZoneUSPacific();
        }
        return zone;
    }
}
