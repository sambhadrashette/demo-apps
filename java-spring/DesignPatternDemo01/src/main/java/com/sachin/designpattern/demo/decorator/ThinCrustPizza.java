package com.sachin.designpattern.demo.decorator;

public class ThinCrustPizza extends Pizza {

    @Override
    public String getDescription() {
        return "Thin crust pizza ";
    }

    @Override
    public double cost() {
        return 100;
    }
}
