package com.sachin.designpattern.demo.adapter;

public class DuckAdapter implements Duck {
    private Drone drone;

    public DuckAdapter(Drone drone) {
        this.drone = drone;
    }

    @Override
    public void fly() {
        this.drone.spinRoters();
        this.drone.takeOff();
    }

    @Override
    public void quack() {
        this.drone.beep();
    }
}
