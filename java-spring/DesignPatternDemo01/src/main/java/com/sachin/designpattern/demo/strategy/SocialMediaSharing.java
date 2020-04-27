package com.sachin.designpattern.demo.strategy;

public class SocialMediaSharing implements ShareStrategy {
    @Override
    public void share() {
        System.out.println("Sharing via social media");
    }
}
