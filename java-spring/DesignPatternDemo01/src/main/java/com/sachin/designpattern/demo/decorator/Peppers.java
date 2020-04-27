package com.sachin.designpattern.demo.decorator;

public class Peppers extends ToppingDecorator {
    public Peppers(Pizza pizza) {
        this.pizza = pizza;
    }

    @Override
    public String getDescription() {
        return this.pizza.getDescription() + " with peppers";
    }

    @Override
    public double cost() {
        return pizza.cost() + 2.0;
    }
}
