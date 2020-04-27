package com.sachin.designpattern.demo.adapter;

public class DuckSimulator {
    public static void main(String[] args) {
        Duck duckAdapter = new DuckAdapter(new SuperDrone());
        testDuck(duckAdapter);
    }

    public static void testDuck(Duck duck) {
        duck.quack();
        duck.fly();
    }
}
