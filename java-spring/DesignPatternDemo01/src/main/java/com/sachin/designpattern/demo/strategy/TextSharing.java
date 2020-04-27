package com.sachin.designpattern.demo.strategy;

public class TextSharing implements ShareStrategy {
    @Override
    public void share() {
        System.out.println("Sharing through text");
    }
}
