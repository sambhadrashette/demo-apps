package com.sachin.designpattern.demo.decorator;

public abstract class ToppingDecorator extends Pizza {
    Pizza pizza;
    @Override
    public abstract String getDescription();
}
