package com.sachin.designpattern.demo.factory;

public class ZoneInvalid extends Zone {

    @Override
    public String getDisplayName() {
        return null;
    }

    @Override
    public int getOffset() {
        return 0;
    }
}
