package com.sachin.designpattern.demo.adapter;

public class SuperDrone implements Drone {

    @Override
    public void beep() {
        System.out.println("Beep beep beep");
    }

    @Override
    public void spinRoters() {
        System.out.println("Roters are spinning");
    }

    @Override
    public void takeOff() {
        System.out.println("Taking off");
    }
}
