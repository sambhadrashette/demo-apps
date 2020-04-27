package com.sachin.designpattern.demo.decorator;

public class ThickCrustPizza extends Pizza {

    @Override
    public String getDescription() {
        return "Thick crust pizza ";
    }

    @Override
    public double cost() {
        return 200;
    }
}
